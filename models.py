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

    def __init__(self):
        pass

    # in future: poisson model gets as argument class with saved data