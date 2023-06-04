from PIL import Image
import os
import subprocess
import math
from time import sleep 

source_file = "image.png" #name of the image
output_file = "same_image.png"

image = Image.open(source_file)
width, height = image.size
pixels = list(image.convert('RGB').getdata())
r_values = []
g_values = []
b_values = []

for r, g, b in pixels:
    r_values.append(r)
    g_values.append(g)
    b_values.append(b)

# Prepare compressed data file
compressed_data = bytes(r_values + g_values + b_values)
with open("x", 'wb') as f:
    f.write(compressed_data)

subprocess.run(f"cmd.exe /c .\paq8l\paq8l.exe -7 x", shell=True)  
os.remove("x")
rename_file = f"{width}-{height}-{source_file}"
os.rename("x.paq8l", f"{rename_file}.paq8l")

size = os.path.getsize(source_file)
sizex = os.path.getsize(f"{rename_file}.paq8l")
percentage = 100 - math.ceil((sizex * 100) / size)
print(f"{size} bytes --> {sizex} bytes")
print(f"{percentage}% smaller!")

sleep(3)

# Decompression
subprocess.run(f"cmd.exe /c .\paq8l\paq8l.exe {rename_file}.paq8l", shell=True)

sleep(3)

with open("x", 'rb') as f:
    k = list(f.read())

r_values = k[:len(k) // 3]
g_values = k[len(k) // 3:2 * len(k) // 3]
b_values = k[2 * (len(k) // 3):]

bmp = Image.new("RGB", (width, height))
pixels = [(r_values[i], g_values[i], b_values[i]) for i in range(len(r_values))]
bmp.putdata(pixels)
bmp.save(output_file)
os.remove("x")
