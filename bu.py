from datetime import datetime
import time
import pytesseract
from PIL import Image
import os
import cv2
import time

# crop the image
# croppedIm = Image1.crop((38, 570, 182, 610)) # number

# img = cv2.imread('number.jpg')
# text = pytesseract.image_to_string(img)
# print(text)



# get the list of images
def get_list_of_images():
    images_set = set()
    for image in os.listdir("/home/eselse/Documents/Screenshots"):
        if image.endswith("Audit.jpg"):
            images_set.add(os.path.join("/home/eselse/Documents/Screenshots", image))
    return images_set


# convert img to number
def img_to_number(img):
    # Open the image
    jpg_image = Image.open(img)

    # Crop the image
    cropped_jpg_image = jpg_image.crop((38, 570, 182, 610))

    # Save the cropped image of the number
    cropped_jpg_image.save('number.jpg')

    # Convert image to text
    number_image = cv2.imread('number.jpg')
    try:
        number = int(pytesseract.image_to_string(number_image).replace("\n", ''))
        return number
    except ValueError as e:
        return -1


def write_to_file(nums_list):
    dateTime = datetime.now()
    name_for_file = dateTime.isoformat("|")[:10]
    string = 0
    f = open(f'{name_for_file}.txt', 'w')
    for line in nums_list:
        if string > 1 and string % 50 == 0:
            f.write('-------\n')
        else:
            f.write(f"{line}\n")
        string += 1


result_set = set()
start = time.monotonic()

set_of_files = get_list_of_images()
total_files = len(set_of_files)
i = 0
for file in set_of_files:
    if i % 50 == 0 and i > 1:
        print(f'{i} numbers been recognized.')
    r = img_to_number(file)
    if r != -1:
        result_set.add(r)
    i += 1


result_list = sorted(list(result_set))

# for res in result_list:
    # print(res)

write_to_file(result_list)

total_nums = len(result_list)

end = time.monotonic()
time_spent = int(end - start)
print(f"{time_spent} seconds passed")
print(f'{total_nums-total_nums // 50}/{total_files} numbers added in file')