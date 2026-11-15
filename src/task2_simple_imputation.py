import pandas as pd


def impute_missing_values(df):
    """
    Impute missing values in the dataset using mean, median, and mode.

    Parameters:
    df (pd.DataFrame): DataFrame with missing values.

    Returns:
    pd.DataFrame: DataFrame with missing values imputed.
    """
    
    if df is None or df.empty:
        return df
    
    df_imputed = df.copy()
    
    if 'A' in df_imputed.columns:
        df_imputed['A'] = df_imputed['A'].fillna(df_imputed['A'].mean())
        
    if 'B' in df_imputed.columns:
        df_imputed['B'] = df_imputed['B'].fillna(df_imputed['B'].median())
        
    if 'C' in df_imputed.columns:
        mode_val = df_imputed['C'].mode()
        if not mode_val.empty:
            df_imputed['C'] = df_imputed['C'].fillna(mode_val[0])
    
    return df_imputed


# Example data
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': ['cat', None, 'dog', 'dog']
}
df = pd.DataFrame(data)

# Apply the function to the dataset
df_imputed = impute_missing_values(df)
print(df_imputed)