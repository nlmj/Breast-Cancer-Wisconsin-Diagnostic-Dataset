import numpy as np

class LinearRegression:
    def __init__(self, alpha, batch_size, num_classes, sequence_length):
        """ Initialisation of Linear Regression Class

        Parameter
        ---------
        alpha : float
            learning rate
        batch_size : int 
            number of samples to work through before updating model parameters
        num_classes : int
            number of classes in dataset
        sequence_length : int
            number of samples in dataset
        """

        self.alpha = alpha
        self.batch_size = batch_size
        self.num_classes = num_classes
        self.sequence_length = sequence_length