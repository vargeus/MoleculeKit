"""
Configuration file
"""



conf = {}
######################################################################################################################
# Settings for data io
## Note that we need to convert original data (SMILES) to Pytorch Geometric data object before we run main.py
##    'dataset' is the dataset name
##    'split' is the split methods: 'random', 'stratified' or 'scaffold'
##    'split_ratio' is used for the ratio of split: e.g. [0.8, 0.1, 0.1] means we split 80% of data as training, 10% as valid and the remaining 10% as test
##    'seed' is used as the random seed for random split.
######################################################################################################################
conf['split'] = 'random'
conf['split_ratio'] = [0.8,0.1,0.1]
conf['seed'] = 122




######################################################################################################################
# Settings for experimental setup
##    'model' chooses model from 'ml2' and 'ml3': ml2 is the proposed hierachical message passing model; ml3 is the model without subgraph-level representations, compared to ml2.
##    'task_type': 'regression' or 'classification'.
##    'metric' is the evaluation method: 'mae', 'rmse', 'prc', 'roc'
##    'num_tasks' denotes how many tasks we have in choosed dataset.
##    'graph_level_feature': if it is true, we combine the 200-d feature extracted by rkdit with the representation output by network together, and the use the combined representation to do property prediction.
######################################################################################################################
conf['model'] = 'ml2'
conf['task_type'] = 'regression'
conf['metric'] = 'rmse'
conf['num_tasks'] = 1
conf['graph_level_feature'] = True



######################################################################################################################
# Settings for training
##    'epochs': maximum training epochs
##    'early_stopping': patience used to stop training
##    'lr': starting learning rate
##    'lr_decay_factor': learning rate decay factor
##    'lr_decay_step_size': step size of learning rate decay 
##    'dropout': dropout rate
##    'weight_decay': l2 regularizer term
##    'depth': number of layers
##    'batch_size': training batch_size
######################################################################################################################
conf['epochs'] = 400
conf['early_stopping'] = 200
conf['lr'] = 0.001
conf['lr_decay_factor'] = 0.8
conf['lr_decay_step_size'] = 50
conf['dropout'] = 0
conf['weight_decay'] = 0
conf['depth'] = 3
conf['hidden'] =128
conf['batch_size'] = 32


######################################################################################################################
# Settings for val/test
##    'vt_batch_size': val/test batch_size
######################################################################################################################
conf['vt_batch_size'] = 1000