def alpha():
    all_w = {"A": [[' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' '],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*']],
             "B": [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ']],
             "C": [[' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' '],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' '],
                   [' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ']],
             "D": [['*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
             "E": [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ']],
             "F": [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
             "G": [[' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ']],
             "H": [['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*']],
             "I": [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   [' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']],
             "J": [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*'],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*'],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ']],
             "K": [['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*']],
             "L": [['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']],
             "M": [['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*']],
             "N": [['*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', '*', '*', '*', ' ', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*']],
             "O": [[' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ']],
             "P": [['*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
             "Q": [[' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', ' ', ' ']],
             "R": [['*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*']],
             "S": [[' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*'],
                   [' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' '],
                   ['*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ']],
             "T": [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ']],
             "U": [['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ']],
             "V": [['*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*'],
                   ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ']],
             "W": [['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
                   ['*', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', '*'],
                   ['*', '*', ' ', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', ' ', '*', '*'],
                   [' ', '*', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', '*', ' '],
                   [' ', ' ', '*', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ']],
             "X": [['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
                   [' ', ' ', '*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', ' ', ' '],
                   ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*']],
             "Y": [['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*'],
                   [' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                   [' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ']],
             "Z": [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                   ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']],
             ",": [[' ', ' '],
                   [' ', ' '],
                   [' ', ' '],
                   [' ', ' '],
                   [' ', ' '],
                   [' ', ' '],
                   [' ', ' ']],
             " ": [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]}
    return all_w


# n = ""
# for i in range(7):
#     n = n + input()
# d = []
# s = []
# for ind, i in enumerate(n, start=1):
#     if i == "1":
#         i = "*"
#     else:
#         i = " "
#     s.append(i)
#     if ind % 2 == 0:
#         d.append(s)
#         s = []
#
# for i in d:
#     print(i, ",", sep="")

# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
