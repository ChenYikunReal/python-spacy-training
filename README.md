# SpaCy库尝试NLP

![](spacy.png)

安装命令（自动安最新的就行，不过不一定保证兼容性 ）
```shell script
pip install spacy
```

## 说明
1.原先的`2.0.11`版本是在不太行，所以升级到了`2.3.0`版本，但是Python兼容性做的不是很好，所以改了一些API，比如原先[词干提取](src/词干提取.ipynb)中的语句`from spacy.lang.en import LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES`就报错了。<br/>
查了一下原因，说是V2.2的时候改了这里，将大型查找表移出了主库。lemmatizer数据现在存储在单独的程序包中，spacy-lookups-data并Lemmatizer使用Lookups对象而不是各个变量进行初始化。<br/>
需要下载`spacy-lookups-data`库：`pip install spacy-lookups-data`

2.CMD输入如下命令可以安装英语语言包（必须给`管理员权限`）：
```shell script
python -m spacy download en
```

3.[词向量的使用](src/词向量的使用.ipynb)中有`nlp = spacy.load('en_core_web_lg')`语句，也是需要下载对应内容的（给`管理员权限`）：
```shell script
python -m spacy download en_core_web_lg
```
