#input('jojo')
#input('secret')

#print('{username}, password {password} is {passwordlength} long')
#print('{username}, password {secret} is {6} long')
#print('{username}, your password {******} is {6} long')
#print('{jojo}, your password {******} is {6} long')

#print('*' * 10) result> **********

username = input('What is your username?')
password = input('What is your password?')

print(f'{username}, your password, {password}, is {"*" * len(password)} letters long')

input()