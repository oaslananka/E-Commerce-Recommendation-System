
# E-Commerce Recommendation System

## Project Description

A comprehensive project that develops a personalized product recommendation system for an e-commerce platform. This project utilizes machine learning techniques to analyze user behavior and predict products that users are likely to be interested in. The solution is built with Python, leveraging popular libraries such as Pandas, scikit-learn, and Surprise, and is designed to be easily deployable using Docker and cloud services like AWS and Google Cloud.

## Key Features

- Data Processing: Includes scripts for cleaning, preprocessing, and transforming raw e-commerce data.
- Model Training: Implements collaborative filtering using matrix factorization techniques.
- Evaluation: Provides tools for cross-validation and model performance evaluation.
- Deployment: Dockerized environment for easy deployment and scalability.
- Extensive Documentation: Detailed notebooks for data exploration, feature engineering, and model training.
- Testing: Comprehensive unit tests to ensure code reliability and correctness.

## Technologies Used

- Python
- Pandas
- scikit-learn
- Surprise
- Docker
- AWS SageMaker
- Google Cloud AI Platform

## File and Folder Structure

```
E-Commerce-Recommendation-System/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── feature_engineering.ipynb
│   └── model_training.ipynb
│
├── src/
│   ├── data_preprocessing/
│   │   ├── __init__.py
│   │   └── preprocess.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── recommender.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── main.py
│
├── tests/
│   ├── test_preprocess.py
│   ├── test_recommender.py
│   └── test_helpers.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── configs/
│   ├── config.yaml
│   ├── logging.yaml
│   └── credentials.yaml
│
├── scripts/
│   ├── download_data.sh
│   └── run_training.sh
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

The steps required for the project to work are stated below.

### 1. Clone Repository

```sh
git clone https://github.com/oaslananka/E-Commerce-Recommendation-System.git
cd E-Commerce-Recommendation-System
```

### 2. Install Required Libraries

```sh
pip install -r requirements.txt
```

### 3. Download and Prepare Data

```sh
bash scripts/download_data.sh
```

### 4. Model Training

```sh
bash scripts/run_training.sh
```

## Use

Once the model is trained, you can make predictions with the following command:

```python
from src.model.recommender import Recommender
import pandas as pd

# Load processed data
# df = pd.read_csv('data/processed/ratings_processed.csv')

# Instantiate the Recommender class and load the model
recommender = Recommender(df)
recommender.train_model()

# Sample prediction
user_id = 1
movie_id = 1
prediction = recommender.predict(user_id, movie_id)
print(f'User {user_id}  Movie {movie_id} prediction: {prediction}')
```

## Contribute

If you would like to contribute, please submit a pull request. Any contributions and feedback are welcomed.

## Licence

This project is licensed under the MIT License.
