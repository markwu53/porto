import numpy as np
import matplotlib.pyplot as plt

path = "/Users/apple/Documents/Programs/kaggle/porto/"
path = "/Users/T162880/Documents/Programs/kaggle/porto/"
path = "/Users/Public/Documents/Kaggle/porto/"
train_file = "train.csv"
columns = "id,target,ps_ind_01,ps_ind_02_cat,ps_ind_03,ps_ind_04_cat,ps_ind_05_cat,ps_ind_06_bin,ps_ind_07_bin,ps_ind_08_bin,ps_ind_09_bin,ps_ind_10_bin,ps_ind_11_bin,ps_ind_12_bin,ps_ind_13_bin,ps_ind_14,ps_ind_15,ps_ind_16_bin,ps_ind_17_bin,ps_ind_18_bin,ps_reg_01,ps_reg_02,ps_reg_03,ps_car_01_cat,ps_car_02_cat,ps_car_03_cat,ps_car_04_cat,ps_car_05_cat,ps_car_06_cat,ps_car_07_cat,ps_car_08_cat,ps_car_09_cat,ps_car_10_cat,ps_car_11_cat,ps_car_11,ps_car_12,ps_car_13,ps_car_14,ps_car_15,ps_calc_01,ps_calc_02,ps_calc_03,ps_calc_04,ps_calc_05,ps_calc_06,ps_calc_07,ps_calc_08,ps_calc_09,ps_calc_10,ps_calc_11,ps_calc_12,ps_calc_13,ps_calc_14,ps_calc_15_bin,ps_calc_16_bin,ps_calc_17_bin,ps_calc_18_bin,ps_calc_19_bin,ps_calc_20_bin"
columns = columns.split(",")
len(columns)
"""
id,
target,
ps_ind_01, cat-0-8
ps_ind_02_cat, cat-1-4-n
ps_ind_03, cat-0-12
ps_ind_04_cat, cat-0-1-n
ps_ind_05_cat, cat-0-7-n
ps_ind_06_bin, cat-0-1
ps_ind_07_bin, cat-0-1
ps_ind_08_bin, cat-0-1
ps_ind_09_bin, cat-0-1
ps_ind_10_bin, cat-0-1
ps_ind_11_bin, cat-0-1-all0
ps_ind_12_bin, cat-0-1-all0
ps_ind_13_bin, cat-0-1-all0
ps_ind_14, cat-0-4-all0
ps_ind_15, cat-0-14
ps_ind_16_bin, cat-0-1
ps_ind_17_bin, cat-0-1
ps_ind_18_bin, cat-0-1
ps_reg_01, float-0-1
ps_reg_02, float-0-2
ps_reg_03, float-0-5-n
ps_car_01_cat, cat-0-12-n
ps_car_02_cat, cat-0-1-n
ps_car_03_cat, cat-0-1-nnn
ps_car_04_cat, cat-0-10
ps_car_05_cat, cat-0-1-nn
ps_car_06_cat, cat-0-18
ps_car_07_cat, cat-0-1-n
ps_car_08_cat, cat-0-1
ps_car_09_cat, cat-0-4
ps_car_10_cat, cat-0-2
ps_car_11_cat, cat-0-120
ps_car_11, cat-0-3-n
ps_car_12, float-0-1-n
ps_car_13, float-0-2
ps_car_14, float-0-1-n
ps_car_15, float-0-4
ps_calc_01, float-0-1
ps_calc_02, float-0-1
ps_calc_03, float-0-1
ps_calc_04, cat-0-5
ps_calc_05, cat-0-6
ps_calc_06, int-0-10
ps_calc_07, int-0-10
ps_calc_08, int-0-12
ps_calc_09, int-0-8
ps_calc_10, int-0-25
ps_calc_11, int-0-20
ps_calc_12, int-0-10
ps_calc_13, int-0-14
ps_calc_14, int-0-25
ps_calc_15_bin, int-0-1
ps_calc_16_bin, int-0-1
ps_calc_17_bin, int-0-1
ps_calc_18_bin, int-0-1
ps_calc_19_bin, int-0-1
ps_calc_20_bin,  int-0-1
"""

values = []
with open(path+train_file) as fd:
    fd.readline()
    while True:
        line = fd.readline()
        if not line: break
        fields = line.strip().split(",")
        values.append(fields)

label = np.array([ int(value[1]) for value in values ])
ind = np.array(range(len(label)))
ones = ind[label[ind] == 1]
ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)
def co(n):
    field = np.array([float(value[2+n]) for value in values])
    field1 = field[ones]
    ax1.cla()
    ax2.cla()
    ax1.hist(field)
    ax2.hist(field1)

ind = np.array([2,20,22,23,32,33,42,44,46,47,48,50])
"""
2,20,22,23,32,33,42*,44*,46*,47*,48*,50*
"""

def f(n):
    print([value[n] for value in values[:10]])
    plt.hist([float(value[n]) for value in values])

a = [ value for value in values if value < 0.1]
b = [ value for value in values if value > 0.9]
c = [ value for value in values if value >= 0.1 and value <= 0.9 ]
a0 = [ value for value in values if value == 0.0 ]
b0 = [ value for value in values if value == 1.0 ]
