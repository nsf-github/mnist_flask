import numpy as np
from PIL import Image
from tensorflow.python.keras.models import load_model


my_model = load_model('my_model.h5')


def image_prepare(file_name):
    my_image = Image.open(file_name)
    my_image = my_image.crop((145, 11, 345, 211))
    # 保存剪切出来的图片
    # cut_name = '1.png'
    pixels = my_image.load()
    for i in range(my_image.size[0]):
        for j in range(my_image.size[1]):
            if pixels[i, j] != (0, 0, 0, 255):
                pixels[i, j] = (255, 255, 255, 255)
    # my_image.save(cut_name)

    my_image = my_image.resize((28, 28), Image.ANTIALIAS).convert('L')  # 变换成28*28像素，并转换成灰度图
    tv = list(my_image.getdata())  # 获取像素值
    # tva = [(255 - x) * 1.0 / 255.0 for x in tv]  # 转换像素范围到[0 1], 0是纯白 1是纯黑
    tv = [[tv[i * 28: (i + 1) * 28] for i in range(28)]]
    result = np.array(tv).reshape(-1, 28, 28, 1) / 255.0
    a = my_model.predict(result)
    return np.argmax(a)
