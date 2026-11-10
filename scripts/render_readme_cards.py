#!/usr/bin/env python3
"""Single-file, dependency-free GitHub profile SVG renderer.
Optional: fonttools (pyftsubset) to embed local fonts. STATIC=1 reveals final frames.
"""
import base64
import calendar
import datetime as dt
import html
import json
import os
import subprocess
from urllib.request import Request, urlopen
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == 'scripts' else HERE
CARDS = ROOT / 'cards'
DATA = ROOT / 'data' / 'contributions.json'
CARDS.mkdir(exist_ok=True)
STATIC = os.getenv('STATIC', '0') == '1'
INK = '#0a0e1a'
BG = '#111827'
PANEL = '#192439'
LINE = '#374151'
WHITE = '#f3f4f6'
MUTED = '#abb9cf'
CYAN = '#4dd9e8'
GOLD = '#f5c400'
GREEN = '#00c85a'
RED = '#ff796b'

# Match the author's Minecraft-inspired site: Press Start 2P + VT323.
# Subset open-source fonts from the same Google Fonts families as the portfolio.
# CI fetches these OFL-licensed font files once before embedding; no runtime requests by the SVG.
FONTS = [('Pixel', 'PressStart2P-Regular.ttf'), ('Terminal', 'VT323-Regular.ttf')]

def fonts_css():
    css = []
    for family, name in FONTS:
        path = ROOT / 'fonts' / name
        if not path.is_file():
            if os.getenv('SKIP_FONT_DOWNLOAD') == '1':
                continue
            try:
                path.parent.mkdir(exist_ok=True)
                family_dir = 'pressstart2p' if family == 'Pixel' else 'vt323'
                url = f'https://raw.githubusercontent.com/google/fonts/main/ofl/{family_dir}/{name}'
                with urlopen(Request(url, headers={'User-Agent':'profile-readme-renderer'}), timeout=15) as r:
                    path.write_bytes(r.read())
            except Exception as e:
                print(f'Font unavailable ({name}): {e}; using fallback')
                continue
        woff = ROOT / 'fonts' / (path.stem + '.woff')
        if not woff.exists() or woff.stat().st_mtime < path.stat().st_mtime:
            try:
                subprocess.run(['pyftsubset', str(path), '--output-file='+str(woff), '--flavor=woff',
                    '--text='+''.join(chr(i) for i in range(32,127))+'→•—'], check=True, capture_output=True)
            except (FileNotFoundError, subprocess.CalledProcessError):
                continue
        data = base64.b64encode(woff.read_bytes()).decode('ascii')
        css.append(f"@font-face{{font-family:'{family}';src:url(data:font/woff;base64,{data}) format('woff');font-weight:400;}}")
    return ''.join(css)

FONT_CSS = fonts_css()

def esc(x): return html.escape(str(x), quote=True)
def text(x, y, s, size=21, color=WHITE, family='Terminal', extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}, monospace" font-size="{size}" {extra}>{esc(s)}</text>'

