# n = 8
# m = 7
# o = 9

# if n and m and o % 2 == 0:

#     if n<m and n<o:
#         print(n)

#     elif m<n and m<o:
#         print(m)

#     else:
#         print(o)

# elif n % 2 !=0:

#     if m % 2 !=0:

#         if o % 2 !=0:

#             if n > m and n > o:
#                 print(n)

#             elif m > n and m > o:
#                 print(m)

#             else:
#                 print(o)
#         else:
            
#             if m > n:
#                 print(m)

#             else:
#                 print(n)

#     else:

# birth_year= input("Please enter your birth year: ")
# print("You are born in year " + birth_year)

# x= -3
# ans=0
# num_iterations=0
# while(num_iterations < x):
#      ans = ans + x
#      print(ans)
#      num_iterations += 1
# print(f' {x} * {x} = {ans}')

# num_x = int(input('How many times should I print the letter X? '))
# x = 0
# to_print = '7'
# while x <= num_x -1:
#     x+=1
#     print(to_print)

number = []
stop = 0
while stop < 10:
    num = int(input("Please enter a number:"))
    number.append(num)
    stop += 1

even = []
odd = []
for num in number:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

empty = []
if odd == empty:
    print("All numbers are even")

else:
    num = odd[0]
    position = 0
    for n in odd:
        position += 1
        if num > n:
            num = num
        else:
            num = odd[position-1]

    print(F'{num} is the largest odd number.')