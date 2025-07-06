from subprocess import run
import unittest
from calculator.pkg import calculator
from functions.get_files_info import get_file_content, get_files_info, write_file
from functions.run_python import run_python_file


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
#
#   def test_successfully_main(self):
#       res = get_file_content("calculator", "main.py")
#       print(res)
#
#   def test_succesfully_subdir(self):
#       res = get_file_content("calculator", "pkg/calculator.py")
#       print(res)
#
#   def test_invalid(self):
#       res = get_file_content("calculator", "/bin/cat")
#       print(res)
#
#   def test_write_base_directory(self):
#       res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#       print(res)
#   
#   def test_write_sub_directory(self):
#       res = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#       print(res)
#
#
#   def test_write_invalid(self):
#       res = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#       print(res)

    def test_main_file(self):
        res = run_python_file("calculator", "main.py")
        print(res)

    def test_different_file(self):
        res = run_python_file("calculator", "tests.py")
        print(res)

    def test_super_dir_file(self):
        res = run_python_file("calculator", "../main.py")
        print(res)

    def test_invalid_file(self):
        res = run_python_file("calculator", "nonexistent.py")
        print(res)


if __name__ == "__main__":
    unittest.main()
