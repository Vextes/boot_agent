from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def test():
    test1 = get_file_content("calculator", "main.py")
    print("Result for test1:")
    print(f"{test1}\n")

    test2 = get_file_content("calculator", "pkg/calculator.py")
    print("Result for test2:")
    print(f"{test2}\n")
    
    test3 = get_file_content("calculator", "/bin/cat")
    print("Result for test3:")
    print(f"{test3}\n")
    
    test4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for test4:")
    print(f"{test4}\n")

def test_file_info():
    test1 = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(f"{test1}\n")

    test2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(f"{test2}\n")

    test3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(f"{test3}\n")

    test4 = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(f"{test4}\n")

if __name__ == "__main__":
    test()