question_1 = input("write number :  ")
question_2 = input("what action ?:  ")
question_3 = input("write number :  ")

if question_2 == "+":
    print(int(question_1) + int(question_3))
elif question_2 == "-":
    print(int(question_1) - int(question_3))
elif question_2 == "*":
    print(int(question_1) * int(question_3))
elif question_2 == "//":
     print(int(question_1) // int(question_3))

else: print("end")







