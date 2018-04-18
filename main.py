import urllib.request as url
import urllib.parse as parse

__author__ = 'elad'

print("hello from pycharm")

params = parse.urlencode({'station': 'DAR'})
url1 = "http://www.lvh.me:3000/notification/get_user?%s" % params

contents = url.urlopen(url1).read().decode('utf-8')

print("contents ", contents)
