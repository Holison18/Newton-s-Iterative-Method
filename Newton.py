# This program helps you to find the roots of a function using Newton's method

def newtons_method(funct,functDeriv,x,n):
    # convert the function to a function that is evaluable
    def f(x):
        f = eval(funct)
        return f
    
    # convert the derivative of the function to a function that is evaluable
    def df(x):
        df = eval(functDeriv)
        return df
    
    # Perform n number of iterations
    for intercept in range(1,n):
        m = x - (f(x)/df(x))
        x = m

    print(f"The roots of the function{funct} is found to be at {x} after {n} interations.")


Your_function = input("Function,f(x): ")
deriv_function = input("Derivative of your function,f'(x): ")
initial_guess = float(input("Initial Guess,x: "))
itr = int(input("Number of iterarions,n: "))

newtons_method(Your_function,deriv_function,initial_guess,itr)