import matplotlib.pyplot as plt

import data_manager
import graph
import model


if __name__ == "__main__":

    # create Data Manager for initialization of data base and load data into a variable
    manager = data_manager.Manager()
    data_list = manager.load_data()

    model = model.Model(data_list)
    keys = model.get_best_func()
    test_table = model.validate_best_func(best_func_keys=keys)


    graph.plot_data(data_list['ideal'], label='Ideal Functions', multiple_y=True)
    graph.plot_data(data_list['test'], label='Test Data', multiple_y=False)
    graph.plot_data()



