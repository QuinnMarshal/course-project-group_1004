#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

    
def load_and_process(path):
    
    # Method Chain 1(Load data, fix column names and remove missing values)
    
    df1 = (
            pd.read_csv(path)
            .rename(columns = {"age" : "Age", "sex" : "Sex", "bmi" : "BMI", "children" : "Children", "smoker" : "Smoker", "region" : "Region", "charges" : "Insurance Cost"})
            .dropna()
        )
    
    # Method Chain 2(Round BMI and Insurance Cost, sort data by increasing Insurance Cost and re-number rows.)
    
    df2 = (
            df1
            .round({"BMI" : 1, "Insurance Cost" : 2})
            .sort_values("Insurance Cost", ascending = True)
            .reset_index(drop = True)
            
        )
    
    # Method Chain 3(Add new column "weight_class" displaying appropriate weight class for each row by using function 'check_weight_class'. Rename it to "Weight Class")
    
    df3 = (
            df2
            .assign(weight_class = check_weight_class(df2['BMI']))
            .rename(columns = {"weight_class" : "Weight Class"})
        )

    return df3

def check_weight_class(BMI):
    
    # Checks BMI of person and returns the correct Weight class based on where it falls on the BMI scale.
    # Takes in BMI column, creates a list with corresponding weight classes, and returns the list
    
    weight_class_list = []
    for i in range(0, len(BMI)):
        if BMI[i] > 30.0:
            weight_class_list.append("Obese")
        elif BMI[i] >=25 and BMI[i] < 30.0:
            weight_class_list.append("Overweight")
        elif BMI[i] >=18.5 and BMI[i] < 25.0:
            weight_class_list.append("Normal")
        else:
            weight_class_list.append("Underweight")
            
    
    return weight_class_list


# In[ ]:




