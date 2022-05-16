import os


def rename_file(file_path, new_file_name):
    os.rename(file_path, new_file_name)


if __name__ == '__main__':
    rename_file("test.txt", "rename.txt")
