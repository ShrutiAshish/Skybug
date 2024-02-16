import random
import string
# lower = 'abcdefghijklmnopqrstuvwxyz'
# upper = lower.upper()
# symbol = '[]{}()_.#@$*!%^&<>'
# number = '0123456789'
# all = lower + upper + symbol + number
# length = int(input("Enter Your Length "))

# password = ''
# for i in range(length):
#     password = ''.join([password,random.choice(all)])


# print(password)

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

length = int(input("Enter Your Length "))
s =[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print(f'Your password is : {"".join(random.sample(s,length))}' )