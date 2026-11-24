import pandas as p
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer as ct
from sklearn.pipeline import Pipeline
model=DecisionTreeClassifier()
data=p.read_csv('titanic.csv')
Y=data[['Survived']]
X=data[['Sex','Embarked','Age','Pclass']]
"""encoder=OneHotEncoder()
encoded=encoder.fit_transform(data[['Sex','Embarked']])
encoded=p.DataFrame(encoded.toarray(),columns=encoder.get_feature_names_out())
X=p.concat([encoded,data[['Age','Pclass']]],axis=1)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42)
model.fit(X_train,Y_train)
user_test=['female','S',58,1]
user_encoded=encoder.transform([['female','S']])
user_encoded=p.DataFrame(user_encoded.toarray(),columns=encoder.get_feature_names_out())
user_int=p.DataFrame([[58,1]],columns=['Age','Pclass'])
U=p.concat([user_encoded,user_int],axis=1)
print(model.predict(U))
print(model.predict_proba(U))
print(model.tree_.feature)
print(model.tree_.threshold)
print(model.tree_.max_depth)
print(model.decision_path(U).toarray())
leaf = model.apply(U)[0]
print("Leaf:", leaf)
print("Leaf values:", model.tree_.value[leaf])
print(X.columns)
print(U.columns)
print(data[(data['Sex']=='female') & (data['Embarked']=='S') & (data['Age']==58) & (data['Pclass']==1)])"""

#Using pipeline &gridsearchcv in sklearn

preprocessor=ct([('strings',OneHotEncoder(),['Sex','Embarked'])],remainder='passthrough')
pipeline=Pipeline([('preprocessor',preprocessor),('model',DecisionTreeClassifier())])
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
print(X_train.shape)
print(Y_train.shape)
param_grid={
'model__max_depth':[3,5,8],
'model__min_samples_leaf':[2,3,4]
}
grid=GridSearchCV(estimator=pipeline,cv=5,param_grid=param_grid,scoring='accuracy')
grid.fit(X_train,Y_train)
test=p.DataFrame([['female','S',58,1]],columns=['Sex','Embarked','Age','Pclass'])
print(grid.predict(test))
print(accuracy_score(grid.predict(X_test),Y_test))


