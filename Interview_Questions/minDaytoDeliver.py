#!/bin/python3

def minDaysToDeliverParcels(parcels):
    """
    This function calculates the minimum number of days required
    to deliver all parcels from all delivery centers.
    """
    # Use a set to remove duplicates and count unique positive delivery days
    days_needed = len(set(parcels) - {0})
    return days_needed

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
