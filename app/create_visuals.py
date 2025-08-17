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
        
        most_sig(subject, sf_path)
        # #### below is just a test example
        # sf = pd.read_csv(sf_path)
        # fname = "output/"+str(key)+"_visual_ex.csv"
        # sf.to_csv(fname, index=False)
        ####


def most_sig(subject, sf_path):
    # look at the questions with a pval 0.0 (too small to detect)
    
    # Load and filter the data
    df = pd.read_csv(sf_path)
    df_sig = df[df['pval'] == 0.0]
    
    # Remove columns 'pval' and 'significant'
    df_sig = df_sig.drop(columns=['pval', 'significant'])

    # Plot for each unique question
    i = 1 # to keep track of the figure number
    for question in df_sig['Question'].unique():
        sub = df_sig[df_sig['Question'] == question]
        x_labels = (sub['CategoryL_low'] + ' vs ' + sub['CategoryL_high']).apply(lambda s: str(s).replace('\r', '').replace('\n', ''))
        x = range(len(sub))
        width = 0.35
        
        q_str = qs_from_highlights(question)
        
        # Create a bar plot
        plt.figure(figsize=(8, 5))
        plt.bar(x, sub['PercentA_low'], width=width, label='PercentA_low')
        plt.bar([xi + width for xi in x], sub['PercentA_high'], width=width, label='PercentA_high')
        plt.xticks([xi + width/2 for xi in x], x_labels, rotation=45)
        plt.yticks([0, 25, 50, 75, 100], ['0%', '25%', '50%', '75%', '100%'])
        plt.title(question.strip('" ').replace('\r', '').replace('\n', ''))
        plt.ylabel('Percent')
        plt.tight_layout()
        plt.legend()
        plt.savefig(f"output/visuals/{q_str}_{subject}_ms_{i}.png")
        plt.close()
        i += 1
    return 

def qs_from_highlights(q):
    # check if the q matches one of the highlighted qs,
    #  if so, return the substring that should be added to the file name
    #  if not, return an empty string
    q = q.strip()
    
    highlighted_qs = {
        # resources
        'Remote: Access to high-speed internet': 'internet',
        'Remote: desktop; laptop or tablet': 'device',
        'Remote: A quiet place to work': 'quiet',
        "Remote: teacher available to help w/ lang arts": 'teacher',
        "Remote: teacher available to help w/ math": 'teacher',
        # student specific
        "Remote math: Recognize when don't understand": 'recognize',
        'Remote math: Ask for help when you need it': 'ask',
        "Remote E/LA: Recognize when don't understand": 'recognize',
        "Remote E/LA: Ask for help when you need it": 'ask',
        "How difficult or easy was it to learn remotely": 'difficulty',
        # note: math_by_sig does not have "Lot Diff"/difficulty pair because the
        #   average score for that pair is the almost same as the overall average,
        #   so it is not considered an answer from "high" or "low" performing students
        "Remote E/LA: Find resource online if dont underst":'find'
        
    }

    sub_string = ""
    
    # check if q is similar to any highlighted questions
    for key in highlighted_qs.keys():
        if key in q:
            sub_string = highlighted_qs[key]
        
    return sub_string
