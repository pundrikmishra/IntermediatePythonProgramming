blog_1 = 'I am so awesome'
blog_2 = 'Cars are cool'
blog_3 = 'Aww look at my cat!!'

site_title = 'My Blog'


def blog_posts(*pm):
    for post in pm:
        print(post)

blog_posts(blog_1)
print('---------------------------------------------------------------------------------------------------------------------------------')
print('makati'*21)
print('---------------------------------------------------------------------------------------------------------------------------------')

# def blog_posts(*args):
def blog_posts(title, *args):
    print(title)
    for post in args:
        print(post)

blog_posts(site_title, blog_1,blog_2, blog_3)

print('---------------------------------------------------------------------------------------------------------------------------------')
print('pundrik'*18)
print('---------------------------------------------------------------------------------------------------------------------------------')


def blog_posts(title, **kwargs):
    print(title)
    for p_title, post in kwargs.items():
    # for post in kwargs.items():
        # print(post, kwargs, post)
        print(p_title, post)
        print(post)


blog_posts(site_title,
            blog_1 = 'I am so awesome',
            blog_2 = 'Cars are cool',
            blog_3 = 'Aww look at my cat!!')

print('---------------------------------------------------------------------------------------------------------------------------------')
print('kajal'*26)
print('---------------------------------------------------------------------------------------------------------------------------------')


def blog_posts(title, *args, **kwargs):
    print(title)
    for arg in args:
        print(arg)
    for p_title, post in kwargs.items():
        print(post)
        print(p_title,post)

blog_posts(site_title,
            '1', '2', '3',
            blog_1 = 'I am so awesome',
            blog_2 = 'Cars are cool',
            blog_3 = 'Aww look at my cat!!')


print('---------------------------------------------------------------------------------------------------------------------------------')
print('jaydeep'*18)
print('---------------------------------------------------------------------------------------------------------------------------------')


from matplotlib import pyplot as plt
 

def graph_operation(x,y):
    print('functions that graphs {} and {}'.format(str(x), str(y)))
    plt.plot(x,y)
    plt.show()

x1 = [1,2,4,5,3]
y1 = [2,3,3,5,1]

graph_me = [x1,y1]

graph_operation(*graph_me)
# graph_operation(x1,y1)
