from pandas_profiling import ProfileReport
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data_df = pd.read_csv('/content/needit_family.csv',header = 0,sep=',')

'''
data_df = data_df[['ASGS_2016','Houses - median sale price ($)','Houses - number of transfers (no.)',
                       'Total number of businesses', 'Total number of business entries',
                  'Total number of business exits']]


data_df = data_df.drop(['DWELL_3','DWELL_4','FAMILY_9',
                        'HHTYPE_6','HOUSE_2','HOUSE_3',
                        'HOUSE_4'], axis=1)

#data_df = data_df.drop(['INCOME_18','INCOME_2.1','INCOME_36'], axis=1)
data_df = data_df[['Houses - median sale price ($)','INCOME_17','INCOME_11',
                  'INCOME_2','INCOME_8','INCOME_5']]

#1.Median total income (excl. Government pensions and allowances) ($) INCOME_17
#2.Median superannuation and annuity income ($)  INCOME_11
#3.Median employee income ($) INCOME_2
#4.Median investment income ($)  INCOME_8
#5.Median own unincorporated business income ($)  INCOME_5


list = ['Houses - median sale price ($)','INCOME_17','INCOME_11',
                  'INCOME_2','INCOME_8','INCOME_5']


'''

#data_df['Houses - median sale price ($)'] = data_df['Houses - median sale price ($)'].astype(float)

data_df = data_df.replace('-', np.nan, regex=True)
data_df = data_df.dropna(thresh=9)

list1 = ['ASGS_2016','Year','Houses - median sale price ($)',
         'HHTYPE_6','RENT_2','RENT_3','TENURE_2','TENURE_3',
         'TENURE_4','MARRIAGE_2','MARRIAGE_4']

for column in list1:
  data_df[column] = [float(str(i).replace(",", "")) for i in data_df[column]]

'''
for column in list1:
  data_df[column] = data_df[column].fillna((data_df[column].mean()))

print(data_df)
'''
list2 = ['index','ASGS_2016','Year','Houses - median sale price ($)',
         'HHTYPE_6','RENT_2','RENT_3','TENURE_2','TENURE_3',
         'TENURE_4','MARRIAGE_2','MARRIAGE_4']

scaler = StandardScaler()
data_df = pd.DataFrame(scaler.fit_transform(data_df),columns=list2)

'''
for column in list:
  data_df[column] = data_df[column].replace(float(0),data_df[column].mean())
'''

profile = ProfileReport(data_df, explorative=True)

#data_profile = profile.get_description()


#data_profile.to_file(outputfile = '/content/profile.txt')
profile.to_file('/content/profile-family.html')
