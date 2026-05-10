import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Generate dummy data for System Health Monitoring
# Features: CPU Usage %, Memory Usage %, Disk Usage %, DB Load %
# Labels: 0 (Healthy), 1 (Warning), 2 (Critical)

X = []
y = []

np.random.seed(42)

for _ in range(500):
    # Healthy
    X.append([np.random.uniform(10, 55), np.random.uniform(20, 65), np.random.uniform(10, 75), np.random.uniform(10, 45)])
    y.append(0)
    
    # Warning
    X.append([np.random.uniform(55, 80), np.random.uniform(65, 85), np.random.uniform(75, 90), np.random.uniform(45, 75)])
    y.append(1)
    
    # Critical
    X.append([np.random.uniform(80, 100), np.random.uniform(85, 100), np.random.uniform(90, 100), np.random.uniform(75, 100)])
    y.append(2)

X = np.array(X)
y = np.array(y)

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

with open('system_health_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as system_health_model.pkl")
