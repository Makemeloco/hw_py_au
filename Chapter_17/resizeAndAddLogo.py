#! python3
# resizeAndAddLogo.py - изменяет размеры всех изображений в текущем каталоге таким образом, чтобы они вписывались в квадрат с размерами 300х300, и добавляет изображение catlogo.png в его нижний правый угол.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

os.makedirs('withLogo', exist_ok=True)

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# resize to make logo 100px wide, height adjusted to keep aspect ratio
logoIm = logoIm.resize((100, int(100 * (logoHeight / logoWidth))))
# reassign now smaller width and height to variables
logoWidth, logoHeight = logoIm.size

# цикл по всем файлам в текущем рабочем каталоге
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue  # пропустить файлы, не являющиеся файлами изображений и файл самого лого

    im = Image.open(filename)
    width, height = im.size

    # проверка необходимости изменения размеров изображения
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # расчет необходимых новых значений ширины и высоты.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # изменение размеров изображения
        print('Изменение размеров изображения %s...' % (filename))
        im = im.resize((width, height))

    # добавление логотипа
    print('Добавление логотипа в изображение %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    # сохранение изменений
    im.save(os.path.join('withLogo', filename))
