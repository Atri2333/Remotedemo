import os

def createlabel(root_dir, label):
    img_dir = os.path.join(root_dir,label+"_image")
    label_dir = os.path.join(root_dir,label+"_label")
    img_list = os.listdir(img_dir)
    for i in img_list:
        file_name = i.split('.')[0]
        with open(os.path.join(label_dir,f"{file_name}.txt"),'w') as f:
            f.write(label)

root_dir = r"hymenoptera_data/train"
createlabel(root_dir,"ants")
createlabel(root_dir,"bees")