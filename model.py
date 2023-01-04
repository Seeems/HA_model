import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graph
from sklearn.metrics import mean_absolute_error


class Model:
    """
    Model Class for all data transformations.

    Classes:
        Model

    Functions:
        initialize_database(directory_path: str = PROJECT_LOCATION)
        database_modification()

    Misc variables:
        none
    """
    def __init__(self, data):
        self.ideal_df = data['ideal']
        self.test_df = data['test']
        self.train_df = data['train']

    def get_best_functions(self):
        """:type
        """
        best_func_keys = []
        error_dict = {}
        train_iterator = 1

        # for each train dataset get squared error to all ideal functions
        while train_iterator <= (len(self.train_df.columns) - 2):

            ideal_iterator = 1

            while ideal_iterator <= (len(self.ideal_df.columns) - 2):

                # Get sum of all squared errors
                error_dict[f'{ideal_iterator}'] = np.sum(
                    (self.train_df[f'y{train_iterator}'] - self.ideal_df[f'y{ideal_iterator}']) ** 2)

                ideal_iterator += 1

            # Get minimal error of least squared error and save in ordered list
            best_ideal = {k: v for k, v in sorted(error_dict.items(), key=lambda item: item[1])}
            best_func_keys.append(f'y{list(best_ideal.keys())[0]}')
            train_iterator += 1
        return best_func_keys

    def validate_best_func(self, best_func_keys):
        difference_df = pd.DataFrame(self.train_df['x'])
        # load ideal and train function and calculate differences
        train_index = 1

        for i in best_func_keys:
            difference_df[f'train_y{train_index}'] = self.train_df[f'y{train_index}']
            differences_list = []
            for train_value, ideal_value in zip(self.train_df[f'y{train_index}'], self.ideal_df[i]):
                difference_df[i] = self.ideal_df[i]
                # Substract x from y and save the result with factor sqrt(2) into dataframe
                differences_list.append((train_value - ideal_value) * math.sqrt(2))

            difference_df[f'Diff_factor_{i}'] = pd.Series(differences_list)
            train_index += 1

        differences_index = 1
        test_table_df = pd.DataFrame(self.test_df['x'])
        test_difference_list = {}
        test_difference_df = pd.DataFrame()
        test_diff_consol = []

        for x, t_test_value in zip(self.test_df['x'], self.test_df['y']):
            index = difference_df[difference_df['x'] == x].index[0]

            for i in best_func_keys:
                y_ideal = self.ideal_df.iloc[index][i]
                test_difference_list[x] = (y_ideal - t_test_value)
                print(str((y_ideal - t_test_value)))

            test_diff_consol.append(test_difference_list)

            test_difference_df[f'diff_ideal_' + str(i) + str(x)] = pd.Series(test_difference_list)
        df = pd.DataFrame(test_diff_consol)
        print('Test')