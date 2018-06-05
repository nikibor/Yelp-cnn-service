from keras.models import load_model
import numpy as np


class CNN:

    def __init__(self):
        self.model = load_model('./data/CNN.h5')

    def classify(self, vector):
        input = np.array(vector)
        input = input.reshape(1, 10, 10, 1)
        result = self.model.predict(input)
        return result


class LSTM:

    def __init__(self):
        self.model = load_model('./data/LSTM.h5')

    def classify(self, vector):
        input = np.array(vector)
        input = input.reshape(1, 10, 10, 1)
        result = self.model.predict(input)
        return result


class GradientDescent:
    def __init__(self):
        self.model = load_model('./data/LSTM.h5')

    def classify(self, vector):
        pass


class LogisticRegression:
    def __init__(self):
        pass

    def classify(self, vector):
        pass
