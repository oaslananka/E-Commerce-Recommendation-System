import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def clean_data(df):
    df = df.dropna()
    return df


def preprocess_data(df):
    """
    Preprocesses the given DataFrame by encoding the 'userId' and 'movieId' columns.

    Args:
        df (pandas.DataFrame): The input DataFrame containing the 'userId' and 'movieId' columns.

    Returns:
        pandas.DataFrame: The preprocessed DataFrame with the 'user_id' and 'movie_id' columns added.

    """
    df['user_id'] = df['userId'].astype('category').cat.codes
    df['movie_id'] = df['movieId'].astype('category').cat.codes
    return df


def save_processed_data(df, file_path):
    df.to_csv(file_path, index=False)
