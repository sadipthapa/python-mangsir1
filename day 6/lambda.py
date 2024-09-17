# def sum_by_ten(a):
#     return a+10

# s=lambda a:a+10
# print(s(10))


#print(sum_by_ten(2))

def myfunc(n):
    return lambda x:x*n

# lambda x:x*2
doubler=myfunc(2)
# lambda x:x*3
tripler=myfunc(3)
print(doubler(10))
print(doubler(20))
print(tripler(15))