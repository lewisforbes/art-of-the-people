from instabot import Bot
import base64
from PIL import Image
from tempfile import NamedTemporaryFile
from django.conf import settings

from instabot import Bot
def newBot(my_user=settings.USERNAME, my_pass=settings.PASSWORD):
    bot = Bot()
    bot.login(username=my_user, password=my_pass, is_threaded=True)
    return bot

bot = newBot()  

def post_img(b64_str, title, artist):
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
        bot.upload_photo(temp_jpg.name,caption=my_caption)
        print("Posted.")
    except:
        print("Failed to post.")
        
    return True 

def post_img_temp(x,y,z):
    print("Received: ", y, z)
    return True