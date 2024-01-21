
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from ttkbootstrap.style import Style
from tkinter import ttk



#Cfg janela
    
janela = Tk()
Style = Style(theme = 'superhero')
janela.title("𝕯𝖔𝖜𝖓𝖙𝖚𝖇𝖊")
janela.geometry('400x350')
janela.minsize(width=350,height=300)
janela.maxsize(width=450,height=400)
janela.resizable(width=False,height=False)


#função para msc ou video

def salvar():

    global filename
    filename = filedialog.askdirectory()
    mm = combo.get()
    arma = t2.get()


    if mm == '𝑀𝒫3':

     video = YouTube(arma)
     video.streams.get_audio_only().download(output_path=filename)
     print('sucesso')  

    if mm == '𝑀𝒫4-𝐻𝐼𝒢𝐻':

     video = YouTube(arma)
     video.streams.get_highest_resolution().download(output_path=filename)
     print('sucesso')    

    if mm == '𝑀𝒫4-𝐿𝒪𝒲 ':

     video = YouTube(arma)
     video.streams.get_lowest_resolution().download(output_path=filename)
     print('sucesso') 

def on_enter(e):
  t2.delete(0,'end')

def on_leave(e):
  n=t2.get()
  if n == '':
    t2.insert(0,'            𝒟𝑖𝑔𝑖𝑡𝑒 𝑜 𝑙𝑖𝑛𝑘       ')


#Entrada de dados 


t2 = Entry(janela,fg='black',border=1)
t2.insert(0,'            𝒟𝑖𝑔𝑖𝑡𝑒 𝑜 𝑙𝑖𝑛𝑘       ')
t2.bind('<FocusIn>',on_enter)
t2.bind('<FocusOut>',on_leave)
t2.place( width=150,height=30,y=90,x=130)



#botoes
 
b1 = Button(janela, text = '𝔇𝔬𝔴𝔫𝔩𝔬𝔞𝔡',command = salvar,width=20,height=2)
b1.place( width=150,height=30,y=170,x=130)

#selecionador entre msc ou video

combo = ttk.Combobox(janela,height=1,width=20)
combo['values']=( '𝑀𝒫3','𝑀𝒫4-𝐻𝐼𝒢𝐻','𝑀𝒫4-𝐿𝒪𝒲')
combo.place(width=150,height=30,y=130,x=130)


janela.mainloop()
