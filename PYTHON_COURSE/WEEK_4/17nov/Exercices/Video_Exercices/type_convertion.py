# name = 'Adrian John'
# age = 20
# relationship_status = 'single'

# relationship_status = "it's complicated"
# #change the status
# print(relationship_status)

birth_year = input('what year were you born?')
actual_year = input('What is the actual year?')
age = int(actual_year) - int(birth_year)
print('you are actually %d' % (age))

input() #for pause the system after executing the file