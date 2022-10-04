from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import tkinter
from tkinter import filedialog
import os

# myFont = ImageFont.truetype('None', 65)
fle = tkinter.filedialog.askopenfilenames(filetypes=[('', '*')],initialdir = "{PWD}") 

for i in fle:
  input_image = Image.open(str(i))
  output_image = ImageDraw.Draw(input_image)
  output_image.text((3115 ,440),"hogehogehogehogehoge", fill=(0, 0, 0),)
  input_image.save("new_" + os.path.basename(i) )