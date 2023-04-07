import random
print("Выберите игру")
b=str(input());
if b=="Отгадай число":
    a=random.randint(1,20)

    vopros1=int (input("Попробуй угадать число до двадцати"))
    while vopros1!=a:
        if vopros1 < a:
            print("Больше")
        else:
            print("Меньше")
        vopros1=int (input("Угадай число до двадцати"))                

    print("Ты выйграл")

elif b=="Камень,ножницы бумага":
    a=random.randint(1,3)
    if a==1:
        a='бумага'
    if a==2:
        a="камень"
    if a==3:
        a="ножницы"

    vopros1=input("Выбери камень, ножницы или бумага")
    print(a)
    if vopros1==a:
        print("Ничья")
    if vopros1=="камень":
        if a=="бумага":
            print("Ты проиграл")
        if a=="ножницы":
            print("Ты выйграл")
    elif vopros1=="ножницы":
        if a=="камень":
            print("Ты проиграл")
        if a=="бумага":
            print("Ты выйграл")
    elif vopros1=="бумага":
        if a=="ножницы":
            print("Ты проиграл")
        if a=="камень":
            print("Ты выйграл")
    else:
        print("Такого значения нет")
        
else:
    print("такой игры нет")
