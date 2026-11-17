import pandas as pd
import numpy as np


def calculate_bmi(df):
    """
    Calculate the Body Mass Index (BMI) for each individual.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'height' and 'weight' columns.

    Returns:
    pd.DataFrame: DataFrame with an additional 'BMI' column.
    """
    
    if df is None or df.empty:
        return df
    
    df_bmi = df.copy()
    
    if 'height' in df_bmi.columns and 'weight' in df_bmi.columns:
        df_bmi['BMI'] = df_bmi['weight'] / (df_bmi['height'] ** 2)

    return df_bmi


def categorize_bmi(df):
    """
    Categorize the BMI into Underweight, Normal weight, Overweight, and Obese.

    Parameters:
    df (pd.DataFrame): DataFrame containing the 'BMI' column.

    Returns:
    pd.DataFrame: DataFrame with an additional 'BMI_category' column.
    """
    
    if df is None or df.empty:
        return df
    
    df_cat = df.copy()
    
    if 'BMI' in df_cat.columns:
        conditions = [
            df_cat['BMI'] < 18.5,
            (df_cat['BMI'] >= 18.5) & (df_cat['BMI'] < 25),
            (df_cat['BMI'] >= 25) & (df_cat['BMI'] < 30),
            df_cat['BMI'] >= 30
        ]
        
        choises = ['Underweight', 'Normal weight', 'Overweight', 'Obese']
        
        df_cat['BMI_category'] = np.select(conditions, choises, default=None)

    return df_cat


# Example data
data = {
    'height': [1.60, 1.75, 1.82, 1.90, 1.65],
    'weight': [55, 80, 72, 90, 70]
}
df = pd.DataFrame(data)

# Apply the functions to the dataset
df = calculate_bmi(df)
df = categorize_bmi(df)
print(df)
