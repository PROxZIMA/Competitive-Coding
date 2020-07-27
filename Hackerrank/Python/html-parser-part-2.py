from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            for elem in data.split('\n'):
                print(elem)
        else:
            print('>>> Single-line Comment\n'+data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data\n'+data)

l = input()
html = sys.stdin.read()

parser = MyHTMLParser()
parser.feed(html)
parser.close()
