def run():
    def Ttt(sys, n):
        if sys == "tw":
            t = 0
            r = 0
            for i in n:
                o = int(i) * (2 ** r)
                t += o
                r += 1
            print(t)
        elif sys == "te":
            u = int(n)
            x = 0
            while 2 ** x < int(n):
                x += 1
            t = ""
            r = 0
            for i in range(x):
                o = str(int(u) % 2)
                t = t + o
                r += 1
                u = u / 2
            if int(n) == 2 ** x:
                t = t + "1"
            RL = []
            u = str(t)
            t = ""
            for i in u:
                RL.append(i)
            RL.reverse()
            for element in RL:
                t = t + element
            print(t)

    n = input("Number -- ")
    Ttt("te", n)