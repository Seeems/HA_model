import setup_logger
from model import Model


class Analyzer(Model):
    """
    Analyzer Class for data analytics.

    Classes:
        Analyzer

    Functions:
        validation_kpi()
    """
    def __init__(self, data, test_table_df):
        super().__init__(data)
        self.test_table_df = test_table_df
        self.logger = setup_logger.setup('analytics')

    def validation_kpi(self):
        """
        Print KPIs (Rate, Percentage, Mean of Difference) of validated functions.
        This is used for data interpretation.
        :return: None
        """
        df_length = len(self.test_table_df.index)
        nan_count = self.test_table_df['Delta Y'].isna().sum()
        rate = df_length - nan_count
        percentage = (rate/df_length)*100
        difference_mean = self.test_table_df['Delta Y'].mean()

        self.logger.info(f'Validated Data - Hits: {rate} of {df_length}')
        self.logger.info(f'Validated Data - HitRate: {percentage}%')
        self.logger.info(f'Validated Data - Mean: {difference_mean}')
        print('----------------Analytics-------------------')
        print(f'Train Data Shape: {train_df.shape}')
        print(f'Ideal Data Shape: {ideal_df.shape}')
        print(f'Test Data Shape: {test_df.shape}')
        print('--------------------------------------------')
        print(f'Test difference lower than train difference which is factorized with sqrt(2)')
        print(f'{rate} of {df_length}')
        print(f'{percentage}%')
        print(f'{difference_mean}')

        return True
