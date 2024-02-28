# Equation we are supposed to optimize
# This is supposed to come from the interface!
# Put it in the form some equation = 0


def func(x, y, z):
    return 6 * x**3 + 9 * y**2 + 90 * z - 25


# Fitness function
# This function is supposed to evaluated how fit the parameters have become. 
# If this function returns 99999; they are completely fit 
# If not, we judge the fitness by how large the number has become

def fitness(x, y, z):
    ans = func(x, y, z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    
