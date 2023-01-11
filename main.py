import data_manager
import graph
import model
import analytics


if __name__ == "__main__":

    # create Data Manager for initialization of data base and load data into a variable
    manager = data_manager.Manager()
    data_list = manager.load_data()

    model = model.Model(data_list)
    keys = model.get_best_func()
    test_table = model.validate_best_func(best_func_keys=keys)

    kpi = analytics.Analyzer(data_list, test_table)
    kpi.validation_kpi()

    test_values_nan = test_table[test_table['Delta Y'].isna()]
    test_values_func = test_table[test_table['Delta Y'].notnull()]
    
    manager.write_to_db(test_table, 'Test-Data-Validated')

    graph.plot_data(data_list['ideal'], label='Ideal Functions', multiple_y=True, key='ideal')
    graph.plot_data(data_list['test'], label='Test Data', multiple_y=False)
    graph.plot_data(data_list['train'], label='Train Data', multiple_y=True, key='train')
    graph.plot_validation(test_values_func, test_values_nan, data_list['ideal'], keys, label='Validation Testdata to Ideal Function')



