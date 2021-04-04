import pandas
import numpy as np 
import pandas as pd 
from sklearn.decomposition import IncrementalPCA,PCA
def load_cnn_virus():


    dataframe = pandas.read_csv('0_300.csv')
    print("read finished!!!")
    array = dataframe.values
    
    import random
    random.shuffle(array) # random the dataset

    features = array[:,0:300]

    labels = array[:,300] 

    from sklearn.model_selection import train_test_split

    train_features,test_features, train_labels, test_labels = train_test_split(features,labels,  test_size = 0.2, random_state = 0)  


    train_labels = train_labels.reshape((train_labels.shape[0],1))
    test_labels = test_labels.reshape((test_labels.shape[0],1))

    
    print(train_features.shape)
    print(train_labels.shape)
    
    train = np.hstack((train_features,train_labels))
    train = pandas.DataFrame(train)
    
    test = np.hstack((test_features,test_labels))
    test = pandas.DataFrame(test)
    print("to CSV")
    train.to_csv("train"+"_"+str(300)+'_'+"0.8per"+".csv.gz"
     , header=False
     , index=False
     , chunksize=1000
     , compression='gzip'
     , encoding='utf-8')
    test.to_csv("test"+"_"+str(300)+'_'+"0.2per"+".csv.gz"
     , header=False
     , index=False
     , chunksize=1000
     , compression='gzip'
     , encoding='utf-8')