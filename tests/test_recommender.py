import unittest
import pandas as pd
from src.model.recommender import Recommender


class TestRecommender(unittest.TestCase):
    """
    A test case for the Recommender class.

    This test case includes test methods to verify the functionality of the Recommender class.

    Attributes:
        df (pandas.DataFrame): The test DataFrame containing user ratings.
        recommender (Recommender): An instance of the Recommender class.

    """

    def setUp(self):
        """
        Set up the test environment by creating a DataFrame and initializing the Recommender object.

        This method is called before each test case to prepare the necessary data and objects.

        Parameters:
        - None

        Returns:
        - None
        """
        data = {
            'user_id': [0, 1, 2],
            'movie_id': [0, 1, 2],
            'rating': [5.0, 4.0, 3.0]
        }
        self.df = pd.DataFrame(data)
        self.recommender = Recommender(self.df)

    def test_prepare_data(self):
        """
        Test the prepare_data method of the Recommender class.

        This method verifies that the prepare_data method returns a non-empty result.

        Parameters:
        - None

        Returns:
        - None
        """
        data = self.recommender.prepare_data()
        self.assertIsNotNone(data)

    def test_train_model(self):
        """
        Test the train_model method of the Recommender class.

        This method verifies that the train_model method sets the model attribute to a non-empty value.

        Parameters:
        - None

        Returns:
        - None
        """
        self.recommender.train_model()
        self.assertIsNotNone(self.recommender.model)

    def test_predict(self):
        """
        Test the predict method of the Recommender class.

        This method verifies that the predict method returns a float value.

        Parameters:
        - None

        Returns:
        - None
        """
        self.recommender.train_model()
        prediction = self.recommender.predict(0, 0)
        self.assertIsInstance(prediction, float)

    def test_evaluate_model(self):
        """
        Test the evaluate_model method of the Recommender class.

        This method verifies that the evaluate_model method returns a dictionary with 'test_rmse' and 'test_mae' keys.

        Parameters:
        - None

        Returns:
        - None
        """
        self.recommender.train_model()
        results = self.recommender.evaluate_model()
        self.assertIn('test_rmse', results.keys())
        self.assertIn('test_mae', results.keys())


if __name__ == '__main__':
    unittest.main()
