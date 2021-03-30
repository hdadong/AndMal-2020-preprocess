import numpy as np 
import pandas as pd 
from sklearn.decomposition import IncrementalPCA,PCA

blocksize = 10 #把每个CSV分成10份融合成一个CSV
cols = list(range(1,9504))#不要第一列的MD5
feature_size = 300
pdchunk=[]
data = ["Adware",
           "Backdoor",
           "FileInfector",
           "NoCategory",
           "PUA",
           "Ransomware",
        "Riskware",
           "Scareware",
        "Trojan",
        "Banker",
           "Dropper",
           "SMS",
           "Spy",
           "Zeroday",
            "Ben0",
        "Ben1",
        "Ben2",
        "Ben3",
        "Ben4"   
       ]
size = [47210,
        1538,
        669,
        2296,
        2051,
        6202,
        97349,
        1556,
        13559,
        887,
        2302,
        3125,
        3540,
        13340,
        32083,#Ben0
        47859,#Ben1
        42633,#Ben2
        7845,#Ben3
        31752 #Ben4
       ]

d=[]
sklearn_pca = PCA(n_components=feature_size)

for i in range(0,len(data)):#获取每个CSV的分块对象
    chunk_size = int(size[i]/blocksize)
    dataset = pd.read_csv(data[i]+".csv",dtype=float,skiprows=1, chunksize=chunk_size, iterator=True ,usecols=cols)
    #dataset = list(dataset)
    d.append(dataset)
    #print(i)
print("finish first read CSVs and Strat training PCA")
for i in range(0,1):#一共建立blocksizeCSV来训练PCA
    t = None
    labels=[]
    
    for p in range(0,len(data)):
        #print(p)
        chunk_size = int(size[p]/blocksize)
        
        c = np.array(d[p].get_chunk(chunk_size).dropna(axis=0, how='any'))

        if p == 0:
            t = c
        else:
            t = np.vstack((t,c))

    sklearn_pca.fit(t)
print("PCA train finished !，n_components_：",sklearn_pca.n_components_ )

d = None
d = [] #erase
print("erased and reopen the CSVs!")
for i in range(0,len(data)):#获取每个CSV的分块对象
    chunk_size = int(size[i]/blocksize)
    dataset = pd.read_csv(data[i]+".csv",dtype=float,skiprows=1, chunksize=chunk_size, iterator=True ,usecols=cols)
    #dataset = list(dataset)
    d.append(dataset)
    #print(i)
print("start pca and split the CSVs ")

for i in range(0,blocksize):#一共建立blocksizeCSV
    '''
    t= None
    labels = None
    '''
    t = []
    labels = []

    for p in range(0,len(data)):
        chunk_size = int(size[p]/blocksize)
        c = np.array(d[p].get_chunk(chunk_size).dropna(axis=0, how='any'))

        c = sklearn_pca.transform(c)
        #print(c.shape)
        label = np.ones((c.shape[0],1))
        if p < 14:
            label = label*p
        else:# p=12~16都是良性的数据，标签一样
            label = label*14
        '''
        if p == 0:
            t = c
            labels = label
        else:
            t = np.vstack((t,c))
            labels = np.vstack((labels,label))
        '''
        data_label = np.hstack((c,label))
        data_label = pd.DataFrame(data_label)
        t.append(data_label)
    '''
    t = sklearn_pca.transform(t)
    print(t.shape)
    t_labels = np.hstack((t,labels))
    df = pd.DataFrame(t_labels)
    '''
    df = pd.concat(t, ignore_index=True)
    #df.to_csv(str(i)+".csv",index=False,header=False,chunksize=1000)

    df.to_csv(str(i)+"_"+str(feature_size)+".csv.gz"
         , header=False
         , index=False
         , chunksize=1000
         , compression='gzip'
         , encoding='utf-8')
    print(str(i)+"_"+str(feature_size)+".csv.gz finished!")
