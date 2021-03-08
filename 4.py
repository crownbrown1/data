import pandas as pd
from datetime import datetime, timedelta
r=pd.read_csv("drug_exposure.csv")
s=r.loc[:,["person_id","drug_concept_id","drug_exposure_start_date","drug_exposure_end_date"]]
f=s[s["person_id"].isin(["1891866"])]
la=pd.DatetimeIndex(f["drug_exposure_end_date"])-pd.DatetimeIndex(f["drug_exposure_start_date"])
new=f.assign(days = la)
last=new.sort_values('days',ascending=False)
del last['days']
print(last)






