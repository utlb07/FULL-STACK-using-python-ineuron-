a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  

Area = (a + b + c) / 2   
area = (Area*(Area-a)*(Area-b)*(Area-c)) 
print('The area of the triangle is %0.2f' %area)   