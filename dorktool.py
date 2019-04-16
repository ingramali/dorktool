#Prints a nice little splash screen.
print "==================="
print "=---CompNerd03----="
print "=--2019/04/14-----="
print "==================="
print "Used for searching Google dorks."
#To search.
from googlesearch import search
ip=raw_input("Dork: ")
#Fakes a user agent to prevent Google from flagging your connection as a botnet.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#Finds and prints a set number of results.
for url in search(ip, stop=15):
    print(url)





