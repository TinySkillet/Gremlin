from functions import run_python_file


# result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

# print(result1)
# print(result2)
# print(result3)

result1 = run_python_file("calculator", "main.py")
result2 = run_python_file("calculator", "main.py", ["3 + 5"])
result3 = run_python_file("calculator", "tests.py")
result4 = run_python_file("calculator", "../main.py")
result5 = run_python_file("calculator", "nonexistent.py")

print(result1, result2, result3, result4, result5, sep="\n\n")

# result1 = get_files_info("calculator", ".")

# result2 = get_files_info("calculator", "pkg")

# result3 = get_files_info("calculator", "/bin")

# result4 = get_files_info("calculator", "../")


# print("Result for '.' directory:\n", result1, sep="")
# print("\n")
# print("Result for 'pkg' directory:\n", result2, sep="")
# print("\n")
# print("Result for '/bin' directory:\n", result3, sep="")
# print("\n")
# print("Result for '../' directory:\n", result4, sep="")
# print("\n")

# result1 = get_file_content("calculator", "main.py")
# result2 = get_file_content("calculator", "pkg/calculator.py")
# result3 = get_file_content("calculator", "bin/cat")
# result4 = get_file_content("calculator", "pkg/does_not_exist.py")
# result5 = get_file_content("calculator", "lorem.txt")

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
