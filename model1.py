import pyttsx3
import pdfplumber
import PyPDF2
import os

def pdf2audio(file ):
    #Creating a PDF File Object
    pdfFileObj = open(file, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #Get the number of pages
    pages = pdfReader.numPages

    with pdfplumber.open(file) as pdf:
    #Loop through the number of pages
        for i in range(0, pages): 
            page = pdf.pages[i]
            text = page.extract_text()
            print(len(text))
    
            words = text.split(' ')[:5]
            sentence = ' '.join(words)
            print(sentence)

            speaker = pyttsx3.init()
            speaker.say(sentence)
            speaker.runAndWait()


def pdf_list_func():
    # program run using list 
    for i in os.listdir('/Users/nisshhh7/Audiobook with python/):
        file = os.path.join('/Users/nisshhh7/Audiobook with python/,i)
        pdf2audio(file)
        break


def pdf_tuple_func():
    # program run using tuple 
    pdf_tuple = ("book-10.pdf", "book-11.pdf", "./bo","book-13.pdf","book-14.pdf")

    for i in pdf_tuple:
        pdf2audio(i)
        break


def pdf_dict_func():
    # program run using dictionary 
    pdf_dict = {
        'pdf1':'book-10.pdf',
        'pdf2':'book-11.pdf',
        'pdf3':'./bo',
    } 

    for i in pdf_dict:
        print(pdf_dict[i])
        pdf2audio(pdf_dict[i])
        break


def pdf_set_func():
    # program run using set
    pdf_set = {'book-10.pdf', 'book-11.pdf', './bo'} 

    for i in pdf_set:
        print(i)
        try :
            pdf2audio(i)
        except:
            pass

        break


# Defining main function
def main():

    # a = pdf_list_func()
    # b = pdf_tuple_func()
    # c = pdf_dict_func()
    # d = pdf_set_func()

    pdfs_list = ['list_func','tuple_func','dict_func','set_func']

    input_val = str(input())

    while(1):
        if input_val in pdfs_list:
            if 'list_func'==input_val:
                pdf_list_func()
                break
            else:
                break
        else:
            break


if __name__=="__main__":
    main()


files = [f for f in os.listdir('/Users/nisshhh7/Audiobook with python/) if os.path.isfile(f) and f.endswith('.pdf')]
pdf2audio(file)
print(files)