def multiply(num1, num2):
    """
    This function multiplies two numbers via repeated addition.

    args: num1, num2 (the two numbers being multiplied)
    return: int
    """
    result = 0
    for i in range(num2):
        result += num1
    return result

def exponentiate(base, exponent):
    """
    This function brings a number to a power without using the exponetiate functionaility. 

    args: base (the number), and exponent (the power it is being brought to)
    return: int
    """
    result = 0
    if exponent >= 0:
        if exponent == 1:
            result = base
            return result
        elif exponent == 0:
            result =  1
            return result
        if exponent%2 != 0 and base < 0:
            result = abs(base)
            for i in range(exponent-1):
                result = result * abs(base)   
            result = result * (-1) 
        else: 
            result = abs(base)
            for i in range(exponent-1):
                result = result * abs(base)
    return result

def square(num):
    """
    This function squares a number with one line of code using the exponentiate function. 

    args: num (the number being squared)
    return: int
    """
    return exponentiate(num, 2)

def main():
    res = multiply(3,5)
    print(res)
    res = exponentiate(-3,0)
    print(res)
    res = square(-5)
    print(res)

main()


            
        
