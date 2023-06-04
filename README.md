# png-bmp-Lossless-Compressor
A new lossless compressor for png and bmp images

First version of the PNG / BMP Lossless compressor, it can compress images in the png or bmp format of more than 24 bits between 15 and 40% of its original size.

The algorithm changes the order of the bytes (RGB values) so that it is easier for the paq8 compressor to compress the image.

Error found: when decompressing it generates the same image but in 32 bits, making it a bit different in size compared to its original size, but at the same quality.

Run with Python.
     
contact: https://twitter.com/missingus3r
