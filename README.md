# NYCTaxiFareLPSID
Repository pour le premier projet de Data Science de la LP SID qui consiste à participer à la compétition Kaggle [New York City Taxi Fare Prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction) par Enzo Risbetz et Charles-Meldhine Madi Mnemoi.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bit.ly/LPRoubaixNYCTaxiFare)

Outils utilisés : Python (Pandas, Seaborn, Scikit-learn, Intel Extension for Scikit-learn, tune-sklearn, Streamlit), Google Maps API

Notre démarche a été la suivante :
 * **Réalisation d'une feuille de route d'un projet Data Science**
 * **Nettoyage des données**
   * Gestion des valeurs manquantes 
   * Gestion des valeurs aberrantes 
* **Analyse exploratoire**
  * Etude des distributions des variables explicatives
  * Identification des variables intéressantes pour la prédiction avec l'étude des corrélations et des tests statistiques
  * Création de nouvelles variables
* **Modélisation**
  * Préprocessing 
    * OrdinalEncoding, Standardscaling et Trimming des valeurs extrêmes avec un FunctionTransformer personnalisé
  * Entraînement des modèles
    * Validation croisée pour observer les courbes d'apprentissage et trouver les bons hyperparamètres avec GridSearchCV
    * Choix du modèle à l'aide de la comparaison des métriques (MSE et MAE) sur les résultats de la validation croisée
  * Evaluation du modèle final sur les données de test
* **Mise en production**
  * Création de pipelines Scikit-learn pour automatiser le préprocessing et export du modèle avec joblib
  * Création d'une application web avec Streamlit

Retours d'expérience :
 * Appplication de nos compétences en manipulation de données et modélisation
 * Approfondissement de nos compétences dans la manipulation de pipelines Scikit-learn
 * Première rencontre d'un problème qui nous était inconnu : le temps de calcul pour des très grands datasets
   * Découverte de libraries permettant de l'accélérer (un peu) : sklearnex et tune-skleanr



