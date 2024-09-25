import os
import numpy as np
import numpy as np, pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn import tree, metrics, model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
# Veriyi yükleme
data = pd.read_csv(&#39;heart.csv&#39;)
# Sınıf değişkenini belirleme
data[&#39;target&#39;],target_names = pd.factorize(data[&#39;target&#39;])
print(target_names)
print(data[&#39;target&#39;].unique())
#veriyi ve sınıf değişkenini belirleme
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
# Eğitim ve test kümelerine ayırma:
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=0)
# karar ağacını eğitme
dtree = tree.DecisionTreeClassifier(criterion=&#39;gini&#39;, max_depth=4, random_state=0)
from sklearn.ensemble import BaggingClassifier
bg = BaggingClassifier(dtree,max_samples=0.8,max_features=10,n_estimators=20,random_state=2)
bg.fit(X_train, y_train)
y_pred=bg.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
count_misclassified = (y_test != y_pred).sum()

print(&#39;Misclassified samples: {}&#39;.format(count_misclassified))
accuracy = metrics.accuracy_score(y_test, y_pred)
print(&#39;Accuracy: {:.2f}&#39;.format(accuracy))