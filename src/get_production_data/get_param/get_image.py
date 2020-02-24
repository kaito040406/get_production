import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib.error
import urllib.request



def Get_images(d_soup, nomber):
  image_boxs = d_soup.select(".a-dynamic-image#landingImage", recursive=False)
  for image_box in image_boxs:
    for image in image_box.get("data-a-dynamic-image").split('"'):
      if 'https://' in image:
        Image_download(image, nomber)
        i += 1
      if i > 1:
        break
    time.sleep(0.1)

  return image


def Image_download(url, nomber):
  dst_path = "images/"+ "image" +str(nomber)
  try:
    with urllib.request.urlopen(url) as web_file:
      data = web_file.read()
      with open(dst_path, mode='wb') as local_file:
          local_file.write(data)
  except urllib.error.URLError as e:
    print(e)
    pass