import matplotlib.pyplot as plt

plt.ion()


def plot(generation, fitness, avgfitness):
    plt.clf()

    # Plotting fitness
    plt.subplot(2, 1, 1)
    plt.title("Training...")
    plt.ylabel("Fitness")
    plt.plot(generation, fitness, label="fitness")
    plt.legend()

    # Plotting average fitness
    plt.subplot(2, 1, 2)
    plt.xlabel("Number of Generations")
    plt.ylabel("Average Fitness")
    plt.plot(generation, avgfitness, "r--", label="average fitness")
    plt.legend()

    plt.show()
    plt.pause(0.01)
