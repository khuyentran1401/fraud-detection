# **DEMO**: Fraud Detection Application

Demo application for Git submodules tutorial. Shows how to use shared ML utilities as a Git submodule for feature engineering and risk scoring.

## Features

- **Feature Engineering**: Extract time-based features for fraud detection
- **Risk Scoring**: Calculate risk scores using shared utilities
- **Shared Dependencies**: Uses `ml-utils` submodule for consistent feature engineering

## Setup

1. **Clone with submodules**:
   ```bash
   git clone --recurse-submodules https://github.com/khuyentran1401/fraud-detection-demo.git
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

## Architecture

This application demonstrates how to use Git submodules to share ML utilities across projects:

- `main.py` - Main fraud detection pipeline
- `ml-utils/` - Shared ML utilities (Git submodule)
  - `features.py` - Feature engineering functions
  - Risk scoring and validation utilities

## Usage

The application processes transaction data and generates features for fraud detection using shared ML utilities that are also used by credit scoring and trading algorithm projects.