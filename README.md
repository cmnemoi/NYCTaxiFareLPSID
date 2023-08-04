# NYCTaxiFareLPSID

Repository for the first Data Science project of Lille's Bachelor of Economics, which consists of participating in the Kaggle competition [New York City Taxi Fare Prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction) by Enzo Risbetz and Charles-Meldhine Madi Mnemoi.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cmnemoi-nyc-taxi-fare.streamlit.app/)

# Installation

You need Python 3.9+ to run this project. If you have Anaconda or Miniconda, create a virtual environment with the following commands and then install the required packages:
```bash
conda create -n NYCTaxiFareLPSID python=3.9 -y
conda activate NYCTaxiFareLPSID
pip install -r requirements.txt
```

To run the app locally : `streamlit run src/app/main.py`

You need a Google Maps API key to run the app locally. You can get one [here](https://developers.google.com/maps/documentation/javascript/get-api-key).
Then create a `.streamlit/secrets.toml` file with the following content: `GOOGLE_MAPS_API="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"`

Tools used: Python (Pandas, Seaborn, Scikit-learn, Intel Extension for Scikit-learn, tune-sklearn, Streamlit), Google Maps API

Our approach was as follows:
* **Development of a Data Science project roadmap**
* **Data cleaning**
  * Handling missing values
  * Handling outliers
* **Exploratory analysis**
  * Study of explanatory variables distributions
  * Identification of interesting variables for prediction through correlation and statistical tests
  * Creation of new variables
* **Modeling**
  * Preprocessing
    * OrdinalEncoding, Standard scaling, and Trimming of extreme values with a custom FunctionTransformer
  * Model training
    * Cross-validation to observe learning curves and find optimal hyperparameters using GridSearchCV
    * Model selection based on comparison of metrics (MSE and MAE) from cross-validation results
  * Evaluation of the final model on test data
* **Deployment**
  * Creation of Scikit-learn pipelines for automated preprocessing and model export using joblib
  * Creation of a web application using Streamlit

Experience feedback:
* Application of our data manipulation and modeling skills
* Deepening of our knowledge in handling Scikit-learn pipelines
* Encountered a new problem: computation time for very large datasets
  * Discovery of libraries to accelerate it (somewhat): sklearnex and tune-sklearn