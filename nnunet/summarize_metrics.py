'''
run python nnunet/evaluation/model_selection/summarize_results_in_one_json.py -t 1 -f 0 -m 2d
'''

from batchgenerators.utilities.file_and_folder_operations import *


file_name = '/home/umii/mo000007/data/nnUNet_trained_models/nnUNet/summary_jsons_new/Task001_Fatchecker__2d__original_trained__validation_raw__0.json'
# file2 = 'Task001_Fatchecker__2d__original_trained__validation_raw_postprocessed__0.json'
# '/home/umii/mo000007/data/results/Task001_Fatchecker' + 'fold_0'
test_folder = '/home/umii/mo000007/data/results/Task001_Fatchecker/fold_0'
reference_folder = '/home/umii/mo000007/data/nnUNet_raw_data_base/nnUNet_raw_data/Task001_Fatchecker/labelsTs'

jfile = load_json(file_name)

# jfile['results']['mean']['0']
# jfile['results']['mean']['1']
# jfile['results']['mean']['mean']

# ['Accuracy', 'Dice', 'False Discovery Rate', 
# 'False Negative Rate', 'False Omission Rate', 
# 'False Positive Rate', 'Jaccard', 'Negative Predictive Value', 
# 'Precision', 'Recall', 'Total Positives Reference', 'Total Positives Test', 'True Negative Rate'])