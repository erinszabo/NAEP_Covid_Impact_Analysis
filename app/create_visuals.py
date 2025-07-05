import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from analyze_survey import analyze

############### Functions ###############

# create separate functions to look at separate things.
# each image I end up with should have its own function 
#   that is then called inside of visuals



######## Driver Function #################

def visuals(subject_path_dict):
    """ use information from analysis to create images describing the findings
    returns: a tuple of strings, paths of the generated images"""
    
    for key, value in subject_path_dict.items():
        subject = key
        sf_path = value # subject file path
        
        # #### below is just a test example
        # sf = pd.read_csv(sf_path)
        # fname = "output/"+str(key)+"_visual_ex.csv"
        # sf.to_csv(fname, index=False)
        ####
        
        
def most_sig():
    # look at the questions with a pval 0.0 (too small to detect)
    pass
    
