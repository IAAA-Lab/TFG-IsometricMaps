import sys
from PIL import Image

images = list(map(Image.open, ['./3.png', './4.png']))
widths, heights = zip(*(i.size for i in images))

max_width = max(widths)
total_height = sum(heights)
#total_width = sum(widths)
#max_height = max(heights)

#new_im = Image.new('RGB', (max_width, total_height))
#new_im = Image.new('RGB', (total_width, max_height))

new_im = Image.new('RGB', (max_width, total_height))
#new_im = Image.new('RGB', (max_width, total_height - 670))
#new_im = Image.new('RGB', (total_width - 285, max_height))

# General de arriba a abajo

#y_offset = 0
#x_offset = 0
#for im in images:
  #new_im.paste(im, (0, y_offset))
  #y_offset += im.size[1] - 10
  #new_im.paste(im, (x_offset, 0))
  #x_offset += im.size[0]

# Manual (abajo a arriba)

y_offset = images[0].size[1]
new_im.paste(images[1], (0, y_offset))
#new_im.paste(images[1], (0, y_offset - 670))
new_im.paste(images[0], (0, 0))

# Manual (izquierda a derecha)

#x_offset = images[0].size[0]
#new_im.paste(images[0], (0, 0))
#new_im.paste(images[1], (x_offset - 285, 0))

new_im.save('./final.png')
