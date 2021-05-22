import re
def chek(password):
    f1 = 0

    while True:

        if (len(password) < 8):
            print("t1")
            f1 = -1
            break
        elif not re.search('[a-z]', password):
            print("t2")
            f1 = -1
            break
        elif not re.search('[A-Z]', password):
            print("t3")
            f1 = -1
            break
        elif not re.search('[0-9]', password):
            print("t4")
            f1 = -1
            break
        elif not re.search('[_@$]', password):
            print("t5")
            f1 = -1
            break
        elif re.search("\s", password):
            print("t6")
            f1 = -1
            break
        else:
            print("t7")
            f1 = 0
            print("this is valid ")
            break
    if f1 == -1:
        print("t8")
        print("not valid")

if __name__ =='_main_':
    chek(10)
