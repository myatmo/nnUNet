import SimpleITK as sitk

FILENAME = '../../data/nnUNet_raw_data_base/nnUNet_raw_data/Task001_Fatchecker/imagesTr/56400444.jpg'
print(sitk.GetArrayFromImage(sitk.ReadImage(FILENAME)).shape)