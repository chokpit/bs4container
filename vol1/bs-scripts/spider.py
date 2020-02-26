import bs4 as bs
import urllib.request
import sys
import os

script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
rel_path = "temp/temp_urls.txt"
abs_file_path = os.path.join(script_dir, rel_path)

print(abs_file_path)
fh = open(abs_file_path, 'a+')
with open(abs_file_path) as fr:
    for line in fr: #like while not EOF
        print(line)
        if (line.startswith('https') or line.startswith('http')):
            primary_url = line[:line.index('/')]
        else:
            fixed_line = '{}{}'.format(primary_url,line)
        source = urllib.request.urlopen(line).read()

        soup = bs.BeautifulSoup(source,'lxml')
        for url in soup.find_all('a'):
            fh.write("\n {}".format(url.get('href')))
fr.close()
fh.close()