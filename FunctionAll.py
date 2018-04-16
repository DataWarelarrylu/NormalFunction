import re

def ReadFile(url,vReg):
    f = open(url, 'r', encoding='utf-8')
    vres = (f.read())
    return re.findall('vReg"', vres)