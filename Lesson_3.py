question_1 = input("write number :  ")
question_2 = input("what action ?:  ")
question_3 = input("write number :  ")

if question_2 == "+":
    print(int(question_1) + int(question_3))
elif question_2 == "-":
    print(int(question_1) - int(question_3))
elif question_2 == "*":
    print(int(question_1) * int(question_3))
elif question_2 == "//" and int(question_3) !=0:
    print(int(question_1) // int(question_3))
    print("delenie na nol")
else:print("end")








