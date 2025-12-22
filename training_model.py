import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

print("Memuat data...")
df = pd.read_csv('./data/data_bersih.csv')

columns_to_drop = [
    'instant', 
    'dteday',   
    'casual',      
    'registered',  
    'cnt'
]

print(f"\nMenghapus kolom: {columns_to_drop}")
X = df.drop(columns_to_drop, axis=1) 
y = df['cnt'] 

print("Kolom yang dipakai untuk training:", list(X.columns))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# latih model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# evaluasi model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R2 Score: {r2:.4f}")

# simpan model
joblib.dump(model, './model/bike_sharing_rf_model.pkl')
print("\nModel BERHASIL diperbarui dan disimpan sebagai 'bike_sharing_rf_model.pkl'")