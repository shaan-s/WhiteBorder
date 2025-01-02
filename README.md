# Introduction
This is an image processing script that adds white borders to an image of any size, conforming it to a square shape. I use this for instagram posts due to their aspect ratio restrictions. This script is a fork of [TwoPhotosOnA6x4](https://github.com/shaan-s/TwoPhotosOnA6x4) and was created in December 2024.

# Usage
At least 1 image should be dragged onto the script's file. It will then create the image(s) in the same directory and display them. For example,

Source image:
![image](https://github.com/user-attachments/assets/4536f80e-6659-4977-a47d-13398e651e3c)

Output:
![1735856689_0](https://github.com/user-attachments/assets/a381b2ca-5e5b-4496-94b3-8e20475d8d4b)


# Configuration

The image's final resolution can be adjusted by editing the script's variables. On line 9,

```
finalw=1200 
finalh=1200
margin=finalw//15
```

The final width and height can be modified. The margin is dependent on the width (e.g. `margin=finalw//30` would produce a slimmer margin).

# Installation

This script uses Pillow, (PIL) which must be installed first:

`python3 -m pip install --upgrade Pillow`

`git clone https://github.com/shaan-s/WhiteBorder`

Then drag images onto the script.