def rect(x,y,w,h,fill,r=0,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {extra}/>'

def css():
    return FONT_CSS + '''
    .fade{opacity:0;animation:rise .65s ease forwards;}
    .pixel{opacity:0;animation:appear .28s steps(1,end) forwards;}
    .bar{transform:scaleY(0);transform-box:fill-box;transform-origin:center bottom;animation:grow .7s cubic-bezier(.2,.9,.25,1) forwards;}
    .shine{animation:glow 3s ease-in-out infinite;}
    .float{animation:float 3.4s ease-in-out infinite;}
    @keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
    @keyframes appear{to{opacity:1}}
    @keyframes grow{to{transform:scaleY(1)}}
    @keyframes glow{0%,100%{opacity:.75}50%{opacity:1}}
    @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
    @media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;opacity:1!important;transform:none!important;}}
    ''' + (''' .fade,.pixel,.bar,.shine,.float{animation:none!important;opacity:1!important;transform:none!important;} ''' if STATIC else '')

def svg(w,h,body,delay=0):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><style>{css()}</style>
    {rect(0,0,w,h,BG,14)}{rect(2,2,w-4,h-4,'none',12, f'stroke="{LINE}" stroke-width="2"')}
    {rect(0,0,8,h,CYAN if delay==0 else GOLD if delay==3 else CYAN,0)}{body}</svg>'''

def write(name, data): (CARDS / name).write_text(data, encoding='utf-8')

def fade(inner, delay):return f'<g class="fade" style="animation-delay:{delay:.2f}s">{inner}</g>'

def hero():
    s = rect(37,28,120,27,'#264359',5)+text(49,47,'BACKEND ENGINEER',17,CYAN)
    s += fade(text(40,112,'SHIVAM NATH',37,GOLD,'Pixel'),.12)
    s += fade(text(40,167,'GOSWAMI',43,WHITE,'Pixel'),.5)
    s += fade(text(41,216,'Building the logic behind the screen.',29,CYAN),.9)
    s += fade(text(41,250,'Java  /  Spring Boot  /  REST APIs  /  PostgreSQL',21,MUTED),1.15)
    s += fade(text(41,288,'B.Tech CSE @ SRMIST     |     Backend Developer',20,WHITE),1.4)
    # Code-themed pixel avatar, not a personal photograph.
    s += rect(683,38,145,190,'#0a0e1a',6)+rect(692,47,127,172,'#162b35',3)
    s += text(704,83,'{',56,CYAN,'Terminal', 'class="shine"')+text(747,126,'S',64,GOLD,'Pixel','class="float"')+text(790,190,'}',58,CYAN)
    s += rect(706,202,100,4,GREEN)+text(698,242,'LEVEL: JAVA',15,GREEN)
    s += fade(text(41,335,'> BUILD   > LEARN   > SHIP',21,GREEN),1.65)
    write('hero.svg',svg(860,365,s))

def tile(slug,number,title,subtitle,color,delay):
    b=rect(23,25,76,76,color,8)
    b+=text(42,79,number,35,INK,'Pixel')
    b+=fade(text(23,145,title,30,WHITE,'Pixel'),delay)
    b+=fade(text(23,186,subtitle,23,MUTED),delay+.18)
    b+=text(252,226,'↗',28,color)
    write(slug+'.svg',svg(280,244,b,3))

def load_days():
    if not DATA.exists(): return {}
    raw=json.loads(DATA.read_text(encoding='utf-8'))
    vals=raw.get('days',raw.get('contributions',[])) if isinstance(raw,dict) else raw
    if isinstance(vals,dict):vals=[{'date':d,'count':n} for d,n in vals.items()]
    out={}
    for v in vals:
        if not isinstance(v,dict):continue
        try:
            d=dt.date.fromisoformat(str(v.get('date',''))[:10]);n=int(v.get('count',v.get('contributionCount',0)))
            out[d]=max(0,n)
        except(ValueError,TypeError):continue
    return out

def metrics(days):
    today=dt.datetime.now(dt.timezone.utc).date()
    start=today-dt.timedelta(days=364)
    window={d:n for d,n in days.items() if start<=d<=today}
    active=sum(n>0 for n in window.values())
    total=sum(window.values())
    busiest=max(window.items(),key=lambda a:a[1]) if window else None
    streak=0
    cursor=today if days.get(today,0)>0 else today-dt.timedelta(days=1)
    while days.get(cursor,0)>0 and cursor>=start:
        streak+=1;cursor-=dt.timedelta(days=1)
    return today,start,active,total,busiest,streak

def activity(days):
    today,start,active,total,busiest,streak=metrics(days)
    label=lambda v:str(v) if days else '—'
    s=fade(text(30,48,'ACTIVITY // LAST 365 DAYS',24,CYAN,'Pixel'),2.15)
    for x,head,val in [(30,'CONTRIBUTIONS',label(total)),(303,'CURRENT STREAK',label(streak)+' days' if days else '—'),(580,'ACTIVE DAYS',label(active))]:
        s+=text(x,98,head,19,MUTED)+fade(text(x,140,val,32,GOLD,'Pixel'),2.4)
    busiest_label=(busiest[0].strftime('%d %b %Y')+'  /  '+str(busiest[1])+' contributions') if busiest else 'Awaiting first data refresh'
    s+=text(30,183,'BUSIEST DAY: '+busiest_label,23,WHITE)
    m=defaultdict(int)
    for date,n in days.items():
        if start<=date<=today:m[(date.year,date.month)]+=n
    months=[]
    for i in range(11,-1,-1):
        yy=today.year; mm=today.month-i
        while mm<=0:mm+=12;yy-=1
        months.append((yy,mm))
    largest=max([m[k] for k in months] or [0]);peak=max(months,key=lambda k:m[k])
    for i,k in enumerate(months):
        x=33+i*67;value=m[k]
        bh=max(3,round(115*value/max(largest,1)))
        c=CYAN if value and k==peak else GREEN
        s+=rect(x,338-bh,37,bh,c,3,f'class="bar" style="animation-delay:{2.8+i*.06:.2f}s"')
        s+=text(x,365,calendar.month_abbr[k[1]],19,MUTED)
        if value and k==peak:s+=text(x-4,328-bh,str(value),17,CYAN)
    s+=text(29,400,'MONTHLY CONTRIBUTIONS  /  DATA FROM GITHUB',18,MUTED)
    write('activity.svg',svg(860,420,s,2))

def heatmap(days):
    today,start,active,total,busiest,streak=metrics(days)
    anchor=start-dt.timedelta(days=(start.weekday()+1)%7)
    s=fade(text(25,43,'CONTRIBUTION MAP',24,CYAN,'Pixel'),1.7)
    top=91
    for col in range(53):
        for row in range(7):
            d=anchor+dt.timedelta(days=col*7+row)
            if d>today or d<start:color='#1b2838'
            else:
                n=days.get(d,0)
                color='#203442' if n==0 else '#1d6377' if n<3 else '#278aa4' if n<6 else '#35b6cc' if n<11 else CYAN
            x=25+col*15.3;y=top+row*17
            s+=rect(round(x,1),y,11.5,12,color,2,f'class="pixel" style="animation-delay:{1.9+col*.035+row*.016:.2f}s"')
    s+=text(25,238,'LESS',16,MUTED)
    for i,c in enumerate(['#203442','#1d6377','#278aa4','#35b6cc',CYAN]):s+=rect(74+i*19,224,13,13,c,2)
    s+=text(182,238,'MORE',16,MUTED)
    s+=text(668,239,'UPDATED DAILY',16,CYAN)
    write('heatmap.svg',svg(860,260,s,1))

def repo(slug,number,title,description,stack,color,delay):
    s=rect(27,22,59,59,color,8)+text(40,63,number,25,INK,'Pixel')
    s+=fade(text(107,61,title,26,WHITE,'Pixel'),delay)
    s+=fade(text(29,119,description,24,MUTED),delay+.15)
    s+=text(29,164,stack,22,color)
    s+=text(801,166,'↗',25,color)
    write('repo-'+slug+'.svg',svg(860,190,s,4))

def main():
    days=load_days()
    hero()
    tile('build','01','BUILD','Projects & APIs',CYAN,3.3)
    tile('learn','02','LEARN','DSA & systems',GOLD,3.45)
    tile('connect','03','CONNECT','Work together',GREEN,3.6)
    heatmap(days)
    activity(days)
    repo('supportlyai','01','supportlyAi','RAG-powered WhatsApp customer support automation','SPRING BOOT  /  JWT  /  RAG  /  MYSQL',CYAN,4.1)
    repo('task-tracker','02','Task Tracker CLI','A Java task manager with local file persistence','JAVA  /  CLI  /  FILE IO',GOLD,4.3)
    repo('fake-news','03','Fake News Detector','An exploration of machine learning for news classification','PYTHON  /  MACHINE LEARNING',GREEN,4.5)
    print('Rendered',len(list(CARDS.glob('*.svg'))),'SVG cards. Data days:',len(days),'STATIC:',STATIC)

if __name__=='__main__':main()
