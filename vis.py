import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(
    "UTKFace_with_age_range.csv",
    index_col=False,
    usecols=["gender", "race", "age_range", "age"],
)

X = data[["gender", "race"]]
y = data["age_range"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()  # Initialize the model
model.fit(X_train, y_train)  # Train the model
predictions = model.predict(X_test)  # Make predictions
accuracy = accuracy_score(y_test, predictions)  # Compute accuracy
print(f"Model accuracy: {accuracy}")

tree.plot_tree(
    model,
    filled=True,
    proportion=True,
    rounded=True,
    feature_names=["gender", "race"],
    class_names=["Underage", "Young Adult", "Adult", "Old"],
)
plt.savefig("tree.png", dpi=500)
plt.clf()
sns.countplot(data=data, x="age")
plt.savefig("age.png", dpi=500)
plt.clf()
sns.countplot(data=data, x="race")
plt.savefig("race.png", dpi=500)
plt.clf()
sns.countplot(data=data, x="gender")
plt.savefig("gender.png", dpi=500)
plt.clf()
sns.countplot(data=data, x="age_range")
plt.savefig("age_range.png", dpi=500)
plt.clf()
