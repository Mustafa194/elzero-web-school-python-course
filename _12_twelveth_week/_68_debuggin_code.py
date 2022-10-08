my_list = [i for i in range(11)]
my_dictionary = {
    'Name': 'Mustafa',
    'Age': 36,
    'Country': 'Iraq'
}

for num in my_list:
    print(num)

for dict_key, dict_value in my_dictionary.items():
    print(f"{dict_key} => {dict_value}")

def function_one():
    print('Hello from function one')
function_one()