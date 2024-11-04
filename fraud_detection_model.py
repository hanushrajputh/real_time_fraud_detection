# fraud_detection_model.py
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class FraudDetectionModel:
    def __init__(self):
        # Dummy training data: 2 features instead of 3
        X_train = np.array([[100, 1], [200, 2], [150, 1], [300, 2]])  # Example features
        y_train = np.array([0, 1, 0, 1])  # Labels: 0 for non-fraud, 1 for fraud
        self.model = DecisionTreeClassifier()
        self.model.fit(X_train, y_train)

    def predict(self, transaction):
        # Adjust the features based on training data
        features = [transaction["amount"], transaction["account_from"]]  # Only use 2 features
        return self.model.predict([features])[0] == 1
