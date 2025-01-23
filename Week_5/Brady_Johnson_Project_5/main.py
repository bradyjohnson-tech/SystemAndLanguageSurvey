# Date: 11/21/2024
# Brady Johnson
# IDE: Pycharm
# macOSSequoia v15.1

import os
import shutil
import random


def create_folder():
    folder_name = input("Please enter the name of the folder you want to created: ")

    cwd = os.getcwd()
    path = os.path.join(cwd, folder_name)

    if os.path.exists(path) and os.path.isdir(path):
        print(f"Folder '{folder_name}' already exists... Removing it.")
        shutil.rmtree(path)

    os.makedirs(path)
    print(f"Folder '{folder_name}' has been created at {path}")

    return path


def generate_random_numbers_and_save(file_path):
    random_numbers = [random.randint(0, 1000) for _ in range(100)]

    with open(file_path, 'w') as file:
        for number in random_numbers:
            file.write(f"{number}\n")

    print(f"100 random numbers have been generated and saved to {file_path}")


def main():
    folder_path = create_folder()
    file_path = os.path.join(folder_path, "numbers100.txt")
    generate_random_numbers_and_save(file_path)


if __name__ == "__main__":
    main()