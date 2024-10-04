people = {'users': {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}

for name, age in people['users'].items():
    if age > 19:
        print(name)
