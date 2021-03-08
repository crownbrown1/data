import pandas as pd
from datetime import datetime, timedelta
import sys
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
r=pd.read_csv("drug_exposure.csv")
s=r.loc[:,["person_id","drug_concept_id","drug_exposure_start_date","drug_exposure_end_date"]]
f=s[s["person_id"].isin(["1891866"])]
la=pd.DatetimeIndex(f["drug_exposure_end_date"])-pd.DatetimeIndex(f["drug_exposure_start_date"])
new=f.assign(days = la)
last=new.sort_values('days',ascending=False)
del last['days']
sys.stdout=open('4답.txt','w')
print(last)






