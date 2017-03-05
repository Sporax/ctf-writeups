# Fair and Square

This file was provided for the challenge, along with a description of someone having no clue what to do with it. The file seems to contain pixel data, so I tried converting it into an image:

```$ python3
> from PIL import Image
> file = open('fair-and-square.txt').read()
> pixels = tuple(eval(file))

Now that the pixels have been read, I needed to decide a file length, so I checked all possible lengths:
> lengths = [x for x in range(1, len(pixels)) if not len(pixels) % x]
> lengths = [(x, len(pixels) // x) for x in lengths]
> print(lengths)
# 
As the title of the challenge suggests, the image is probably a square. So the dimensions are probably 216x216:
> image = Image.new('RGB', (216, 216))
> image.putdata(pixels)
> image.save("result.png")

This is the result:

Unfortunately, I got stumped at this point, but after the challenge ended someone told me it looks like piet. I used this piet interpreter

And this is the flag
