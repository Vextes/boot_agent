from functions.get_files_info import get_files_info

def test():
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