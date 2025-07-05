import unittest
from calculator.pkg import calculator
from functions.get_files_info import get_file_content, get_files_info


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass
    
#   def test_base_directory(self):
#       res = get_files_info("calculator", ".")
#       print(res)
#
#   def test_sub_directory(self):
#       res = get_files_info("calculator", "pkg")
#       print(res)
#
#   def test_invalid_directory(self):
#       res = get_files_info("calculator", "/bin")
#       print(res)
#
#   def test_super_directory(self):
#       res = get_files_info("calculator", "../")
#       print(res)
#
#
#   def test_truncate(self):
#       res = get_file_content("calculator", "lorem.txt")
#       print(res)
#

    def test_successfully_main(self):
        res = get_file_content("calculator", "main.py")
        print(res)

    def test_succesfully_subdir(self):
        res = get_file_content("calculator", "pkg/calculator.py")
        print(res)

    def test_invalid(self):
        res = get_file_content("calculator", "/bin/cat")
        print(res)





if __name__ == "__main__":
    unittest.main()
