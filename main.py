import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_dataset(dataset, target_col):
    """
    Preprocesses a given dataset by performing label encoding on categorical variables
    and standardization on numerical variables.
    
    Args:
        dataset (pandas.DataFrame): The dataset to be preprocessed.
        target_col (str): The name of the target column in the dataset.

    Returns:
        preprocessed_dataset (pandas.DataFrame): The preprocessed dataset.
    """
    # Separate features and labels
    X = dataset.drop(target_col, axis=1)
    y = dataset[target_col]

    # Perform label encoding for categorical variables
    cat_cols = X.select_dtypes(include='object').columns
    for col in cat_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    # Perform standardization for numerical variables
    num_cols = X.select_dtypes(include='number').columns
    scaler = StandardScaler()
    X[num_cols] = scaler.fit_transform(X[num_cols])

    # Return preprocessed dataset
    preprocessed_dataset = pd.concat([X, y], axis=1)
    return preprocessed_dataset
