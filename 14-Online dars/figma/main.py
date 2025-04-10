# modullar amaliyoti
# import random
# # ro'yxat

# fruits = ['olma', 'banan', 'shaftoli', 'apelsin']
# # tasodifiy tanlangan meva

# random_fruit = random.choice(fruits)

# print(f"Tasodifiy tanlangan meva: {random_fruit}")


# import math
# # son
# num = 5.67
# # yaxlitlash
# ceil_num = math.ceil(num)
# floor_num = math.floor(num)

# print(f"Asl son: {num}")
# print(f"Yuqoriga yaxlitlash: {ceil_num}")
# print(f"Pastga yaxlitlash: {floor_num}")

# import math
# num = 5.76

# ceil_num = math.ceil(num)
# floor_num = math.floor(num)

# print(f"Asl son; {num}")
# print(f"Yuqoriga yaxlitlash: {ceil_num}")
# print(f"Pastga yaxlitlash: {floor_num}")



# import random
# import string

# # parol yaratish
# length = 8
# characters = string.ascii_letters + string.digits
# password = ''.join(random.choice(characters) for _ in range(length))

# print(f"Tasodify parol: {password}")


# import os

# # joriy katalog
# current_dir = os.getcwd()

# # Katalogdagi fayllar
# files = os.listdir(current_dir)

# print(f"Joriy katalog: {current_dir}")
# print("katalogdagi fayllar:")
# for file in files:
#     print(file)



# import random 

# # Latoriya raqamlarni yaratish
# lottery_numbers = random.sample(range(1, 50), 6)

# print(f"Tasodify lororeya raqamlari: {lottery_numbers}")


# import random

# secret_number = random.randint(1,100)
# attempts = 0

# print("Men 1 dan 100 gacha bir sonni o'yladim. Uni topishga harakat qiling!")

# while True:
#     guess = int(input("sonni kiriting: "))
#     attempts += 1
#     if guess < secret_number:
#         print("Katta son kiriting!")
#     elif guess > secret_number:
#         print("Kichuk son kiriting!")
#     else:
#         print(f"Tabriklayiz! Siz {attempts} urinishda to'g'ri topdingiz.")
#         break    

  

# Abyektga yo'naltirilgan dasturlash


# class Person:
#     def __init__(a,name,age,phone,ball):
#        a.name = name
#        a.age = age
#        a.phone = phone
#        a.ball = ball

#     def info(a):
#         return a.name , a.age , a.phone
    
#     def result(self):
#         if self.ball>150:
#             print("O'qi dabba")
#         else:
#             print("Ha! otam nima bo'lyaoti")    

# b = Person('Mirondabba',18,+964353238,150)

# print(b.result())


class Car:
    def __init__(a,model,color,price,km):
       a.model = model
       a.color = color
       a.price = price
       a.km = km

    def info(a):
        return a.model , a.color , a.price
    
    def ge_into(self):
        return f'{self.model} {self.price} {self.color} {self.km}'
            
    def get_price(self):
        if self.km>100000:
            return self.price*0,9
        else:
            return self.price
        
a = Car('bmw','black',50000,460000)
print(a.get_price)














