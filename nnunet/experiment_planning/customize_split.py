import os
import pandas as pd
from collections import OrderedDict
from batchgenerators.utilities.file_and_folder_operations import *


def get_file_id(filename):
    id = os.path.splitext( os.path.basename(filename))[0]
    return id


def do_split():
    df_dir = '/home/umii/mo000007/zooniverse/dataset/'
    save_dir = '/home/umii/mo000007/data/nnUNet_preprocessed/Task001_Fatchecker/splits_final.pkl'

    train_data = df_dir + 'train_df.pkl'
    val_data = df_dir + 'val_df.pkl'

    train_df = pd.read_pickle(train_data)
    val_df = pd.read_pickle(val_data)

    splits = OrderedDict()

    # get ids from file path and save it to splits with train and val columns
    splits['train'] = train_df['images'].apply(lambda row: get_file_id(row)).to_numpy()
    splits['val'] = val_df['images'].apply(lambda row: get_file_id(row)).to_numpy()

    # save splits as splits_final.pkls under nnUNet_preprocessed/Task001_Fatchecker folder
    save_pickle(splits, save_dir)

if __name__ == "__main__":
    do_split()