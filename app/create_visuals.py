from analyze_survey import analyze

############### Functions ###############

# create separate functions to look at separate things.
# each image I end up with should have its own function 
#   that is then called inside of visuals


######## Driver Function #################

def visuals():
    """ use information from analysis to create images describing the findings
    returns: a tuple of strings, paths of the generated images"""
    analyze()
    

######## Calls: Remove when ready ###########

visuals()
