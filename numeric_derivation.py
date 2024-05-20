
def derive(f, x, h=0.0001):
    derive_formula = int((f(x+h)-f(x-h))/(2*h))  # function implemented 
    return derive_formula  # TODO: implement this function 
