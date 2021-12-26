import json

def get_list():
    with open('carskg.json', 'rt') as my_file:
        dictionary = json.load(my_file)
        my_file.close()
        data_json = [dict(i) for i in dictionary]
        
    return data_json

data_json = get_list()

new_list = []

for dict_ in data_json:
    
    for list_ in dict_.values():
        new_list.append(list_)

new_list = ''.join(new_list)
new_list = new_list.split('\n')


result = []

for string in new_list:
    result.append(string.strip())

print(result)