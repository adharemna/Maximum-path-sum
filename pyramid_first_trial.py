def brute_force_path(triangle):
    def explore_path(row, col):
        if row == len(triangle) - 1:  # Base case: at the bottom row
            return triangle[row][col], ''

        left_sum, left_path = explore_path(row + 1, col)
        right_sum, right_path = explore_path(row + 1, col + 1)

        if left_sum > right_sum:
            return triangle[row][col] + left_sum, 'L' + left_path
        else:
            return triangle[row][col] + right_sum, 'R' + right_path

    max_sum, path = explore_path(0, 0)
    return max_sum, path

def extract_bottom_pyramids(triangle):
    if len(triangle) < 15:
        raise ValueError("The pyramid should have at least 15 rows.")
    
    bottom_pyramids_list = []
    for i in range(len(triangle) - 14):  
        bottom_pyramids_list.append([[0] * u for u in range(1, 16)])
        for j in range(15):
            for k in range(j+1):
                if i+k<len (triangle[len(triangle) - 15 + j]):
                    bottom_pyramids_list[i][j][k]=triangle[len(triangle) - 15 + j][i+k]
    return bottom_pyramids_list

def solution(file):
    # Step 1: Read the file and store the pyramid as a list of lists
    with open(file, 'r') as f:
        pyramid = [list(map(int, line.split())) for line in f]
    
    # Step 2: Make two copies of the large pyramid
    pyramid1 = [row[:] for row in pyramid]
    pyramid2 = [row[:] for row in pyramid]
    
    while len(pyramid1) > 15:
        # Step 4: Extract 15-row pyramids from the bottom of the large pyramid
        bottom_pyramids = extract_bottom_pyramids(pyramid1)

        for i, bottom_pyramid in enumerate(bottom_pyramids):
            # Step 5: Apply the brute_force_path function on each 15-row pyramid
            max_sum, path = brute_force_path(bottom_pyramid)

            # Step 6: Replace the top of the 15-row corresponding pyramid in pyramid1 with the max sum
            pyramid1[len(pyramid1) - 14][i] = max_sum

            # Step 6 (continued): Store the path in pyramid2
            pyramid2[len(pyramid1) - 14][i] = path

        # Step 7: Remove the 15-row pyramids from pyramid1
        pyramid1 = pyramid1[:-15]
    """
    print(pyramid)
    print(bottom_pyramids)"""
    max_sum,path=brute_force_path(pyramid1)
    pyramid2[0][0]=path
    return max_sum, pyramid2

# Usage example:
file_path = "triangle.txt"
result, path = solution(file_path)
print(result, path)
#i got 714 as a result
