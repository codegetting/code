
def read_file(file_path):
    with open(file_path) as r:
        for line in r.read():
            print(line, end='')


if __name__ == '__main__':
    read_file("testfile")
