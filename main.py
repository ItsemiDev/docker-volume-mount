import os


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


def read_files_from_folder(folder):
    for filename in os.listdir(folder):
        f = os.path.join(folder, filename)
        print(f"Reading the file: {f}", flush=True)
        if os.path.isfile(f):
            print(read_file(f), flush=True)


if __name__ == "__main__":
    read_files_from_folder("./input")
