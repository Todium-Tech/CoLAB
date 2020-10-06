import ctypes

SPI_WALLPAPER = 0x14
SPIF_UPDATINGFILE = 0x2 # To Upadte The File Instantly 

sourc = r"C:\Users\Belgin\Desktop\Python Coding\wallpaper.jpg"

ctypes.windll.user32.SystemParametersInfoW(SPI_WALLPAPER,0,sourc,SPIF_UPDATINGFILE)