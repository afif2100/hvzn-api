import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import joblib


# Run in name called
if __name__ == "__main__":
    # Load the diabetes dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
    )
    df = df[["Age", "BMI", "Outcome"]]
    X = df[["Age", "BMI"]]
    y = df["Outcome"]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0
    )

    # Create an instance of the logistic regression model
    model = LogisticRegression(max_iter=100)

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Print the accuracy of the model
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    # save model
    with open("model/model.pkl", mode="wb") as file:
        joblib.dump(model, file)
