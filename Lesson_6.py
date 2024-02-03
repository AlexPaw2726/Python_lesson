# value_dict = [{"name": "John", "age": 15},
#               {"name": "Jack", "age": 45},
#               {"name": "Alex", "age": 38},
#               {"name": "Michal", "age": 20},
#               {"name": "Viktoriya", "age": 61}]
# young_list = []
# long_name_list = []
# min_age = 1000
# max_name_len = 0
# av_age = 0
#
# for person in value_dict:
#     age = person.get("age")
#     name_len = len(person.get("name"))
#     av_age += age
#     if age == min_age:
#         young_list.append(person.get("name"))
#     elif age < min_age:
#         young_list.clear()
#         young_list.append(person.get("name"))
#         min_age = age
#     if name_len == max_name_len:
#         long_name_list.append(person.get("name"))
#     elif name_len > max_name_len:
#         long_name_list.clear()
#         long_name_list.append(person.get("name"))
#         max_name_len = name_len
# av_age = round(av_age/len(value_dict))
# print(young_list)
# print(long_name_list)
# print(av_age)




# my_dict_1 = {1: 1, 2: 2, 3: 3, 11: 100}
# my_dict_2 = {11: 11, 2: 22}
#
# def exercise_6_2(dict_1, dict_2):
#     result_1 = list(set(dict_1.keys()).intersection(set(dict_2.keys())))
#     result_2 = list(set(dict_1.keys()).difference(set(dict_2.keys())))
#     result_3 = {key: dict_1[key] for key in result_2}
#     result_4 = dict_1.copy()
#     for key in dict_2:
#         if key in result_4:
#             result_4[key] = [result_4[key], dict_2[key]]
#         else:
#             result_4[key] = dict_2[key]
#     return result_1, result_2, result_3, result_4
#
# print(exercise_6_2(my_dict_1, my_dict_2))





















