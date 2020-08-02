#imports
from Models import Depression_detection
from pathlib import Path
import pandas as pd

# get th parent path
base_path = Path.cwd().parent
training_positive_path = base_path.joinpath('./2017/train/positive_examples_anonymous_chunks')
training_negative_path = base_path.joinpath('./2017/train/negative_examples_anonymous_chunks')
test_path = base_path.joinpath('./2017/test')

Dd = Depression_detection(base_path,
                          training_positive_path,
                          training_negative_path,
                          test_path)

#Concatenate all the frames for each folder after parsing them
training_positive_dateframe = pd.concat(Dd.parse_folder(training_positive_path))
training_negative_dataframe = pd.concat(Dd.parse_folder(training_negative_path))
test_dataframe = pd.concat(Dd.parse_folder(test_path))

#add labels to positive and negative subjects
training_positive_dateframe['LABEL'] = 1
training_negative_dataframe['LABEL'] = 0

#save them to csv file
training_positive_dateframe.to_csv('training_positive_dateframe.csv')
training_negative_dataframe.to_csv('training_negative_dataframe.csv')

