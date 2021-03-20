import requests
import emoji
from bs4 import BeautifulSoup as bs
def getText(txt):
    if '<' in str(txt): return str(txt).split('<')[1].split('>')[1]
    else: return txt

def getInfo(s_name):
    r=requests.get("https://tr.op.gg/summoner/userName="+s_name)
    soup=bs(r.content,"lxml")
    name=soup.find("span",attrs={"class":"Name"})
    if name is None:
        return 0
    else:
        level=soup.find("span",attrs={"class":"Level tip"})
        soloq_rank=soup.find("div",attrs={"class":"TierRank"})
        soloq_lp=soup.find("span",attrs={"class":"LeaguePoints"})
        if soloq_lp is not None:
            soloq_lp=str(soloq_lp).split("\n")[1].strip()
        else:
            soloq_rank="Unranked"
            soloq_lp=""
        flex_rank=soup.find("div",attrs={"class":"sub-tier__rank-tier"})
        flex_lp=soup.find("div",attrs={"class":"sub-tier__league-point"})
        if flex_lp is not None:
            pass
        else:
            flex_lp=""

        return [getText(name),getText(level),getText(soloq_rank),soloq_lp,getText(flex_rank).strip(),getText(flex_lp)]
