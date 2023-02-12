import numpy as np
from matplotlib import pyplot as plt
import math

def show_multiple_images(img_num, row, col, im_list, fig_row, fig_col):
    plt.rcParams["figure.figsize"] = [fig_row, fig_col]
    #plt.rcParams["figure.autolayout"] = True
    im_idx = 0
    for i in range(1, row+1):
        for j in range(1, col+1):
            if im_idx == img_num:
                break
            # print(i, j)
            layout_idx = im_idx + 1
            # print("layout_idx: ", layout_idx)
            plt.subplot(row, col, layout_idx)
            plt.imshow(im_list[im_idx])
            im_idx = im_idx + 1
    plt.show()
    
    return None

