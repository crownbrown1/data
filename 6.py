import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
r=pd.read_csv("condition_occurrence.csv")
s=r.loc[:,["person_id","condition_concept_id"]]
f=s[s["condition_concept_id"].isin(["3191208","36684827","3194332","3193274","43531010","4130162","45766052","45757474","4099651","4129519","4063043","4230254","4193704","4304377","201826","3194082","3192767"])]
c=f["person_id"]
cn=c.values
cnn=cn.tolist()
r1=pd.read_csv("person.csv")
s1=r1.loc[:,["person_id","birth_datetime"]]
f1=s1[s1["person_id"].isin(cnn)]
f2=f1.query("birth_datetime <= '2002-01-01'")#18세 이상
c1=f2["person_id"].values.tolist()
r2=pd.read_csv("drug_exposure.csv")
s2=r2.loc[:,["person_id","drug_concept_id","drug_exposure_start_datetime","drug_exposure_end_datetime"]]#약물날짜,사람아이디
ff1=s2[s2["drug_concept_id"].isin(["40163924"])]#metformin 복용자
la=pd.DatetimeIndex(ff1["drug_exposure_end_datetime"])-pd.DatetimeIndex(ff1["drug_exposure_start_datetime"])
new=ff1.assign(es=la)
new["es"]=new["es"].astype(str)
new["es"]=new["es"].str.replace(pat='days',repl=r"",regex=True)
new["es"]=pd.to_numeric(new["es"])
new1=new.query("es >= 90")#90일 이상 복용 환자수
del new1["es"]
new2=new1[new1["person_id"].isin(c1)]
sys.stdout=open('6답.txt','w')
print(new2.drop_duplicates("person_id",keep="first"))
#답 : 30 명 






