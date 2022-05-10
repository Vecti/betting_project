# here defined basic model class



from scipy.stats import poisson

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
        """
        number of goals scored/number of matches
        """
        return self.data.loc[self.data['Team'] == team][scored_goal_column] / self.data.loc[self.data['Team'] == team][number_of_games_column]

    def global_attack_ratio(self, scored_goal_column):
        """
        sum of all scored goals / amount of matches
        """
        return self.sum_of_goal(scored_goal_column) / (28*9)

    def defend_team_ratio(self, team,  lost_goal_column, number_of_games_column):
        """
        number of goals lost/number of matches
        """
        return self.data.loc[self.data['Team'] == team][lost_goal_column] / self.data.loc[self.data['Team'] == team][number_of_games_column]

    def global_defend_ratio(self, lost_goal_column):
        """
        practically same as global_attack_ration but from opposite perspective
        """
        return self.sum_of_goal(lost_goal_column) / (28*9)
    
    def home_team_goal_expectancy(self, home_team, away_team, scored_goal_column, lost_goal_column, number_of_games_column):
        """
        home team GE: home team attack * away team defence * global attack ratio
        """
        home_team_goal_expected = self.attack_team_ratio(home_team, scored_goal_column, number_of_games_column)
        away_team_goal_expected = self.defend_team_ratio(home_team, lost_goal_column, number_of_games_column)
        return home_team_goal_expected, away_team_goal_expected
    
    def poisson_formula(team, goals_expected):
        """
        simplified version, for given team we provide number of goals expected from home_team..., calculates it
        fill using poisson.pmf(k, lambda)
        """

    # in future: poisson model gets as argument class with saved data