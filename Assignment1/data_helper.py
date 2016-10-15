from sklearn.preprocessing import Imputer, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from plot_helper import *

class data_helper:
    def __init__(self):
        pass
    
    def search_wine_data(self):
        
        '''
        1 - fixed acidity
        2 - volatile acidity
        3 - citric acid
        4 - residual sugar
        5 - chlorides
        6 - free sulfur dioxide
        7 - total sulfur dioxide
        8 - density
        9 - pH
        10 - sulphates
        11 - alcohol
        Output variable (based on sensory data):
        12 - quality (score between 0 and 10)
        '''
        
        # load the red wine data
        # source: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
        df = pd.read_csv('./data/winequality-red.csv', sep=';')
        
        '''   
        CORR
                               quality  
        fixed acidity        0.124052  
        volatile acidity     -0.390558  
        citric acid          0.226373  
        residual sugar       0.013732  
        chlorides            -0.128907  
        free sulfur dioxide  -0.050656  
        total sulfur dioxide -0.185100  
        density              -0.174919  
        pH                    -0.057731  
        sulphates             0.251397  
        alcohol               0.476166  
        quality               1.000000  
        '''
        
        df['quality_3'] = pd.qcut(df['quality'], 3, labels=[0,1,2]).values.astype(np.int64)
        
        split = 5 #df['quality'].median()
        df['quality_2'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] <= split), 'quality_2'] = 0
        df.loc[(df['quality'] > split), 'quality_2'] = 1
        
        df['quality_4'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] <= 4), 'quality_4'] = 1
        df.loc[(df['quality'] > 4), 'quality_4'] = 0
        
    def load_wine_data_full_set(self):
        df = pd.read_csv('./data/winequality-red.csv', sep=';')
        
        x_col_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                       'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'] 
        
        x, y = df.loc[:,x_col_names].values, df.loc[:,'quality'].values
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        
        return X_train, X_test, y_train, y_test
    
    
    def load_wine_data_knn(self):
        df = pd.read_csv('./data/winequality-red.csv', sep=';')
        
        split = df['quality'].median()
        df['quality_2'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] < split), 'quality_2'] = 0
        df.loc[(df['quality'] >= split), 'quality_2'] = 1
        
        df['volatile_acidity_ph_ratio'] = df['volatile acidity'] / df['pH'] 
        df['fixed_acidity_ph_ratio'] = df['fixed acidity'] / df['pH'] 
        df['sulphates_residual_sugar_ratio'] = df['sulphates'] / df['residual sugar'] 
        df['alcohol_residual_sugar_ratio'] = df['alcohol'] / df['residual sugar'] 
        df['volatile_acidity_ph_ratio'] = df['volatile acidity'] / df['pH'] 


        #x_col_names = ['volatile acidity', 'alcohol', 'volatile_acidity_ph_ratio'] 
        x_col_names = ['alcohol', 'volatile acidity', 'sulphates', 'pH'] 
        
        x, y = df.loc[:,x_col_names].values, df.loc[:,'quality_2'].values
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        
        return X_train, X_test, y_train, y_test
    

    def load_wine_data(self):
        df = pd.read_csv('./data/winequality-red.csv', sep=';')
        
        split = df['quality'].median()
        df['quality_2'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] < split), 'quality_2'] = 0
        df.loc[(df['quality'] >= split), 'quality_2'] = 1
        
        df['volatile_acidity_ph_ratio'] = df['volatile acidity'] / df['pH'] 
        df['fixed_acidity_ph_ratio'] = df['fixed acidity'] / df['pH'] 
        df['sulphates_residual_sugar_ratio'] = df['sulphates'] / df['residual sugar'] 
        df['alcohol_residual_sugar_ratio'] = df['alcohol'] / df['residual sugar'] 
        df['volatile_acidity_ph_ratio'] = df['volatile acidity'] / df['pH'] 


        #x_col_names = ['volatile acidity', 'alcohol', 'volatile_acidity_ph_ratio'] 
        x_col_names = ['volatile acidity', 'alcohol', 'pH'] 
        
        x, y = df.loc[:,x_col_names].values, df.loc[:,'quality_2'].values
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        
        return X_train, X_test, y_train, y_test
    
    def load_wine_data_orig2(self):
        
        '''
        1 - fixed acidity
        2 - volatile acidity
        3 - citric acid
        4 - residual sugar
        5 - chlorides
        6 - free sulfur dioxide
        7 - total sulfur dioxide
        8 - density
        9 - pH
        10 - sulphates
        11 - alcohol
        Output variable (based on sensory data):
        12 - quality (score between 0 and 10)
        '''
        
        # load the red wine data
        # source: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
        df = pd.read_csv('./data/winequality-red.csv', sep=';')
        
        '''   
        CORR
                               quality  
        fixed acidity        0.124052  
        volatile acidity     -0.390558  
        citric acid          0.226373  
        residual sugar       0.013732  
        chlorides            -0.128907  
        free sulfur dioxide  -0.050656  
        total sulfur dioxide -0.185100  
        density              -0.174919  
        pH                    -0.057731  
        sulphates             0.251397  
        alcohol               0.476166  
        quality               1.000000  
        '''
        
        df['quality_3'] = pd.qcut(df['quality'], 3, labels=[0,1,2]).values.astype(np.int64)
        
        split = 5 #df['quality'].median()
        df['quality_2'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] <= split), 'quality_2'] = 0
        df.loc[(df['quality'] > split), 'quality_2'] = 1
        
        df['quality_4'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] <= 4), 'quality_4'] = 1
        df.loc[(df['quality'] > 4), 'quality_4'] = 0
        
        
        df['alcohol_std'] = df['alcohol'].std()
        df['alcohol_norm'] = df['alcohol'] / df['alcohol_std']
        df['alcohol_norm_med'] = df['alcohol_norm'].median()
        df['alcohol_norm_abs_med'] = df['alcohol_norm_med'].abs()
        df['alcohol_factor'] = df['alcohol_norm'] / df['alcohol_norm_abs_med']
        #df['alcohol_factor_quant'] = pd.qcut(df['alcohol_factor'], 10, labels=[0,1,2,3,4,5,6,7,8,9]).values.astype(np.int64)
        df['alcohol_factor_quant'] = pd.qcut(df['alcohol_factor'], 2, labels=[0,1]).values.astype(np.int64)
        
        df['alcohol_factor_quant'].corr(df['quality_3'])
        #0.50415520619906773
        
        
        df['sulphates_std'] = df['sulphates'].std()
        df['sulphates_norm'] = df['sulphates'] / df['sulphates_std']
        df['sulphates_norm_med'] = df['sulphates_norm'].median()
        df['sulphates_norm_abs_med'] = df['sulphates_norm_med'].abs()
        df['sulphates_factor'] = df['sulphates_norm'] / df['sulphates_norm_abs_med']
        #df['sulphates_factor_quant'] = pd.qcut(df['sulphates_factor'], 10, labels=[0,1,2,3,4,5,6,7,8,9]).values.astype(np.int64)
        df['sulphates_factor_quant'] = pd.qcut(df['sulphates_factor'], 2, labels=[0,1]).values.astype(np.int64)
        
        df['sulphates_factor_quant'].corr(df['quality_3'])
        #0.50415520619906773
        
                
        df['volatile_acidity_std'] = df['volatile acidity'].std()
        df['volatile_acidity_norm'] = df['volatile acidity'] / df['volatile_acidity_std']
        df['volatile_acidity_norm_med'] = df['volatile_acidity_norm'].median()
        df['volatile_acidity_norm_abs_med'] = df['volatile_acidity_norm_med'].abs()
        df['volatile_acidity_factor'] = df['volatile_acidity_norm'] / df['volatile_acidity_norm_abs_med']
        #df['volatile_acidity_factor_quant'] = pd.qcut(df['volatile_acidity_factor'], 10, labels=[0,1,2,3,4,5,6,7,8,9]).values.astype(np.int64)
        df['volatile_acidity_factor_quant'] = pd.qcut(df['volatile_acidity_factor'], 2, labels=[0,1]).values.astype(np.int64)
        
        df['volatile_acidity_factor_quant'].corr(df['quality_3'])
        #-0.35545462139356093
        
        df['citric_acid_ph_ratio'] = df['citric acid'] / df['pH'] 
        df['citric_acid_ph_ratio_std'] = df['citric_acid_ph_ratio'].std()
        df['citric_acid_ph_ratio_norm'] = df['citric_acid_ph_ratio'] / df['citric_acid_ph_ratio_std']
        df['citric_acid_ph_ratio_norm_med'] = df['citric_acid_ph_ratio_norm'].median()
        df['citric_acid_ph_ratio_norm_abs_med'] = df['citric_acid_ph_ratio_norm_med'].abs()
        df['citric_acid_ph_ratio_factor'] = df['citric_acid_ph_ratio_norm'] / df['citric_acid_ph_ratio_norm_abs_med']
        df['citric_acid_ph_ratio_factor_quant'] = pd.qcut(df['citric_acid_ph_ratio_factor'], 10, labels=[0,1,2,3,4,5,6,7,8,9]).values.astype(np.int64)

        df['citric_acid_ph_ratio_factor_quant'].corr(df['quality_3'])
        #0.20929496088306607
        
        df['total_sulfur_dioxide_std'] = df['total sulfur dioxide'].std()
        df['total_sulfur_dioxide_norm'] = df['total sulfur dioxide'] / df['total_sulfur_dioxide_std']
        df['total_sulfur_dioxide_norm_med'] = df['total_sulfur_dioxide_norm'].median()
        df['total_sulfur_dioxide_norm_abs_med'] = df['total_sulfur_dioxide_norm_med'].abs()
        df['total_sulfur_dioxide_factor'] = df['total_sulfur_dioxide_norm'] / df['total_sulfur_dioxide_norm_abs_med']
        #df['total_sulfur_dioxide_factor_quant'] = pd.qcut(df['total_sulfur_dioxide_factor'], 10, labels=[0,1,2,3,4,5,6,7,8,9]).values.astype(np.int64)
        df['total_sulfur_dioxide_factor_quant'] = pd.qcut(df['total_sulfur_dioxide_factor'], 2, labels=[0,1]).values.astype(np.int64)
        
        df['total_sulfur_dioxide_factor_quant'].corr(df['quality_3'])
        #-0.22585898166340387

        df['citric_acid_std'] = df['citric acid'].std()
        df['citric_acid_norm'] = df['citric acid'] / df['citric_acid_std']
        df['citric_acid_norm_med'] = df['citric_acid_norm'].median()
        df['citric_acid_norm_abs_med'] = df['citric_acid_norm_med'].abs()
        df['citric_acid_factor'] = df['citric_acid_norm'] / df['citric_acid_norm_abs_med']
        #df['citric_acid_factor_quant'] = pd.qcut(df['citric_acid_factor'], 10, labels=[0,1,2,3,4,5,6,7,8,9]).values.astype(np.int64)
        df['citric_acid_factor_quant'] = pd.qcut(df['citric_acid_factor'], 2, labels=[0,1]).values.astype(np.int64)
        
        
        df['citric_acid_factor_quant'].corr(df['quality_3'])
        #df['citric_acid_factor_quant'].corr(df['quality_3'])
        
        
        '''
        
        df['phSugarRatio'] = df['pH'] / df['residual sugar']
        df['phCitricAcidRatio'] = df['pH'] / df['citric acid']
        df['phVolatileAcidRatio'] = df['pH'] / df['volatile acidity']
        df['phFixedAcidRatio'] = df['pH'] / df['fixed acidity']
        
        df['quality3'] = pd.qcut(df['quality'], 3, labels=['poor', 'average', 'best'])
        
        df['fixed_acidity_quantiles'] = pd.qcut(df['fixed acidity'], 3, labels=['poor', 'average', 'best'])
        
        
        df['quality_cut'] = pd.qcut(df['quality'], 3, labels=[0, 1, 2])
        
        
        df = pd.get_dummies(df[['Sex', 'Pclass', 'Age', 'Survived', 'Fare', 'SibSp', 'Parch']])    
    
        #df['phSugarRatioScore'] = df['phSugarRatio'] / df['phSugarRatio'].std() 
        #med = df['phSugarRatioScore'].median()
        #abs_med = abs(med)
        #df['phSugarRatioStd'] = df['phSugarRatioScore'] / abs_med
        
        #df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
        #df.plot.scatter(x='quality', y='phSugarRatioStd')
        
        mean = df['quality'].mean()
        
        df['quality2'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] <= mean), 'quality2'] = 0
        df.loc[(df['quality'] > mean), 'quality2'] = 1
        '''
        
        
        # separate the x and y data
        # y = quality, x = features (using fixed acid, volatile acid and alcohol)
        #x_col_names = ['fixed acidity', 'volatile acidity', 'alcohol', 'total sulfur dioxide', 'sulphates', 'citric acid', 'phVolatileAcidRatio']
        '''
        x_col_names = ['citric_acid_factor_quant',
                       'alcohol_factor_quant',
                       'volatile_acidity_factor_quant',
                       'citric_acid_ph_ratio_factor_quant',
                       'total_sulfur_dioxide_factor_quant']
        '''
        x_col_names = ['citric_acid_factor',
                       'alcohol_factor',
                       'volatile_acidity_factor',
                       #'citric_acid_ph_ratio_factor',
                       'total_sulfur_dioxide_factor',
                       'sulphates_factor']
        
        x_col_names = ['citric_acid_factor_quant',
                       'alcohol_factor_quant',
                       'volatile_acidity_factor_quant',
                       #'citric_acid_ph_ratio_factor',
                       'total_sulfur_dioxide_factor_quant',
                       'sulphates_factor_quant']
        
        #x_col_names = ['alcohol_factor',
        #               'volatile_acidity_factor',
        #               'total_sulfur_dioxide_factor']
        
        #x_col_names = ['fixed acidity', 'volatile acidity', 'alcohol']
        
        
        
        
        '''   
        CORR
                               quality  
        fixed acidity        0.124052  
        volatile acidity     -0.390558  
        citric acid          0.226373  
        residual sugar       0.013732  
        chlorides            -0.128907  
        free sulfur dioxide  -0.050656  
        total sulfur dioxide -0.185100  
        density              -0.174919  
        pH                    -0.057731  
        sulphates             0.251397  
        alcohol               0.476166  
        quality               1.000000  
        '''
        df['volatile_acidity_ph_ratio'] = df['volatile acidity'] / df['pH'] 
        df['fixed_acidity_ph_ratio'] = df['fixed acidity'] / df['pH'] 
        df['sulphates_residual_sugar_ratio'] = df['sulphates'] / df['residual sugar'] 
        df['alcohol_residual_sugar_ratio'] = df['alcohol'] / df['residual sugar'] 
        
        ph = plot_helper()
        #ph.plot_scatter(df['quality'], df['alcohol'])
        
        #ph.plot_scatter(df['quality'], df['alcohol_factor'])
        #ph.plot_scatter(df['quality_3'], df['pH'])
        #ph.plot_scatter(df['quality_3'], df['volatile_acidity_ph_ratio'])
        #ph.plot_scatter(df['quality_3'], df['fixed_acidity_ph_ratio'])
        #ph.plot_scatter(df['quality_3'], df['sulphates_residual_sugar_ratio'])
        #ph.plot_scatter(df['quality_3'], df['alcohol_residual_sugar_ratio'])
        
        df['volatile_acidity_ph_ratio'] = df['volatile acidity'] / df['pH'] 
        
        
        
        x_col_names = ['citric acid', 'volatile acidity', 'alcohol', 'total sulfur dioxide', 'sulphates', 'volatile_acidity_ph_ratio']
        x_col_names = ['alcohol', 'volatile_acidity_ph_ratio', 'alcohol_residual_sugar_ratio', 'fixed_acidity_ph_ratio']
        #x_col_names = ['citric acid', 'volatile acidity', 'alcohol', 'total sulfur dioxide', 'sulphates']
        #x_col_names = ['volatile_acidity_ph_ratio', 'alcohol_residual_sugar_ratio', 'fixed_acidity_ph_ratio']
        #x_col_names = ['alcohol', 'volatile acidity', 'sulphates']
        #x_col_names = ['alcohol', 'volatile acidity']
        
        x_col_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                       'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'] 
        
        x, y = df.loc[:,x_col_names].values, df.loc[:,'quality'].values
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        
        return X_train, X_test, y_train, y_test
    
    def load_titanic_data_orig(self):
        
        df = pd.read_csv('./data/titanic_train.csv', sep=',')
        
        # we need to encode sex. using the sklearn label encoder is
        # one way. however one consideration is that the learning
        # algorithm may make assumptions about the magnitude of the
        # labels. for example, male is greater than female. use
        # one hot encoder to get around this.
        #ohe = OneHotEncoder(categorical_features=[0])
        #ohe.fit_transform(x).toarray()
        
        # Even better pandas has a one hot encoding built in!
        df = pd.get_dummies(df[['Sex', 'Pclass', 'Age', 'Survived', 'Fare', 'SibSp', 'Parch']])    
        
        # this data set is missing some ages. we could impute a value
        # like the average or median. or remove the rows having missing
        # data. the disadvantage of removing values is we may be taking
        # away valuable information that the learning algorithm needs.
        imr = Imputer(strategy='most_frequent')
        imr.fit(df['Age'].reshape(-1, 1))
        imputed_data = imr.transform(df['Age'].reshape(-1, 1))
        
        df['Age']  = imputed_data
        
        
        #y = df['Survived'].values
        #x = df.iloc[:,[0,1,3,4]].values
        
        #x_col_names = df.iloc[:,[0,1,3,4]].columns
        x_col_names = ['Pclass', 'Age', 'Fare', 'SibSp', 'Parch', 'Sex_female', 'Sex_male']
        x, y = df.loc[:,x_col_names].values, df.loc[:,'Survived'].values
        
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        
        return X_train, X_test, y_train, y_test
        
    def load_wine_data_orig(self, scale=False):
        
        '''
        1 - fixed acidity
        2 - volatile acidity
        3 - citric acid
        4 - residual sugar
        5 - chlorides
        6 - free sulfur dioxide
        7 - total sulfur dioxide
        8 - density
        9 - pH
        10 - sulphates
        11 - alcohol
        Output variable (based on sensory data):
        12 - quality (score between 0 and 10)
        '''
        
        # load the red wine data
        # source: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
        df = pd.read_csv('./data/winequality-red.csv', sep=';')
        
        df['phSugarRatio'] = df['pH'] / df['residual sugar']
        df['phCitricAcidRatio'] = df['pH'] / df['citric acid']
        df['phVolatileAcidRatio'] = df['pH'] / df['volatile acidity']
        df['phFixedAcidRatio'] = df['pH'] / df['fixed acidity']
        
        df['quality3'] = pd.qcut(df['quality'], 3, labels=['poor', 'average', 'best'])
        
        #df = pd.get_dummies(df[['Sex', 'Pclass', 'Age', 'Survived', 'Fare', 'SibSp', 'Parch']])    
    
        #df['phSugarRatioScore'] = df['phSugarRatio'] / df['phSugarRatio'].std() 
        #med = df['phSugarRatioScore'].median()
        #abs_med = abs(med)
        #df['phSugarRatioStd'] = df['phSugarRatioScore'] / abs_med
        
        #df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
        #df.plot.scatter(x='quality', y='phSugarRatioStd')
        
        mean = df['quality'].mean()
        
        df['quality2'] = df['quality']
        
        # group the quality into binary good or bad
        df.loc[(df['quality'] >= 0) & (df['quality'] <= mean), 'quality2'] = 0
        df.loc[(df['quality'] > mean), 'quality2'] = 1
        
        
        
        # separate the x and y data
        # y = quality, x = features (using fixed acid, volatile acid and alcohol)
        #x_col_names = ['fixed acidity', 'volatile acidity', 'alcohol', 'total sulfur dioxide', 'sulphates', 'citric acid', 'phVolatileAcidRatio']
        #x_col_names = ['fixed acidity', 'volatile acidity', 'alcohol', 'phVolatileAcidRatio']
        x_col_names = ['fixed acidity', 'alcohol']
        
        x, y = df.loc[:,x_col_names].values, df.loc[:,'quality'].values
        if scale:
            x = StandardScaler().fit_transform(x)
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
        
        return X_train, X_test, y_train, y_test
    
    
    def load_titanic_data_full_set(self):
        
        df = pd.read_csv('./data/titanic_train.csv', sep=',')
        
        # we need to encode sex. using the sklearn label encoder is
        # one way. however one consideration is that the learning
        # algorithm may make assumptions about the magnitude of the
        # labels. for example, male is greater than female. use
        # one hot encoder to get around this.
        #ohe = OneHotEncoder(categorical_features=[0])
        #ohe.fit_transform(x).toarray()
        
        '''
        PassengerId                          1
        Survived                             0
        Pclass                               3
        Name           Braund, Mr. Owen Harris
        Sex                               male
        Age                                 22
        SibSp                                1
        Parch                                0
        Ticket                       A/5 21171
        Fare                              7.25
        Cabin                              NaN
        Embarked                             S
        '''
                
        # Even better pandas has a one hot encoding built in!
        dfx = pd.get_dummies(df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']])    
        
        imr = Imputer(strategy='most_frequent')
        imr.fit(dfx)
        x = imr.transform(dfx)
        y = df.loc[:,'Survived'].values
                
        # this data set is missing some ages. we could impute a value
        # like the average or median. or remove the rows having missing
        # data. the disadvantage of removing values is we may be taking
        # away valuable information that the learning algorithm needs.
        #imr = Imputer(strategy='most_frequent')
        #imr.fit(df['Age'].reshape(-1, 1))
        #imputed_data = imr.transform(df['Age'].reshape(-1, 1))
        #df['Age']  = imputed_data
        
        #y = df['Survived'].values
        #x = df.iloc[:,[0,1,3,4]].values
        
        #x_col_names = df.iloc[:,[0,1,3,4]].columns
        #x_col_names = ['Pclass', 'Age', 'Fare', 'SibSp', 'Parch', 'Sex_female', 'Sex_male']
        #x, y = df.loc[:,x_col_names].values, df.loc[:,'Survived'].values
        
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        
        # export
        '''
        y.shape = (y.shape[0], 1)
        x = StandardScaler().fit_transform(x)
        xy = np.hstack((x, y))
        np.savetxt('titanic.txt', xy, delimiter=',')
        
        y_test.shape = (y_test.shape[0], 1)
        X_test = StandardScaler().fit_transform(X_test)
        xy_test = np.hstack((X_test, y_test))
        np.savetxt('titanic_test.txt', xy_test, delimiter=',')
        
        y_train.shape = (y_train.shape[0], 1)
        X_train = StandardScaler().fit_transform(X_train)
        xy_train = np.hstack((X_train, y_train))
        np.savetxt('titanic_train.txt', xy_train, delimiter=',')
        '''
        return X_train, X_test, y_train, y_test
        
    def load_titanic_data(self):
        
        df = pd.read_csv('./data/titanic_train.csv', sep=',')
        
        '''
        PassengerId                          1
        Survived                             0
        Pclass                               3
        Name           Braund, Mr. Owen Harris
        Sex                               male
        Age                                 22
        SibSp                                1
        Parch                                0
        Ticket                       A/5 21171
        Fare                              7.25
        Cabin                              NaN
        Embarked                             S
        '''
                
        # Even better pandas has a one hot encoding built in!
        dfx = pd.get_dummies(df[['Pclass', 'Sex', 'Age', 'Fare', 'Cabin']])    
        
        imr = Imputer(strategy='most_frequent')
        imr.fit(dfx)
        x = imr.transform(dfx)
        y = df.loc[:,'Survived'].values
    
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        
        return X_train, X_test, y_train, y_test
    
    def load_nba_data(self):
        df = pd.read_csv('./data/shot_logs.csv', sep=',')
        
        le = LabelEncoder()
        le.fit(df['LOCATION'])
        le.transform(df['LOCATION']) 
        df['LOCATION_ENC'] = le.transform(df['LOCATION'])
            
        le = LabelEncoder()
        le.fit(df['SHOT_RESULT'])
        le.transform(df['SHOT_RESULT']) 
        df['SHOT_RESULT_ENC'] = le.transform(df['SHOT_RESULT'])
            
        x_col_names = ['SHOT_DIST', 'TOUCH_TIME', 'LOCATION_ENC', 'PTS_TYPE', 'DRIBBLES', 'FINAL_MARGIN']
        x_col_names = ['SHOT_DIST', 'CLOSE_DEF_DIST', 'DRIBBLES']
        x, y = df.loc[:,x_col_names].values, df.loc[:,'SHOT_RESULT_ENC'].values
        
        
        
        
        # split the data into training and test data
        # for the wine data using 30% of the data for testing
        X_train, X_test, y_train, y_test = train_test_split(x,
                                                            y,
                                                            test_size=0.25,
                                                            random_state=0)

        return X_train, X_test, y_train, y_test
    