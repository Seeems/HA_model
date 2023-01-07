import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import seaborn as sns

import data_manager

def plot_data(df, label=None, multiple_y=True):
    i = 0
    x = 0
    v = 1

    if multiple_y:
        while x <= 9:
            fig, axs = plt.subplots(nrows=5, ncols=1)
            while i <= 4:
                if v < 51:
                    axs[i].plot(df['x'], df[f'y{v}'])
                    axs[i].set_title(f'y{v}')

                i += 1
                v += 1
            fig.suptitle(label, fontsize=14)
            plt.draw()
            plt.show()
            x += 1
            i = 0

    else:

        plt.scatter(df[f'x'], df['y'], label=label)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()
        plt.draw()
        plt.show()
