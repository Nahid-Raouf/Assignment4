number=int(input('Enter your number: '))
sum=1
counter=1

while number>sum :
   sum*=counter 
   counter+=1
   
counter-=1  
 
if sum==number:
    print('number',number,'is factoril of number',counter)
    
else:
    print('add',number,'your number is not factorial')