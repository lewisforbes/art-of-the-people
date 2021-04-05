
from instabot import Bot
import base64
from PIL import Image
from tempfile import NamedTemporaryFile
from django.conf import settings

def post_img(b64_str):
    b64_bytes = bytes(b64_str[22:], 'utf-8')
    # with open(old_filepath, "wb") as fh:
    #     fh.write(base64.decodebytes(b64_bytes))

    with NamedTemporaryFile(mode='w+b', delete=False) as temp_png:
         temp_png.write(base64.decodebytes(b64_bytes))
    old_filepath = temp_png.name

    
    im = Image.open(old_filepath)
    bg = Image.new("RGBA", im.size, "WHITE")
    bg.paste(im, (0, 0), im)
    temp_jpg = NamedTemporaryFile(delete=False)
    bg.convert('RGB').save(temp_jpg.name, "JPEG")

    # # reads in credentials
    # f = open("aotp\static\.creds.txt", "r")
    # raw = f.readlines()
    # my_user = raw[0].strip()
    # my_pass = raw[1].strip()
    # f.close()

    my_user = getattr(settings, "USERNAME", None)
    my_pass = getattr(settings, "PASSWORD", None)

    my_caption = "Please unfollow this account lol"
    bot = Bot()
    try:
        bot.login(username=my_user, password=my_pass, is_threaded=True)
        bot.upload_photo(temp_jpg.name,caption=my_caption)
    except:
        pass

    print("Done")
    return True