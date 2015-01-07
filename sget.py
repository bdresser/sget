#! /usr/bin/python

import urllib2
import urllib
import urlparse
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib import urlretrieve
from os.path import relpath
import os
import sys

depth = 2

def main(url, out_folder, indent):

    global depth 

    try:
        req = urllib2.Request(url)
	conn =  urllib2.urlopen(req)
        parsed = list(urlparse.urlparse(url))
	content = conn.read() 
    except urllib2.URLError, e:
        print 'Your HTTP error response code is: ', e

    soup = BeautifulSoup(content)

    for link in soup.find_all('a'):
        href = link.get('href')
        if href == '#':
            continue
        full_path = urlparse.urljoin(url, href) 
        o = urlparse.urlparse(href)
        relative_path = os.path.relpath(full_path, url)
        k = relative_path.rfind("../"); 
        
        if relative_path.startswith("..") and o.netloc:
            print(indent + full_path + " [external]")
        else:
            relative_path = relative_path[k+3:]
            outpath = os.path.join(out_folder, relative_path)
      #      urllib.urlretrieve(full_path, outpath)
            print(indent + relative_path + " [success]")
            if depth > 0:
                depth = depth - 1
                indent+="  "
                print(full_path + "is full path")
                main(full_path, out_folder, indent)
            #print(outpath)
	


if __name__ == "__main__":
    url = sys.argv[-1]
    out_folder = "test/"
    if not url.lower().startswith("http"):
        out_folder = sys.argv[-1]
        url = sys.argv[-2]
        if not url.lower().startswith("http"):
            print "error: command line args"
            sys.exit(-1)

    print("URL: " + url)
    print("current: " + os.getcwd())
    print("target: " + out_folder)
    print
    print("DONT RUN THE REST")
#    main(url, out_folder, "")

