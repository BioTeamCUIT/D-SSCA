import pandas as pd
import os
import glob
import math
import csv
import numpy as np
from tqdm import tqdm

ROOT_PATH = 'D:\MRJOHN\BHSITE\data'
TYPE_LIST = ["sequence", "histone", "shape"]
CELL_TYPE = ["Gm12878", "H1hesc", "Helas3", "Hepg2", "K562"]
RATIO_TRAIN = 0.8
seq_len = 201

# progress_bar = tqdm(CELL_TYPE)
for index_cell, item_cell in enumerate(CELL_TYPE):
    path_tf = glob.glob(ROOT_PATH + "\\" + item_cell + "\\*")
    progress_bar = tqdm(path_tf)
    for index_tf, item_tf in enumerate(progress_bar):
        tf_name = item_tf.split("\\")[-1]
        progress_bar.set_description("Processing {}/{}".format(item_cell, tf_name))
        for index_type, item_type in enumerate(TYPE_LIST):
            path_type = item_tf + "\\" + item_type
            if item_type == "sequence":
                data = pd.read_csv(path_type + "\\" + tf_name + ".csv", header=None)
                data_train = data.iloc[0:math.ceil(data.shape[0] * RATIO_TRAIN), :]
                data_test = data.iloc[math.ceil(data.shape[0] * RATIO_TRAIN):, :]
                data_train.to_csv(path_type + "\\" + "Train_" + item_type[0:3] + ".csv", index=False, header=False)
                data_test.to_csv(path_type + "\\" + "Test_" + item_type[0:3] + ".csv", index=False, header=False)
                # print(data_train.shape, data_test.shape)
            # if item_type == "histone":
            #     data = pd.read_csv(path_type + "\\" + tf_name + ".csv", header=None, keep_default_na=True, names=np.arange(1, 22, 1))
            #     start = data.shape[0]/9
            #     start = math.ceil(start * 0.8) * 9
            #     data_train = data.iloc[0:start, :]
            #     data_test = data.iloc[start:, :]
            #     data_train.to_csv(path_type + "\\" + "Train_" + item_type[0:3] + ".csv", index=False, header=False)
            #     data_test.to_csv(path_type + "\\" + "Test_" + item_type[0:3] + ".csv", index=False, header=False)
            # if item_type == "shape":
            #     path = glob.glob(path_type + "\\*.data.*")
            #     for index_shape, item_shape in enumerate(path):
            #         # print(item_shape)
            #         shape_name = item_shape.split('.')[-1]
            #         i_file = open(item_shape)
            #         # o_file = csv.writer(open(path_type + "\\" + shape_name + '.csv', 'w', newline=''))
            #         """
            #             write header
            #         """
            #         all_row = []
            #         row = []
            #         for i in range(seq_len):
            #             row.append(i + 1)
            #
            #         for line in i_file.readlines():
            #             """
            #                 文件格式:
            #                     >1
            #                     NA,NA,4.96,.......,4.92,NA,NA
            #             """
            #             line = line.replace('\n', '')
            #             if line[0] == '>':
            #                 all_row.append(row)
            #                 row = []
            #             else:
            #                 line = line.split(',')
            #                 for char in line:
            #                     if char == 'NA':
            #                         row.append(float(0))
            #                     else:
            #                         row.append(float(char))
            #         all_row.append(row)
            #         data = pd.DataFrame(all_row)
            #         shape_train = data.iloc[0:math.ceil((data.shape[0]-1) * RATIO_TRAIN), :]
            #         shape_test = data.iloc[math.ceil((data.shape[0]-1) * RATIO_TRAIN):, :]
            #         # print(shape_test.shape)
            #         shape_test = np.row_stack((np.arange(1, 202, 1), shape_test))
            #         shape_test = pd.DataFrame(shape_test)
            #         shape_train.to_csv(path_type + "\\" + "Train_" + shape_name + ".csv", index=False, header=False)
            #         shape_test.to_csv(path_type + "\\" + "Test_" + shape_name + ".csv", index=False, header=False)
            #         i_file.close()
    #                 break
    #     break
    # break

