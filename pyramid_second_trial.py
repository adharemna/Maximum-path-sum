def find_maximum_total_path(triangle):
    n = len(triangle)

    for row in range(n - 2, -1, -1):
        for col in range(len(triangle[row])):
            left_child = triangle[row + 1][col]
            right_child = triangle[row + 1][col + 1]

            if left_child > right_child:
                triangle[row][col] += left_child
            else:
                triangle[row][col] += right_child

    max_sum = triangle[0][0]

    return max_sum

def read_pyramid_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    pyramid = [[int(num) for num in line.strip().split()] for line in lines]

    return pyramid

def solution(file_path):
    pyramid = read_pyramid_file(file_path)
    max_sum= find_maximum_total_path(pyramid)
    return max_sum

# Example usage
file_path = 'triangle.txt'
max_sum= solution(file_path)
print("Maximum Sum:", max_sum)
#it had a Maximum Sum: 7273, way better than the first algorithm

