#!/usr/bin/env python
#coding=utf-8
import pandas as pd

path_to_file = '/media/devitte/9AEA04A9EA04842B/Backup-Fishtank/'
file_name = 'train_raw_w-abril.csv'

dataframe = pd.read_csv(path_to_file + file_name, sep=',',engine='c')
dates = dataframe.Data
try:
    new_dates = pd.to_datetime(dates)
except:
    print('Date format not supported yet')

dataframe.Data = new_dates
dataframe.to_csv(filename)
print('\n\nDates updated sucessfully')
