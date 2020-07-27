from html.parser import HTMLParser
import sys

l = input()
html = sys.stdin.read()

class myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        if attrs != []:
            for elem in attrs:
                print(f'-> {elem[0]} > {elem[1]}')
    def handle_startendtag(self, tag, attrs):
        print (tag)
        if attrs != []:
            for elem in attrs:
                print(f'-> {elem[0]} > {elem[1]}')

parser = myhtmlparser()
parser.feed(html)
