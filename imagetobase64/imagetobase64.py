# 文件对话框：QFileDialog
import base64

# 图片base流还原图片是需加：data:image/jpg;base64,
image_path = 'C:/Users/lanningbo/Desktop/image/iamgetest/cjq.jpg'
with open(image_path, 'rb') as f:
    image = f.read()
    image_base64 = str(base64.b64encode(image), encoding='utf-8')
    print(image_base64)

