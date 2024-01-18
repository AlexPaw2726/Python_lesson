question_1 = int(input("write number :  "))
question_2 = input("what action ?:  ")
question_3 = int(input("write number :  "))

if question_2 == "+":
    result = (question_1 + question_3)
    print(result)
elif question_2 == "-":
    result = (question_1 - question_3)
    print(result)
elif question_2 == "*":
    result = (question_1 * question_3)
    print(result)
elif question_2 == "/":
    if question_3 == 0:
     print("error")
else:
    result = (question_1 / question_3)
    print(result)

value_list = [12, 3, 4, 10]
value_list[0] = 10
value_list[3] = 12
print(value_list)












