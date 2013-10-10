def f(r,x):
    return r*x*(1-x)

def logistic(r,x0):
    while True:
        yield x0
        x0 = f(r,x0)
