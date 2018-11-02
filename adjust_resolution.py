from functions.constants import *
import os

directory = os.fsencode(new_con_path)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    for [width, height] in new_resolution:
        resized_image = cv2.resize("data/convict/resolution_trans_images" + filename, (width, height)) 

    # 保存
    if not os.path.exists("data/convict/resolution_trans_images"):
        os.mkdir("data/convict/resolution_trans_images")
    
    img_src.astype(np.float64)
    cv2.imwrite("resolution_trans_images/" + str(i) + ".jpg" ,img) 