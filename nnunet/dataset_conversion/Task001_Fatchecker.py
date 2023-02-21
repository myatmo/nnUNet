import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *
from nnunet.dataset_conversion.utils import generate_dataset_json
from nnunet.paths import nnUNet_raw_data, preprocessing_output_dir
from nnunet.utilities.file_conversions import convert_2d_image_to_nifti
import os

if __name__ == '__main__':
    """
    Working with 2D data in nnU-Net requires a small workaround in the creation of the dataset. Essentially, all images 
    must be converted to pseudo 3D images (so an image with shape (X, Y) needs to be converted to an image with shape 
    (1, X, Y). The resulting image must be saved in nifti format. Hereby it is important to set the spacing of the 
    first axis (the one with shape 1) to a value larger than the others. If you are working with niftis anyways, then 
    doing this should be easy for you. This example here is intended for demonstrating how nnU-Net can be used with 
    'regular' 2D images. We selected the massachusetts road segmentation dataset for this because it can be obtained 
    easily, it comes with a good amount of training cases but is still not too large to be difficult to handle.
    """

    base = '../../data/temp_data/'
    # this folder should have the training and testing subfolders

    # now start the conversion to nnU-Net:
    task_name = 'Task001_Fatchecker'
    target_base = join(nnUNet_raw_data, task_name)
    target_imagesTr = join(target_base, "imagesTr")
    target_imagesTs = join(target_base, "imagesTs")
    target_labelsTs = join(target_base, "labelsTs")
    target_labelsTr = join(target_base, "labelsTr")

    maybe_mkdir_p(target_imagesTr)
    maybe_mkdir_p(target_labelsTs)
    maybe_mkdir_p(target_imagesTs)
    maybe_mkdir_p(target_labelsTr)

    # convert the training examples. Not all training images have labels, so we just take the cases for which there are
    # labels
    images_dir_tr = join(base, 'imagesTr')
    labels_dir_tr = join(base, 'labelsTr')
    training_cases = subfiles(labels_dir_tr, suffix='.png', join=False)
    for t in training_cases:
        print("Converting file ", t)
        imgt = t.replace('.png', '.jpg')
        unique_name = t[:-4]  # just the filename with the extension cropped away, so img-2.png becomes img-2 as unique_name
        input_image_file = join(images_dir_tr, imgt)
        input_segmentation_file = join(labels_dir_tr, t)

        output_image_file = join(target_imagesTr, unique_name)  # do not specify a file ending! This will be done for you
        output_seg_file = join(target_labelsTr, unique_name)  # do not specify a file ending! This will be done for you

        # this utility will convert 2d images that can be read by skimage.io.imread to nifti. You don't need to do anything.
        # if this throws an error for your images, please just look at the code for this function and adapt it to your needs
        if not os.path.exists(output_image_file + "_0000.nii.gz"):
            convert_2d_image_to_nifti(input_image_file, output_image_file, is_seg=False)
            print("Done.")

        # the labels are stored as 0: background, 1: lipid.
        if not os.path.exists(output_seg_file + ".nii.gz"):
            convert_2d_image_to_nifti(input_segmentation_file, output_seg_file, is_seg=True)
            print("Done.")

    # now do the same for the test set
    images_dir_ts = join(base, 'imagesTs')
    labels_dir_ts = join(base, 'labelsTs')
    testing_cases = subfiles(labels_dir_ts, suffix='.png', join=False)
    for ts in testing_cases:
        print("Converting file ", ts)
        imgts = ts.replace('.png', '.jpg')
        unique_name = ts[:-4]
        input_image_file = join(images_dir_ts, imgts)
        input_segmentation_file = join(labels_dir_ts, ts)

        output_image_file = join(target_imagesTs, unique_name)
        output_seg_file = join(target_labelsTs, unique_name)

        if not os.path.exists(output_image_file + "_0000.nii.gz"):
            convert_2d_image_to_nifti(input_image_file, output_image_file, is_seg=False)
            print("Done.")

        if not os.path.exists(output_seg_file + ".nii.gz"):
            convert_2d_image_to_nifti(input_segmentation_file, output_seg_file, is_seg=True)
            print("Done.")

    # finally we can call the utility for generating a dataset.json
    generate_dataset_json(join(target_base, 'dataset.json'), target_imagesTr, target_imagesTs, ('Red', 'Green', 'Blue'),
                          labels={0: 'background', 1: 'lipid'}, dataset_name=task_name, license='umn.edu')

    """
    once this is completed, you can use the dataset like any other nnU-Net dataset. Note that since this is a 2D
    dataset there is no need to run preprocessing for 3D U-Nets. You should therefore run the 
    `nnUNet_plan_and_preprocess` command like this:
    
    > nnUNet_plan_and_preprocess -t 120 -pl3d None
    
    once that is completed, you can run the trainings as follows:
    > nnUNet_train 2d nnUNetTrainerV2 120 FOLD
    
    (where fold is again 0, 1, 2, 3 and 4 - 5-fold cross validation)
    
    there is no need to run nnUNet_find_best_configuration because there is only one model to choose from.
    Note that without running nnUNet_find_best_configuration, nnU-Net will not have determined a postprocessing
    for the whole cross-validation. Spoiler: it will determine not to run postprocessing anyways. If you are using
    a different 2D dataset, you can make nnU-Net determine the postprocessing by using the
    `nnUNet_determine_postprocessing` command
    """
