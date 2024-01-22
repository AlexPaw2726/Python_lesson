# value_list = [1,2,8,6,5]
# print(value_list)
# value_list.reverse()
# print(value_list)
#
# value_list.sort()
# print(value_list)

# value_int = 0
# is_true = True
#
# while is_true:
#     value_int += 1
#     print(value_int)
#     if value_int > 3:
#       break

my_list = [0, 1, 0, 12, 3]
my_list.sort(reverse=True, key=bool)
print(my_list)