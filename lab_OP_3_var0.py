import sys


if len(sys.argv) > 1:
    formulaa = ""
    for i in range(1, len(sys.argv)):
        formulaa = str(formulaa) + str(sys.argv[i])
    print("Result: ")
else:
    print("ERROR")