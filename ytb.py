from tkinter import*
import pytube
import os
import youtube_dl
def ex():
	quit()
def download():
  search_item = inp.get()
  ydl_opts = {'format': 'best','noplaylist':True,'extract-  audio':True,}
  path = "C:/Users/Home/Videos"
  os.chdir(path)
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([search_item])	
root=Tk()
root.resizable(width=False, height=False)
#root.wm_iconbitmap('icon.ico')
root.wm_title('SAM downloader')
lable = Label(root,text="welcome to youtube video downloader").grid(row=0,column=2,)
inp =Entry(root)
inp.grid(row=1,column=2)
button = Button(root,text="Download",command=download).grid(row=2,column=2)
button2 = Button(root,text="Exit",command=ex).grid(row=3,column=2)
lablew = Label(root,text="Your video will be saved in Videos of libary").grid(row=4,column=2,)
lablewe = Label(root,text="Made by samir thapa 0_0").grid(row=5,column=2,)
root.mainloop()