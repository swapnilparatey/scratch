# Let's keep it simple - it's a 4-liner
# This is from some GeekForGeeks article - forgot about posting the link

from typing import BinaryIO

import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

r = requests.get(image_url) # create HTTP response object

f: BinaryIO
with open("C:\\Users\\linpa\\Desktop\\Crap\\python_logo.png",'wb') as f:
    f.write(r.content)

###############################################

file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"

r = requests.get(file_url, stream = True)

with open("C:\\Users\\linpa\\Desktop\\Crap\\python.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):

        # writing one chunk at a time to pdf file
        if chunk:
            pdf.write(chunk)

##################################################
"""
import requests
from bs4 import BeautifulSoup

# specify the URL of the archive here
archive_url = "http://www-personal.umich.edu/~csev/books/py4inf/media/"

def get_video_links():
    # create response object
    r = requests.get(archive_url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'html5lib')

    # find all links on web-page
    links = soup.findAll('a')

    # filter the link sending with .mp4
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]
    print(video_links)

    return video_links

def download_video_series(video_links):
    for link in video_links:

        '''iterate through all links in video_links
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split('/')[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True)
        print(r)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All videos downloaded!")
    return


if __name__ == "__main__":
    # getting all video links
    video_links = get_video_links()

    # download all videos
    download_video_series(video_links)
"""


################################################################




