import re
import os

infilepath = 'frontend/dist/index.html'
outfilepath = 'templates/index.html'

if not os.path.exists(os.path.dirname(outfilepath)):
    os.makedirs(os.path.dirname(outfilepath))

with open(infilepath, 'r') as infile, open(outfilepath, 'w+') as outfile:
    html = infile.read()
    html = re.sub(r'/(static/(.*?\.(css|js)))', r'{% static "\2" %}', html)
    html = '{% load staticfiles %}\n' + html
    outfile.write(html)
print 'Done.'

