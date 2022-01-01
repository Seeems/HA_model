from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.fftpack import fft
from IPython.display import display, Math
from scipy.interpolate import interp1d

def differentiate_functions(df1, df2):
    best_func = []
    error_list = []
    error_dict = {}
    df1_iterator = 1
    while df1_iterator <= (len(df1.columns) - 2):

        df2_iterator = 1

        while df2_iterator <= (len(df2.columns) - 2):

            error_dict[f'{df2_iterator}'] = np.sum(
                (df1[f'y{df1_iterator}'] - df2[f'y{df2_iterator}']) ** 2)

            df2_iterator += 1

        best_ideal = {k: v for k, v in sorted(error_dict.items(), key=lambda item: item[1])}
        best_func.append(list(best_ideal.keys())[0])


        df1_iterator += 1


    return best_func

def validate_best_func(df1, df2, best_func):
    error_list = []
    for i in best_func:
        error_list.append(mean_squared_error(df1['y'], df2[f'y{i}']))

    for i in error_list:
        if i > np.sqrt(2):
            print('Failed!')
    return error_list

def identify_ideal_func(data):
    ideal_df = data['ideal']
    test_df = data['test']
    train_df = data['train']



    best_func = differentiate_functions(train_df, ideal_df)


    ll = [1,2,3,4]

    for i in best_func:
        plt.plot(ideal_df[f'x'], ideal_df[f'y{i}'], label = f"ideal y{i}")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.show()

    for i in ll:
        plt.plot(train_df[f'x'], train_df[f'y{i}'], label=f"train y{i}")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.show()

    print(validate_best_func(test_df, ideal_df, best_func))

