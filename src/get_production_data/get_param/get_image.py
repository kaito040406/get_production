import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import sys
sys.path.append('../../')
from save_data import save


def Get_images(d_soup, nomber):
  i = 0
  image_boxs = d_soup.select(".a-dynamic-image#landingImage", recursive=False)
  if len(image_boxs) == 0:
    image = "情報なし"
  else:
    for image_box in image_boxs:
      for image in image_box.get("data-a-dynamic-image").split('"'):
        if 'https://' in image:
          image = save.Image_download(image, nomber)
          i += 1
        if i > 1:
          break
      time.sleep(0.1)
  return image