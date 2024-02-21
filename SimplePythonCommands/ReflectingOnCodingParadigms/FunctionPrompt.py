#  Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

Q1. How does this solution ensure data immutability?
    A. This solution does not ensure data immutability. Data immutability refers to the inability to change the state of data after it has been created. However, in this solution, the 'arr' list is mutable, and its content can be changed. For instance, appending elements to the 'arr' list and sorting it modifies its state. To ensure data immutability, one could use immutable data structures or avoid modifying existing data structures. 


Q2. Is this solution a pure function? Why or why not?
    A. No, this solution is not a pure function. A pure function is a function that, given the same input, will always produce the same output and has no side effects. In this solution, the 'sorted' function is used, which may produce different outputs for the same input if the input list 'array' contains elements with different values. Additionally, the function modifies the state of the 'arr' list, which is a side effect.


Q3. Is this solution a higher order function? Why or why not?
    A. No, this solution is not a higher-order function. A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. The 'flatten_and_sort' function in this solution neither takes a function as an argument nor returns a function as its result.


Q4. Would it have been easier to solve this problem using a different programming style?
    A. The choice of programming style depends on various factors such as the problem requirements, the developer's familiarity with different paradigms, and the trade-offs between different approaches. While the provided solution works, solving the problem using a functional programming style might offer advantages such as clearer code structure, better support for immutable data, and easier reasoning about the code's behavior, especially for operations like mapping, filtering, and reducing collections.


Q5. Why in particular is functional programming a helpful paradigm when solving this problem?
    A. Functional programming emphasizes the use of immutable data and pure functions, which can simplify reasoning about the code and reduce the likelihood of bugs, especially in concurrent or parallel environments. In this problem, functional programming could facilitate the transformation of the input list by applying functions like mapping, filtering, and sorting in a declarative and composable manner, potentially leading to more concise and readable code. Additionally, functional programming encourages the use of higher-order functions, which can promote code reuse and modularity.

'''