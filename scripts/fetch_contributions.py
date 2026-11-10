#!/usr/bin/env python3
"""Fetch the public GitHub contribution calendar through GitHub GraphQL.
Uses GITHUB_TOKEN and works for a public user; private contributions may not appear.
"""
import datetime as dt
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

user=os.getenv('GITHUB_USERNAME','shvmmonk')
token=os.getenv('GITHUB_TOKEN')
if not token:raise SystemExit('GITHUB_TOKEN is required. No placeholder counts written.')
today=dt.datetime.now(dt.timezone.utc)
start=today-dt.timedelta(days=364)
query='''query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){contributionsCollection(from:$from,to:$to){contributionCalendar{weeks{contributionDays{date contributionCount}}}}}}'''
payload=json.dumps({'query':query,'variables':{'login':user,'from':start.isoformat(),'to':today.isoformat()}}).encode()
req=Request('https://api.github.com/graphql',payload,{'Authorization':'Bearer '+token,'Content-Type':'application/json','User-Agent':'profile-cards'})
with urlopen(req,timeout=40) as response: data=json.load(response)
if 'errors' in data or not data.get('data',{}).get('user'):
    raise SystemExit('GitHub GraphQL returned an error: '+str(data.get('errors')))
weeks=data['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
days=[{'date':d['date'],'count':d['contributionCount']} for week in weeks for d in week['contributionDays']]
file=Path(__file__).resolve().parent/'data'/'contributions.json'
file.parent.mkdir(parents=True,exist_ok=True)
file.write_text(json.dumps({'username':user,'updated_at':today.isoformat(),'days':days},indent=2)+'\n')
print('Fetched',len(days),'days for',user)
