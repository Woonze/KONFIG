import os
import tarfile
import argparse

class ShellEmulator:
    def __init__(self, virtual_fs_path):
        self.current_path = "/"
        self.history = []

        self.username = os.getlogin()
        self.virtual_fs_path = virtual_fs_path

        # Извлекаем виртуальную файловую систему
        self.extract_virtual_fs()

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description='Запуск эмулятора командной строки vshell.')
        parser.add_argument('--virtual_fs', type=str, required=True, help='Путь к образу файловой системы (tar или zip).')

        args = parser.parse_args()

        if not os.path.exists(args.virtual_fs):
            parser.error(f"Файл виртуальной файловой системы '{args.virtual_fs}' не найден.")

        return args

    def extract_virtual_fs(self):
        if not os.path.exists(self.virtual_fs_path):
            print("Файл виртуальной файловой системы не найден.")
            exit(1)

        with tarfile.open(self.virtual_fs_path) as tar:
            tar.extractall(path="virtual_fs", filter=tarfile.data_filter)

    def execute_command(self, command):
        command = command.strip()
        if not command:
            return

        self.history.append(command)

        print(f"$ {command}")

        command_dict = {
            "ls": self.list_files,
            "cd": lambda path: self.change_directory(path),
            "pwd": self.print_working_directory,
            "cat": lambda filename: self.cat_file(filename),
            "exit": self.exit_shell,
            "history": self.show_history,
            "touch": lambda filename: self.touch_file(filename),
            "rmdir": lambda dirname: self.remove_directory(dirname),
            "mkdir": lambda dirname: self.mkdir(dirname)
        }

        cmd_func = command_dict.get(command.split()[0], None)

        if cmd_func:
            args = " ".join(command.split()[1:])
            cmd_func(args)
        else:
            print(f"{self.username}: команда не найдена")

    def list_files(self, _):
        try:
            target_path = os.path.normpath(f"virtual_fs{self.current_path}")
            files = os.listdir(target_path)
            output = "\n".join(files) if files else "Пустая директория"
            print(output)
        except FileNotFoundError:
            print(f"Директория '{self.current_path}' не найдена.")
        except Exception as e:
            print(f"Ошибка при выводе содержимого директории: {e}")

    def change_directory(self, path):

        # Проверяем на некорректные сегменты пути
        if any(segment not in ("", ".", "..") and not segment.isalnum() for segment in path.split("/")):
            print(f"Директория '{path}' не найдена или недопустима.")
            return

        path = path.strip()
        if not path or path == "~":
            # Переход в домашнюю директорию (корень)
            self.current_path = "/"
            print("Перешли в домашнюю директорию: /")
            return

        # Проверка на некорректный путь (например, слишком много точек)
        if any(segment not in ("", ".", "..") and not segment.isalnum() for segment in path.split("/")):
            print(f"Директория '{path}' не найдена или недопустима.")
            return

        if path == "..":
            # Переход на уровень выше
            if self.current_path != "/":
                self.current_path = os.path.dirname(self.current_path.rstrip("/")) or "/"
            print(f"Текущая директория: {self.current_path}")
            return

        # Абсолютный путь
        if path.startswith("/"):
            new_path = os.path.normpath(f"virtual_fs{path}")
            virtual_path = os.path.normpath(path)
        else:
            # Относительный путь
            new_path = os.path.normpath(os.path.join(f"virtual_fs{self.current_path}", path))
            virtual_path = os.path.normpath(os.path.join(self.current_path, path))

        # Проверяем существование директории
        if os.path.isdir(new_path):
            self.current_path = virtual_path
            print(f"Перешли в директорию: {self.current_path}")
        else:
            print(f"Директория '{path}' не найдена или не является директорией.")

    def print_working_directory(self, _):
        print(f"{self.username}:{self.current_path}")

    def cat_file(self, filename):
        try:
            with open(os.path.join(f"virtual_fs{self.current_path}", filename), 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Файл не найден")

    def touch_file(self, filename):
        try:
            file_path = os.path.join(f"virtual_fs{self.current_path}", filename.strip())
            with open(file_path, 'a'):
                pass
            print(f"Файл '{filename}' создан.")
        except Exception as e:
            print(f"Ошибка при создании файла '{filename}': {str(e)}")

    def show_history(self, _):
        history_output = "\n".join(self.history) or "История пуста"
        print(f"История команд:\n{history_output}")

    def remove_directory(self, dirname):
        if not dirname.strip():
            print("Укажите имя директории для удаления")
            return

        dir_path = os.path.join(f"virtual_fs{self.current_path}", dirname.strip())
        try:
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                os.rmdir(dir_path)
                print(f"Директория '{dirname.strip()}' удалена.")
            else:
                print("Директория не найдена или не пуста")
        except Exception as e:
            print(f"Ошибка при удалении директории '{dirname.strip()}': {e}")

    def mkdir(self, dirname):
        if not dirname.strip():
            print("Укажите имя директории для создания")
            return
        dir_path = os.path.join(f"virtual_fs{self.current_path}", dirname.strip())
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Директория '{dirname.strip()}' создана.")
        except Exception as e:
            print(f"Ошибка при создании директории: {e}")

    def exit_shell(self, _):
        print("Выход из эмулятора...")
        exit(0)

if __name__ == "__main__":
    args = ShellEmulator.parse_arguments()
    emulator = ShellEmulator(args.virtual_fs)

    while True:
        command = input(f"{emulator.username}:{emulator.current_path} $ ")
        emulator.execute_command(command)
