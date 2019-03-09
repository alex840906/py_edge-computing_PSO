import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def draw(evaluation_value, iteration):
    x = np.arange(0, iteration)
    plt.plot(x, evaluation_value)
    plt.show()