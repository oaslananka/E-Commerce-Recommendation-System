
# E-Commerce Recommendation System

## Project Description

This project aims to develop a recommendation engine that provides personalized product recommendations for an e-commerce platform. By analyzing users' past shopping data, a machine learning model will be created to predict products they may be interested in in the future.

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
