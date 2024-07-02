import random

# Letters/alphabets
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']

# Numbers/digits
n = ['0','1','2','3','4','5','6','7','8','9']

# Symbols
s = ['!','#','$','%','@','^','&','*','(',')']

def generate_password(numb_l, numb_n, numb_s, difficulty):
    password_list = []

    
    for _ in range(numb_l):
        c=random.choice(l)
        password_list+=c
    for _ in range(numb_n):
        c=random.choice(n)
        password_list+=c

    for _ in range(numb_s):
        c=random.choice(s)
        password_list+=c

    random.shuffle(password_list)
    password = ''.join(password_list)
    if difficulty == "Weak":
        len(password)<8
        numb_l = max(numb_l // 2, 1)
        numb_n = max(numb_n // 2, 1)
        numb_s = max(0,0)
    elif difficulty == "Normal":
        8<len(password)<12
        numb_l = max(numb_l, 1)
        numb_n = max(numb_n, 1)
        numb_s = max(numb_s, 1)
    elif difficulty == "Strong":
        len(password)>=12
        numb_l = max(numb_l * 2, 1)
        numb_n = max(numb_n * 2, 1)
        numb_s = max(numb_s * 2, 1)

    
    return password
