import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
import zipfile

path = "/Users/T162880/Documents/Programs/kaggle/porto/"
path = "/Users/apple/Documents/Programs/kaggle/porto/"
path = "/Users/Public/Documents/Kaggle/porto/"
train_file = "train.csv"
test_file = "test.csv"
columns = "id,target,ps_ind_01,ps_ind_02_cat,ps_ind_03,ps_ind_04_cat,ps_ind_05_cat,ps_ind_06_bin,ps_ind_07_bin,ps_ind_08_bin,ps_ind_09_bin,ps_ind_10_bin,ps_ind_11_bin,ps_ind_12_bin,ps_ind_13_bin,ps_ind_14,ps_ind_15,ps_ind_16_bin,ps_ind_17_bin,ps_ind_18_bin,ps_reg_01,ps_reg_02,ps_reg_03,ps_car_01_cat,ps_car_02_cat,ps_car_03_cat,ps_car_04_cat,ps_car_05_cat,ps_car_06_cat,ps_car_07_cat,ps_car_08_cat,ps_car_09_cat,ps_car_10_cat,ps_car_11_cat,ps_car_11,ps_car_12,ps_car_13,ps_car_14,ps_car_15,ps_calc_01,ps_calc_02,ps_calc_03,ps_calc_04,ps_calc_05,ps_calc_06,ps_calc_07,ps_calc_08,ps_calc_09,ps_calc_10,ps_calc_11,ps_calc_12,ps_calc_13,ps_calc_14,ps_calc_15_bin,ps_calc_16_bin,ps_calc_17_bin,ps_calc_18_bin,ps_calc_19_bin,ps_calc_20_bin"
columns = columns.split(",")
my_submission = "my_submission.csv"

ind = np.array([2,20,22,23,32,33,42,44,46,47,48,50])
values = []
labels = []
with open(path+train_file) as fd:
    fd.readline()
    while True:
        line = fd.readline()
        if not line: break
        fields = line.strip().split(",")
        values.append(np.array([float(item) for item in fields[2:]])[ind])
        labels.append(float(fields[1]))


train_data = values[:450000]
train_labels = labels[:450000]
test_data = values[450000:]
test_labels = labels[450000:]

dtrain =xgb.DMatrix(np.array(train_data), label=np.array(train_labels))
dtest =xgb.DMatrix(np.array(test_data), label=np.array(test_labels))

param = {
    "max_depth": 3,
    "eta": .03,
    "silent": 1,
    "objective": "binary:logistic",
}

# specify validations set to watch performance
watchlist  = [(dtest, " eval"), (dtrain, " train")]
#watchlist  = [(dtrain,'train')]
num_round = 200
bst = xgb.train(param, dtrain, num_round, watchlist)

#preds = bst.predict(dtest)
#labels = dtest.get_label()

ids = []
batch = []
ncount = 0
with open(path+test_file) as fd, open(path+my_submission, "w") as fdw:
    fd.readline()
    fdw.write("{}\n".format("id,target"))
    while True:
        line = fd.readline()
        if not line: break
        ncount += 1
        if ncount % 100000 == 0:
            dbatch =xgb.DMatrix(np.array(batch))
            bpreds = bst.predict(dbatch)
            for item in zip(ids, bpreds):
                fdw.write("{},{:.5f}\n".format(*item))
            print(ncount)
            ids = []
            batch = []
        fields = line.strip().split(",")
        ids.append(fields[0])
        batch.append(np.array([float(item) for item in fields[1:]])[ind])
    dbatch =xgb.DMatrix(np.array(batch))
    bpreds = bst.predict(dbatch)
    for item in zip(ids, bpreds):
        fdw.write("{},{:.5f}\n".format(*item))

def zipit():
    with zipfile.ZipFile(path+my_submission+".zip", "w", compression=zipfile.ZIP_DEFLATED) as fd:
        fd.write(path+my_submission)

