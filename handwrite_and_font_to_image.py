import json
import numpy as np
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os.path

CN_CHARSET = None
CN_T_CHARSET = None
JP_CHARSET = None
KR_CHARSET = None

DEFAULT_CHARSET = "./charset/cjk.json"


def load_global_charset():
    global CN_CHARSET, JP_CHARSET, KR_CHARSET, CN_T_CHARSET
    cjk = json.load(open(DEFAULT_CHARSET))
    CN_CHARSET = cjk["gbk"]
    JP_CHARSET = cjk["jp"]
    KR_CHARSET = cjk["kr"]
    CN_T_CHARSET = cjk["gb2312_t"]


def draw_single_char(ch, font):
    img = Image.new("RGB", (256, 256), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), ch, (0, 0, 0), font=font)
    return img


def draw_example(ch, src_font):
    if os.path.isfile("handwriting/" + ch + ".png"):
        dst_img = Image.open("handwriting/" + ch + ".png")
    else:
        return None
    src_img = draw_single_char(ch, src_font)
    example_img = Image.new("RGB", (256 * 2, 256), (255, 255, 255))
    example_img.paste(dst_img, (0, 0))
    example_img.paste(src_img, (256, 0))
    return example_img


def handwrite_and_font_to_image(src, charset):
    src_font = ImageFont.truetype(src, size=150)
    print(src_font)
    count = 0
    for c in charset:
        e = draw_example(c, src_font)
        if e:
            e.save(os.path.join('sample_dir', "%d_%04d.jpg" % (0, count)))
            count += 1


if __name__ == "__main__":
    load_global_charset()
    charset = 'KR'
    charset = locals().get("%s_CHARSET" % charset)

    src = 'source_font/NanumBarunGothic.ttf'

    handwrite_and_font_to_image(src, charset)
