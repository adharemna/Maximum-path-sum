import unittest
from pyramid_first_trial import brute_force_path
from pyramid_second_trial import find_maximum_total_path

class TestBruteForcePath(unittest.TestCase):
    def test_small_pyramid(self):
        pyramid = [
            [3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3],
        ]
        expected_result = 23
        _, path = brute_force_path(pyramid)
        self.assertEqual(_, expected_result)

    def test_medium_pyramid(self):
        pyramid = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
        ]
        expected_result = 390
        _, path = brute_force_path(pyramid)
        self.assertEqual(_, expected_result)


class TestFindMaximumTotalPath(unittest.TestCase):
    def test_small_pyramid(self):
        pyramid = [
            [3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3],
        ]
        expected_result = 23
        result = find_maximum_total_path(pyramid)
        self.assertEqual(result, expected_result)

    def test_medium_pyramid(self):
        pyramid = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
        ]
        expected_result = 390
        result = find_maximum_total_path(pyramid)
        self.assertEqual(result, expected_result)


        
if __name__ == '__main__':
    unittest.main()
