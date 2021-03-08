import pandas as pd
from datetime import datetime, timedelta
import sys
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
r=pd.read_csv("visit_occurrence.csv")
r["visit_start_date"]=pd.DatetimeIndex(r["visit_start_date"])
r["visit_end_date"]=pd.DatetimeIndex(r["visit_end_date"])
total=r["visit_end_date"]-r["visit_start_date"]#총내원일수
#sys.stdout=open('2query.txt','w')
new=r.assign(es=total)
new["es"]=new["es"].astype(str)
new["es"]=new["es"].str.replace(pat='days',repl=r"",regex=True)
new["es"]=pd.to_numeric(new["es"])


print(new["es"].sum())#31137 총내원일수


new1=new.loc[:,["person_id","es"]]
new2 = new1.groupby(["person_id"]).sum()#환자가 내원한 일수
print(new2.loc[new2["es"].idxmax()])#총 내원 일수 최댓값을 가지는 환자:1059760,횟수:18720





