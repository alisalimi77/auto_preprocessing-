# Data Preprocessor

A Python class for data preprocessing tasks such as object to numeric transformation, handling null values, standardization, and normalization.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Methods](#methods)
- [Examples](#examples)
- [License](#license)

## Introduction

The `DataPreprocessor` class provides methods to perform common data preprocessing tasks. It supports object to numeric transformation, handling null values, standardization, and normalization. The class utilizes the pandas library and scikit-learn's `StandardScaler` and `MinMaxScaler` for certain operations.

## Usage

To use the `DataPreprocessor` class, follow these steps:

1. Import the necessary libraries:
    ```python
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import MinMaxScaler
    ```

2. Create an instance of the `DataPreprocessor` class:
    ```python
    preprocessor = DataPreprocessor()
    ```

3. Perform the desired data preprocessing tasks using the available methods:
    - Object to Numeric Transformation:
        ```python
        transformed_data = preprocessor.object_to_numeric(dataset)
        ```
    - Handling Null Values:
        ```python
        filled_data = preprocessor.handle_null_values(dataset, fill_value)
        ```
    - Standardization:
        ```python
        standardized_data = preprocessor.standardize_dataset(dataset)
        ```
    - Normalization:
        ```python
        normalized_data = preprocessor.normalize_dataset(dataset)
        ```

## Methods

- `object_to_numeric(dataset)`: Converts object data to numerical data in the dataset.
- `handle_null_values(dataset, fill_value)`: Handles null values in the dataset by filling them with a specified value.
- `standardize_dataset(dataset)`: Standardizes the dataset by scaling the numerical features to have zero mean and unit variance.
- `normalize_dataset(dataset)`: Normalizes the dataset by scaling the numerical features to a fixed range (e.g., [0, 1]).

## Examples

Here are some examples of how to use the `DataPreprocessor` class:

```python
# Create an instance of DataPreprocessor
preprocessor = DataPreprocessor()

# Object to Numeric Transformation
transformed_data = preprocessor.object_to_numeric(dataset)

# Handling Null Values
filled_data = preprocessor.handle_null_values(dataset, fill_value)

# Standardization
standardized_data = preprocessor.standardize_dataset(dataset)

# Normalization
normalized_data = preprocessor.normalize_dataset(dataset)
