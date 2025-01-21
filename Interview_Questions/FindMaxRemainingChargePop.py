def transform_list(A):
    """
    Transforms the input list A[] into a new list B[] following the given rules:
    1. B[i] = A[i-1] + A[i+1] (if both exist)
    2. B[i] = A[i+1] (if A[i-1] does not exist)
    3. B[i] = A[i-1] (if A[i+1] does not exist)
    4. B[i] = A[i] (if both A[i-1] and A[i+1] do not exist)
    """
    n = len(A)
    B = []
    
    for i in range(n):
        if i == 0:  # No A[i-1]
            if i + 1 < n:  # Check if A[i+1] exists
                B.append(A[i + 1])
            else:  # Only A[i] exists
                B.append(A[i])
        elif i == n - 1:  # No A[i+1]
            B.append(A[i - 1])
        else:  # Both A[i-1] and A[i+1] exist
            B.append(A[i - 1] + A[i + 1])
    
    return B

def find_max_index(B):
    """
    Identifies the index of the maximum value in the list B[].
    """
    max_value = max(B)  # Find the maximum value in B
    max_index = B.index(max_value)  # Find the first occurrence of the maximum value
    return max_index, max_value

def find_min_index(B):
    """
    Identifies the index of the maximum value in the list B[].
    """
    min_value = min(B)  # Find the maximum value in B
    min_index = B.index(min_value)  # Find the first occurrence of the maximum value
    return min_index, min_value

def process_after_max(A, B):
    """
    After identifying the maximum value index i-max in B[], perform the following:
    1. Replace A[i-max] with B[i-max].
    2. Remove A[(i-max)-1] and A[(i-max)+1] from A.
    3. Handle edge cases where neighbors may not exist.
    """
    i_max, b_max = find_max_index(B)
    
    # Step 1: Replace A[i-max] with B[i-max]
    A[i_max] = b_max
    
    # Step 2: Remove neighbors of A[i-max] (if they exist)
    if i_max + 1 < len(A) and i_max - 1 >= 0:  # Both neighbors exist
        del A[i_max + 1]
        del A[i_max - 1]
    elif i_max + 1 < len(A):  # Only the right neighbor exists
        del A[i_max + 1]
    elif i_max - 1 >= 0:  # Only the left neighbor exists
        del A[i_max - 1]
    # If neither neighbor exists, no further deletion is needed
    
    return A

def process_after_min(A, B):
    """
    After identifying the maximum value index i-max in B[], perform the following:
    1. Replace A[i-max] with B[i-max].
    2. Remove A[(i-max)-1] and A[(i-max)+1] from A.
    3. Handle edge cases where neighbors may not exist.
    """
    i_min, b_min = find_min_index(B)
    
    # Step 1: Replace A[i-min] with B[i-min]
    A[i_min] = b_min
    
    # Step 2: Remove neighbors of A[i-min] (if they exist)
    if i_min + 1 < len(A) and i_min - 1 >= 0:  # Both neighbors exist
        del A[i_min + 1]
        del A[i_min - 1]
    elif i_min + 1 < len(A):  # Only the right neighbor exists
        del A[i_min + 1]
    elif i_min - 1 >= 0:  # Only the left neighbor exists
        del A[i_min - 1]
    # If neither neighbor exists, no further deletion is needed
    
    return A


# Example usage:
A = [1, 2, 3, 4, 5]
B = transform_list(A)
print("Input List A:", A)
print("Transformed List B:", B)

# Perform operations after finding the maximum
A = process_after_max(A, B)
print("Modified List A after processing:", A)

# Now lets put all of these functions together.

def reduce_list_to_one_max(A):
    """
    Repeatedly transforms the list A[] using the following steps:
    1. Compute B[] from A[] using the transformation rules.
    2. Find the maximum value in B[] and its index.
    3. Replace A[i-max] with B[i-max].
    4. Remove neighbors of A[i-max] from A[].
    5. Continue until A[] is reduced to a single element.
    """
    while len(A) > 1:
        # Step 1: Transform A[] into B[]
        n = len(A)
        B = []
        for i in range(n):
            if i == 0:  # No A[i-1]
                if i + 1 < n:  # Check if A[i+1] exists
                    B.append(A[i + 1])
                else:  # Only A[i] exists
                    B.append(A[i])
            elif i == n - 1:  # No A[i+1]
                B.append(A[i - 1])
            else:  # Both A[i-1] and A[i+1] exist
                B.append(A[i - 1] + A[i + 1])
        
        # Step 2: Find the maximum value in B[] and its index
        i_max = B.index(max(B))
        b_max = B[i_max]
        
        # Step 3: Replace A[i-max] with B[i-max]
        A[i_max] = b_max
        
        # Step 4: Remove neighbors of A[i-max] from A[]
        if i_max + 1 < len(A) and i_max - 1 >= 0:  # Both neighbors exist
            del A[i_max + 1]
            del A[i_max - 1]
        elif i_max + 1 < len(A):  # Only the right neighbor exists
            del A[i_max + 1]
        elif i_max - 1 >= 0:  # Only the left neighbor exists
            del A[i_max - 1]
        # If neither neighbor exists, no further deletion is needed
    
    return A[0]  # Return the remaining single element

# Example usage:
A = [1, 2, 3, 4, 5]
result = reduce_list_to_one_max(A)
print("Final Result:", result)


