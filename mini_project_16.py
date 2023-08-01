# Mini Project 16
import cv2
import os

def resize_images(inputF, outputF, scale_perc=50):
    # Creating an output folder if the provided one does not exist
    if not os.path.exists(outputF):
        os.makedirs(outputF)

    # Getting file names of the images in the input folder:
    image_files = os.listdir(inputF)

    for image_file in image_files:
        input_path = os.path.join(inputF, image_file)
        output_path = os.path.join(outputF, image_file)
        # Reading the image
        image = cv2.imread(input_path)
        # Getting the image's dimensions
        height, width = image.shape[:2]

        # Calculating the new dimensions for resizing
        new_width = int(width * scale_perc / 100)
        new_height = int(height * scale_perc / 100)

        # Resizing the images
        resized_image = cv2.resize(image, (new_width, new_height))

        #Saving the resized images
        cv2.imwrite(output_path, resized_image)

    print("All the images of the input folder have been successfully resized!")

input_folder_path = 'D:\Coding\Python programmming\summer_school\images'
output_folder_path = 'Resized_folder'
resize_images(input_folder_path, output_folder_path, scale_perc=50)
