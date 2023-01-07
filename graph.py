import matplotlib.pyplot as plt


def plot_data(df, label: str = None, multiple_y: bool = True, key=None):
    """
    Method to plot given data.
    :param df: DataFrame, data to plot
    :param label: string, Label of chart
    :param multiple_y: bool, True if the data has more than one Y value
    :param key: string, Getting specific data plots
    :return: None
    """
    i = 0
    x = 0
    v = 1

    if multiple_y:
        if key == 'ideal':
            while x <= 9:
                fig, axs = plt.subplots(nrows=5, ncols=1)
                while i <= 4:
                    if v < 51:
                        axs[i].plot(df['x'], df[f'y{v}'])
                        axs[i].set_title(f'y{v}')

                    i += 1
                    v += 1
                fig.suptitle(label, fontsize=14)
                fig.tight_layout()
                plt.draw()
                plt.show()
                x += 1
                i = 0
        elif key == 'train':
            while x <= 0:
                fig, axs = plt.subplots(nrows=4, ncols=1)
                while i <= 3:
                    if v < 51:
                        axs[i].plot(df['x'], df[f'y{v}'])
                        axs[i].set_title(f'y{v}')

                    i += 1
                    v += 1
                fig.suptitle(label, fontsize=14)
                fig.tight_layout()
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


def plot_validation(test_func, test_nan, ideal_func, best_func_key, label=None):
    """
    Method to plot validated test data and assigned ideal function with data points
    :param test_func: DataFrame, all validated test data with ideal functions
    :param test_nan: DataFrame, all validated test data without ideal functions
    :param ideal_func: DataFrame, all given ideal functions
    :param best_func_key: list, all selected best functions
    :param label: string, Plot title
    :return: None
    """
    # Plot all test data, green for validated data with ideal function, red for validated data without ideal function
    plt.title(label)
    plt.scatter(test_func[f'x'], test_func['Y1'], label="Validated data", color='green')
    plt.scatter(test_nan[f'x'], test_nan['Y1'], label="Not validated data", color='red')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.draw()
    plt.show()

    # Plot for a specific ideal function all validated data
    for i in best_func_key:
        col_name = test_func.columns[-1]
        values = test_func.loc[test_func[col_name] == i]
        plt.scatter(values['x'], values['Y1'], color='green', label='Test Data')
        plt.plot(ideal_func['x'], ideal_func[i], color='blue', label='Ideal Function')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()
        plt.draw()
        plt.show()
