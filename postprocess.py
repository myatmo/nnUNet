import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *
from nnunet.paths import nnUNet_raw_data
from nnunet.utilities.file_conversions import convert_2d_segmentation_nifti_to_img
import os

if __name__ == '__main__':
    base = '../../data/results/'
    task_name = 'Task001_Fatchecker'
    target_base = join(base, task_name)
    target_imagesTr = join(target_base, "fold_0")
    target_imagesTs = join(target_base, "imagesTs")

    maybe_mkdir_p(target_imagesTr)
    maybe_mkdir_p(target_labelsTs)

    images_dir_tr = join(base, 'imagesTr')
    labels_dir_tr = join(base, 'labelsTr')
    nifti_file = ''
    output_filename = ''
    test_files = subfiles(nifti_file, suffix='.nii.gz', join=False)
    convert_2d_segmentation_nifti_to_img(nifti_file, output_filename,
                                        transform=lambda x: (x == 255).astype(int))
    