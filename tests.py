from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    test1 = run_python_file("calculator", "main.py")
    print("Result for test1:")
    print(f"{test1}\n")
    
    test2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for test2:")
    print(f"{test2}\n")
    
    test3 = run_python_file("calculator", "tests.py")
    print("Result for test3:")
    print(f"{test3}\n")
    
    test4 = run_python_file("calculator", "../main.py")
    print("Result for test4:")
    print(f"{test4}\n")
    
    test5 = run_python_file("calculator", "nonexistent.py")
    print("Result for test5:")
    print(f"{test5}\n")
    
    test6 = run_python_file("calculator", "lorem.txt")
    print("Result for test6:")
    print(f"{test6}\n")


def test_write_file():
    test1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for test1:")
    print(f"{test1}\n")
    
    test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for test2:")
    print(f"{test2}\n")
    
    test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for test3:")
    print(f"{test3}\n")

def test_file_content():
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