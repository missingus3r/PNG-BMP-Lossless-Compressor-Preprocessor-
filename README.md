# png-bmp-Lossless-Compressor
A new lossless compressor for png and bmp images

First version of the PNG / BMP Lossless compressor, written entirely in powershell, it can compress images in the png or bmp format of more than 24 bits between 15 and 40% of its original size.

The algorithm changes the order of the bytes (RGB values) so that it is easier for the paq8 compressor to compress the image.

The only error it has is that when decompressing it generates the same image but in 32 bits, making it a bit bigger in size compared to its original size.

Use: Edit in PowerShell ISE or any text editor
     input for compression: c image.png
     input for decompression: d image.png.paq8l
     
