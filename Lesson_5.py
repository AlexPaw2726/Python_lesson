

# value = "_"
# value_is_digit = value.isprintable()
# print(value_is_digit)

# value = "x"
# value_is_digit = value.isalpha()
# print(value_is_digit)

# value = "get_value"
# value_is_digit = value.islower()
# print(value_is_digit)


# value = "get value"
# value_is_digit = value.isspace()
# print(value_is_digit)


# value = "get!value"
# value_is_digit = value.isupper()
# print(value_is_digit)

# value = "some_super_puper_value"
# value_is_digit = value.islower()
# print(value_is_digit)

# value = "Get_value"
# value_is_digit = value.isupper()
# print(value_is_digit)

# value = "get_Value"
# value_is_digit = value.islower()
# print(value_is_digit)

# value = "getValu"
# value_is_digit = value.isnumeric()
# print(value_is_digit)

# value = "3m"
# value_is_digit = value.isnumeric()
# print(value_is_digit)

# value = "m3"
# value_is_digit = value.isprintable()
# print(value_is_digit)



question_1 = int(input("write number :  "))
question_2 = input("what action ?:  ")
question_3 = int(input("write number :  "))

while True:
    question_4 = input("continue action ?:  ")
    if question_4 == "yes" or question_4 == "y":
          if   question_2 == "+":
             result = (question_1 + question_3)
             print(result)
          elif  question_2 == "-":
              result = (question_1 - question_3)
              print(result)
          elif question_2 == "*":
             result = (question_1 * question_3)
             print(result)
          elif  question_2 == "/":
              result = (question_1 / question_3)
              print(result)
          if  question_3 == 0:
              print("error")
          else:
              print("Thank You")
              break









