example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

print('pundrik'*10)

for i, k in enumerate(example):
    print(i, k)


new_dict = dict(enumerate(example))
print(new_dict)
[print(i,j) for i, j in enumerate(new_dict)]