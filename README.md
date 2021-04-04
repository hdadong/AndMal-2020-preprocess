# AndMal-2020-preprocess
<br>数据集来自https://www.unb.ca/cic/datasets/andmal2020.html
<br>本文件夹下0~9.csv是执行jupyter notebook 划分出来的10份CSV 9503维度的特征+1维度的标签
<br>第14到第18个CSV都是良性的


# 2021.3.30更新
<br>新增了prepoces.py
<br>使用PCA对特征进行了降维，生成了300维的特征，sklearn神经网络准确率达到89


# 2021.4.5更新
<br>新增了split_train_test.py
<br>读取40W，300维的数据，然后随机打乱后，分成训练集和测试集的CSV


# 参考文献
<br> 分批训练PCA，虽然没用到
https://stackoverflow.com/questions/32191219/python-pca-on-matrix-too-large-to-fit-into-memory
