import unittest
import pandas as pd
from src.data_preprocessing import preprocess


class TestPreprocess(unittest.TestCase):
    """
    A test case class for testing the preprocess module.
    """

    def setUp(self):
        """
        Set up the test case by creating a sample DataFrame.
        """
        data = {
            'userId': [1, 2, 3, None],
            'movieId': [1, 2, 3, 4],
            'rating': [5.0, 4.0, 3.0, None]
        }
        self.df = pd.DataFrame(data)

    def test_load_data(self):
        """
        Test the load_data function.
        """
        df = preprocess.load_data('data/raw/ml-latest-small/ratings.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_clean_data(self):
        """
        Test the clean_data function.
        """
        df_cleaned = preprocess.clean_data(self.df)
        self.assertFalse(df_cleaned.isnull().values.any())

    def test_preprocess_data(self):
        """
        Test the preprocess_data function.
        """
        df_preprocessed = preprocess.preprocess_data(self.df.dropna())
        self.assertIn('user_id', df_preprocessed.columns)
        self.assertIn('movie_id', df_preprocessed.columns)


if __name__ == '__main__':
    unittest.main()
