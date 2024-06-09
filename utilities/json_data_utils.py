import json


def read_json_data(file_path='TestData/LoginData.json'):
    with open(file_path) as f:
        data = json.load(f)
    return data

# print(data)
# for item in data:
#     print('******************')
#     print(item['username'])
#     print(item['password'])
#     print(item['exp'])
