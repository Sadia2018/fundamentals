# x = [ [5,2,3], [10,8,9] ]
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# # TODO: Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)
# # TODO: Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name'] = "Bryant"
# print(students)
# # TODO: In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = 'Andres'
# print( sports_directory['soccer'])
# # TODO: Change the value 20 in z to 30
# z[0]['y'] = 30
# print(z)

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterate_dictionary(students)
# # TODO: should output: (it's okay if each key-value pair ends up on 2 separate lines;
# def iterate_dictionary(list):
#     for i in range(0, len(list)):
#         output = ""
#         for key,val in list[i].items():
#          output += f" {key} - {val},"
#         print(output)

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def print_info(dict):
#     for key,val in dict.items():
#         print("--------------")
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])

# print_info(dojo)

class User:
    # declaring a class attribute
    bank_name = "First National Dojo"
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0
        guido = User()
    monty = User()
guido.bank_name = "Dojo Credit Union"
print(guido.bank_name) # output: Dojo Credit Union 
print(monty.bank_name)
