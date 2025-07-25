"""Fraud Detection Application

Uses shared ML utilities for feature engineering and risk scoring.
"""

# Import from shared ML utilities submodule
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'ml-utils'))

from features import (
    calculate_risk_score,
    extract_time_features,
    validate_transaction_data
)

def main():
    """Main fraud detection pipeline"""
    print("Fraud Detection System")
    print("Using shared ML utilities for feature engineering")
    
    # Test basic functionality of shared utilities
    sample_data = {'income': 50000, 'debt': 10000}
    risk_score = calculate_risk_score(sample_data)
    
    print(f"\nTesting shared ML utilities:")
    print(f"Risk score calculation: {risk_score}")
    
    # Test validation function (simplified without pandas)
    validation_report = validate_transaction_data({'test': [1, 2, 3]})
    print(f"Validation report: {validation_report}")
    
    print("\n✅ Successfully using shared ML utilities from submodule!")


if __name__ == "__main__":
    main()