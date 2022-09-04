import random
lenght = int(input(" Enter leghnt of your random list: "))
num_list=[]
for i in range (lenght):
    num=random.randint(0,99)
    num_list.append(num)
print('your list =',num_list)