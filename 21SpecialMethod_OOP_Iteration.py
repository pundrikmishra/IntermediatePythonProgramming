# x= range(5)
# print(x)
# for i in x:
#     print(i)


# y= (i for  i in range(5))
# print(y)
# next(y)
# next(y)
# y.__next__()
# y.__next__()
# for i in y:
#     print(i)



class range_examp:

    def __init__(self , end, step=1):
        self.current = 0
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            # return_val = self.current
            return return_val


for i in range_examp(5):
    print(i)
    print(i)