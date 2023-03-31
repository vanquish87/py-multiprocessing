import time, os
import concurrent.futures
from PIL import Image, ImageFilter


def image_names(directory_path):
    # use os.listdir() to get a list of all files in the directory
    files = os.listdir(directory_path)

    file_list = [file for file in files]

    return file_list


dir = r"C:\jimmy\py-multiprocessing\unsplash-pics"
img_names = image_names(dir)

t1 = time.perf_counter()

size = (300, 400)


def process_image(img_name):
    img = Image.open(dir + "\\" + img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


if __name__ == '__main__': 
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
        
    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')