menu = [
    [ 'Egg Sandwich', 'Bagel', 'Coffee' ],
    [ 'BLT', 'PB&J', 'Turkey Sandwich' ],
    [ 'Soup', 'Salad', 'Spaghetti', 'Taco' ]
]

print(menu[0][1])

menus = {
    'Breakfast': [ 'Egg Sandwich', 'Bagel', 'Coffee' ],
    'Lunch': [ 'BLT', 'PB&J', 'Turkey Sandwich' ],
    'Dinner': [ 'Soup', 'Salad', 'Spaghetti', 'Taco' ]
}

# by default, the for loop loops over the keys [Breakfast, Lunch, Dinner] only
# to allow also the values, use .items()
for name, menu in menus.items():
    print(name, ':', menu)

contacts = {
    'number': 4,
    'students': 
    [
        { 'name': 'Sarah Holderness', 'email': 'sarah@example.com' },
        { 'name': 'Harry Potter', 'email': 'harry@example.com' },
        { 'name': 'Hermione Granger', 'email': 'hermione@example.com' },
        { 'name': 'Ron Weasly', 'email': 'ron@example.com' }
    ]
}

for student in contacts['students']:
    print(student['email'])