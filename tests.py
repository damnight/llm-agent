import unittest
from functions.get_files_info import get_files_info


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_base_directory(self):
        res = get_files_info("calculator", ".")
        print(res)

    def test_sub_directory(self):
        res = get_files_info("calculator", "pkg")
        print(res)

    def test_invalid_directory(self):
        res = get_files_info("calculator", "/bin")
        print(res)

    def test_super_directory(self):
        res = get_files_info("calculator", "../")
        print(res)




if __name__ == "__main__":
    unittest.main()
