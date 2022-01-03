import glob
import os
import shutil

PATH_ROOT = "D:\\MRJOHN\\BHSITE\\data"
TYPE_LIST = ["sequence", "histone", "shape"]
CELL_TYPE = ["Gm12878", "H1hesc", "Helas3", "Hepg2", "K562"]

for index, item in enumerate(TYPE_LIST):
    for index_cell, item_cell in enumerate(CELL_TYPE):
        path = PATH_ROOT + "\\" + item + "\\" + item_cell + "\\*"
        path_tf = glob.glob(path)
        for index_tf, item_tf in enumerate(path_tf):
            # print(item_tf)
            tf = item_tf.split("\\")[-1].split(".")[0]
            # print("{}\\{}\\{}\\{}".format(PATH_ROOT, item_cell, tf, item))
            path_destination = "{}\\{}\\{}\\{}".format(PATH_ROOT, item_cell, tf, item)
            # print(path_destination)
            if not os.path.exists(path_destination):
                os.makedirs(path_destination)
            if item != "shape":
                shutil.copy(item_tf, path_destination)
            else:
                path_shape = glob.glob(item_tf + "\\*.data.*")
                # print(path_shape)
                for index_shape, item_shape in enumerate(path_shape):
                    shutil.copy(item_shape, path_destination)
                    # print(item_shape)