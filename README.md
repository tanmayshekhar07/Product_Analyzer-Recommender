# Product_Recommendation_System

This project focuses on building a robust Product Recommendation System, paired with a detailed Sentiment Analysis of each product. It's designed to offer insightful product recommendations to users while analyzing customer sentiments associated with each product.

## Project Overview

The system is developed using Python and Jupyter Notebooks. The primary objectives of the project include:

### Product Recommendation: 
Utilize collaborative filtering and other advanced techniques to recommend products to users.
Sentiment Analysis: Perform an in-depth sentiment analysis on product reviews to gauge customer satisfaction and preferences.
Repository Structure

### Final.ipynb: 
This Jupyter Notebook contains the core logic of the project. It involves steps like data preprocessing, model building for the recommendation system, and sentiment analysis algorithms.
app.py: A Streamlit-based web application that allows users to interact with the recommendation system and view sentiment analysis results.
Key Features


## Recommendation System:
We used two main methods or metrics on which we built our Recommendation models and those were Cosine similarity and Word2Vec.
● Similarity Matrix: We computed a cosine similarity matrix from the TF-IDF vectors. This similarity matrix quantifies the likeness between products based on their names.
● Function Design: A function was created that takes a product name as input and returns a list of top similar products based on cosine similarity scores from the TF-IDF vectors.
● Word2Vec Based Model Implementation: A Word2Vec model was trained on the tokenized product names to capture semantic relationships in the text.
● The recommendation function was further revised to work with the Word2Vec-based features, providing recommendations that consider both textual semantics and price.

After Performing the Sentiment Analysis to our Dataset we added a column labelled as Sentiment and our main goal with this column was to provide the user with a Sentiment Count graph of the product of his/her choice which would help the user decide if the product is worth buying or no.


### Recommendation Engine: 
The system recommends products based on user preferences and historical data, using techniques like cosine similarity.
Sentiment Analysis: Analyzes customer reviews to determine the sentiment (positive, negative, neutral) towards each product.
Interactive Web Application: Built using Streamlit, this application provides a user-friendly interface for interacting with the recommendation system and viewing sentiment analysis.
Technologies Used

Python: Primary programming language.
Pandas, Matplotlib, Seaborn: For data manipulation and visualization.
Scikit-learn, NLTK: For building the recommendation model and performing sentiment analysis.
Streamlit: For creating the web application.
Getting Started

To get started with this project, you need to have Python installed on your system. Follow these steps:

Clone the repository to your local machine.
Install the required dependencies: pip install -r requirements.txt.
Run the Jupyter Notebook (Final.ipynb) to understand the logic behind the recommendation system and sentiment analysis.
Launch the Streamlit app (app.py) to interact with the system.
Usage

## Comclusion: 
The sentiment analysis project aimed at dissecting cell phone reviews from Amazon has provided substantial insights into the application of machine learning and deep learning models in NLP tasks. The comprehensive journey from data acquisition through preprocessing to modeling and evaluation has underscored the intricate challenges and considerations inherent in sentiment analysis.

## Achievements: 
### Sentiment Analysis:
Objective: The goal was to extract insights from customer reviews, categorizing them into positive, negative, or neutral sentiments. This understanding is crucial for businesses to gauge customer satisfaction and improve their offerings.
Process: Utilizing natural language processing (NLP) techniques, the textual data from reviews was preprocessed, tokenized, and vectorized. Machine learning models like Naive Bayes, SVM, or deep learning models like LSTM could have been employed to classify the sentiment of each review.
Outcome: The sentiment analysis would provide valuable insights into customer opinions and trends, which can inform product development, marketing strategies, and customer service improvements.

### Recommendation System:
Objective: To develop a system that suggests products to users based on their preferences,
using content-based filtering approaches.
TF-IDF Approach: We initially employed a TF-IDF vectorization strategy to transform 'product_name' data into a numerical format, followed by cosine similarity calculations to find similar products.
Word2Vec Approach: As an alternative, we implemented a Word2Vec model, which provided semantic representations of the product names. This model was combined with normalized price data for a more nuanced recommendation.
Streamlit UI: A user-friendly interface was created using Streamlit, allowing users to interact with the system and receive personalized recommendations.

### Integration of Sentiment Analysis and Recommendation System:
The sentiment analysis and recommendation system, though developed independently, can be integrated. The insights from sentiment analysis (like identifying highly favored products) can refine the recommendation engine, prioritizing products with positive sentiments.

Use the Final.ipynb notebook for a detailed walkthrough of the data processing, model building, and analysis phases.
Launch the Streamlit app for a practical application of the recommendation system and sentiment analysis.
License

## This project is licensed under the MIT License 
- see the LICENSE.md file for details.
