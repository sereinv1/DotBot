# coding=utf-8
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'

def Print_Scanning(url, CMS):
    print(r + '    [' + y + '*' + r + '] ' + c + url + w + ' [ ' + CMS + ' ]')


def Timeout(url):
    print(r + '    [' + y + '*' + r + '] ' + c + url + r + ' [ TimeOut!!/NotValid Url ]')


def Print_NotVuln(NameVuln, site):
    print(c + '       [' + y + '-' + c + '] '
          + r + site + ' ' + y + NameVuln + c + ' [Not Vuln]')


def Print_Username_Password(username, Password):
    print(y + '           [' + c + '+' + y + '] ' + c + 'Username: ' + g + username)
    print(y + '           [' + c + '+' + y + '] ' + c + 'Password: ' + g + Password)


def Print_Vuln(NameVuln, site):
    print(c + '       [' + y + '+' + c + '] ' + r + site + ' ' +
          y + NameVuln + g + ' [Vuln!!]')


def Print_Vuln_index(indexPath):
    print(c + '       [' + y + '+' + c + '] ' + y + indexPath + g + ' [Index Uploaded!]')


def Print_vuln_Shell(shellPath):
    print(c + '       [' + y + '+' + c + '] '
          + y + shellPath + g + ' [Shell Uploaded!]')

def Print_vuln_Config(site):
    print(c + '       [' + y + '+' + c + '] ' + y + site + g + ' [Config Downloaded!]')



def returnYes(target, CVE, Name, CMS):
    return ["Target: ",target," : ",Name," Status:"," Vulnerable"]

def returnNo(target, CVE, Name, CMS):
    return ["Target: ",target," Exploit: ",Name," Status: "," Not Vulnerable"]



'''
ScannedRez = [['google.com','CVE-2015-1579','revslider', '{}YES{}'.format(g, w), 'Wordpress'],
              ['google.com','CVE-2015-1579','revslider', '{}NO{}'.format(r, w), 'Wordpress'],
              ['google.com','CVE-2015-1579','revslider', '{}NO{}'.format(r, w), 'Wordpress']]

t = PrettyTable(['TARGET', 'CVE', 'Name', 'Vulnerable', 'CMS'])
for rez in ScannedRez:
    t.add_row(rez)

print t

'''

