import textwrap

def wrap(string, max_width):
    wrap = textwrap.wrap(string, width=max_width)
    return '\n'.join(wrap)

string = input()
width = int(input())