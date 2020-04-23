import timeit

# print(timeit.timeit('90000000000000000000000000000000000000000000000000000' , number=500000000))


input_list = range(100)

def div_by_five(num):
        if num % 5 ==0:
                return True
        else:
                return False


xyz = (i for i in input_list if div_by_five(i))
for i in xyz:
        print(i)


# xyz = [i for i in input_list if div_by_five(i)]
# for i in xyz:
#         print(i)


# print(timeit.timeit('''
# input_list = range(100)

# def div_by_five(num):
#         if num % 5 ==0:
#                 return True
#         else:
#                 return False

# xyz = [i for i in input_list if div_by_five(i)]

# ''', number=50000))

print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
        if num % 5 ==0:
                return True
        else:
                return False


xyz = (i for i in input_list if div_by_five(i))
for i in xyz:
        print(i)


''', number = 50))