from functions.get_files_info import get_files_info


result1 = get_files_info("calculator", ".")

result2 = get_files_info("calculator", "pkg")

result3 = get_files_info("calculator", "/bin")

result4 = get_files_info("calculator", "../")


print("Result for '.' directory:\n", result1, sep="")
print("\n")
print("Result for 'pkg' directory:\n", result2, sep="")
print("\n")
print("Result for '/bin' directory:\n", result3, sep="")
print("\n")
print("Result for '../' directory:\n", result4, sep="")
print("\n")
