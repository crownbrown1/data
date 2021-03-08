import pandas as pd
from datetime import datetime, timedelta
r=pd.read_csv("visit_occurrence.csv")
r["visit_start_date"]=pd.DatetimeIndex(r["visit_start_date"])
r["visit_end_date"]=pd.DatetimeIndex(r["visit_end_date"])
total=r["visit_end_date"]-r["visit_start_date"]#총내원일수
print(total)




