"""Fraud Detection Application

Uses shared ML utilities for feature engineering and risk scoring.
"""

# Import from shared ML utilities submodule
import sys
import os
import pandas as pd
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.path.dirname(__file__), 'ml-utils'))

from features import extract_time_features, calculate_velocity

def prepare_fraud_features(transactions_df):
    """Prepare features for fraud detection using shared utilities"""
    # Extract time-based features for fraud detection
    df = extract_time_features(transactions_df, 'transaction_time')
    
    # Calculate transaction velocity features
    df = calculate_velocity(df, 'user_id', 'transaction_time')
    
    return df

def main():
    """Main fraud detection pipeline"""
    print("Fraud Detection System")
    print("Using shared ML utilities for feature engineering")
    
    # Create sample transaction data
    sample_transactions = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 3],
        'transaction_time': [
            datetime.now() - timedelta(hours=2),
            datetime.now() - timedelta(hours=1),
            datetime.now() - timedelta(hours=3),
            datetime.now(),
            datetime.now() - timedelta(minutes=30)
        ],
        'amount': [100.0, 250.0, 75.0, 500.0, 150.0]
    })
    
    print(f"\nProcessing {len(sample_transactions)} transactions...")
    
    # Fraud detection model uses consistent utilities
    fraud_features = prepare_fraud_features(sample_transactions)
    print(f"Generated {len(fraud_features.columns)} features for fraud detection")
    print(f"Features: {list(fraud_features.columns)}")
    
    print("\n✅ Successfully using shared ML utilities from submodule!")


if __name__ == "__main__":
    main()