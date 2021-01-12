import requests
import json
import sys

url = "https://api.covid19india.org/data.json"
response = requests.get(url)
x = response.json()

def get_country_stat():
    y = x["cases_time_series"]
    d = y[-1]
    return("Total Confirmed : "+d["totalconfirmed"]+"\n"+
           "Total Recovered : "+d["totalrecovered"]+"\n"+
           "Total Deceased  : "+d["totaldeceased"]+"\n"+
           "Updated On      : "+d["date"])


def get_state_list():
    s = x["statewise"]
    states = []
    for i in range(1,len(s)):
        states.append(s[i]["state"])
    return states

def get_state_stat(state):
    states = x["statewise"]
    for i in range(1,len(states)):
        if states[i]["state"] == state:
            s = states[i]
            return("<code>Total Active    : "+s["active"]+"\n"+
                   "Total Confirmed : "+s["confirmed"]+"\n"+
                   "Total Recovered : "+s["recovered"]+"\n"+
                   "Total Deceased  : "+s["deaths"]+"\n"+
                   "Updated On      : "+s["lastupdatedtime"]+"</code>")


            
