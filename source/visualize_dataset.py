import cv2
import matplotlib.pyplot
import os
import glob


def visualize(image_path: str, label_path: str) -> None:
    '''
        Plot images and its corresponding labels.

        Args:
            image_path (str): path to an image file.
            label_path (str): path to a label file.
        
        Returns:
            None
    '''

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    ih, iw, _ = image.shape

    with open(label_path, 'r') as file:
        lines = file.readlines()
    
    if lines == '':
        return
    
    lines = [line[2:] for line in lines]

    labels = []
    class_field = 0

    print(class_field)

    for line in lines:
        labels.append(list(map(float, line.split())))
    
    for x, y, w, h in labels:
        x *= iw
        y *= ih
        w *= iw
        h *= ih

        a = [x - w / 2, x + w / 2, x + w / 2, x - w / 2, x]
        b = [y + h / 2, y + h / 2, y - h / 2, y - h / 2, y]

        matplotlib.pyplot.scatter(
            x=a, y=b, s=10, c='red', marker='o', linewidths=-1
        )
    
    matplotlib.pyplot.imshow(image)
    matplotlib.pyplot.show()


def reformat_labels(label_path: str) -> None:
    with open(label_path, 'r') as file:
        lines = file.readlines()
    
    if lines == '':
        return
    
    lines = [line[2:] + '\n' for line in lines]

    result = ''

    for line in lines:
        result = result + '0 ' + line
    
    with open('resources/result_1.txt', 'a') as result_file:
        result_file.write(result)


def scan_label_files(folder_path: str) -> None:
    all_label_files = glob.glob(os.path.join(folder_path, '*.txt'))

    for file in all_label_files:
        reformat_labels(file)
        print(file)


image_path = 'resources/Dataset_2/train/images/2b_png.rf.bd386bc20daa5a421597aef4b1a14c22.jpg'
label_path = 'resources/Dataset_2/train/labels/2b_png.rf.bd386bc20daa5a421597aef4b1a14c22.txt'
#visualize(image_path=image_path, label_path=label_path)
scan_label_files('resources/Dataset_2/train/labels/')
