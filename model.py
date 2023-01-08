import math
import setup_logger
import numpy as np
import pandas as pd


class Model:
    """
    Model Class for all data transformations.

    Classes:
        Model

    Functions:
        get_best_func() -> list
        validate_best_func(list) -> pd.DataFrame
    """

    def __init__(self, data):
        """
        Initialize class with needed variables of tables
        :param data: Dict, Contains Dictionary of table Dataframes
        :var ideal_df: Takes the data of ideal functions
        :var test_df: Takes the data of test values
        :var train_df: Takes the data of given train functions
        """
        self.ideal_df = data['ideal']
        self.test_df = data['test']
        self.train_df = data['train']
        self.logger = setup_logger.setup('model')

    def get_best_func(self) -> list:
        """
        Compares the ideal functions to the train functions by minimum sum of squared differences
        and returns the names of ideal functions that best describe the train data.

        :return: best_func_keys: list, names of ideal functions which best describe the train data
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
        self.logger.info(f'Successfully found best ideal functions')
        return best_func_keys

    def validate_best_func(self, best_func_keys: list, diff: str) -> pd.DataFrame:
        """
        Validate best function with test values and calculate difference. Returns a dataframe of test values and
        given difference of best ideal func if difference is smaller then the difference
        between train and test factorized by sqrt(2).
        :param best_func_keys: list, List of best functions which are evaluated by get_best_func() Method
        :param diff: string, diff=ms will take mean squared difference for validation
        :return: test_table_df: pd.Dataframe, Data of test table
        """
        difference_df = pd.DataFrame(self.train_df['x'].round(1))
        # load ideal and train function and calculate differences
        train_index = 1

        for i in best_func_keys:
            difference_df[f'train_y{train_index}'] = self.train_df[f'y{train_index}']
            differences_list = []
            for train_value, ideal_value in zip(self.train_df[f'y{train_index}'], self.ideal_df[i]):
                difference_df[i] = self.ideal_df[i]
                # Substract x from y and save the result with factor sqrt(2) into dataframe
                differences_list.append(abs(train_value - ideal_value) * math.sqrt(2))

            difference_df[f'Diff_factor_{i}'] = pd.Series(differences_list)
            train_index += 1

        test_table_df = pd.DataFrame(self.test_df['x'])
        test_difference_list = {}
        test_difference_df = pd.DataFrame()
        idx = 0

        # calculate difference between ideal function and test[y]
        for x, t_test_value in zip(self.test_df['x'], self.test_df['y']):
            index = difference_df[difference_df['x'] == x].index[0]

            for i in best_func_keys:
                y_ideal = self.ideal_df.iloc[index][i]
                test_difference_list[i] = math.sqrt(abs(y_ideal - t_test_value))

            test_difference_df[f'{str(idx)}_{str(x)}'] = pd.Series(test_difference_list)
            idx += 1

        # Transform dataframe regarding given data structure (table 3 in exercise sheet)
        test_difference_df = test_difference_df.transpose()
        test_table_df['Y1'] = self.test_df['y']

        # Initialize lists of delta Y and number of ideal function
        deltas = []
        ideal_func = []

        # Get each row of test_difference_df
        # index = x; row = Differences between Test Y and Ideal Functions
        for index, row in test_difference_df.iterrows():

            # Find minimum difference
            min_idx = row.idxmin()
            test_diff_value = float(test_difference_df.loc[index][min_idx])

            # Get x value from ColumnName
            x_value = float(index.split('_')[1])

            # Get mean squared difference value of Train & Ideal in order to compare both values
            if diff == 'ms':
                compare_value = float((difference_df[f'Diff_factor_{min_idx}'].sum()**2)/len(difference_df[f'Diff_factor_{min_idx}']))
            else:
                compare_value = float(difference_df.loc[difference_df['x'] == x_value, f'Diff_factor_{min_idx}'])

            # Compare if test_diff_value is lower than mean squared difference
            if test_diff_value < compare_value:
                deltas.append(test_diff_value)
                ideal_func.append(min_idx)
            else:
                deltas.append(None)
                ideal_func.append(None)

        # Transform dataframe regarding given data structure (table 3 in exercise sheet)
        test_table_df['Delta Y'] = deltas
        test_table_df['Nummer der idealen Funktion'] = ideal_func
        self.logger.info('Successfully validated data')
        return test_table_df
