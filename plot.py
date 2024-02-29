# Plot Graph

import matplotlib.pyplot as plt

plt.ion()


def plot(generation, fitness):
    plt.clf()
    plt.title("Training...")
    plt.xlabel("Number of Generations")
    plt.ylabel("Fitness")
    plt.plot(generation, fitness)
    plt.show(block=False)
    plt.pause(0.01)
