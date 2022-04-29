from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
import FinanceDataReader as fdr
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import numpy as np

#데이터 가져오기 : train_test_split
#데이터셋 재생성 : cross_val_score, KFold, GridSearchCV
#알고리즘 : DecisionTreeClassifier, LogisticRegression, RandomForestClassifier

def tts(data, label, size, random):
    X_train, X_test, Y_train, Y_test = train_test_split(data, label, test_size=size, random_state=random)
    return X_train, X_test, Y_train, Y_test

class Data_module():
    
        
           
    def __init__(self, data, label, size, random):
        self.data = data
        self.label = label
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(data, label, test_size=size, random_state=random)
        self.clf_list = [DecisionTreeClassifier(random_state=random), RandomForestClassifier(random_state=random), LogisticRegression(max_iter=3000)]     
    #data는 label의 여집합, size는 0.x단위

    def cross_val_score(self, cvv):
        for i in self.clf_list:
            self.cvscore = cross_val_score(i, self.data, self.label, cv=cvv)
            for self.j, self.k in enumerate(self.cvscore):
                print(f"cross_val_score #{self.j+1}의 정확도 : {self.k:.4f}")
            print(f"cross_val_score {i}의 평균 정확도 : {np.mean(self.cvscore):.4f}\n")
        print("="*80+"\n")

    def KFold(self, folds):
        self.kfold = KFold(n_splits=folds)
        self.scores=[]
        for p in self.clf_list:
            self.clf = p
            for i, (j, k) in enumerate(self.kfold.split(self.data)):
                self.X_train, self.X_test = self.data.values[j], self.data.values[k]
                self.Y_train, self.Y_test = self.label.values[j], self.label.values[k]
                self.clf.fit(self.X_train, self.Y_train)
                self.predictions = self.clf.predict(self.X_test)
                self.accuracy = accuracy_score(self.Y_test, self.predictions)
                self.scores.append(self.accuracy)
                print(f'KFold 교차 검증 #{i+1}의 정확도 : {self.accuracy:.4f}')
            self.mean_score = np.mean(self.scores)
            print(f'KFold 교차 검증 {p}의 평균 정확도 : {self.mean_score:.4f}\n')
        print("="*80+"\n")

    def GridSearchCV(self, cvv):
        for p in self.clf_list[0:2]:
            self.clf = p
            self.parameters = {'max_depth':[2,3,5,10], 'min_samples_split':[2,3,5], 'min_samples_leaf':[1,5,8]}
            self.grid_dclf = GridSearchCV(self.clf, param_grid=self.parameters, scoring='accuracy', cv=cvv)
            self.grid_dclf.fit(self.X_train, self.Y_train)
            print(f'GridSearchCV 최적 하이퍼 파라미터 : {self.grid_dclf.best_params_}')
            print(f'GridSearchCV 최고 정확도 : {self.grid_dclf.best_score_:.4f}')
            self.best_dclf = self.grid_dclf.best_estimator_
            self.dpredictions = self.best_dclf.predict(self.X_test)
            self.accuracy = accuracy_score(self.Y_test, self.dpredictions)
            print(f'GridSearchCV 최적하이퍼 파라미터의 {p} 정확도 : {self.accuracy:.4f}\n')
        print("="*80+"\n")

class Clf_module():            
    def __init__(self, data, label, size, random):
        self.data = data
        self.label = label
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(data, label, test_size=size, random_state=random)
        self.clf_list = [DecisionTreeClassifier(random_state=random), RandomForestClassifier(random_state=random), LogisticRegression(max_iter=3000)]    
        for i in self.clf_list:    
            self.clf = i
            self.clf.fit(self.X_train, self.Y_train)
            self.dt_pred = self.clf.predict(self.X_test)
            print(f'{i} 정확도 : {accuracy_score(self.Y_test,self.dt_pred):.4f}\n')
        print("="*80+"\n")