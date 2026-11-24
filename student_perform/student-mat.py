import pandas as p
from sklearn.tree import DecisionTreeRegressor,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as mp
from sklearn.preprocessing import OneHotEncoder
model=DecisionTreeRegressor()
data=p.read_csv("student-mat.csv",sep=';')
encoder=OneHotEncoder()
encoded=encoder.fit_transform(data[['school','sex']])
print(encoded)
print(encoder.get_feature_names_out())
encoded=p.DataFrame(encoded.toarray(),columns=encoder.get_feature_names_out())
X=p.concat([data[['studytime','age']],encoded.reset_index(drop=True)],axis=1)
Y=data[['G1','G2','G3']]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42)
model.fit(X_train,Y_train)
y_predict=model.predict(X_test)
print(mean_absolute_error(Y_test,y_predict))
plot_tree(model,feature_names=X_train.columns,filled=True,max_depth=3)
mp.show()