from tkinter import *
import random
from plot import plot
from evaluate import evaluate_expression

window = Tk()
window.geometry("500x500")
window.title("Calculator")


def solve():
    exp = entry.get()

    # Calculate Fitnes
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
    avgfitness = []  # Store average fitness

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
        avgfitness.append(sum(fitnesses) / len(fitnesses))

        if x.get() == 1:
            plot(generation, fitnesses, avgfitness)  # Plot Graph

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

    grid_size = window.grid_size()  # Get size of grid
    lable_expression = Label(window, text="Expression: " + exp)
    lable_generation = Label(window, text="Generations: " + str(len(best)))
    lable_best_fitness = Label(
        window, text="Best fitness: " + str(round(max(fitnesses)))
    )
    lable_expression.grid(
        column=0,
    )
    lable_generation.grid(column=0)
    lable_best_fitness.grid(column=0)
    if "x" in exp:
        lable1 = Label(window, text="x: " + str(round(max(best)[1][0], 3)))
        lable1.grid(row=grid_size[1], column=1)
    if "y" in exp:
        lable2 = Label(window, text="y: " + str(round(max(best)[1][1], 3)))
        lable2.grid(row=grid_size[1] + 1, column=1)
    if "z" in exp:
        lable3 = Label(window, text="z: " + str(round(max(best)[1][2], 3)))
        lable3.grid(row=grid_size[1] + 2, column=1)

    lable_error = Label(
        window,
        text="Error: " + str(round(1 / rankedsolutions[0][0], 3)),
    )
    lable_error.grid(row=grid_size[1], column=2)

    lable_avgfitness = Label(
        window,
        text="Average fitness: " + str(round(avgfitness[-1])),
    )
    lable_avgfitness.grid(row=grid_size[1] + 1, column=2)


entry = Entry(window, width=35, borderwidth=5)
entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=160,
)

button = Button(window, text="Solve", padx=40, command=solve)
button.grid(row=1, column=0)


x = IntVar()
plotc = Checkbutton(window, text="Plot", variable=x, onvalue=1, offvalue=0)
plotc.grid(row=1, column=1)


def clear():
    widgets = window.winfo_children()
    for widget in widgets:
        if isinstance(widget, Label):
            if widget != lable0 and widget != lable_enter:
                widget.destroy()


button_clear = Button(window, text="Clear", padx=40, command=clear)
button_clear.grid(row=1, column=2)

lable0 = Label(window, text="=0")
lable0.grid(row=0, column=2)

lable_enter = Label(window, text="Enter the expression:")
lable_enter.grid(row=0, column=0)

window.mainloop()
