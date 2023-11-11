import tkinter
import customtkinter
from pytube import YouTube


def Start_Download():
    # try:
        finishlabel.configure(text="")
        YTLink=url_variable.get()
        if(len(YTLink)==0):
            finishlabel.configure(text="You have not given any url",text_color="red")
        else:
            YTObject = YouTube(YTLink,on_progress_callback=On_Progress)
            video = YTObject.streams.get_highest_resolution()
            title.configure(text=YTObject.title)
            video.download()
            finishlabel.configure(text="Download Complete",text_color="green")
            inputBox.delete(0, 'end')
            title.configure(text="Insert a Youtube link")

    # except:
    #     finishlabel.configure(text="Download Error",text_color="red")
def On_Progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size-bytes_remaining
    Percentage_of_Completion=bytes_downloaded/total_size*100
    percentage = str(int(Percentage_of_Completion))
    pPercentage.configure(text=percentage+'%')
    pPercentage.update()
    ProgressBar.set(float(Percentage_of_Completion/100))
    if(Percentage_of_Completion<33):
        ProgressBar.configure(progress_color="red")
    elif(Percentage_of_Completion>=33 and Percentage_of_Completion<66):
        ProgressBar.configure(progress_color="yellow")
    else:
        ProgressBar.configure(progress_color="green")
#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our App Frame
app=customtkinter.CTk()
app.geometry("720x480")
app.title("YTvidoff")

#Adding UI elements
#image

#title label
title=customtkinter.CTkLabel(app,text="Insert a Youtube link")
title.pack(padx=10, pady=10)

#input text box
url_variable = tkinter.StringVar()
inputBox=customtkinter.CTkEntry(app,width=350,height=50,textvariable=url_variable)
inputBox.pack()

#Download button
download=customtkinter.CTkButton(app,text="Download", command=Start_Download)
download.pack(padx=10,pady=20)

#Finished downloading
finishlabel=customtkinter.CTkLabel(app,text="")
finishlabel.pack(padx=10,pady=20)

#Progress bar and percentage of completion
pPercentage=customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

ProgressBar=customtkinter.CTkProgressBar(app,width=400)
ProgressBar.set(0)
ProgressBar.pack(padx=10,pady=20)

#Run app
app.mainloop()