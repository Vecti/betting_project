# here defined basic model class

class Models():
    """
    Parent class for specific models
    Currently empty, in future with abstract methods like evaluate/score/predict etc
    """

    def __init__(self):
        pass


class PoissonModel(Models):
    """
    Basic model which calculates attack/def ratio for given clubs and calculates probabilities for given scenario using 
    Poisson distribution.
    For future: try bivariete poisson distribution
    """
    # poisson shouldn get data as argument
    # but on which you want to calculate it?
    # it must get data (as arima gets it) - BUT IT IS NOT ITS 
    def __init__(self, data):
        self.data = data
    

    
    # static method does not get implicit first argument
    #so this first argument should 

    # use staticmethod if function is not 'dependent on the object of the class'
    # so if we want something like 'is provided number > 20' when
    # a) number is from self. -> dont use static
    # b) number is random - use static

    def sum_of_goal(self, scored_goal_column):
        return sum(self.data[scored_goal_column])

    def attack_team_ratio(self, team,  scored_goal_column, number_of_games_column):
        return self.data.loc[self.data['Team'] == team][scored_goal_column] / self.data.loc[self.data['Team'] == team][number_of_games_column]

    def global_attack_ratio(self, scored_goal_column):
        return self.sum_of_goal(scored_goal_column) / (28*9)

    # in future: poisson model gets as argument class with saved data