from analyze_survey import analyze
from create_visuals import visuals
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


########### Driver Function #############

def gen_doc():
    """ generate the pdf document that will display findings """
    analyzed = analyze()
    figures = visuals(analyzed) # probably a list or dictionary of visuals
    
    document, width, height = start_pdf()
    
    
    # finally, save the document as a pdf
    document.save()
    
    return

############ String Constants ################
INTRO = "" # write my introduction paragraph here
CONCLUSION = "" 

##############################################

############# Helper Functions #################

def start_pdf():
    # create the blank document to be edited with futue funtions
    #   give it a file name and a title, initial formatting only
    pdf_path = "output/analysis_report.pdf"
    title = "Analysis Report" # TODO: make this more descriptive, consistent with project name 
    
    # create the doc
    doc = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # add a title to the doc
    doc.setFont("Helvetica-Bold", 20)
    doc.drawString(50, height - 50, title)
    
    return doc, width, height

def add_paragraph():
    # add paragraph to doc
    pass

def list_top_sig_questions():
    # 
    pass

def insert_image(image_path):
    pass



###############################

gen_doc()
