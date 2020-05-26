from PIL import Image
from pieces import pieces_types
from glob import glob
import random
import numpy as np

imgs = []
button = Image.open("imgs/button_48x48.png")

for img_filename in glob("imgs/in/*.jpg"):
    img = Image.open(img_filename)
    imgs.append(img)


for idd, piece in enumerate(pieces_types):
    layout = piece.layout

    w, h = layout.shape
    img_w, img_h = imgs[0].width, imgs[0].height

    dst = Image.new("RGBA", (img_w * w, img_h * h), color=(255,255,255, 0))

    number_of_fields = np.count_nonzero(layout == 1)
    buttons_left = piece.buttons

    indices = list(range(number_of_fields))
    random.shuffle(indices)

    indices_chosen = indices[:buttons_left]

    chosen_image = imgs[idd]

    for i in range(w):
        for j in range(h):
            if layout[i, j] == 1:
                idx = i+j*w

                dst_coords = (i*img_w, j*img_h)
                dst.paste(chosen_image, dst_coords)

                if idx in indices_chosen and buttons_left > 0:
                    new_button = button.rotate(random.randint(0, 90))

                    button_coords = (int(i*img_w+((img_w-new_button.width)/2)), int(j*img_h+((img_h-new_button.height)/2)))
                    dst.paste(new_button, button_coords, new_button)
                    buttons_left -= 1

    print(dst)
    dst.save(f"imgs/out/{piece.name}.png")
