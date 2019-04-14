print "==================="
print "=---PlagueHax-----="
print "=--2019/04/14-----="
print "==================="
print "Used for searching Google dorks."

from googlesearch import search
ip=raw_input("Dork: ")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
for url in search(ip, stop=15):
    print(url)


