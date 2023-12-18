import pandas as pd
import numpy as np

def searchidname(DF, this_id, this_value):
    if this_id == "empid_in":
        res = DF.loc[DF["empidstr"].str.contains('^{}'.format(this_value),regex=True),["empid","empname"]]
    
    elif  this_id == "empname_in":
        res = DF.loc[DF["empname"].str.contains('{}'.format(this_value),regex=True),["empid","empname"]]
    #
    
    return res.to_dict('records')
#