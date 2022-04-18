# class to extract and prepare required data for models
import pandas as pd

class DataProvider():
    """
    for now read local file, in future - read data from web
    """

    def __init__(self, path) -> None:
        self.data = self.load_and_data(path, sep=';')

    def load_and_data(self, path, sep):
        self.data =  pd.read_csv(path, sep=sep)
        return self.data
    

    

    # @classmethod
    # def sum_of_goal(scored_goal_column):
    #     return self.data.scored_goal_column
    


