
import random



print('-----Ваша карточка-----')
cart1_str1 = []
for i in range(3):
    cart1 = [random.randint(1 , 90)for i in range(5)]
    cart1.sort()
    cart1_str = '   '.join(str(e) for e in cart1)
    print(cart1_str)
print('-----------------------')
print('--Карточка компьютера--')
for i in range(3):
    cart2 = [random.randint(1 , 90)for i in range(5)]
    cart2.sort()
    cart2_str = '   '.join(str(e) for e in cart2)
    print(cart2_str)   
print('-----------------------')

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
       39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
       57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
       75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
seq_copy = list(seq) 
i = 0
user = ''
while i <= 90:     
    num_boch = random.choice(seq_copy)
    seq_copy.remove(num_boch)
    remain = len(seq_copy)
    
    
    print('Выпал номер:', num_boch)
    print('Осталось:', remain)
    
           
    if num_boch in cart1:
        cart1.remove(num_boch)
        remain_1 = len(cart1)
        if remain_1 == 0:
            print('Вы выиграли!')
            break
    if num_boch in cart2:
        cart2.remove(num_boch)
        remain_2 = len(cart2)
        if remain_2 == 0:
            print('Выиграл компьютер!')
            break
    i += 1
   

