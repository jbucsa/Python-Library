import math
import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MarketDataLevel:
    """Represents a single price level in the market data."""
    quantity: int
    price: float


@dataclass
class TradeReport:
    """Represents an incoming trade to be hedged."""
    quantity: int
    risk_per_qty: float


@dataclass
class HedgeReport:
    """Represents the resulting hedge trade."""
    quantity: int
    avg_price: float

    def __str__(self) -> str:
        """Formats the report for printing with the price rounded to two decimal places."""
        return f"{self.quantity} {self.avg_price:.2f}"


class Hedger:
    """
    Manages market data and calculates hedge trades against incoming risk.
    """
    def __init__(self, bids: List[MarketDataLevel], offers: List[MarketDataLevel]):
        """
        Initializes the Hedger with market data and sorts it for efficient trading.

        Args:
            bids: A list of market data levels available to sell to.
            offers: A list of market data levels available to buy from.
        """
        # Sort bids by price descending to sell to the highest bidder first.
        self.bids = sorted(bids, key=lambda x: x.price, reverse=True)
        # Sort offers by price ascending to buy from the cheapest seller first.
        self.offers = sorted(offers, key=lambda x: x.price)
        # Initialize the cumulative unhedged risk.
        self.unhedged_risk = 0.0

    def hedge_trade(self, trade_report: TradeReport) -> Optional[HedgeReport]:
        """
        Calculates and executes a hedge trade for an incoming trade report.

        The method updates the total unhedged risk, determines the integer
        quantity to trade to offset this risk, executes the trade against the
        market data, and returns a report of the hedge trade.

        Args:
            trade_report: The incoming trade details.

        Returns:
            A HedgeReport detailing the quantity and average price of the executed
            hedge trade. Returns a report with quantity 0 if no hedge is needed.
        """
        # 1. Calculate and accumulate risk.
        incoming_risk = trade_report.quantity * trade_report.risk_per_qty
        self.unhedged_risk += incoming_risk

        # 2. Determine the whole number of units to trade to offset the risk.
        # A positive risk requires a sell (negative quantity).
        # A negative risk requires a buy (positive quantity).
        # int() truncates towards zero, e.g., int(2.9) is 2, int(-2.9) is -2.
        hedge_quantity = -int(self.unhedged_risk)

        # 3. If no trade is needed, return a zero-quantity report.
        if hedge_quantity == 0:
            return HedgeReport(quantity=0, avg_price=0.0)

        # 4. Update the unhedged risk with the amount that is being hedged.
        # The fractional part remains.
        self.unhedged_risk += hedge_quantity

        total_value = 0.0
        total_filled_quantity = 0

        # 5. Execute the trade against the market data.
        if hedge_quantity > 0:  # We need to buy
            quantity_to_buy = hedge_quantity
            for level in self.offers:
                if quantity_to_buy <= 0:
                    break
                fill_quantity = min(quantity_to_buy, level.quantity)
                total_value += fill_quantity * level.price
                total_filled_quantity += fill_quantity
                level.quantity -= fill_quantity
                quantity_to_buy -= fill_quantity
        else:  # We need to sell
            quantity_to_sell = abs(hedge_quantity)
            for level in self.bids:
                if quantity_to_sell <= 0:
                    break
                fill_quantity = min(quantity_to_sell, level.quantity)
                total_value += fill_quantity * level.price
                total_filled_quantity += fill_quantity
                level.quantity -= fill_quantity
                quantity_to_sell -= fill_quantity

        # 6. Calculate the average fill price.
        avg_price = total_value / total_filled_quantity if total_filled_quantity else 0.0

        return HedgeReport(quantity=hedge_quantity, avg_price=avg_price)


def parse_market_data_level(md_line: str) -> List[MarketDataLevel]:
    """Parses a line of market data string into a list of MarketDataLevel objects."""
    tokens = md_line.split()
    return [MarketDataLevel(int(quantity), float(price)) for quantity, price in zip(tokens[::2], tokens[1::2])]


def main() -> None:
    """
    Main function to read input, process trades, and print hedge reports.
    """
    lines_parsed = 0
    hedger = None
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if lines_parsed == 0:
            offers = parse_market_data_level(line)
        elif lines_parsed == 1:
            bids = parse_market_data_level(line)
            hedger = Hedger(bids, offers)
        else:
            split_trade_line = line.split()
            trade_report = TradeReport(int(split_trade_line[0]), float(split_trade_line[1]))
            res = hedger.hedge_trade(trade_report)
            # The problem implies an output for every trade, so we don't check for None.
            print(res)

        lines_parsed += 1


if __name__ == "__main__":
    main()