def reduce_list_to_one_min(A):
    """
    Repeatedly transforms the list A[] using the following steps:
    1. Compute B[] from A[] using the transformation rules.
    2. Find the minimum value in B[] and its index.
    3. Replace A[i-min] with B[i-min].
    4. Remove neighbors of A[i-min] from A[].
    5. Continue until A[] is reduced to a single element.
    """
    while len(A) > 1:
        # Step 1: Transform A[] into B[]
        n = len(A)
        B = []
        for i in range(n):
            if i == 0:  # No A[i-1]
                if i + 1 < n:  # Check if A[i+1] exists
                    B.append(A[i + 1])
                else:  # Only A[i] exists
                    B.append(A[i])
            elif i == n - 1:  # No A[i+1]
                B.append(A[i - 1])
            else:  # Both A[i-1] and A[i+1] exist
                B.append(A[i - 1] + A[i + 1])
        
        # Step 2: Find the minimum value in B[] and its index
        i_min = B.index(min(B))
        b_min = B[i_min]
        
        # Step 3: Replace A[i-min] with B[i-min]
        A[i_min] = b_min
        
        # Step 4: Remove neighbors of A[i-min] from A[]
        if i_min + 1 < len(A) and i_min - 1 >= 0:  # Both neighbors exist
            del A[i_min + 1]
            del A[i_min - 1]
        elif i_min + 1 < len(A):  # Only the right neighbor exists
            del A[i_min + 1]
        elif i_min - 1 >= 0:  # Only the left neighbor exists
            del A[i_min - 1]
        # If neither neighbor exists, no further deletion is needed
    
    return A[0]  # Return the remaining single element

# Example usage:
A = [1, 2, 3, 4, 5]
result = reduce_list_to_one_min(A)
print("Final Result:", result)



def reduce_list_to_oneMax(A):
    """
    Repeatedly transforms the list A[] using the following steps:
    1. Compute B[] from A[] using the transformation rules.
    2. Find the maximum value in B[] and its index.
    3. Replace A[i-max] with B[i-max].
    4. Remove neighbors of A[i-max] from A[].
    5. Continue until A[] is reduced to a single element.
    Returns the final value and the number of steps taken.
    """
    steps = 0  # Initialize step counter

    while len(A) > 1:
        steps += 1  # Increment the step counter
        
        # Step 1: Transform A[] into B[]
        n = len(A)
        B = []
        for i in range(n):
            if i == 0:  # No A[i-1]
                if i + 1 < n:  # Check if A[i+1] exists
                    B.append(A[i + 1])
                else:  # Only A[i] exists
                    B.append(A[i])
            elif i == n - 1:  # No A[i+1]
                B.append(A[i - 1])
            else:  # Both A[i-1] and A[i+1] exist
                B.append(A[i - 1] + A[i + 1])
        
        # Step 2: Find the maximum value in B[] and its index
        i_max = B.index(max(B))
        b_max = B[i_max]
        
        # Step 3: Replace A[i-max] with B[i-max]
        A[i_max] = b_max
        
        # Step 4: Remove neighbors of A[i-max] from A[]
        if i_max + 1 < len(A) and i_max - 1 >= 0:  # Both neighbors exist
            del A[i_max + 1]
            del A[i_max - 1]
        elif i_max + 1 < len(A):  # Only the right neighbor exists
            del A[i_max + 1]
        elif i_max - 1 >= 0:  # Only the left neighbor exists
            del A[i_max - 1]
        # If neither neighbor exists, no further deletion is needed
    
    return A[0], steps  # Return the remaining single element and the step count

# Example usage:
A = [1, 2, 3, 4, 5]
result, steps = reduce_list_to_oneMax(A)
print("Final Result:", result)
print("Total Steps Taken:", steps)




def reduce_list_to_oneMin(A):
    """
    Repeatedly transforms the list A[] using the following steps:
    1. Compute B[] from A[] using the transformation rules.
    2. Find the minimum value in B[] and its index.
    3. Replace A[i-min] with B[i-min].
    4. Remove neighbors of A[i-min] from A[].
    5. Continue until A[] is reduced to a single element.
    Returns the final value and the number of steps taken.
    """
    steps = 0  # Initialize step counter

    while len(A) > 1:
        steps += 1  # Increment the step counter
        
        # Step 1: Transform A[] into B[]
        n = len(A)
        B = []
        for i in range(n):
            if i == 0:  # No A[i-1]
                if i + 1 < n:  # Check if A[i+1] exists
                    B.append(A[i + 1])
                else:  # Only A[i] exists
                    B.append(A[i])
            elif i == n - 1:  # No A[i+1]
                B.append(A[i - 1])
            else:  # Both A[i-1] and A[i+1] exist
                B.append(A[i - 1] + A[i + 1])
        
        # Step 2: Find the minimum value in B[] and its index
        i_min = B.index(min(B))
        b_min = B[i_min]
        
        # Step 3: Replace A[i-min] with B[i-min]
        A[i_min] = b_min
        
        # Step 4: Remove neighbors of A[i-min] from A[]
        if i_min + 1 < len(A) and i_min - 1 >= 0:  # Both neighbors exist
            del A[i_min + 1]
            del A[i_min - 1]
        elif i_min + 1 < len(A):  # Only the right neighbor exists
            del A[i_min + 1]
        elif i_min - 1 >= 0:  # Only the left neighbor exists
            del A[i_min - 1]
        # If neither neighbor exists, no further deletion is needed
    
    return A[0], steps  # Return the remaining single element and the step count

# Example usage:
A = [1, 2, 3, 4, 5]
result, steps = reduce_list_to_oneMin(A)
print("Final Result:", result)
print("Total Steps Taken:", steps)

