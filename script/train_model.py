import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
data = pd.read_csv(
    "dataset/heart_statlog_cleveland_hungary_final.csv"
)

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)

# Features and target
X = data.drop("target", axis=1)
y = data["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

# Train
print("Training Random Forest model...")

model.fit(X_train, y_train)

print("Model training completed!")

# Test
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL RESULTS")
print("==============================")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model in MAIN project folder
joblib.dump(
    model,
    "random_forest_model.pkl"
)

print("\n==============================")
print("SUCCESS")
print("==============================")
print("Model saved as random_forest_model.pkl")