# class to extract and prepare required data for models
import pandas as pd

class DataProvider():
    """
    for now read local file, in future - read data from web
    """

    def __init__(self) -> None:
        pass

    def load_data(self, path):
        self.data =  pd.read_csv(path)
        return self.data
    

    @classmethod
    def sum_of_goal(scored_goal_column):
        return self.data.scored_goal_column
    


