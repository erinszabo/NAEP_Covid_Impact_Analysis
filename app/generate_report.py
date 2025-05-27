from analyze_survey import analyze
from create_visuals import visuals

#### function calls ####

# when project is complete, the only function call 
# should be gen_doc()
########################

def gen_doc():
    """ generate the markdown document that will display findings """
    d = analyze()
    visuals(d)
    
    
   # v1, v2, v3 = visuals() # assuming 3 visuals are created
   
   # as the doc is built, use v1-v3 to reference image paths where needed
    
    

############# helper functions below #################

gen_doc()

