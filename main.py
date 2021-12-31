import seaborn as sns
import matplotlib.pyplot as plt

import data_manager
import graph
import model


sns.set_theme(style="darkgrid")

if __name__ == "__main__":

    # create Data Manager for initialization of data base and load data into a variable
    manager = data_manager.Manager()
    data_list = manager.load_data()
    
    model.func(data_list)
    
    # Herausfinden, welche Art von Funktion gesucht ist --> Polynom 2. Grade
    i = 1
    while i <= 50:
        break
        sns.lineplot(data_list['train']['x'], data_list['train'][f'y{i}'])
        i += 1
        plt.show()

    # model.func(data_list)

