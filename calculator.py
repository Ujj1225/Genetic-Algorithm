import random
from plot import plot
import math
from evaluate import evaluate_expression

exp = input("Expression: ")  # Get the expression


# Calculate Fitness
def fitness(x, y, z):
    ans = evaluate_expression(exp, x, y, z)
    return abs(1 / ans)


# Create 1000 random 1st generation solutions
solutions = []
for s in range(1000):
    solutions.append(
        (
            random.uniform(0, 10000),
            random.uniform(0, 10000),
            random.uniform(0, 10000),
        )
    )

generation = []  # Store generation number
fitnesses = []  # Store each generation best fitness value
best = []  # Store each generation best fitness and tuple

for i in range(1000):
    rankedsolutions = []
    for s in solutions:  # Create tuple with fitness and coordinate values (x,y,z)
        rankedsolutions.append((fitness(s[0], s[1], s[2]), s))

    rankedsolutions.sort()  # Sort in increasing fitness order

    rankedsolutions.reverse()  # Sort in decreasing fitness order (1st element has highest fitness)

    best.append(rankedsolutions[0])  # Append best fitness and its coordinate

    print(
        "Generation " + str(i) + ": " + str(rankedsolutions[0])
    )  # Print generation number , best fitness and coordinate

    generation.append(i)  # Append generation number
    fitnesses.append(rankedsolutions[0][0])  # Append best fitness
    plot(generation, fitnesses)  # Plot Graph

    if rankedsolutions[0][0] > 99999:  # If fitness exceeds 99999 end the program
        break

    bestsolutions = rankedsolutions[:100]  # Select best 100 coordinates

    # Combiantion and Mutation

    newGen = []
    for _ in range(1000):  # Create 1000 newgenration with combination and mutation
        x1 = random.choice(bestsolutions)
        e1 = x1[1][0] * random.uniform(0.99, 1.01)  # Mutation
        x2 = random.choice(bestsolutions)
        e2 = x2[1][1] * random.uniform(0.99, 1.01)
        x3 = random.choice(bestsolutions)
        e3 = x3[1][2] * random.uniform(0.99, 1.01)

        newGen.append((e1, e2, e3))

    solutions = newGen

print("Expression: " + exp + "\nSolutions:")
if "x" in exp:
    print("x: " + str(max(best)[1][0]))  # Print the best solution
if "y" in exp:
    print("y: " + str(max(best)[1][1]))
if "z" in exp:
    print("z: " + str(max(best)[1][2]))
print("Error: " + str(1 / rankedsolutions[0][0]))  # Print error
