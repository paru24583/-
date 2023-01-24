#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import random
MEMBER = 22
bun = [3,4,10,14]
member = list(range(1,MEMBER+1))
ri = list(set(member)-set(bun))

#シャッフル
seed = input("seed値を入力してね:")

if seed == "":
    print("seed値は入力されませんでした")
else:
    random.seed(seed)

random.shuffle(ri)
random.shuffle(bun)
member = ri +bun

blank = [22,23,24]
for a in blank:
    member.insert(a,"")

#5列に分割する関数
ROW = 5
def split(lst):  
    for i in range(0, len(lst), ROW): 
        yield lst[i:i + 5]

#行と列の数が邪魔なので調整
BLANK = ["","","","",""]
pd.DataFrame(split(member),BLANK,BLANK)

