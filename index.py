from flask import Flask, render_template
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import xml.etree.ElementTree as ET

OS_CHINA_RSS = 'http://www.oschina.net/news/rss'

def getXMLString(url):
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla')
    xml = None
    try:
        res = urlopen(req)
        xml = res.read().decode()
    except (URLError, HTTPError) as e:
        print(e)
    return xml

app = Flask(__name__)

@app.route('/')
def index():
    xml = getXMLString(OS_CHINA_RSS)
    if xml:
        root = ET.fromstring(xml)
        channel = root[0]
        return render_template('index.html', channel=channel[6:])
    return '<h1>Bad Request</h1>'

if __name__ == '__main__': app.run(host='0.0.0.0', port=8080, debug=True)
