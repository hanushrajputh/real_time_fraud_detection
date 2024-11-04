
from bloom_filter import BloomFilter
from graph_community_detection import GraphCommunityDetector
from fraud_detection_model import FraudDetectionModel
from sliding_window import SlidingWindow
import random

bloom_filter = BloomFilter(size=1000, hash_count=3)
community_detector = GraphCommunityDetector()
fraud_model = FraudDetectionModel()
window = SlidingWindow(window_size=100)

def simulate_transaction():
    return {
        "transaction_id": random.randint(1, 10000),
        "account_from": random.randint(1, 100),
        "account_to": random.randint(1, 100),
        "amount": random.uniform(10, 1000)
    }

def detect_fraud(transaction):
    if bloom_filter.check(transaction["transaction_id"]):
        print("Potential fraud detected: Bloom Filter flagged")

    community_result = community_detector.analyze(transaction)
    if community_result:
        print("Potential fraud detected: Community detection flagged")

    is_fraud = fraud_model.predict(transaction)
    if is_fraud:
        print("Potential fraud detected: ML Model flagged")

def main():
    for _ in range(100):
        transaction = simulate_transaction()
        window.add(transaction)
        detect_fraud(transaction)

if __name__ == "__main__":
    main()
    