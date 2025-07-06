from analyze_survey import analyze
from create_visuals import visuals

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import Frame
from reportlab.lib.units import inch


########### Driver Function #############

def gen_doc():
    """ generate the pdf document that will display findings """
    analyzed = analyze()
    figures = visuals(analyzed) # probably a list or dictionary of visuals
    
    doc, width, height = start_pdf()
    
    x_pos = 20 # starting bottom left x position
    y_pos = .2 # starting bottom left y position  
    
    # # test add paragraph
    # y_pos = add_paragraph (doc, TEST, x_pos, y_pos)
    # y_pos = add_paragraph (doc, "TEST words words words", x_pos, y_pos)
    # y_pos = add_paragraph (doc, "hbo;jknjpip7oftykcgvjhbkniy7pfotykcghvjbknhi;yfutdkxfchgvjbkhiogu;yfldturkxfhg j.vkblhioug;yfltyfhg.jvbkhogu;iyfutlcgjhkbjoug;yfitulfhgj.hkbjug;iyfutlc", x_pos, y_pos)
    # y_pos = add_paragraph (doc, str(width)+"  "+str(height)+"    hbo;knhi;yfutdkxfchgvjbkhiogu;yfldturkxfhg j.vkblhioug;yfltyfhg.jvbkhogu;iyfutlcgjhkbjoug;yfitulfhgj.hkbjug;iyfutlc", x_pos, y_pos)
    
    
    
    # finally, save the document as a pdf
    doc.save()
    
    return

############ String Constants ################
INTRO = "" # write my introduction paragraph here
CONCLUSION = "" 

TEST = " Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

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

def add_paragraph(doc, text, x, y, width=7.5*inch, height=10*inch):
    """ Add a paragraph to the doc

    Args:
        doc (canvas): the doc the paragraph is to be added to
        text (str): the text to be added
        x (float): the horizontal distance from the left of the page
        y (float): the vertical distance from the bottom of the page
        width (float): the width of the text block (in points or inches)
        height (float): the height of the text block (in points or inches)

    Returns:
        new_y (float): the new vertical distance from the bottom of the page for next item
    """
    
    # set paragraph style
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Helvetica"
    style.fontSize = 11
    style.leading = 15  # line spacing

    # create paragraph and frame
    paragraph = Paragraph(text, style)
    frame = Frame(x, y, width, height, showBoundary=0) # height does not seem to need dependence on text length

    # wrap paragraph in a frame and draw it
    frame.addFromList([paragraph], doc)
    
    # for every 95 chars (ceiling), I want a new line plus one gap line  (let a line be 14)
    space = 14 * -(-len(text)//95) + 14
    
    new_y = y - space  # update vertical position for next addition to doc
    
    return new_y
    
    



def list_top_sig_questions():
    # 
    pass

def insert_image(image_path):
    pass



###############################

gen_doc()
