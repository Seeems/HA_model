import unittest
from data_manager import Manager
from model import Model


class UnitTestModel(unittest.TestCase):

    def test_get_best_func(self):
        manager = Manager()
        data_list = manager.load_data()
        model = Model(data_list)

        ideal_func = ['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11', 'y12', 'y13', 'y14',
                      'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23', 'y24', 'y25', 'y26', 'y27',
                      'y28', 'y29', 'y30', 'y31', 'y32', 'y33', 'y34', 'y35', 'y36', 'y37', 'y38', 'y39', 'y40',
                      'y41', 'y42', 'y43', 'y44', 'y45', 'y46', 'y47', 'y48', 'y49', 'y50']
        list_keys = model.get_best_func()
        if all(x in ideal_func for x in list_keys):
            check_var = True
        else:
            check_var = False
        self.assertTrue(check_var, f'The List {str(list_keys)} should contain some functions from y1 to y50')
