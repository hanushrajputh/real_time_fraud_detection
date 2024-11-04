
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class FraudDetectionModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        self.model.fit(np.array([[1, 0], [0, 1]]), [0, 1])

    def predict(self, transaction):
        features = [transaction["amount"], transaction["account_from"], transaction["account_to"]]
        return self.model.predict([features])[0] == 1
    