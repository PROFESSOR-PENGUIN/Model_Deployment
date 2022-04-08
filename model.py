import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from flaml import AutoML
import pickle


SAVED_MODEL='automl_model.pkl'

data=load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

automl_settings = {
    "time_budget": 60,  # in seconds
    "metric": 'accuracy',
    "task": 'classification',
    "estimator_list": ['lgbm'],
    "log_file_name": "logfile.log",
}
automl=AutoML()
automl.fit(X_train=X_train, y_train=y_train,
           **automl_settings)

# Print the best model
print(automl.model.estimator)

with open(SAVED_MODEL,'wb') as f:
    pickle.dump(automl,f,pickle.HIGHEST_PROTOCOL)

# with open('automl_model.pkl', 'rb') as f:
#     automl = pickle.load(f)
# y_pred_proba = automl.predict_proba(X_test)[:,1]
# print(y_pred_proba)

