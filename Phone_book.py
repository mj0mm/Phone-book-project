info = {  
    'Amal' : '1111111111' ,
    'Mohammed' : '2222222222' ,
    'Khadija'  : '3333333333' ,
    'Abdullah'  : '4444444444' ,
    'Rawan'  : '5555555555',        # تم عمل  dic 
    'Faisal' : '6666666666' ,
    'Layla' : '7777777777' 
}

def getOwner(dic , number):
    if number.isdigit() and len(number) == 10:    #  اذا كان طول الرقم يساوي 10 
        for name, number in dic.items():
            if user_input == number:
                print(name)
                break                             #اذا تحقق الشرط راح توقف 
        else:
            print("Sorry the number is not found!") # اذا لم يتحقق الشرط راح يطبع هذه الرساله 
    else:
        print("This is invalid number")             #  اذا الرقم لم يساوي 10 راح يطبع هذه الرساله


def getNumber(dic , name):
    for name, number in dic.items():
        if user_input == name:                      # اذا المستخدم ادخل الاسم وكان يساوي الاسم
            print(number)                             # راح يطبع له الرقم الخاص بالاسم المدخل 
            break                                   #اذا تحقق الشرط راح توقف
    else:                                       
        print("Sorry the name is bot found!")   # اذا الاسم المدخل غير موجود راح يطبع هذه الرساله



def addNewUser(dic):                                # انشاء داله لاضافة اسم ورقم جديد 
    name = input("Enter the name of the new user: ") # انشاء متغير يتم ادخال اسم الشخص الغير موجود ب القاموس
    number = input("Enter the number of the new user: ") # انشاء متغير يتم ادخال رقم الشخص الغير موجود ب القاموس
    dic[name] = number

    return dic


i = int(input(
    'Welcome to the phone book.\nTo search using the phone number please enter the number: 1 \nTo search using the name please enter the number: 2 \nTo add a new name and number to the phone book please enter the number: 3 \nTo exit press 4: '))
while i != 4:                                                          # اذا لوب لا يساوي 4 انتقل للي بعده اذا يساوي 4 يتم اغلاق التطبيق
    if i == 1:                                                          # اذا يساوي 1 نفذ لي الشرط اللي بعده
        user_input = input('Enter the number of user: ')                    #  متغير يدخل المستخدم رقم اللي يبي بحثت عنه 
        getOwner(info, user_input)
    elif i == 2:                                                          # اذا يساوي 2 نفذ لي الشرط اللي بعده 
        user_input = input('Enter the name of user: ')                          #  متغير يدخل المستخدم اسم اللي يبي بحثت عنه 
        getNumber(info, user_input)
    elif i == 3:                                                             # اذا يساوي 3 نفذ لي الشرط اللي بعده 
        print(addNewUser(info))                                                 # dic يتم اضافه اسم جديد ورقم جديد في  addNewUser استناد الى داله 

    else:
        print(" You must choose one of '1-2-3-4' ")
        break

    i = int(input(
        'Welcome to the phone book.\nTo search using the phone number please enter the number: 1 \nTo search using the name please enter the number: 2 \nTo add a new name and number to the phone book please enter the number: 3 \nTo exit press 4: '))