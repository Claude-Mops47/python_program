import pyautogui as pg


def prime_factor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            count = 1
            for j in range(2, (i//2 + 1)):
                if (i % j == 0):
                    count = 0
                    break
            if (count == 1):
                print(i, end='')


n = int(input("number: "))
prime_factor(n)


# while True:
#     a = pg.confirm("Are you Gay ?", buttons=['Yes', 'Nope'])
#     if a == 'Yes':
#         break
