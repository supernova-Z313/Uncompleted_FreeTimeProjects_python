"""
a page that have a line of words or else made by the 0 and 1 (or more char) in terminal
all 0 turn randomly to 1 and just what char should change randomly turn to 0
use 3 char to turn different line
use a long list and a player for the word have big than len page
"""


def main():
    from code_ph import words, alphabets

    page = [[" " for i in range(160)] for j in range(31)]
    all_w = alphabets.alpha()

    word_in = input().split(" ")
    while True:
        for i in word_in:
            a = words.Alphabet(i, all_w)
            a.random_alpha(page)

            a.eysak(page, 0.7, 4)

            a.clean_l(page, 0.15, tem="tp,bt", final="*")
            # a.clean_l(page, 0.08, tem="top", final="+")
            a.clean_l(page, 0.03, tem="ri,le", final=" ")

    # input()


if __name__ == "__main__":
    main()

# left_b = []
# for ind, i in enumerate(a.list_word()):
#     lin = []
#     for j in i:
#         lin += j
#     for inx, j in enumerate(lin):
#         if j == "*":
#             left_b.append((ind, inx))
# k_k = int(len(left_b)/8)
# while True:
#     if len(left_b) <= k_k:
#         for x in left_b:
#             ind, inx = x
#             k = ((int(len(i)/2) + 1) * 15) + (int(len(i)/2) * 2)
#             page[12+ind][int((160-k)/2)+inx] = "*"
#         left_b.clear()
#         time.sleep(0.2)
#         os.system("cls")
#         for i in page:
#             print("".join(i))
#         break
#     else:
#         step = random.sample(left_b, k=k_k)
#         for x in step:
#             ind, inx = x
#             k = ((int(len(i)/2) + 1) * 15) + (int(len(i)/2) * 2)
#             f1 = 12+ind
#             f2 = int((160-k)/2)+inx
#             page[f1][f2] = "*"
#             left_b.remove(x)
#         time.sleep(0.2)
#         os.system("cls")
#         for xx in page:
#             print("".join(xx))
