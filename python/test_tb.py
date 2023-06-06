from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = r"hymenoptera_data/train/bees_image/16838648_415acd9e3f.jpg"
img_PIL = Image.open(image_path)
# img_PIL.show()
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("fuck", img_array, 1, dataformats="HWC")

writer.close()