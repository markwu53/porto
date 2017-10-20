import xgboost as xgb
import numpy as np
import scipy.sparse
import pickle

train_file = "/Programs/git/zillow/agaricus.txt.train"
test_file = "/Programs/git/zillow/agaricus.txt.test"
dtrain = xgb.DMatrix(train_file)
dtest = xgb.DMatrix(test_file)

# specify parameters via map, definition are same as c++ version
param = {'max_depth':8, 'eta':.1, 'silent':1, 'objective':'binary:logistic' }

# specify validations set to watch performance
watchlist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 2
bst = xgb.train(param, dtrain, num_round, watchlist)

# this is prediction
preds = bst.predict(dtest)
labels = dtest.get_label()
print ('error=%f' % ( sum(1 for i in range(len(preds)) if int(preds[i]>0.5)!=labels[i]) /float(len(preds))))
bst.save_model('0001.model')
# dump model
bst.dump_model('dump.raw.txt')
# dump model with feature map
#bst.dump_model('dump.nice.txt','featmap.txt')

# save dmatrix into binary buffer
dtest.save_binary('dtest.buffer')
# save model
bst.save_model('xgb.model')
# load model and data in
bst2 = xgb.Booster(model_file='xgb.model')
dtest2 = xgb.DMatrix('dtest.buffer')
preds2 = bst2.predict(dtest2)
# assert they are the same
