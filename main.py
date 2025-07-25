"""Fraud Detection Application

Uses shared ML utilities for feature engineering and risk scoring.
"""

# Import from shared ML utilities submodule
from ml_utils.features import (
    calculate_risk_score,
    extract_time_features,
    validate_transaction_data
)

import pandas as pd


def prepare_fraud_features(transactions_df):
    """Prepare features for fraud detection model
    
    Args:
        transactions_df: Raw transaction data
        
    Returns:
        DataFrame: Processed features ready for model training
    """
    # Validate data quality using shared validation
    validation_report = validate_transaction_data(transactions_df)
    print(f"Data validation: {validation_report['validation_passed']}")
    
    # Extract time-based features for fraud detection
    df = extract_time_features(transactions_df, 'transaction_time')
    
    # Calculate risk scores
    df['risk_score'] = df.apply(
        lambda row: calculate_risk_score({
            'income': row.get('income', 0),
            'debt': row.get('debt', 0)
        }), axis=1
    )
    
    return df


def main():
    """Main fraud detection pipeline"""
    print("Fraud Detection System")
    print("Using shared ML utilities for feature engineering")
    
    # Sample transaction data
    sample_data = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'transaction_time': [
            '2024-01-15 10:30:00',
            '2024-01-15 14:22:00', 
            '2024-01-15 18:45:00',
            '2024-01-15 09:15:00',
            '2024-01-15 22:10:00'
        ],
        'amount': [100, 250, 75, 500, 180],
        'income': [50000, 75000, 60000, 90000, 45000],
        'debt': [10000, 15000, 0, 25000, 8000]
    })
    
    # Process features using shared utilities
    processed_features = prepare_fraud_features(sample_data)
    
    print(f"\nGenerated {len(processed_features.columns)} features for fraud detection")
    print("\nSample processed data:")
    print(processed_features[['user_id', 'risk_score', 'hour', 'is_weekend']].head())


if __name__ == "__main__":
    main()