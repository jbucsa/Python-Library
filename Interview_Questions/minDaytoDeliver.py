#!/bin/python3

def minDaysToDeliverParcels(parcels):
    """
    Simulates day-by-day parcel delivery until all centers have 0 parcels.
    Returns the number of days required.
    """
    days = 0

    while any(p > 0 for p in parcels):
        # Find the minimum non-zero value (daily delivery amount)
        min_nonzero = min(p for p in parcels if p > 0)

        # Subtract that from all non-zero centers
        parcels = [p - min_nonzero if p > 0 else 0 for p in parcels]

        days += 1

    return days

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parcels_count = int(input().strip())
    parcels = []

    for _ in range(parcels_count):
        parcels_item = int(input().strip())
        parcels.append(parcels_item)

    result = minDaysToDeliverParcels(parcels)
    fptr.write(str(result) + '\n')
    fptr.close()
