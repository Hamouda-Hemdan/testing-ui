import unittest
from app import canFinish

class TestCourseSchedule(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(canFinish(2, [[1, 0]]))

    def test_example2(self):
        self.assertFalse(canFinish(2, [[1, 0], [0, 1]]))

    def test_no_prerequisites(self):
        self.assertTrue(canFinish(3, []))

    def test_single_course(self):
        self.assertTrue(canFinish(1, []))

    def test_circular_dependency(self):
        self.assertFalse(canFinish(3, [[0, 1], [1, 2], [2, 0]]))

    def test_multiple_courses_with_no_circular_dependency(self):
        self.assertTrue(canFinish(4, [[1, 0], [2, 1], [3, 2]]))

    def test_all_courses_interdependent(self):
        self.assertFalse(canFinish(3, [[0, 1], [1, 2], [2, 0], [0, 2]]))

    def test_large_input(self):
        self.assertTrue(canFinish(500, [[i, i + 1] for i in range(499)]))

    def test_disconnected_graph(self):
        self.assertTrue(canFinish(5, [[1, 0], [3, 2]]))

    def test_single_chain(self):
        self.assertTrue(canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))

    def test_single_course_with_self_dependency(self):
        self.assertFalse(canFinish(1, [[0, 0]]))

if __name__ == '__main__':
    unittest.main()
