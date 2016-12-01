import xgboost as xgb
dtrain = xgb.DMatrix('car.txt.train')
dvalid = xgb.DMatrix('car.txt.valid')
dtest = xgb.DMatrix('car.txt.test')
param = {'max_depth': 4,
         'eta': 0.1,
         'gamma': 1.0,
         'min_child_weight': 10,
         'save_period': 0,
         'booster': 'gbtree',
         #'min_child_weight':1,
         #for logistics regression if data imblance
         #'max_delta_step':0
         'subsample':0.8,
         'colsample_bytree':0.6,
         #'colsample_bylevel':1,
         # A value greater than 0 can be used in case of high class imbalance as it helps in faster convergence.
         #'scale_pos_weight':0,
         #L2 regression, in case of overfitting
         #'lambda':0,
         #L1 regression, when many properties
         #'alpha':0,
         #L2 regression of bias
         #'lambda_bias':0,
         #the result of prediction
         #'name_pred':pred.txt
         'objective': 'reg:linear'}
num_round = 200
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
bst = xgb.train(param, dtrain, num_round, watchlist)
# preds = bst.predict(dtest)
# preds = bst.predict(dvalid)
# write_pred('pred.txt', preds)
bst.dump_model('dump.nice.txt', 'featmap.txt')

