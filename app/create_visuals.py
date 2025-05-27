from analyze_survey import analyze
import seaborn as sns
import matplotlib.pyplot as plt

############### Functions ###############

# create separate functions to look at separate things.
# each image I end up with should have its own function 
#   that is then called inside of visuals


######## Driver Function #################

def visuals():
    """ use information from analysis to create images describing the findings
    returns: a tuple of strings, paths of the generated images"""
    analyze() 
    # ^ At some point I need to decide if this should be here,
    # or if I should just call above "visuals" in generate_report.py 
    # either I continue with this 'chaining' method
    # or let gen report be a driver and import all
    

######## Calls: Remove when ready ###########

visuals()
