from instabot import Bot
import base64
from PIL import Image
from tempfile import NamedTemporaryFile
from django.conf import settings

import os

from instabot import Bot
def newBot(my_user=settings.USERNAME, my_pass=settings.PASSWORD):
    reset(my_user) # may do nothing
    bot = Bot()
    bot.login(username=my_user, password=my_pass, is_threaded=True)
    return bot

def reset(username):
    base_path = os.path.abspath(os.getcwd()) + "/config/"
    fname = "{}_uuid_and_cookie.json".format(username)
    cookie_path = os.path.join(base_path, fname)

    if os.path.isfile(cookie_path):
        os.remove(cookie_path)


def post_img(b64_str, title, artist):
    bot = newBot()

    b64_bytes = bytes(b64_str[22:], 'utf-8')

    with NamedTemporaryFile(mode='w+b', delete=False) as temp_png:
         temp_png.write(base64.decodebytes(b64_bytes))
    old_filepath = temp_png.name
    
    im = Image.open(old_filepath)
    bg = Image.new("RGBA", im.size, "WHITE")
    bg.paste(im, (0, 0), im)
    temp_jpg = NamedTemporaryFile(delete=False)
    bg.convert('RGB').save(temp_jpg.name, "JPEG")
    
    my_caption = "\'{}\' by {}.\nDM to enquire.".format(title, artist)
    try:
        bot.upload_photo(temp_jpg.name, caption=my_caption)
    except:
        pass