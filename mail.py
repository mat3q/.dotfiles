# author mat3
# hello python world
from xml.dom import minidom
import urllib.request as urllib2

url = urllib2.HTTPPasswordMgrWithDefaultRealm()
url.add_password(None, "https://mail.google.com/mail/feed/atom", "login(without @gmail)", "pass")
urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(url)))

dom = minidom.parse(urllib2.urlopen("https://mail.google.com/mail/feed/atom"))
count = dom.getElementsByTagName('fullcount')[0].childNodes[0].nodeValue
print(count)
