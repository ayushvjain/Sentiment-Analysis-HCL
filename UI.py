import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import audio_to_text as att 
import Project as Project 

LARGEFONT =("Verdana", 35)
tp  = ""
text_of_audio = ""
class tkinterApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", expand = True)

        container.grid_rowconfigure(0, weight = 2)
        container.grid_columnconfigure(0, weight = 2)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Sentiment_Analysis, Page1, Page2, Page4, Page5, Page6, Page7):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(Sentiment_Analysis)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
# First Window Sentiment Analysis Screen
class Sentiment_Analysis(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # label of frame Layout 2
        label = ttk.Label(self, text ="Sentiment Analysis      ", font = LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Text",
        command = lambda : controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Audio",
        command = lambda : controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
#Second Window For Text
class Page1(tk.Frame):
    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Text", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        label1 = ttk.Label(self, text ="Enter Your Text")
        
        # putting the button in its place
        # by using grid
        label1.grid(row = 1, column = 1, padx = 10, pady = 10)

        T = Text(self, height = 1, width = 52)
        T.grid(row = 1, column = 2, padx = 10, pady = 10)

        tp = T
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Get Analysis",
                            command = lambda : define(parent,controller,T))
    
        # putting the button in its place by
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        #button to show frame1 with sentiment analysis
        button3 = ttk.Button(self, text = "Home",
                            command = lambda : controller.show_frame(Sentiment_Analysis))
        
        button3.grid(row = 3, column = 1, padx = 10, pady=10)


def define(parent,controller,T):
    tp = Project.imp_data(T.get("1.0", "end-1c"))[0]
    ttt = Page3(parent, controller,tp)
    app.frames[Page3] = ttt
    ttt.grid(row = 0, column = 0, sticky ="nsew")
    controller.show_frame(Page3)

#Third Window for Audio
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Audio", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Record",
                            command = lambda : controller.show_frame(Page4))
    
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Upload File",
                            command = lambda : controller.show_frame(Page5))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text = "Home",
                            command = lambda : controller.show_frame(Sentiment_Analysis))
        
        button3.grid(row = 3, column = 1, padx = 10, pady=10)
#Fourth Window for getting the output
class Page3(tk.Frame):
    def __init__(self, parent, controller,w):
        print(w)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Analysis", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text = "Home",
                            command = lambda : controller.show_frame(Sentiment_Analysis))
        
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        label2 = ttk.Label(self, text = "Your Sentence is",)
        label2.grid(row = 1, column = 1, padx = 10, pady=10)
        label3 = ttk.Label(self, text = w)
        label3.grid(row = 1, column = 2, padx = 10, pady=10)
    

#Fifth Window for record Audio Screen
class Page4(tk.Frame):
    record_a = ""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.variable_r = None
        label = ttk.Label(self, text = "Record Audio", font = LARGEFONT)
        label.grid(row=0, column = 4, padx = 10, pady=10)
        
        button1 = ttk.Button(self, text = "Click to Record",
                            command = self.start_audio)
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
    
        button2 = ttk.Button(self, text = "Stop Record",
                            command = self.stop_audio)
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)   
                     
        button3 = ttk.Button(self, text = "Get Text format",
                            command = lambda : controller.show_frame(Page7))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
                     
        button4 = ttk.Button(self, text = "Get Analysis",
                            command = lambda : controller.show_frame(Page3))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        button5 = ttk.Button(self, text = "Home",
                            command = lambda : controller.show_frame(Sentiment_Analysis))
        button5.grid(row = 5, column = 1, padx = 10, pady = 10)
    
    def start_audio(self):
        self.variable_r,self.audio = att.record_audio()

    def stop_audio(self):
        self.record_a = att.print_audio(self.variable_r,self.audio)
        text_of_audio = record_a
        print(record_a)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Upload Audio", font = LARGEFONT)
        label.grid(row=0, column = 4, padx = 10, pady=10)
        
        button1 = ttk.Button(self, text = "Home",
                            command = lambda : controller.show_frame(Sentiment_Analysis))
        button1.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        button2 = ttk.Button(self, text = "Click to Upload",
                             command = self.open_file)
        button2.grid(row = 1, column = 1, padx =10, pady=10)
        
        button3 = ttk.Button(self, text = "Get text format",
                            command = lambda : controller.show_frame(Page6))
        button3.grid(row = 2, column = 1, padx =10, pady=10)
        
        button4 = ttk.Button(self, text = "Get Analysis",
                            command = lambda : controller.show_frame(Page3))
        button4.grid(row = 3, column = 1, padx = 10, pady = 10)
                    
    def open_file(self):
        file = askopenfile(mode ='r', filetypes =[('Audio Files', '*.wav'),('Audio Files', '*.mp3')])
        if file is not None:
            content = file.read()
            print(content)

#Senveth Window for Getting audio in text format
class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Record Audio", font = LARGEFONT)
        label.grid(row=0, column = 4, padx = 10, pady=10)
        
        button1 = ttk.Button(self, text ="Get Analysis",
                            command = lambda : controller.show_frame(Page3))
    
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)

#Eight Window for Text format of audio
class Page7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        p1 = controller.frames[Page4]
        label = ttk.Label(self, text = "Record Audio", font = LARGEFONT)
        label.grid(row=0, column = 4, padx = 10, pady=10)
        
        label = ttk.Label(self, text = p1.record_a)
        label.grid(row=1, column = 1, padx = 10, pady=10)

        button1 = ttk.Button(self, text ="Get Analysis",
                            command = lambda : controller.show_frame(Page3))
    
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)

# Driver Code
app = tkinterApp()
app.mainloop()
