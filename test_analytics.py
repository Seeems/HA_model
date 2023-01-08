import unittest
import analytics
import data_manager
import model as md


class UnitTestAnalytics(unittest.TestCase):

    def test_validation_kpi(self):
        manager = data_manager.Manager()
        data_list = manager.load_data()
        model = md.Model(data_list)
        keys = model.get_best_func()
        test_table = model.validate_best_func(best_func_keys=keys)
        analyzer = analytics.Analyzer(data_list, test_table)
        result = analyzer.validation_kpi()
        self.assertTrue(result)
