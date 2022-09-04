numbers = []
for n in range(0, 10):
    number = int(input('Enter number: '))
    numbers.append(number)
for i in range(len(numbers)):
  for j in range(i+1,len(numbers)):
    if numbers[i]>numbers[j]:
      numbers[i],numbers[j]=numbers[j],numbers[i]
print(numbers)

   

