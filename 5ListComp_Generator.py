input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# xyz = [i for i in input_list if div_by_five(i)]
xyz = (i for i in input_list if div_by_five(i))
# xyz = []
# for i in input_list:
#     if div_by_five(i):
#         xyz.append(i)
print(xyz)
# for i in xyz:
#     print(i)
# print("pm")
# for i in xyz:
#     print(i)
xyz = [i for i in input_list if div_by_five(i)]
print(xyz)
[print(i) for i in xyz]
# (print(i) for i in xyz)


[[print(i, ii) for ii in range(5)] for i in range(5)]
# for i in range(5):
#     for ii in range(5):
#         print(i, ii)
abc= [[(i, ii) for ii in range(5)] for i in range(5)]
print(abc)
pm=[[[i, ii] for ii in range(5)] for i in range(5)]
print(pm)


am=([[i, ii] for ii in range(5)] for i in range(5))
print(am)
# print([i for i in am])
for i in am:
    print(i)
amm=(([i, ii] for ii in range(5)) for i in range(5))
# for i in amm:
#     print(i)
for i in amm:
    for ii in i:
        print(ii)
print('pundrik')
# pmm=(((i, ii) for ii in range(50000000000000000000)) for i in range(50000000000000000000000000000000000000))
# # for i in pmm:
# #     print(i)
# for i in pmm:
#     for ii in i:
#         print(ii)

[print(i) for i in range(5)]
print('kajal')
km = (print(i) for i in range(50000000000000000000000000000000000000000000000000000000))
for i in km:
    i