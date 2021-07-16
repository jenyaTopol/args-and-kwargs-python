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


#1.create a function with *argswhich returns the items in a list
#    l1 = get_args_as_list(1,3,3,4,5,6)
#    l1 will be (1,3,3,4,5,6)
#    l2 will be { 'positional_arguments' : [1, 3], '*args' :

def get_arg_as_list(*args):
    result = list(args)
    return result
l1 = get_arg_as_list(1, 3, 3, 4, 5, 6)
print(l1)
#2. create a function with also *args - get_ino_list:
#    get_args_as_dictionary(a,b,*args)
#    l2 = get_args_as_dictionary(1,3,4,5,6)4, 5, 6] }
print('===================')
def get_args_as_dictionary(a,b,c, *args):
    result = dict()
    result['positional arguments'] = [a,b,c]
    result['args'] = list(args)
    return result
res = get_args_as_dictionary(1, 'a', 'b', 1,2,3,4,5)
print(res)
#3. create a function get_tuple_from_list(list1)
#    l3 = get_tuple_from_list([1, 2, 3, 4])
#    l3 will be tubple(1,2,3,4)
def get_tuple_from_list(l1):
    result1 = tuple(l1)
    return result1

#4.  create a function counter_tuple(*args) will return count of items
#    l4 = counter_tuple('a', 'b', 'a', 1, 3, 1)
#    l4 will be{'a' : 2, 'b' : 1, 1 : 2, 3 : 1}
#5.  create a function that will get a parameter - function discovery(param1)
#    discovery([1,2,3]) -- function will  print: 'list can be modified in any way'
#     discovery([1,2,3]) -- function will  print: 'tuple cannot be modified in any way'

print('==================================')

def printDictiomary(**kwargs):  #the difrance between *argsand **kwargs is that *rgs creating a tuple and **kwargs is a dictionary
    for k, v in kwargs.items():
        print(f'key: {k} value: {v}')

#printDictiomary([1,2,3,], 'a',[1,23], -20, key1=1) #x,args and kwargs

printDictiomary(name='jhonny',
                age=12,
                city='Ramat-Gan')
## statistics(k, *args, **kwargs)
# print the value ok f and its type (hint: 'positional', print(type(k)), print(k))
# print if *args was sent (hint use len or count or None...)
# print if **kwayrgs was sent (hint use len or count or None...)
# if *args was sent print: its length, print all of its values, print if it has repitition
# **kwargs:
# print length of the dictionary
# print all keys
# print all values
# print all items together (hint: for kv, in kwargs ...)
#  return- does k appear in dict (as key)?
# *etgar - return a list from kwargs: list1 - keys, list2 - values -- function will return 3 values


print('===================================')



def statistics(k, *args, **kwargs):
    print(f'positional arguments: k = {k} type = {type(k)}')
    if len(args) == 0:
        print('*args argument: was not set so we have an empty tuple')
    else:
        print('*args:')
        print(f'number of items sent = {len(args)}')
        print(f'items = {args}')
        len_args = len(args)
        len_args_no_duplications = len(set(args))
        if len_args == len_args_no_duplications:
            print('no duplicated items in *args')
        else:
            print('there are duplications in *args')

    if len(kwargs) == 0:
        print('**kwargs argument: items were not set so we have an empty dictionary')
        return False, None, None
    else:
        print(f'length of kwargs (number of key-value items): {len(kwargs)}')
        counter = 0
        print('keys:')
        for key1 in kwargs.keys():
            counter = counter + 1
            print(f'[{counter}] : {key1}')
        counter = 0
        print('values:')
        for value1 in kwargs.values():
            counter = counter + 1
            print(f'[{counter}] : {value1}')
        print('key values:')
        counter = 0
        for k1, v1 in kwargs.items():
            counter=counter+1
            print(f'[{counter}] : key={k1} value={v1}')
        if k in kwargs.keys():
            return True, kwargs.keys(), kwargs.values()
        else:
            return False, kwargs.keys(), kwargs.values()

# def statistics(k, *args, **kwargs):
# def statistics(1, (1,1,7), { 'one':10, 'two':20 }):
my_key = 'one1'
k_in_dict, list_keys_kwargs, list_values_kwargs = statistics(my_key, 1, 1, 7, one=10, two=20);
print(f'was {my_key} in dictionary? {k_in_dict}')
print(list_keys_kwargs)
print(list_values_kwargs)
