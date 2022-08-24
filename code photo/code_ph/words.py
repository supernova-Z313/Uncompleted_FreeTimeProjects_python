import time, os, random


class Alphabet:
    def __init__(self, word="", all_ww=dict):
        self.word = [[] for x in range(7)]
        word = word.upper()
        self.l_w = []
        for ite in word:
            self.l_w.append(ite)
        word = ",".join(self.l_w)
        for z in word:
            for ind, c in enumerate(all_ww[z]):
                self.word[ind].append(c)

    def list_word(self):
        return self.word

    def random_alpha(self, page_1):
        self.left_b = []
        self.page = page_1
        for self.ind, self.i in enumerate(self.list_word()):
            self.lin = []
            for self.j in self.i:
                self.lin += self.j
            for self.inx, self.j in enumerate(self.lin):
                if self.j == "*":
                    self.left_b.append((self.ind, self.inx))
        self.k_k = int(len(self.left_b)/8)
        while True:
            if len(self.left_b) <= self.k_k:
                for self.x in self.left_b:
                    self.ind, self.inx = self.x
                    self.k = ((int(len(self.i)/2) + 1) * 15) + (int(len(self.i)/2) * 2)
                    self.page[12+self.ind][int((160-self.k)/2)+self.inx] = "*"
                self.left_b.clear()
                time.sleep(0.2)
                os.system("clear")
                for self.i in self.page:
                    print("".join(self.i))
                break
            else:
                self.step = random.sample(self.left_b, k=self.k_k)
                for self.x in self.step:
                    self.ind, self.inx = self.x
                    self.k = ((int(len(self.i)/2) + 1) * 15) + (int(len(self.i)/2) * 2)
                    self.f1 = 12+self.ind
                    self.f2 = int((160-self.k)/2)+self.inx
                    self.page[self.f1][self.f2] = "*"
                    self.left_b.remove(self.x)
                time.sleep(0.2)
                os.system("clear")
                for self.xx in self.page:
                    print("".join(self.xx))

    def eysak(self, page_2, ti, odd, rever=False):
        for s in range(odd):
            for ind, i in enumerate(page_2):
                for inx, g in enumerate(i):
                    if g == " ":
                        page_2[ind][inx] = "*"
                    else:
                        page_2[ind][inx] = " "
            if rever:
                page_2.reverse()
            time.sleep(ti)
            os.system("clear")
            for x in page_2:
                print("".join(x))
        time.sleep(ti)

    def clean_l(self, page, ti, tem="top", final=" "):

        if tem == "top":
            for ind, i in enumerate(page):
                for inx, g in enumerate(i):
                    page[ind][inx] = final
                time.sleep(ti)
                os.system("clear")
                for x in page:
                    print("".join(x))

        elif tem == "tp,bt":
            len_p = len(page)
            for ind, i in enumerate(page):
                for inx, g in enumerate(i):
                    page[ind][inx] = final
                    page[len_p-ind-1][inx] = final
                time.sleep(ti)
                os.system("clear")
                for x in page:
                    print("".join(x))
                if ind >= len_p/2:
                    break

        elif tem == "ri,le":
            len_c = len(page[0])
            for ind, i in enumerate(page[0]):
                for g in range(len(page)):
                    page[g][ind] = final
                    page[g][len_c-ind-1] = final
                time.sleep(ti)
                os.system("clear")
                for x in page:
                    print("".join(x))
                if ind >= len_c/2:
                    break
