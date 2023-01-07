from model import Model


class Analyzer(Model):

    def __init__(self, data, test_table_df):
        super().__init__(data)
        self.test_table_df = test_table_df

    def validation_kpi(self):
        """
        Print KPIs (Rate, Percentage, Mean of Difference) of validated functions.
        :return: None
        """
        df_length = len(self.test_table_df.index)
        nan_count = self.test_table_df['Delta Y'].isna().sum()
        rate = df_length - nan_count
        percentage = (rate/df_length)*100
        difference_mean = self.test_table_df['Delta Y'].mean()

        print(f'Test difference lower than train difference which is factorized with sqrt(2)')
        print(f'{rate} of {df_length}')
        print(f'{percentage}%')
        print(f'{difference_mean}')
