# # from math import pow
# #
# # LgInt_1 = pow(int(input()),int(input()))
# # LgInt_2 = pow(int(input()),int(input()))
# # print(int(LgInt_1 + LgInt_2))
# MAX = 100000
#
# a = int(input()) # base 'a'
# b = int(input()) # exponent 'b', to which 'a' is raised
# c = int(input()) # base 'c'
# d = int(input()) # exponent 'd', to which 'c' is raised
#
# stor_array_a_b = [] # array of digits representing a^b
# stor_array_c_d = [] # array of digits representing c^d
#
# def multiply(x, res, res_size):
#     carry = 0
#     for i in range(res_size):
# https://www.geeksforgeeks.org/writing-power-function-for-large-numbers/

MAX=100000

def multiply(x, res, res_size):

    # Initialize carry
    carry = 0

    # One by one multiply n with
    # individual digits of res[]
    for i in range(res_size):
        prod = res[i] * x + carry

        # Store last digit of
        # 'prod' in res[]
        res[i] = prod % 10

        # Put rest in carry
        carry = prod // 10

    # Put carry in res and
    # increase result size
    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size+=1

    return res_size

def power(x,n,value=False,show=True):

    # printing value "1" for power = 0
    if (n == 0) :
        print("1")
        return

    res=[0 for i in range(MAX)]
    res_size = 0
    temp = x

    # Initialize result
    while (temp != 0):
        res[res_size] = temp % 10;
        res_size+=1
        temp = temp // 10


    # Multiply x n times
    # (x^n = x*x*x....n times)
    for i in range(2, n + 1):
        res_size = multiply(x, res, res_size)

    if value:
        return res, res_size
    elif show:
        print(x , "^" , n , " = ",end="")
        for i in range(res_size - 1, -1, -1):
            print(res[i], end="")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

powera_b = power(a,b,value=True,show=False)
powerc_d = power(c,d,value=True,show=False)
printsize = 0


a_list = powera_b[0]
c_list = powerc_d[0]

if powera_b[1] > powerc_d[1]:
    printsize = powera_b[1]
elif powera_b[1] == powerc_d[1]:
    if a_list[powera_b[1]] + c_list[powerc_d[1]] > 9:
        printsize = powera_b[1] + 1
    else:
        printsize = powera_b[1]
else:
    printsize = powerc_d[1]

add_list = []
list_carry = 0
for i in range(printsize):
    list_temp = 0
    list_temp = a_list[i] + c_list[i] + list_carry
    if list_temp > 9:
        list_carry = list_temp // 10
    else:
        list_carry = 0
    add_list.append(list_temp % 10)
for i in range(printsize - 1, -1, -1):
            print(add_list[i], end="")
