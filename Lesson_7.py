





# def say_hi(name, age):
#    result = F"Hi. My name is {name} and I'm {age} years old"
#    return result
# print(say_hi(name="Alex", age=32))
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')



# def correct_sentence(text):
#     if text[0].islower():
#         text = text[0].upper() + text[1:]
#     if text[-1] != '.':
#         text += "."
#     return text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'correct_sentence error: forgot about capital letter and dot'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('OK')