import multiprocessing

def spawn(num, num2):
    print('Pundrik!{} {}'. format(num, num2))

if __name__ == '__main__':
    for i in range(55):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start()
        p.join()