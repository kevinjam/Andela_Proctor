#Write a function power that accepts two arguments, 
#Raise a TypeError with the message Argument must be integer or 
#float if the inputs are anything other that ints or floats.
def power(a, b):
    """#a and b and calculates a raised to the power b.."""
    return reduce(lambda result, _: result * a, range(b), 1)