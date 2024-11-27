import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import tkinter as tk
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.emulator = ShellEmulator(self.root, "virtual_fs.tar")

    # Тесты для list_files
    @patch('os.listdir', return_value=['file1.txt', 'file2.txt'])
    def test_list_files_success(self, mock_listdir):
        self.emulator.list_files()
        self.assertIn("file1.txt", self.emulator.text_area.get("1.0", tk.END))
        self.assertIn("file2.txt", self.emulator.text_area.get("1.0", tk.END))

    @patch('os.listdir', side_effect=FileNotFoundError)
    def test_list_files_directory_not_found(self, mock_listdir):
        self.emulator.list_files()
        self.assertIn("Директория не найдена", self.emulator.text_area.get("1.0", tk.END))

    @patch('os.listdir', return_value=[])
    def test_list_files_empty_directory(self, mock_listdir):
        self.emulator.list_files()
        self.assertIn("Директория пуста", self.emulator.text_area.get("1.0", tk.END))

    # Тесты для change_directory
    @patch('os.path.isdir', return_value=True)
    def test_change_directory_success(self, mock_isdir):
        self.emulator.change_directory("subdir")
        self.assertEqual(self.emulator.current_path, "/subdir")

    @patch('os.path.isdir', return_value=False)
    def test_change_directory_not_found(self, mock_isdir):
        self.emulator.change_directory("nonexistent")
        self.assertIn("Директория не найдена", self.emulator.text_area.get("1.0", tk.END))

    @patch('os.path.isdir', return_value=True)
    def test_change_directory_root(self, mock_isdir):
        self.emulator.change_directory("/")
        self.assertEqual(self.emulator.current_path, "/")

    # Тесты для print_working_directory
    def test_print_working_directory_root(self):
        self.emulator.current_path = "/"
        self.emulator.print_working_directory()
        self.assertIn(f"{self.emulator.username}:/", self.emulator.text_area.get("1.0", tk.END))

    def test_print_working_directory_subdir(self):
        self.emulator.current_path = "/subdir"
        self.emulator.print_working_directory()
        self.assertIn(f"{self.emulator.username}:/subdir", self.emulator.text_area.get("1.0", tk.END))

    def test_print_working_directory_empty(self):
        self.emulator.current_path = ""
        self.emulator.print_working_directory()
        self.assertIn(f"{self.emulator.username}:/", self.emulator.text_area.get("1.0", tk.END))

    # Тесты для cat_file
    @patch('builtins.open', new_callable=mock_open, read_data="file content")
    def test_cat_file_success(self, mock_file):
        self.emulator.cat_file("file1.txt")
        self.assertIn("file content", self.emulator.text_area.get("1.0", tk.END))

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_cat_file_not_found(self, mock_file):
        self.emulator.cat_file("nonexistent.txt")
        self.assertIn("Файл не найден", self.emulator.text_area.get("1.0", tk.END))

    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_cat_file_empty(self, mock_file):
        self.emulator.cat_file("emptyfile.txt")
        self.assertIn("Файл пуст", self.emulator.text_area.get("1.0", tk.END))

    # Тесты для touch_file
    @patch('builtins.open', new_callable=mock_open)
    def test_touch_file_success(self, mock_file):
        self.emulator.touch_file("newfile.txt")
        self.assertIn("Файл 'newfile.txt' создан.", self.emulator.text_area.get("1.0", tk.END))

    @patch('os.path.exists', return_value=True)
    def test_touch_file_exists(self, mock_exists):
        self.emulator.touch_file("existingfile.txt")
        self.assertIn("Файл уже существует", self.emulator.text_area.get("1.0", tk.END))

    @patch('builtins.open', side_effect=PermissionError)
    def test_touch_file_permission_error(self, mock_file):
        self.emulator.touch_file("protectedfile.txt")
        self.assertIn("Ошибка создания файла", self.emulator.text_area.get("1.0", tk.END))

    # Тесты для show_history
    def test_show_history_non_empty(self):
        self.emulator.history = ["ls", "pwd", "cd subdir"]
        self.emulator.show_history()
        self.assertIn("ls\npwd\ncd subdir", self.emulator.text_area.get("1.0", tk.END))

    def test_show_history_empty(self):
        self.emulator.history = []
        self.emulator.show_history()
        self.assertIn("История команд пуста", self.emulator.text_area.get("1.0", tk.END))

    def test_show_history_partial(self):
        self.emulator.history = ["ls"]
        self.emulator.show_history()
        self.assertIn("ls", self.emulator.text_area.get("1.0", tk.END))

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()