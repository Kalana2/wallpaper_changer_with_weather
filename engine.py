from collections.abc import Callable
from multiprocessing import Process
import os
import subprocess
import time

class Engine(Process):
    def __init__(self, images):
        super().__init__()
        self.images = images

    def run(self):
        image = self.images.get()

        while True:

            # os.system(f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/snake/Projects/whether app/images/{image}")
            url = image
            url = f"/home/snake/Projects/whether\ app{image[1:]}"
            print(url)
            

            self.__set_wallpaper(url)

            print("Set Wallpaper to ", image)
            time.sleep(10)
            image = self.images.get()


    def __set_wallpaper(self,image_path):
        try:
            subprocess.run([
                "gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{image_path}"
            ], check=True)
            print("Wallpaper set successfully.")
        except subprocess.CalledProcessError as e:
            print("Failed to set wallpaper:", e)
