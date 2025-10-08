import pandas as pd
from sklearn.linear_model import LinearRegression

# Example dataset
data = {
    "demand": [30, 50, 80, 100, 20],
    "time": [12, 18, 20, 19, 15],
    "weather": [1, 0, 1, 0, 1],  # 1=sunny, 0=rainy
    "price": [10, 14, 18, 17, 9]
}

df = pd.DataFrame(data)

X = df[["demand", "time", "weather"]]  # input features
y = df["price"]  # target

model = LinearRegression()
model.fit(X, y)

print("Predicted price:", model.predict([[70, 19, 1]]))  # demand=70, time=19h, sunny
