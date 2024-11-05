import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort1(self):
        input = [(data.Book(["Zoe Lee"],"Wonder")), (data.Book(["Tom Holland"],"Moby Dick")), (data.Book(["Bob Ross"],"Outsiders"))]
        expected = [(data.Book(["Tom Holland"], "Moby Dick")), (data.Book(["Bob Ross"],"Outsiders")), (data.Book(["Zoe Lee"],"Wonder"))]
        result = lab6.selection_sort_books(input)
        self.assertEqual(result, expected)

    def test_selection_sort2(self):
        input = [(data.Book(["JK Rowling"], "Harry Potter")), (data.Book(["John Steinbeck"],"Grapes of Wrath")), (data.Book(["F. Scott Fitzgerald"], "Great Gatsby"))]
        expected = [(data.Book(["John Steinbeck"],"Grapes of Wrath")), (data.Book(["F. Scott Fitzgerald"], "Great Gatsby")),(data.Book(["JK Rowling"], "Harry Potter")) ]
        result = lab6.selection_sort_books(input)
        self.assertEqual(result, expected)

    # Part 2
    def test_swap_case1(self):
        input = "Hello World!"
        expected = "hELLO wORLD!"
        result = lab6.swap_case(input)
        self.assertEqual(result, expected)

    def test_swap_case2(self):
        input = "Zoe Lee"
        expected = "zOE lEE"
        result = lab6.swap_case(input)
        self.assertEqual(result, expected)

    # Part 3
    def test_str_translate1(self):
        input = "Zoe Lee"
        expected = "Zoo Loo"
        result = lab6.str_translate(input, "e", "o")
        self.assertEqual(result, expected)

    def test_str_translate2(self):
        input = "abcdcba"
        expected = "xbcdcbx"
        result = lab6.str_translate(input,"a", "x")
        self.assertEqual(result, expected)

    # Part 4
    def test_histogram1(self):
        input = "the happy happy penguin"
        expected = {"the":1, "happy":2, "penguin":1}
        result = lab6.histogram(input)
        self.assertEqual(result, expected)

    def test_histogram2(self):
        input = "Zoe Lee"
        expected = {"Zoe":1, "Lee":1}
        result = lab6.histogram(input)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()
