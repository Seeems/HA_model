import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import seaborn as sns

import data_manager

def plot_data(df):
    i = 0
    x = 0
    v = 1


    while x <= 9:
        fig, axs = plt.subplots(nrows=5, ncols=1)
        while i <= 4:
            if v < 51:
                axs[i].plot(df['x'], df[f'y{v}'])
                axs[i].set_title(f'y{v}')

            i += 1
            v += 1

        plt.draw()
        plt.show()
        x += 1
        i = 0


