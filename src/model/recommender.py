import pandas as pd
from sklearn.model_selection import train_test_split
from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate


class Recommender:
    """
    A class that represents a recommender system.

    Attributes:
        df (pandas.DataFrame): The input dataframe containing user-item ratings.
        model (surprise.prediction_algorithms.matrix_factorization.SVD): The SVD model used for recommendation.

    Methods:
        prepare_data(): Prepares the data for training the model.
        train_model(): Trains the recommendation model.
        predict(user_id, movie_id): Predicts the rating for a given user and movie.
        evaluate_model(): Evaluates the performance of the recommendation model.
    """

    def __init__(self, df):
        self.df = df
        self.model = SVD()

    def prepare_data(self):
        """
        Prepares the data for training the recommendation model.

        Returns:
            surprise.dataset.Dataset: The prepared dataset for training.
        """
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(self.df[['user_id', 'movie_id', 'rating']], reader)
        return data

    def train_model(self):
        """
        Trains the recommendation model.
        """
        data = self.prepare_data()
        trainset = data.build_full_trainset()
        self.model.fit(trainset)

    def predict(self, user_id, movie_id):
        """
        Predicts the rating for a given user and movie.

        Args:
            user_id (int): The ID of the user.
            movie_id (int): The ID of the movie.

        Returns:
            float: The predicted rating.
        """
        return self.model.predict(user_id, movie_id).est

    def evaluate_model(self):
        """
        Evaluates the performance of the recommendation model.

        Returns:
            dict: The evaluation results including RMSE and MAE.
        """
        data = self.prepare_data()
        results = cross_validate(self.model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
        return results
