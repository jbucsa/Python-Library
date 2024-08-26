def isPower(arr):
    result = []
    for x in arr:
        if x > 0 and (x & (x - 1)) == 0:  # Check if x is a power of 2
            result.append(1)
        else:
            result.append(0)
    return result

# The rest of the provided code (main function and file handling) remains the same.