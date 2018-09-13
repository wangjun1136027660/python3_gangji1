def try_to_make(x):
    try:
        print(1/x)
    except (ZeroDivisionError,TypeError):
        print('ok~')
'''
http://bj.ganji.com/ershoufree/2981225099x.htm
'''

# try_to_make('0')

def f():
    for x in range(1,15):
        y=x*x
        print(y)
f()



