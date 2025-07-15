# A problem requiring you to write a solution using Python. 
# Below is the tarter code. Please use this to maximize your time in solving the problem. 
# Please use Python 3 for this problem. 

import math
import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MarketDataLevel:
    quantity: int
    price: float


@dataclass
class TradeReport:
    quantity: int
    risk_per_qty: float


@dataclass
class HedgeReport:
    quantity: int
    avg_price: float

    def __str__(self) -> str:
        return f"{self.quantity} {self.avg_price:.2f}"


class Hedger:
    def __init__(self, bids: List[MarketDataLevel], offers: List[MarketDataLevel]):
        raise NotImplementedError("# todo - candidate")

    def hedge_trade(self, tradeReport: TradeReport) -> Optional[HedgeReport]:
        raise NotImplementedError("# todo - candidate")


def parse_market_data_level(md_line: str) -> List[MarketDataLevel]:
    tokens = md_line.split()
    return [MarketDataLevel(int(quantity), float(price)) for quantity, price in zip(tokens[::2], tokens[1::2])]


def main() -> None:
    lines_parsed = 0
    hedger = None
    for line in sys.stdin:
        if lines_parsed == 0:
            offers = parse_market_data_level(line)
        elif lines_parsed == 1:
            bids = parse_market_data_level(line)
            hedger = Hedger(bids, offers)
        else:
            split_trade_line = line.split()
            trade_report = TradeReport(int(split_trade_line[0]), float(split_trade_line[1]))
            res = hedger.hedge_trade(trade_report)
            if res is not None:
                print(res)

        lines_parsed += 1


if __name__ == "__main__":
    main()
