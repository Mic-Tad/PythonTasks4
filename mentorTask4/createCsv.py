import pandas as pd
import time


def human_bytes(num, suf='B'):
    for u in ['','K','M','G']:
        if abs(num)<1024.0:
            return "%3.1f%s%s" % (num,u,suf)
        num/=1024.0
    return "%.1f%s%s" % (num,'Yi',suf)
def create_file():
    val=[]
    dict={'year':[],'month':[],'day':[]}
    for i in range(1700,2200):
        for j in range(1,13):
            for k in range(1,31):
                if(k<29 or j!=2):
                    dict['year'].append(i)
                    dict['month'].append(j)
                    dict['day'].append(k)
                    val.append(i+j+k)
     
     
    dates=pd.to_datetime(pd.DataFrame.from_dict(dict), errors = 'coerce')
    t=time.time()   
    df=pd.DataFrame({'date':dates,'value':val})
    dt=time.time()-t
    print(dt)
    df.to_csv('./csvfile.csv',index=False)


create_file()
