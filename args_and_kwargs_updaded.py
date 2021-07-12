def intro(**kwargs):
    print("\nData type of argument:",type(kwargs))

    for key, value in kwargs.items():
        print("{} is {}".format(key,value))

intro(Firstname="jo", Lastname="bo", Age=69, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Israel", Age=96, Phone=9876543210)


#argumentd -- optional parameter + with star
#usually name *args but as long asyou write *it could be anything you want


def foo(x, *args):
    print(f'x = {x}')
    print(type(args))
    for item in args:
        print(f'in args = {item}')
l = [1, 2, 3]
foo(3)
foo(3, 'hello', 'I', 'love', 'python')
foo(3, 3, 3, 4, 7, 10)

'''def get_sum(a, b):
    return a + b
c = get_sum(1)
print(c) ===========> we will get error becouse we didnt define the'b' parameter.'''
def foo_1(x=5, *args):
    print(x)
    print(args)

foo_1(2,4,8,'a') #====> it bacome a list (tuple)
#tuple is a list that you can't change!

def foo_2(x, list1=[]):
    print(f'x = {x}')
    for item in list1:
        print(f'in list1 = {item}')
foo_2(3,['hello', 'I', 'love', 'functions'])
foo_2(3)

print('=============================')

def get_sum_numbers(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

x = get_sum_numbers()
y = get_sum_numbers(1, 5, 6, 7, -6, 200, -1000)
print(x)
print(y)


def run_numbers(win_numbers):
    win_numbers[0] = -1
    win_numbers[-1] = 8.344343

'''important_list = [17, 20. 22, 43, 44, 45]
run_numbers((tuple(important_list)))
print(important_list) =======>> we will get an error here because we cannot change a tuple... although we traied...'''
