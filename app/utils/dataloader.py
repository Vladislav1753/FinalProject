import numpy as np
import pandas as pd
import re as re
import os
from app.settings.constants import DATA

file_path = r"C:\Users\Владислав\Desktop\healthcare-dataset-stroke-data.csv"
data = pd.read_csv(file_path, header=0)


#print(data['work_type'].unique())
#print(data['smoking_status'].unique())

'''
data.drop('id', axis=1, inplace=True)

#data['ever_married'] = data['ever_married'].replace({'Yes': 1, 'No': 0})
#data['ever_married'] = data['ever_married'].astype(int)

#data['Residence_type'] = data['Residence_type'].replace({'Urban': 1, 'Rural': 0})
#data['Residence_type'] = data['Residence_type'].astype(int)


data = pd.get_dummies(data, columns=['ever_married'], prefix='married')
data = pd.get_dummies(data, columns=['Residence_type'], prefix='Residence')
data = pd.get_dummies(data, columns=['gender'], prefix='gender')

#mapping for smoking status
mapping = data.groupby('smoking_status')['stroke'].mean().to_dict()
data['smoking_status'] = data['smoking_status'].map(mapping)

#mapping for work type
mapping = data.groupby('work_type')['stroke'].mean().to_dict()
data['work_type'] = data['work_type'].map(mapping)
print(data['work_type'].unique())

data['bmi'].fillna(data['bmi'].mean(), inplace=True)

print(data.info())
'''

class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    # apply regex
    def get_title(self, name):
        pattern = ' ([A-Za-z]+)\.'
        title_search = re.search(pattern, name)
        # If the title exists, extract and return it.
        if title_search:
            return title_search.group(1)
        return ""

    def load_data(self):

        drop_elements = ['id']
        self.dataset = self.dataset.drop(drop_elements, axis=1)

        target_drop = ['stroke']
        try:
            self.dataset = self.dataset.drop(target_drop, axis=1)
        except KeyError:
            pass


        self.dataset = pd.get_dummies(self.dataset, columns=['ever_married'], prefix='married')
        self.dataset = pd.get_dummies(self.dataset, columns=['Residence_type'], prefix='Residence')
        self.dataset = pd.get_dummies(self.dataset, columns=['gender'], prefix='gender')

        if 'gender_Other' not in self.dataset.columns:
            self.dataset['gender_Other'] = 0

        #smoking status
        mapping_smoking = {
            'formerly smoked': 0.3,
            'never smoked': 0,
            'smokes': 0.5,
            'Unknown': 0
        }
        self.dataset['smoking_status'] = self.dataset['smoking_status'].replace(mapping_smoking)

        #work type
        mapping_work = {
            'Private': 0.5,
            'Self-employed': 0.3,
            'Govt_job': 0.5,
            'children': 0,
            'Never_worked': 0
        }
        self.dataset['work_type'] = self.dataset['work_type'].replace(mapping_work)


        self.dataset['bmi'].fillna(self.dataset['bmi'].mean(), inplace=True)

        return self.dataset