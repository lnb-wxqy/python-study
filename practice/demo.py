from PIL import Image, ImageDraw, ImageFont

# 测试字体格式
font1 = ImageFont.truetype('C:\\Windows\\Fonts\\simhei.ttf', 20)


def addNumber(image, number):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('C:\\Windows\\Fonts\\simhei.ttf', 45)
    draw.text((im.size[0] - 35, 0), str(number), font=font, fill=(255, 0, 0))
    im.save('F:/python/python-study/images/avat.jpg', 'JPEG')


if __name__ == '__main__':
    addNumber('F:/python/python-study/images/cjq.jpg', 5)
