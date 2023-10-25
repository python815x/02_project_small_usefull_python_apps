from PIL import Image

# 540x426
image_name = 'road.jpg'


def resize_image(size1, size2):
    image = Image.open(f'{image_name}')

    print(f'Current size : {image.size}')

    resized_image = image.resize((size1, size2))

    resized_image.save(f'resized_{image_name}')


size1 = int(input('Enter Width: '))
size2 = int(input('Enter Height: '))
resize_image(size1, size2)
