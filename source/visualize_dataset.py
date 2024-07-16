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
    '''
        Reformat a label file to fit input format of model YOLO_v8.

        Args:
            label_path (str): path to a label file.
        
        Returns:
            None
    '''

    with open(label_path, 'r') as file:
        lines = file.readlines()
    
    if lines == '':
        return
    
    lines = [line[2:] + '\n' for line in lines]

    result = ''

    for line in lines:
        result = result + '0 ' + line
    
    with open(label_path, 'w') as result_file:
        result_file.write(result[:-1])


def scan_label_files(folder_path: str) -> None:
    '''
        Reformat all label files in a folder.

        Args:
            folder_path (str): path to a folder.
        
        Returns:
            None
    '''

    all_label_files = glob.glob(os.path.join(folder_path, '*.txt'))

    for file in all_label_files:
        reformat_labels(file)
        print(file)


scan_label_files('resources/Dataset/train/labels/')
scan_label_files('resources/Dataset/test/labels/')
scan_label_files('resources/Dataset/valid/labels/')