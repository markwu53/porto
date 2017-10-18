import numpy as np
import matplotlib.pyplot as plt

path = "/Users/T162880/Documents/Programs/kaggle/porto/"
train_file = "train.csv"
columns = "id,target,ps_ind_01,ps_ind_02_cat,ps_ind_03,ps_ind_04_cat,ps_ind_05_cat,ps_ind_06_bin,ps_ind_07_bin,ps_ind_08_bin,ps_ind_09_bin,ps_ind_10_bin,ps_ind_11_bin,ps_ind_12_bin,ps_ind_13_bin,ps_ind_14,ps_ind_15,ps_ind_16_bin,ps_ind_17_bin,ps_ind_18_bin,ps_reg_01,ps_reg_02,ps_reg_03,ps_car_01_cat,ps_car_02_cat,ps_car_03_cat,ps_car_04_cat,ps_car_05_cat,ps_car_06_cat,ps_car_07_cat,ps_car_08_cat,ps_car_09_cat,ps_car_10_cat,ps_car_11_cat,ps_car_11,ps_car_12,ps_car_13,ps_car_14,ps_car_15,ps_calc_01,ps_calc_02,ps_calc_03,ps_calc_04,ps_calc_05,ps_calc_06,ps_calc_07,ps_calc_08,ps_calc_09,ps_calc_10,ps_calc_11,ps_calc_12,ps_calc_13,ps_calc_14,ps_calc_15_bin,ps_calc_16_bin,ps_calc_17_bin,ps_calc_18_bin,ps_calc_19_bin,ps_calc_20_bin"

values = []
with open(path+train_file) as fd:
    fd.readline()
    while True:
        line = fd.readline()
        if not line: break
        fields = line.strip().split(",")
        values.append(fields[1])

values = [ float(value) for value in values ]
plt.hist(values)

a = [ value for value in values if value < 0.1]
b = [ value for value in values if value > 0.9]
c = [ value for value in values if value >= 0.1 and value <= 0.9 ]
a0 = [ value for value in values if value == 0.0 ]
b0 = [ value for value in values if value == 1.0 ]
