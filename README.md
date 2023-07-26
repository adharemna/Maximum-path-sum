Maximum Sum Path in Triangle

This project provides Python implementations of different algorithms to find the maximum sum path in a triangle. The problem is to find a path from the top to the bottom of the triangle that maximizes the sum of the values along the path.

Table of Contents
- Description
- Features
- Installation
- Usage
- Algorithms
- Tests
- Contributing


1. Description
The problem is solved using three different algorithms:

* Brute Force: This approach uses recursive backtracking to explore all possible paths from the top to the bottom of the triangle. While it is not the most efficient approach, it provides "the" optimal solution to the problem.

* Divide and Conquer(Heuristic): In this approach, the problem is divided into smaller subproblems by breaking the triangle into two smaller triangles. The algorithm recursively finds the maximum sum path in each smaller triangle and combines the results to find the overall maximum sum path.

* Dynamic Programming (Heuristic): This algorithm uses a heuristic approach to efficiently calculate the maximum sum path. It starts from the bottom of the triangle and iteratively computes the maximum sum for each node by considering its two children.


2.Features
- Provides three different algorithms to find the maximum sum path in a triangle.
- Handles pyramids of various sizes, including large ones.
- Includes comprehensive unit tests to ensure the correctness of the algorithms.
- Offers readable and maintainable code with detailed comments.


3. Installation

Clone the repository to your local machine using the following command:
git clone https://github.com/adharemna/Maximum-path-sum

It requires Python 3 to be ran and one of its most basic libraries (unittest).


4. Usage
To find the maximum sum path in a triangle, you can use the provided algorithms. The two main scripts pyramid_first_trial.py and pyramid_second_trial contains an example usage.

from your_module import solution

file_path = "triangle.txt"
result, path = solution(file_path)

print("Maximum Sum:", result)
print("Path:", path)
Replace your_module with the appropriate module name containing the implementations of the algorithms.


5. Algorithms
* Brute Force Algorithm
The brute force approach uses recursive backtracking to explore all possible paths from the top to the bottom of the triangle. While it guarantees finding the maximum sum path, it is not the most efficient approach for large pyramids.

* Divide and Conquer Algorithm
The divide and conquer algorithm divides the problem into smaller subproblems by breaking the triangle into two smaller triangles. The algorithm recursively finds the maximum sum path in each smaller triangle and combines the results to find the overall maximum sum path. Although the idea seemed tempting, after implementing the algorithm and solving the problem using it, the results were not as promising, which led me to the third algorithm.

* Dynamic Programming (Heuristic) Algorithm
The dynamic programming algorithm uses a heuristic approach to efficiently calculate the maximum sum path. It starts from the bottom of the triangle and iteratively computes the maximum sum for each node by considering its two children. While it is more efficient than the brute force approach, it may not always guarantee the optimal solution.



6. Tests
The project includes comprehensive unit tests to verify the correctness and efficiency of the algorithms. To run the tests, use the following command:

Copy code
python -m unittest test_algorithms.py

7. Contributing
Contributions to the project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
