import random
import string
char=string.ascii_letters
char+=string.digits
char+=string.punctuation
length=int(input('enter the length :'))
password=''
for i in range(length):
    n_p=random.choice(char)
    password+=n_p
print(' the random password will be :',password)