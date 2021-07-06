import time

def decorator_with_param(param):
    def inner_decorator(f):
        def wrapper():
            f_result=f1(param)
        return wrapper

def my_decorator(my_function):
    def wrapper(nr):
        custom_param=nr*2
        my_function_rezult=my_function(custom_param)
        return  my_function_rezult**2
    return wrapper

@my_decorator
def f1(nr):
    return nr

#def f2(f,nr):
#    return f(nr)

#def executiont():
 #   def wrapper(nr):
 #       start=time.time()
 #       f_result=f(nr)
 #       end=time.time()
 #       print('execution tme:',end-start)
 #       return f_result
 #   return wrapper


#def f(nr):
#    r=[]
#    for i in nr:
#        if i%2==0:
#            r.append(i)
#    return r

if __name__ == '__main__':
    #x=f1(5)
    #y=f1
    #a=y(5)
    #b=f2(f1,10)
    #print('a',a)
    #print('b',b)
    #my_decorated_f=my_decorator(f1)
    #x=my_decorated_f(10)
    x=f1(30)
    print('x',x)
    #decorated_function=decorator_with_param(5)(f1)
    #y=decorated_function(10)
    #print('y',y)



