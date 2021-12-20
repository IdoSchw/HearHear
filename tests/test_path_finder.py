import unittest
import os

from tools.path_finder import PathFinder


class TestPathFinder(unittest.TestCase):

    def test_path_finder(self):
        path_finder_file_true_location = os.path.join(os.path.dirname(os.path.abspath(os.path.curdir)), 'tools', 'path_finder.py')
        path_finder_location_by_function = PathFinder.find_path(os.path.join('tools', 'path_finder.py'))
        self.assertEqual(path_finder_file_true_location, path_finder_location_by_function)
