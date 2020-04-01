import random
import string

print("welcome to the registrating page, fill your details below")

def user_input():
    first_name = str(input("please enter you first name: "))
    last_name  = str(input("please enter your last name: "))
    passwd1 = first_name[0:2]
    passwd2 = last_name[0:2]
    password = passwd1 + passwd2
    randomString=""
    for i in range(5):
        randomString += (str(chr(random.randint(97,122))))
        password1 = password + randomString
    return [first_name, last_name, password1]

init = True
while init:
    items = []
    items.append(user_input())

    responce1 = str(input(f"the password generated for you is {items[0][2].upper()}, press YES to accept and continue registration or NO to create your own password: "))
    if responce1 in ["YES" , "yes", "Y", "Yes"]:
        #print(items)
        items=[items]
        items.append(user_input())
        print(f"your registration details are FIRSTNAME{items}")
        
    else:
        create_password = str(input("please enter your prefered password: "))
        create_password1 = len(create_password)
        if create_password1 < 7:
            print('Password must be greater or equal to 7 characters, please start again')
        
        items[0][2]=create_password
        print(items)
        new_user  = str(input("Do you wish to continue registration?: " ))
        if new_user in ["YES" , "yes", "Y", "Yes"]:
            print(items)
            continue
        else:
            print("thanks for your registration")
            break




   
    



