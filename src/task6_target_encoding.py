import pandas as pd


def target_encode_smoothing(df, column, target, k):
    """
    Perform target encoding on a categorical column with smoothing.

    Parameters:
    df (pd.DataFrame): DataFrame containing the categorical column and target variable.
    column (str): Name of the categorical column to encode.
    target (str): Name of the target variable.
    k (float): Smoothing parameter to control the impact of small sample sizes.

    Returns:
    pd.DataFrame: DataFrame with an additional encoded column.
    """
    
    if df is None or df.empty or column not in df.columns or target not in df.columns:
        return df
    
    df_encoded = df.copy()
    global_mean = df_encoded[target].mean()
    stats = df_encoded.groupby(column)[target].agg(['count', 'mean'])
    counts = stats['count']
    means = stats['mean']
    smoothed_means = (counts * means + k * global_mean) / (counts + k)
    encoded_col_name = f"{column}_encoded"
    df_encoded[encoded_col_name] = df_encoded[column].map(smoothed_means)
    
    return df_encoded


# Example data
data = {
    'color': ['red', 'blue', 'green', 'red', 'blue', 'green'],
    'target': [1, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Apply the function to the dataset
df_encoded = target_encode_smoothing(df, 'color', 'target', k=2)
print(df_encoded)