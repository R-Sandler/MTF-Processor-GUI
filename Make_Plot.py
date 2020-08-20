import matplotlib.pyplot as plt

def make_plot(x, yList, labelList):
    for index, array in enumerate(yList):
        plt.plot(x, yList[index], label=labelList[index])
    plt.legend()
    plt.show()
