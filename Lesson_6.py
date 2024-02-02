value_dict = [{"name": "John", "age": 15},
              {"name": "Jack", "age": 45},
              {"name": "Alex", "age": 38},
              {"name": "Michal", "age": 20},
              {"name": "Viktoriya", "age": 61}]
young_list = []
long_name_list = []
min_age = 1000
max_name_len = 0
av_age = 0

for person in value_dict:
    age = person.get("age")
    name_len = len(person.get("name"))
    av_age += age
    if age == min_age:
        young_list.append(person.get("name"))
    elif age < min_age:
        young_list.clear()
        young_list.append(person.get("name"))
        min_age = age
    if name_len == max_name_len:
        long_name_list.append(person.get("name"))
    elif name_len > max_name_len:
        long_name_list.clear()
        long_name_list.append(person.get("name"))
        max_name_len = name_len
av_age = round(av_age/len(value_dict))
print(young_list)
print(long_name_list)
print(av_age)

























