def hesab(gol1, gol2, p1, p2):

    if gol1 == p1 and gol2 == p2:
        return 10

    if gol1 > gol2:
        natije1 = 1
    elif gol1 < gol2:
        natije1 = -1
    else:
        natije1 = 0

    if p1 > p2:
        natije2 = 1
    elif p1 < p2:
        natije2 = -1
    else:
        natije2 = 0

    if natije1 == natije2:

        tafavot1 = gol1 - gol2
        tafavot2 = p1 - p2

        if tafavot1 - tafavot2 <= 1 and tafavot1 - tafavot2 >= -1:
            return 7
        else:
            return 5

    else:
        return 2


team = []

for i in range(6):
    name = input("نام تیم " + str(i + 1) + " را وارد کنید: ")
    team.append(name)


bazikon = []

for i in range(5):
    name = input("نام شرکت کننده " + str(i + 1) + " را وارد کنید: ")
    bazikon.append(name)


emtiaz = [0, 0, 0, 0, 0]


bazi = [
    [[0, 5], [1, 4], [2, 3]],
    [[0, 4], [5, 3], [1, 2]],
    [[0, 3], [4, 2], [5, 1]],
    [[0, 2], [3, 1], [4, 5]],
    [[0, 1], [2, 5], [3, 4]]
]


hafte = ["اول", "دوم", "سوم", "چهارم", "پنجم"]

for week in range(5):

    print()
    print("******** هفته", hafte[week], "********")
    print()

    for match in range(3):

        t1 = bazi[week][match][0]
        t2 = bazi[week][match][1]

        print("مسابقه:", team[t1], "با", team[t2])

        pish1 = []
        pish2 = []

        for p in range(5):

            print("پیش بینی", bazikon[p])

            g1 = int(input("پیش بینی گل " + team[t1] + ": "))
            g2 = int(input("پیش بینی گل " + team[t2] + ": "))

            pish1.append(g1)
            pish2.append(g2)

        print()
        print("نتیجه واقعی مسابقه را وارد کنید")

        gol1 = int(input("گل " + team[t1] + ": "))
        gol2 = int(input("گل " + team[t2] + ": "))

        print("نتیجه مسابقه:", team[t1], gol1, "-", gol2, team[t2])

        for p in range(5):

            n = hesab(gol1, gol2, pish1[p], pish2[p])

            emtiaz[p] = emtiaz[p] + n

            print("امتیاز", bazikon[p], "در این مسابقه:", n)

        print()
        print("جدول امتیازها:")

        for i in range(5):
            print(bazikon[i], emtiaz[i])


max_emtiaz = emtiaz[0]

for i in range(5):
    if emtiaz[i] > max_emtiaz:
        max_emtiaz = emtiaz[i]


print()
print("******** برنده نهایی ********")

for i in range(5):
    if emtiaz[i] == max_emtiaz:
        print(bazikon[i], "با", max_emtiaz, "امتیاز")
