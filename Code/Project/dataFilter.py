import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.stats.multicomp as multi



def Replacing(df):
    df["offencedata"] = pd.to_datetime(df["offencedate"])

    df["gender_cd"] = df["gender_cd"].replace("M",1)
    df["gender_cd"] = df["gender_cd"].replace(";M",1)
    df["gender_cd"] = df["gender_cd"].replace("F",0)
    df["gender_cd"] = df["gender_cd"].fillna(0)
    df["gender_cd"] = df["gender_cd"].astype("int64")

    df["gear_type"] = df["gear_type"].replace("Автоматическая",1) 
    df["gear_type"] = df["gear_type"].replace("Механическая",0)

    df["marital_status_cd"] = df["marital_status_cd"].replace("MAR",2)
    df["marital_status_cd"] = df["marital_status_cd"].replace("DIV",0)
    df["marital_status_cd"] = df["marital_status_cd"].replace("UNM",-1)
    df["marital_status_cd"] = df["marital_status_cd"].replace("WID",0)
    df["marital_status_cd"] = df["marital_status_cd"].replace("CIV",1)
    
    df["children_cnt"] = df["children_cnt"].fillna(0)