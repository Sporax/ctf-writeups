# Fair and Square

This file was provided for the challenge, along with a description of someone having no clue what to do with it. The file seems to contain pixel data, so I tried converting it into an image:

    $ python3
    from PIL import Image
    file = open('fair-and-square.txt').read()
    pixels = tuple(eval(file))

Now that the pixels have been read, I needed to decide a file length, so I checked all possible lengths:

    lengths = [x for x in range(1, len(pixels)) if not len(pixels) % x]
    lengths = [(x, len(pixels) // x) for x in lengths]
    print(lengths)
    
    -> [(1, 46656), (2, 23328), (3, 15552), (4, 11664), (6, 7776), (8, 5832), (9, 5184), (12, 3888), (16, 2916), (18, 2592), (24, 1944), (27, 1728), (32, 1458), (36, 1296), (48, 972), (54, 864), (64, 729), (72, 648), (81, 576), (96, 486), (108, 432), (144, 324), (162, 288), (192, 243), (216, 216), (243, 192), (288, 162), (324, 144), (432, 108), (486, 96), (576, 81), (648, 72), (729, 64), (864, 54), (972, 48), (1296, 36), (1458, 32), (1728, 27), (1944, 24), (2592, 18), (2916, 16), (3888, 12), (5184, 9), (5832, 8), (7776, 6), (11664, 4), (15552, 3), (23328, 2)]

As the title of the challenge suggests, the image should be a square. So the dimensions are probably 216x216:

    image = Image.new('RGB', (216, 216))
    image.putdata(pixels)
    image.save("result.png")

This is the result:

![](https://github.com/Sporax/ctf-writeups/blob/master/xiomara-2017/result.png)

Unfortunately, I got stumped at this point, but after the challenge ended someone told me it looks like piet. I used this piet interpreter: http://www.bertnase.de/npiet/npiet-execute.php

Finally, the output is:

    Tried hard?  :O
    I'll give you a clue NOW  :D
    PIL and Piet  :P
    Haha! You know that already. Is'nt it?  -_-
    Here's what you want:
    Xiomara{piLet}
    Enjoy!

Flag: Xiomara{piLet}
