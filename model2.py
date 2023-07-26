import pyttsx3
import pdfplumber
import PyPDF2
import os


def pdf2audio(file):
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
    for i in os.listdir('/Users/nisshhh7/Desktop/Audiobook with python'):
        file = os.path.join('./bo',i)
        pdf2audio(file)
        break


def pdf_tuple_func():
    # program run using tuple 
    pdf_tuple = ("./bobook-10.pdf", "./bobook-11.pdf", "./bobook-12.pdf","./bobook-13.pdf","./bobook-14.pdf")

    for i in pdf_tuple:
        pdf2audio(i)
        break


def runone_pdf(filename):
    folder_path = "./bobook-10.pdf"
    fullpath = os.path.join(folder_path, filename)
    print(fullpath)


# 2 public self attributes in User defined class
class pdf2audioClass_pub:
    # Creating a constructor
    def __init__(self):
        self.pdf1 = str(input())
        self.pdf2 = str(input())
        # These are public attributes

    # Creating a function
    def printstate(self):
        printstat = 'Convert pdf to audio using two public attribute'
        if self.pdf1=='list_func':
            pdf_list_func()

        elif self.pdf2=='tuple_func':
            pdf_tuple_func()

        return printstat


# 2 private self attributes in User defined class
class Music:
    # constructor
    def __init__(self):
        # These are private variables
        self.__pdf1 = "list_func"
        self.__pdf2 = "tuple_func"
    # private function
    def __func(self):
        print('Convert pdf to audio using ')
    def foo(self):
        # Accessing private members of the class
        obj.__func()
        print("pdf1:", obj.__pdf1)
        print("pdf2:", obj.__pdf2)


# 1 private and 1 public method that take arguments
class pdf2audio_arg:
    filename = ''

    def __init__(self, n):
        self.name = n

    # # public function 
    # def printstate(self):
    #     file = self.name
    #     return file
    #     # print("This is the file we're using : ",file)

    # private function
    def __func(self):
        print('Convert pdf to audio using ')

    def priv_foo(self):
        # Accessing private members of the class
        pdf2audio_fun.__func()
        # Accessing public members of the class
        # print("run pdf to audio : ", )

    # Creating a function
    def pub_foo(self):
        printstat = f'This is the file we are using {self.name}'
        print(printstat)


def pdf2audio_repr():
    file_array = []
    for i in os.listdir('./bo'):
        file = os.path.join('./bo',i)
        file_array.append(file)

    # create a printable representation of the list
    printable_numbers = repr(file_array)
    print(printable_numbers)
    print(file_array)


# 1 private and 1 public method that take arguments, return values and are used by your program
pdf2audio_fun = pdf2audio_arg("book-10.pdf")
pdf2audio_fun.priv_foo()
pdf2audio_fun.pub_foo()


# Object creation and used 2 private self attributes
obj = Music()  # Creating an object of the Music class
obj.foo()  # calling the private function



# 2 public self attributes in User defined class
# Creating object of the class
m = pdf2audioClass_pub()
# Accessing the members inside the class
print("printstate: ", m.printstate())
print("pdf1 :", m.pdf1)
print("pdf2 :", m.pdf2)


# # used repr function in python
# pdf2audio_repr()
