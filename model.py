import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
        self.best_func = self.get_best_functions()

    def get_best_functions(self):
        """:type
        """
        best_func = []
        error_dict = {}
        train_iterator = 1

        # for each train dataset get squared error to all ideal functions
        while train_iterator <= (len(self.train_df.columns) - 2):

            ideal_iterator = 1

            while ideal_iterator <= (len(self.ideal_df.columns) - 2):

                # Get all squared errors
                error_dict[f'{ideal_iterator}'] = np.sum(
                    (self.train_df[f'y{train_iterator}'] - self.ideal_df[f'y{ideal_iterator}']) ** 2)

                ideal_iterator += 1

            best_ideal = {k: v for k, v in sorted(error_dict.items(), key=lambda item: item[1])}
            best_func.append(list(best_ideal.keys())[0])

            train_iterator += 1

        return best_func

    def validate_best_func(self):
        error_list = []
        difference_df = pd.DataFrame()
        for i in self.best_func:
            x = 0
            while x < len(self.test_df.index):
                print(x)
                x_pos = self.test_df.iloc[x]['x']
                y_pos = self.test_df.iloc[x]['y']

                index_x_ideal = self.ideal_df.index[self.ideal_df.x == x_pos]
                difference = y_pos - int(self.ideal_df.iloc[index_x_ideal][f'y{i}'])
                data = {'x': [x_pos], 'y': [y_pos], 'delta': [difference], 'func': [f'y{i}']}
                difference_df = difference_df.append(pd.DataFrame(data), ignore_index=True)
                x += 1
            # mse = se / len(self.test_df.index)
            # check = np.sqrt(2)
            # error_list.append(mse)
            # if mse > check:
            #     print('Failed!')

        print(error_list)
        return error_list

    def show_best_func(self):

        for i in self.best_func:
            plt.plot(self.ideal_df[f'x'], self.ideal_df[f'y{i}'], label=f"ideal y{i}")
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()
        # plt.show()

        for i in self.train_df.columns.tolist()[1:]:
            plt.plot(self.train_df[f'x'], self.train_df[f'y{i}'], label=f"train y{i}")
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()
        # plt.show()

