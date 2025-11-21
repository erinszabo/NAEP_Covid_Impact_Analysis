import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from analyze_survey import analyze

############### Functions ###############

# create separate functions to look at separate things.
# each image I end up with should have its own function 
#   that is then called inside of visuals



######## Driver Function #################

def visuals(data_frames):
    """ use information from analysis to create images describing the findings
    returns: a tuple of strings, paths of the generated images"""

    for key, value in data_frames:
        subject = key
        question_dfs = value  # subject question data frames
        i = 1 # to keep track of the figure number
        for question in question_dfs:
            create_bar_graph(question_dfs[question], subject, i)
            i += 1


######### OLD ##########
   # for key, value in subject_path_dict.items():
   #     subject = key
   #     sf_path = value # subject file path
   #     
   #     
   #     most_sig(subject, sf_path)
        
        # #### below is just a test example
        # sf = pd.read_csv(sf_path)
        # fname = "output/"+str(key)+"_visual_ex.csv"
        # sf.to_csv(fname, index=False)
        ####
###########################################

def create_bar_graph(data, subject, i):
    if subject == "math":
        avg = 235 # average score for all students in math
    else:
        avg = 215 # average score for all students in reading
    
    # Scale percents into reasonable widths
    scale = 0.1
    widths = data["Percent"] * scale 

    # Compute left edges so bars don’t overlap
    left_edges = np.cumsum([0] + list(widths[:-1]))

    # Use a nice color palette
    colors = sns.color_palette("Set3", len(data)) # Spectral, mako, viridis

    fig, ax = plt.subplots(figsize=(9,6))

    ## Draw bars
    #for left, width, score, ans, pct, color in zip(left_edges, widths, data["Score"], data["Answer"], data["Percent"], colors):
    #    ax.bar(left, score, width=width, color=color, edgecolor="black", align="edge")
    #    ax.text(left + width/2, score + 1, f"{ans}\n{score}\n{pct}%", 
    #            ha="center", va="bottom", fontsize=9, weight="bold")

    # Draw bars
    for left, width, score, ans, pct, color in zip(left_edges, widths, data["Score"], data["Answer"], data["Percent"], colors):
        ax.bar(left, score, width=width, color=color, edgecolor="black", align="edge")        
        # Label only the answer (bigger and bold)
        ax.text(left + width/2, score + 2, ans, ha="center", va="bottom", fontsize=12, weight="bold")
        # Label percent INSIDE bar, near bottom
        ax.text(left + width/2, 182, f"{pct}%", ha="center", va="center", fontsize=12)
        #ax.text(left + width/2, score/2, f"{pct}%", ha="center", va="center", fontsize=11, weight="bold", color="black")


    # Reference line at average score for the subject
    ax.axhline(avg, linestyle="--", color="gray", label="Average Score of All Students")


    ax.set_ylabel("Average Score by Answer")
    ax.set_title(data["Question"].iloc[0], fontsize=14) 

    # Start y at 180
    ax.set_ylim(180, avg+20) 

    # Remove default x-ticks (since x is now cumulative percent widths)
    ax.set_xticks([])
    ax.set_xlabel("Student Response")
 
    #ax.set_xticklabels(data["Answer"])
    ax.legend()

    #plt.show()
    plt.savefig(f"output/visuals/{subject}_question_{i}.png")
    plt.close()


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
