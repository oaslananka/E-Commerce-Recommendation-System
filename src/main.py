from src.data_preprocessing import preprocess
from src.model.recommender import Recommender
from src.utils.helpers import setup_logging, log_info, log_error

def main():
    """
    This is the main function of the E-Commerce Recommendation System.
    It performs the following steps:
    1. Sets up logging.
    2. Loads raw data from a CSV file.
    3. Cleans and preprocesses the data.
    4. Saves the processed data to a new CSV file.
    5. Trains a recommendation model.
    6. Evaluates the trained model.
    7. Makes a prediction for a specific user and movie.
    """
    setup_logging('logs/app.log')
    
    try:
        raw_data_path = 'data/raw/ml-latest-small/ratings.csv'
        processed_data_path = 'data/processed/ratings_processed.csv'
        log_info('Loading data...')
        df = preprocess.load_data(raw_data_path)
        
        log_info('Data is being cleaned and processed...')
        df = preprocess.clean_data(df)
        df = preprocess.preprocess_data(df)
        
        log_info('Saving processed data...')
        preprocess.save_processed_data(df, processed_data_path)
        
        log_info('The model is being trained...')
        recommender = Recommender(df)
        recommender.train_model()
        
        log_info('The model is being evaluated...')
        evaluation_results = recommender.evaluate_model()
        log_info(f'Evaluation Results: {evaluation_results}')
        
        user_id = 1
        movie_id = 1
        prediction = recommender.predict(user_id, movie_id)
        log_info(f'User {user_id} Movie {movie_id} estimate: {prediction}')
    
    except Exception as e:
        log_error(f'Hata: {str(e)}')

if __name__ == "__main__":
    main()
