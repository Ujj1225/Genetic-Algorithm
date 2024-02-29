# Plot Graph
import matplotlib.pyplot as plt

plt.ion()


def plot(generation, avgfitness, fitness):
    plt.clf()
    plt.title("Training...")
    plt.xlabel("Number of Generations")
    plt.ylabel("Fitness")
    plt.plot(generation, fitness, label="fitness")
    plt.plot(generation, avgfitness, "r--", label="average fitness")
    plt.legend()
    plt.show(block=False)
    plt.pause(0.01)
