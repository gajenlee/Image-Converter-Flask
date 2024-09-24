from PIL import Image
import os

class ImageConverter():

    file_path = "./"
    
    def __init__(self, file_path, convert_type):
        self.file_path = file_path
        self.convert_type = convert_type
    
    def convert(self):
        filename = self.file_path + "Image_file_converter.com." + self.convert_type.lower()
        try:
            with Image.open(self.file_path) as img:
                img.convert("RGB").save(filename, format=self.convert_type)
                print(f"file converted: {filename}")
        except Exception as e:
            print(e)
        return filename