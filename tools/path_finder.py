import os


class PathFinder:

    @staticmethod
    def find_path(path: str, cur_dir: str = None):
        if cur_dir is None:
            cur_dir = os.path.abspath(os.curdir)

        if os.path.dirname(cur_dir) == cur_dir:
            return None

        if not os.path.exists(os.path.join(cur_dir, path)):
            cur_dir = os.path.dirname(cur_dir)
            return PathFinder.find_path(path, cur_dir)

        else:
            return os.path.join(cur_dir, path)
