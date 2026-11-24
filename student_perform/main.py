import pandas as p
import matplotlib.pyplot as mp
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,confusion_matrix
model=DecisionTreeClassifier(max_depth=10)
data=p.read_csv("data.csv")
X=data[['study_hours','attendance','previous_score']]
Y=data['passed']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42)
model.fit(X_train,Y_train)
plot_tree(model,feature_names=X.columns,class_names=["Fail","Pass"],filled= True)
mp.show()
""" new_student=[[5,82,65]]
predictions=model.predict(new_student)
print(predictions) """
predictions=model.predict(X_test)
train=model.predict(X_train)
cm=confusion_matrix(Y_test,predictions)
print(cm)
print(model.tree_.threshold)
print(model.tree_.feature)  
print(accuracy_score(Y_test,predictions))
print(accuracy_score(Y_train,train))  