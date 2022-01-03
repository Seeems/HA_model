import matplotlib.pyplot as plt

import data_manager
import graph
import model


if __name__ == "__main__":

    # create Data Manager for initialization of data base and load data into a variable
    manager = data_manager.Manager()
    data_list = manager.load_data()

    #graph.plot_data(data_list['ideal'], multiple_y=True)
    #graph.plot_data(data_list['test'], multiple_y=False)

    model = model.Model(data_list)
    model.validate_best_func()


