#task 1
# c1='H'
# c2='D'
# c3='S'
# C4='C'
# a=(input('Card type:'))
# if a==c1 or a==c2:
#     print('Red is color of card')
# else:
#     print('Black is color of card')
# #task  2

# from random import*
# c=randint(1,14)
# c2=randint(1,14)
# t=randint(0,4)
# t2=randint(0,4)
# if c == 1:    print ('Ace of ', end = '');
# elif c == 2:  print ('Two of ', end = '');
# elif c == 3:  print ('Three of ', end = '');
# elif c == 4:  print ('Four of ', end = '');
# elif c == 5:  print ('Five of ', end = '');
# elif c == 6:  print ('Six of ', end = '');
# elif c == 7:  print ('Seven of ', end = '');
# elif c == 8:  print ('Eight of ', end = '');
# elif c == 9:  print ('Nine of ', end = '');
# elif c == 10:  print ('Ten of ', end = '');
# elif c == 11:  print ('Jack of ', end = '');
# elif c == 12:  print ('Queen of ', end = '');
# else:                     print ('Kind of ', end = '');
# if t== 0:      print ('Diamond');
# elif t== 1:    print ('Heart');
# elif t == 2:    print ('Spade');
# else: t = 3;    print ('Club')


# if c2 == 1:    print ('Ace of ', end = '');
# elif c2 == 2:  print ('Two of ', end = '');
# elif c2 == 3:  print ('Three of ', end = '');
# elif c2 == 4:  print ('Four of ', end = '');
# elif c2 == 5:  print ('Five of ', end = '');
# elif c2 == 6:  print ('Six of ', end = '');
# elif c2 == 7:  print ('Seven of ', end = '');
# elif c2 == 8:  print ('Eight of ', end = '');
# elif c2 == 9:  print ('Nine of ', end = '');
# elif c2 == 10:  print ('Ten of ', end = '');
# elif c2 == 11:  print ('Jack of ', end = '');
# elif c2 == 12:  print ('Queen of ', end = '');
# else:                     print ('Kind of ', end = '');

# if t2== 0:      print ('Diamond');
# elif t2== 1:    print ('Heart');
# elif t2 == 2:    print ('Spade');
# else: t2 = 3;    print ('Club')


# if t==t2:
#     print('both cards have same type')
    
# if c==c2:
#     print('both cards have same number')

# elif c==c2+1 or c2==c+1:
#     print('cRDS are in sequence')

#it print number not in its order it print number in reverse order
# n=int(input('enter a three digit number:'))
# i=1
# while i<=n:
#     a=n%10   
#     n=n//10
#     print(a)
# i=i+1
#ayesha reverse method pochna h
 #task 5


# from random import *

# def main():
#     n = randint(101, 999)
#     print ('Number: ', n)
#     reverse_number = n % 10                     #To get third digit of n
#     first_digit = n // 100
#     n = n % 100                                 #To get remaining two digits of n
#     second_digit = n // 10
#     reverse_number = reverse_number * 100 + second_digit * 10 + first_digit
#     print ('Reverse Number: ', reverse_number)

# main()



#practice 10

# i=0
# while i<100:
#     if i%2==0:
#         print(i,end=' ')
#     i=i+1

# n=int(input('number:'))
# a=int(input('number:'))
# for i in range (n,a+1):
#     print(i)


