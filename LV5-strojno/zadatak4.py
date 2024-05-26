import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Učitavanje podataka
data = pd.read_csv('occupancy_processed.csv')

# Podijela podataka na skup za učenje i skup za testiranje (omjer 80%-20%)
X_train, X_test, y_train, y_test = train_test_split(data[['S3_Temp', 'S5_CO2']], data['Room_Occupancy_Count'], test_size=0.2, stratify=data['Room_Occupancy_Count'])

# Inicijalizacija i treniranje modela logističke regresije
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Predikcija na skupu za testiranje
y_pred = log_reg.predict(X_test)

# Prikaz matrice zabune
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(conf_matrix)

# Izračun točnosti klasifikacije
accuracy = accuracy_score(y_test, y_pred)
print("Točnost klasifikacije:", accuracy)

# Izračun preciznosti i odziva po klasama
precision = precision_score(y_test, y_pred, average=None)
recall = recall_score(y_test, y_pred, average=None)

print("Preciznost po klasama:", precision)
print("Odziv po klasama:", recall)
