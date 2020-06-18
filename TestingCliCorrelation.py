import matplotlib
import matplotlib.pyplot as plt
import io, base64, os, json, re 
import pandas as pd
import numpy as np
import datetime


gspc_df = pd.read_csv('^GSPC.csv')
gspc_df['Date'] = pd.to_datetime(gspc_df['Date'])
vix_df = pd.read_csv('^VIX.csv')
vix_df['Date'] = pd.to_datetime(vix_df['Date'])
vix_df.tail()
