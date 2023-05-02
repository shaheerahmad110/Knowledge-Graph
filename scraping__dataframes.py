# -*- coding: utf-8 -*-
"""Scraping _dataframes.ipynb
"""

import pandas as pd

from selenium import webdriver

driver=webdriver.Chrome('chromedriver')

driver.get('https://pandas.pydata.org/docs/reference/frame.html')

from selenium.webdriver.common.by import By

elements=driver.find_elements(By.CSS_SELECTOR,'h2')

elements[0].text

title_list=[]
for i in elements:
    title_list.append(i.text)

title_list

def data_by_id(id,index):
    x=driver.find_elements(By.ID,id)
    att_and_data=x[0].text.split('\n')
    func_names=[]
    desc=[]
    endat=len(att_and_data)
    if len(att_and_data)%2!=1 and id!='attributes-and-underlying-data':
        endat=len(att_and_data)-1
    startfrom=1
    if id=='attributes-and-underlying-data':
        startfrom=2
        for i in range(startfrom,endat):
            if i%2==0:
                func_names.append(att_and_data[i])
            else:
                desc.append(att_and_data[i])
    else:
        for i in range(1,endat):
            if i%2==1:
                func_names.append(att_and_data[i])
            else:
                desc.append(att_and_data[i])
    df_dict={'Syntax':func_names,'Description:':desc}
    print(len(func_names),len(desc))
    try:
        print(desc[21])
    except:
        pass
    df=pd.DataFrame(df_dict)
    df.insert(0,column='DataFrame has',value=title_list[index])
    return df

id_list=[]
count=0
df=None
for i in title_list:
    #String formatting
    j=i.lower()
    #j=j.replace('/','')
    j=j.replace(',','')
    #j=j.replace('&','\b')
    j=j.split(' ')
    if '&' in j:
        j.remove('&')
    if '/' in j:
        for z in range(j.count('/')):
            j.remove('/')
    
    print(j)

    if(len(j)>1):
        j='-'.join(j)
    else:
        j=str(j[0])
    print(j)
    if count==0:
        df=data_by_id(j,count)
    else:
        comingdf=data_by_id(j,count)
        df=pd.concat([df,comingdf],axis=0)
        #df=df.append(comingdf,ignore_index=False)
    count=count+1
    pass

df

df.to_csv('dataframes.csv')

"""________________________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________________________
"""