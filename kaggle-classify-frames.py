#!/usr/bin/env python3

from classify_dataset import evaluate
from dataset_utilities import get_datasets

# make sure to provide correct paths to the folders on your machine
data_dir = '/kaggle/working/dataset/dataset_sm/frames/trainval'
test_data_dir = '/kaggle/working/dataset/dataset_sm/frames/test'

train_ds, val_ds, test_ds, weights_dict = get_datasets(data_dir, test_data_dir)

evaluate("kaggle-single-frame", train_ds, val_ds, test_ds, weights_dict)
