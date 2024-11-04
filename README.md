# Real-Time Fraud Detection in Financial Transactions

## Overview

This project implements a real-time fraud detection system for financial transactions. The system analyzes incoming transaction data to flag potentially fraudulent activities based on historical patterns and behavioral analysis. It utilizes several data structures and algorithms to achieve high efficiency and accuracy.

## Features

- Real-time detection of fraudulent transactions
- Use of advanced algorithms such as Bloom Filters, Graph Theory, and Machine Learning
- Sliding window analysis for monitoring recent transaction behavior

## Data Structures & Algorithms Used

1. **Bloom Filters**: Efficiently checks if a transaction pattern has been previously flagged without storing every detail.
2. **Graph Theory (Community Detection)**: Analyzes relationships between accounts (nodes) to detect fraud rings or networks.
3. **Machine Learning Algorithms (e.g., Decision Trees)**: Trained on past data to identify unusual patterns by comparing with known fraud characteristics.
4. **Sliding Windows for Streaming Data**: Analyzes recent transactions within a fixed window size, helping to detect anomalies in behavior over a short period.

### Time Complexity

- **Bloom Filter Lookups**: O(1), highly efficient for real-time applications.
- **Graph Community Detection**: Varies based on graph size, typically O(V log V).
- **Sliding Window Analysis**: O(N) for each window update, where N is the window size.

## Requirements

- Python 3.x
- Required libraries listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hanushrajputh/real_time_fraud_detection.git
   cd real_time_fraud_detection
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Bash or Zsh
   # or
   source venv/bin/activate.fish  # For Fish shell
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the fraud detection system, execute the following command:

```bash
python main.py
```

The program simulates financial transactions and checks each transaction for potential fraud, printing results to the console.

## Directory Structure

```plaintext
real_time_fraud_detection/
│
├── bloom_filter.py          # Implementation of the Bloom Filter
├── fraud_detection_model.py  # Machine learning model for fraud detection
├── graph_community_detection.py # Graph community detection logic
├── main.py                  # Entry point for the application
├── requirements.txt         # List of required packages
├── sliding_window.py        # Sliding window implementation for streaming data
└── README.md                # Project documentation
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.
