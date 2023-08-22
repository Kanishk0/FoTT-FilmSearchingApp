from tkinter import *
from tkinter import messagebox,filedialog
from PIL import ImageTk
from PIL import Image
from colorama import Fore, Back, Style
import tkinter.font as font
import pickle
import webbrowser



def A2019():
    img=Image.open("ASURAN.JPG")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("PETTA.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("VISWASAM.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    
    img3=Image.open("Kaithi.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("BIGIL.JPG")
    img4=img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("NGK.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("NKP.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("SP.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("HERO.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("MRL.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("GO.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("THADAM.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("KOLAIGARAN.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("NVP.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)

    img14=Image.open("THAMBI.JPG")
    img14 = img14.resize((200, 100), Image.ANTIALIAS)
    img14 = ImageTk.PhotoImage(img14)

    img15=Image.open("NT.JPG")
    img15 = img15.resize((200, 100), Image.ANTIALIAS)
    img15 = ImageTk.PhotoImage(img15)

    img16=Image.open("K3.JPG")
    img16 = img16.resize((200, 100), Image.ANTIALIAS)
    img16= ImageTk.PhotoImage(img16)

    img17=Image.open("KAAPAAN.JPG")
    img17= img17.resize((200, 100), Image.ANTIALIAS)
    img17 = ImageTk.PhotoImage(img17)

    img18=Image.open("DEV.JPG")
    img18 = img18.resize((200, 100), Image.ANTIALIAS)
    img18 = ImageTk.PhotoImage(img18)

    img19=Image.open("ENPT.JPG")
    img19 = img19.resize((200, 100), Image.ANTIALIAS)
    img19 = ImageTk.PhotoImage(img19)

    img20=Image.open("PPK.JPG")
    img20 = img20.resize((200, 100), Image.ANTIALIAS)
    img20= ImageTk.PhotoImage(img20)

    


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)
   
    pett=Button(smain,image=img1,command=petta)
    vis=Button(smain,image=img2,command=viswasam)
    VV=Button(smain,image=img17,command=vrv)
    Asura=Button(smain,image=img,command=asuran)
    Kaith=Button(smain,image=img3,command=kaithi)
    Kaith.pack()
    Asura.pack()
    pett.pack()
    vis.pack()
    VV.pack()
    BIGIL=Button(smain,image=img4,command=bigil)
    BIGIL.pack()
    NGK=Button(smain,image=img5,command=ngk)
    NGK.pack()
    NKP=Button(smain,image=img6,command=nkp)
    NKP.pack()
    SP=Button(smain,image=img7,command=superdeluxe)
    SP.pack()
    HERO=Button(smain,image=img8,command=hero)
    HERO.pack()
    MRL=Button(smain,image=img9,command=mrl)
    MRL.pack()
    GO=Button(smain,image=img10,command=gameover)
    GO.pack()
    THADAM=Button(smain,image=img11,command=thadam)
    THADAM.pack()
    KOLAIGARAN=Button(smain,image=img12,command=kolaigaran)
    KOLAIGARAN.pack()
    NVP=Button(smain,image=img13,command=nvp)
    NVP.pack()
    THAMBI=Button(smain,image=img14,command=thambi)
    THAMBI.pack()
    NT=Button(smain,image=img15,command=natpethunai)
    NT.pack()
    K3=Button(smain,image=img16,command=kanchana3)
    K3.pack()
    K5=Button(smain,image=img17,command=Kaapaan)
    K5.pack()
    K51=Button(smain,image=img18,command=Dev)
    K51.pack()
    K51A=Button(smain,image=img19,command=ENPT)
    K51A.pack()


    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    
    smain1.mainloop()





#2019
def petta():
    print("\t\t\tFilm Name:Petta")
    print("\t\t\tCast:Rajinikanth,Simran,Vijay Sethupathy")
    print("\t\t\tDirector:Karthik Suburaj")
    print("\t\t\tAvailable on:Netflix")
    print()

def viswasam():
    print("\t\t\tFilm Name:Viswasam")
    print("\t\t\tCast:Ajith Kumar,Nayanthara")
    print("\t\t\tDirector:Siva")
    print("\t\t\tAvailable on:Prime Video")
    print()

def bigil():
    print("\t\t\tFilm Name:Bigil")
    print("\t\t\tCast:Vijay,Nayanthara")
    print("\t\t\tDirector:Atlee")
    print("\t\t\tAvailable on:Prime Video")
    print()

def ngk():
    print("\t\t\tFilm Name:Ngk")
    print("\t\t\tCast:Surya,Sai Pallavi,Rakul Preet Singh")
    print("\t\t\tDirector:Selvaraghvan")
    print("\t\t\tAvailable on:Prime Video")
    print()

def nkp():
    print("\t\t\tFilm Name:Nerkonda Parvai")
    print("\t\t\tCast:Ajith Kumar,Adhik Ravichandaran,Shrddha Srinath")
    print("\t\t\tDirector:H.Vinoth")
    print("\t\t\tAvailable on:Zee5")
    print()

def vrv():
    print("\t\t\tFilm Name:Vantha Rajavathan Varuven")
    print("\t\t\tCast:STR,Megha Aakash")
    print("\t\t\tDirector:Sundar.C")
    print("\t\t\tAvailable on:Zee5")
    print()

def superdeluxe():
    print("\t\t\tFilm Name:Super Deluxe")
    print("\t\t\tCast:Vijay Sethupathy,Samantha,Fahad Fazil")
    print("\t\t\tDirector:Thyagaraja Kumaraja")
    print("\t\t\tAvailable on:Netflix")
    print()

def hero():
    print("\t\t\tFilm Name:Hero")
    print("\t\t\tCast:Sivakarthikeyan,Abhay Deol,Arjun")
    print("\t\t\tDirector:P.S.Mithran")
    print("\t\t\tAvailable on:Prime Video")
    print()

def mrl():
    print("\t\t\tFilm Name:MR.Local")
    print("\t\t\tCast:Sivakarthikeyan,Nayanthara,Sathish")
    print("\t\t\tDirector:Rajesh")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def kaithi():
    print("\t\t\tFilm Name:Kaithi")
    print("\t\t\tCast:Karthi,Arjun Doss")
    print("\t\t\tDirector:Lokesh Kanagaraj")
    print("\t\t\tAvailable on:Hotstar")
    print()

def gameover():
    print("\t\t\tFilm Name:Game Over")
    print("\t\t\tCast:Taapsee Pannu,Anish Kuruvilla")
    print("\t\t\tDirector:Ashwin Saravanan")
    print("\t\t\tAvailable on:Netflix")
    print()

def asuran():
    print("\t\t\tFilm Name:Asuran")
    print("\t\t\tCast:Dhanush,Teejay")
    print("\t\t\tDirector:Vetrimaaran")
    print("\t\t\tAvailable on:Prime Video")
    print()

def thadam():
    print("\t\t\tFilm Name:Thadam")
    print("\t\t\tCast:Arun Vijay,Tanya Hope")
    print("\t\t\tDirector:Magizh Thirumeni")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def kolaigaran():
    print("\t\t\tFilm Name:Kolaigaran")
    print("\t\t\tCast:Vijay Antony,Arjun,Nassar")
    print("\t\t\tDirector:Andrew Louis")
    print("\t\t\tAvailable on:Hotstar")
    print()

def thambi():
    print("\t\t\tFilm Name:Thambi")
    print("\t\t\tCast:Karthi,Jothika")
    print("\t\t\tDirector:Jeethu Joseph")
    print("\t\t\tAvailable on:Hotstar")
    print()

def kaappan():
    print("\t\t\tFilm Name:Kaappaan")
    print("\t\t\tCast:Surya,Sayyeshaa,Arya")
    print("\t\t\tDirector:K.V.Anand")
    print("\t\t\tAvailable on:Prime Video")
    print()

def nvp():
    print("\t\t\tFilm Name:Namma Veetu Pillai")
    print("\t\t\tCast:Sivakarthikeyan,Aishwarya Rajesh,Soori")
    print("\t\t\tDirector:Pandiaraj")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def natpethunai():
    print("\t\t\tFilm Name:Natpe Thunai")
    print("\t\t\tCast:Adhi,Anagha")
    print("\t\t\tDirector:Parthiban Desingu")
    print("\t\t\tAvailable on:Prime Video")
    print()

def kanchana3():
    print("\t\t\tFilm Name:Kanchana 3")
    print("\t\t\tCast:Raghava Lawrence,Oviya,Vedhika Kumar")
    print("\t\t\tDirector:Raghava Lawrence")
    print("\t\t\tAvailable on:Sunnxt")
    print()



def A2015():
    img=Image.open("OKK.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("VVV.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("RT.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    
    img3=Image.open("KK.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("MAARI.JPG")
    img4=img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("E10.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("INN.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("THOONGAVANAM.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("TM.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("ANEGAN.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("KS.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("NR.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("TO.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("K2.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)

    img14=Image.open("YA.JPG")
    img14 = img14.resize((200, 100), Image.ANTIALIAS)
    img14 = ImageTk.PhotoImage(img14)

    img15=Image.open("MASS.JPG")
    img15 = img15.resize((200, 100), Image.ANTIALIAS)
    img15=ImageTk.PhotoImage(img15)

    img16=Image.open("Asuran.ico")
    img16 = img16.resize((200, 100), Image.ANTIALIAS)
    img16 = ImageTk.PhotoImage(img16)

    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)


    '''smain=Toplevel()
    smain.title('FILM SEARCHING PLATFORM')
    smain.geometry('300x300')
    smain.configure(bg="black")
    scrol=Scrollbar(smain)
    scrol.pack(side = RIGHT,fill = Y)'''
    
    OKK=Button(smain,image=img,command=o_kadhal_kanmani)
    
    OKK.pack()
    VVV=Button(smain,image=img1,command=vai_raja_vai)
    
    VVV.pack()
    RT=Button(smain,image=img2,command=rajathandiram)
    RT.pack()
    KK=Button(smain,image=img3,command=kaakamuttai)
    KK.pack()
    MAARI=Button(smain,image=img4,command=Maari)
    MAARI.pack()
    E10=Button(smain,image=img5,command= E10_endrathukula)
    E10.pack()
    INN=Button(smain,image=img6,command=indru_netru_nalai)
    INN.pack()
    THOONGAVANAM=Button(smain,image=img7,command=thoogavanam)
    THOONGAVANAM.pack()
    TM=Button(smain,image=img8,command=Thangamagan)
    TM.pack()
    ANEGAN=Button(smain,image=img9,command=Anegan)
    ANEGAN.pack()
    KS=Button(smain,image=img10,command=Kaaki)
    KS.pack()
    NR=Button(smain,image=img11,command=Naanum)
    NR.pack()
    TO=Button(smain,image=img12,command=Thanioruvan)
    TO.pack()
    K2=Button(smain,image=img13,command=kanchana2)
    K2.pack()
    ya=Button(smain,image=img14,command=YA)
    ya.pack()
    ya1=Button(smain,image=img15,command=Mass)
    ya1.pack()
    
    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    
    

    smain1.mainloop()
    

#2015
def o_kadhal_kanmani():
    print("\t\t\tFilm Name:O kadhal kanmani")
    print("\t\t\tCast:Dulqar salmaan,Nithya menon")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Hotstar")
    print()

def kanchana2():
    print("\t\t\tFilm Name:Kanchana 2")
    print("\t\t\tCast:Raghava Lawrence,Taapsee Pannu,Nithya Menon")
    print("\t\t\tDirector:Raghava Lawrence")
    print("\t\t\tAvailable on:Sunnxt")
    print()
    


def vai_raja_vai():
    print("\t\t\tFilm Name:Vai Raja Vai")
    print("\t\t\tCast:Gautham Karthik")
    print("\t\t\tDirector:Aishwarya R.Dhanush")
    print("\t\t\tAvailable on:prime video")
    print()

def rajathandiram():
    print("\t\t\tFilm Name:Rajathandiram")
    print("\t\t\tCast:Regina cassandra,Darbuka siva,Veera bahu")
    print("\t\t\tDirector:A.G.Amid")
    print("\t\t\tAvailable on:Hotstar")
    print()

def kaakamuttai():
    print("\t\t\tFilm Name:Kaaka Muttai")
    print("\t\t\tCast:Aishwarya Rajesh,J.vignesh")
    print("\t\t\tDirector:M.Manikandan")
    print("\t\t\tAvailable on:Hotstar")
    print()


def indru_netru_nalai():
    print("\t\t\tFilm Name:Indru Netru Nalai")
    print("\t\t\tCast:Vishnu vishal,Arya,Miya")
    print("\t\t\tDirector:R.Ravi Kumar")
    print("\t\t\tAvailable on:Hotstar")
    print()



def Maari():
    print("\t\t\tFilm Name:Maari")
    print("\t\t\tCast:Dhanush,Kajal Agarwal")
    print("\t\t\tDirector:Balaji Mohan")
    print("\t\t\tAvailable on:Hotstar")
    print()


def E10_endrathukula():
    print("\t\t\tFilm Name:10 Endrathukula")
    print("\t\t\tCast:Chiyaan Vikram,Samantha")
    print("\t\t\tDirector:Vijay Milton")
    print("\t\t\tAvailable on:hotstar")
    print()


def thoogavanam():
    print("\t\t\tFilm Name:Thoongaavanam")
    print("\t\t\tCast:Kamal Haasan,Trisha Krishnan")
    print("\t\t\tDirector:Rajesh M.Selva")
    print("\t\t\tAvailable on:Hotstar")
    print()


def Anegan():
    print("\t\t\tFilm Name:Anegan")
    print("\t\t\tCast:Dhanush,Karthik,Amyra Dustar")
    print("\t\t\tDirector:KV Anand")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def Thangamagan():
    print("\t\t\tFilm Name:Thanga Magan")
    print("\t\t\tCast:Dhanush,Amy Jackson,Samantha,Sathish")
    print("\t\t\tDirector:Velraj")
    print("\t\t\tAvailable on:Sunnxt")
    print() 

def Kaaki():
    print("\t\t\tFilm Name:Kaaki Sattai")
    print("\t\t\tCast:SivaKathikeyan,Sridivya")
    print("\t\t\tDirector:Durai Senthilkumar")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def Naanum():
    print("\t\t\tFilm Name:Naanum RowdyDhaan")
    print("\t\t\tCast:Vijay Sethupathi,Nayantara,RJ Balaji")
    print("\t\t\tDirector:Vignesh Shivan")
    print("\t\t\tAvailable on:Sunnxt")
    print("")

def Thanioruvan():
    print("\t\t\tFilm Name:Thani Oruvan")
    print("\t\t\tCast:Jayam Ravi,Nayantara,Aravind Swami")
    print("\t\t\tDirector:Mohan Raja")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def A2016():
    img=Image.open("visaranai.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("PUGAZH.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("ZERO.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    
    img3=Image.open("THERI.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("MANITHAN.JPG")
    img4=img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("URIYADI.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("VEVV.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("AMMAK.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("KABALI.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("KIK.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("CHENNAI282.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("D16.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("KODI.PNG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("24.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)

    img14=Image.open("AYM.JPG")
    img14 = img14.resize((200, 100), Image.ANTIALIAS)
    img14 = ImageTk.PhotoImage(img14)

    img15=Image.open("RM.JPG")
    img15 = img15.resize((200, 100), Image.ANTIALIAS)
    img15=ImageTk.PhotoImage(img15)

    img16=Image.open("REMO.JPG")
    img16 = img16.resize((200, 100), Image.ANTIALIAS)
    img16 = ImageTk.PhotoImage(img16)

    img17=Image.open("KAASHMORA.JPG")
    img17= img17.resize((200, 100), Image.ANTIALIAS)
    img17 = ImageTk.PhotoImage(img17)

    img18=Image.open("THOZHA.JPG")
    img18 = img18.resize((200, 100), Image.ANTIALIAS)
    img18 = ImageTk.PhotoImage(img18)

    img19=Image.open("IRAIVI.JPG")
    img19 = img19.resize((200, 100), Image.ANTIALIAS)
    img19 = ImageTk.PhotoImage(img19)

    img20=Image.open("DD.JPG")
    img20 = img20.resize((200, 100), Image.ANTIALIAS)
    img20= ImageTk.PhotoImage(img20)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)
    
    
    Visaranai=Button(smain,image=img,command=visaranai)
    Visaranai.pack()
    PUGAZH=Button(smain,image=img1,command=Pugazh)
    PUGAZH.pack()
    ZERO=Button(smain,image=img2,command=zero)
    ZERO.pack()
    THERI=Button(smain,image=img3,command=Theri)
    THERI.pack()
    MANITHAN=Button(smain,image=img4,command=Manithan)
    MANITHAN.pack()
    URIYADI=Button(smain,image=img5,command=Uriyadi)
    URIYADI.pack()
    VEVV=Button(smain,image=img6,command=velainu_vanthuta_velakaran)
    VEVV.pack()
    AMMAK=Button(smain,image=img7,command=Amma_kanakku)
    AMMAK.pack()
    KABALI=Button(smain,image=img8,command=kabali)
    KABALI.pack()
    KIK=Button(smain,image=img9,command=kaduvul_irukan_kumaru)
    KIK.pack()
    CHENNAI282=Button(smain,image=img10,command=Chennai_28_2)
    CHENNAI282.pack()
    d16=Button(smain,image=img11,command=dhruvangal_pathinaru)
    d16.pack()
    KODI=Button(smain,image=img12,command=Kodi)
    KODI.pack()
    S24=Button(smain,image=img13,command=s24)
    S24.pack()
    Aym=Button(smain,image=img14,command=AYM)
    Aym.pack()
    rm=Button(smain,image=img15,command=RM)
    rm.pack()
    re=Button(smain,image=img16,command=REMO)
    re.pack()
    rev=Button(smain,image=img17,command=Kaashmora)
    rev.pack()
    rev1=Button(smain,image=img18,command=Thozha)
    rev1.pack()
    rev12=Button(smain,image=img19,command=Iraivi)
    rev12.pack()
    rev13=Button(smain,image=img20,command=DD)
    rev13.pack()
    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)

    smain1.mainloop()

def visaranai():
    print("\t\t\tFilm Name:Visarani")
    print("\t\t\tCast:Dinesh,Anandhi")
    print("\t\t\tDirector:Vetrimaaran")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Pugazh():
    print("\t\t\tFilm Name:Pugazh")
    print("\t\t\tCast:Jai,RJ Balaji,Surbhi Puranik")
    print("\t\t\tDirector:Manimaran")
    print("\t\t\tAvailable on:Prime video")
    print()



def zero():
    print("\t\t\tFilm Name:Zero")
    print("\t\t\tCast:sshivada,Ashwin Kakumanu")
    print("\t\t\tDirector:Arun kumar,V.Arunkumar")
    print("\t\t\tAvailable on:Prime video")
    print()

def Theri():
    print("\t\t\tFilm Name:Theri")
    print("\t\t\tCast:Vijay,Samantha")
    print("\t\t\tDirector:Atlee")
    print("\t\t\tAvailable on:Prime video")
    print()

def Manithan():
    print("\t\t\tFilm Name:Manithan")
    print("\t\t\tCast:Udhayanidhi Stalin,Aishwarya Rajesh,Vivek")
    print("\t\t\tDirector:I.Ahmed")
    print("\t\t\tAvailable on:Hotstar")
    print()


def Uriyadi():
    print("\t\t\tFilm Name:Uriyadi")
    print("\t\t\tCast:Vijay kumar")
    print("\t\t\tDirector:Vijay Kumar")
    print("\t\t\tAvailable on:Prime video")
    print()

def velainu_vanthuta_velakaran():
    print("\t\t\tFilm Name:Velainu Vandhutta Vellaikaaran")
    print("\t\t\tCast:Vishnu Vishal,Nikki Galrani")
    print("\t\t\tDirector:Ezhil")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Amma_kanakku():
    print("\t\t\tFilm Name:Amma Kanakku")
    print("\t\t\tCast:Amala Paul,Samuthirakani,Revathi")
    print("\t\t\tDirector:Ashwiny Iyer Tiwari")
    print("\t\t\tAvailable on:Hotstar")
    print()

def kabali():
    print("\t\t\tFilm Name:Kabali")
    print("\t\t\tCast:Rajinikanth,kishore,Radhika Apte")
    print("\t\t\tDirector:Pa.Ranjith")
    print("\t\t\tAvailable on:Hotstar")
    print()

def kaduvul_irukan_kumaru():
    print("\t\t\tFilm Name:Kadavul Irukaan Kumaru")
    print("\t\t\tCast:G.V.Prakash,Nikki Galarani,Anandhi")
    print("\t\t\tDirector:M.Rajesh")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Chennai_28_2():
    print("\t\t\tFilm Name:chennai 28 II")
    print("\t\t\tCast:Jai,Premji,Vijay vasanth,Nithin Sathya")
    print("\t\t\tDirector:Venkat Prabhu")
    print("\t\t\tAvailable on:Hotstar")
    print()

def dhruvangal_pathinaru():
    print("\t\t\tFilm Name:Dhuruvangal Pathinaaru:")
    print("\t\t\tCast:Rahman,Yashika Aannand,Anjana Jayaprakash")
    print("\t\t\tDirector:Karthick Naren")
    print("\t\t\tAvailable on:Prime video")
    print()

def s24():
    print("\t\t\tFilm Name:24")
    print("\t\t\tCast:Suriya,Samantha,Nithya Menon")
    print("\t\t\tDirector:Vikram K Kumar")
    print("\t\t\tAvailable on:Prime Video")
    print()    

def Kodi():
    print("\t\t\tFilm Name:Kodi")
    print("\t\t\tCast:Dhanush,Trisha,Anupama Parameswaran")
    print("\t\t\tDirector:Durai Senthilkumar")
    print("\t\t\tAvailable on:Sunnxt")
    print()        

def AYM():
    print("\t\t\tFilm Name:Achcham Yenbadhu Madamaiyadha")
    print("\t\t\tCast:Simbu,Manjima Mohan")
    print("\t\t\tDirector:Gautham Vasudev Menon")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def Bairavaa():
    print("\t\t\tFilm Name:Bairavaa")
    print("\t\t\tCast:Vijay,Keerthy Suresh,Satish")
    print("\t\t\tDirector:Bharathan")
    print("\t\t\tAvailable on:Sunnxt")
    print()    

def A2017():
    img=Image.open("SKBT.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("AAA.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("VIP2.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    
    img3=Image.open("THUPARIVAALAN.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("MERSAL.JPG")
    img4=img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("TOA.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("ARUVI.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("VELAIKARAN.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("AK.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("SI3.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("MAANAGARAM.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("KV.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("BB2.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("MM.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)

    img14=Image.open("AYM.JPG")
    img14 = img14.resize((200, 100), Image.ANTIALIAS)
    img14 = ImageTk.PhotoImage(img14)

    img15=Image.open("BAIRAVAA.JPG")
    img15 = img15.resize((200, 100), Image.ANTIALIAS)
    img15 = ImageTk.PhotoImage(img15)

    img16=Image.open("VIVEGAM.JPG")
    img16 = img16.resize((200, 100), Image.ANTIALIAS)
    img16 = ImageTk.PhotoImage(img16)

    img17=Image.open("VV.JPG")
    img17= img17.resize((200, 100), Image.ANTIALIAS)
    img17 = ImageTk.PhotoImage(img17)

    img18=Image.open("KAVAN.JPG")
    img18 = img18.resize((200, 100), Image.ANTIALIAS)
    img18 = ImageTk.PhotoImage(img18)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    sBKT=Button(smain,image=img,command=SBKT)
    sBKT.pack()
    aAA=Button(smain,image=img1,command=AAA)
    aAA.pack()
    VIP2=Button(smain,image=img2,command=Vip2)
    VIP2.pack()
    THUPARIVAALAN=Button(smain,image=img3,command=Thuparivaalan)
    THUPARIVAALAN.pack()
    MERSAL=Button(smain,image=img4,command=Mersal)
    MERSAL.pack()
    TAO=Button(smain,image=img5,command=Theeranadhigaramondru)
    TAO.pack()
    ARUVI=Button(smain,image=img6,command=Aruvi)
    ARUVI.pack()
    VELAIKARAN=Button(smain,image=img7,command=Vellaikaran)
    VELAIKARAN.pack()
    AK=Button(smain,image=img8,command=Adhekannagal)
    AK.pack()
    SI3=Button(smain,image=img9,command=si3)
    SI3.pack()
    KV=Button(smain,image=img11,command=Katruveliyidai)
    KV.pack()
    MAANAGARAM=Button(smain,image=img10,command=Maanagaram)
    MAANAGARAM.pack()
    BB2=Button(smain,image=img12,command=Bahubali2)
    BB2.pack()
    Mm=Button(smain,image=img13,command=MM)
    Mm.pack()
    Aym=Button(smain,image=img14,command=AYM)
    Aym.pack()
    THERI=Button(smain,image=img16,command=Vivegam)
    THERI.pack()
    THERIA=Button(smain,image=img17,command=VV)
    THERIA.pack()
    THERIANB=Button(smain,image=img18,command=Kavan)
    THERIANB.pack()
    
    

    br=Button(smain,image=img15,command=Bairavaa)
    br.pack()
    
    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

#2017
def SBKT():
    print("\t\t\tFilm Name:Sangili Bungili Kadhava Thora")
    print("\t\t\tCast:Jiva,Sri Divya")
    print("\t\t\tDirector:Ike")
    print("\t\t\tAvailable on:Hotstar")
    print()

def AAA():
    print("\t\t\tFilm Name:AAA")
    print("\t\t\tCast:STR,Tamannaah")
    print("\t\t\tDirector:Adhik Ravichandran")
    print("\t\t\tAvailable on:Prime video")
    print()

def Vip2():
    print("\t\t\tFilm Name:Vip 2")
    print("\t\t\tCast:Dhanush,Amala paul")
    print("\t\t\tDirector:Soundarya Rajinikanth")
    print("\t\t\tAvailable on:Prime video")
    print()

def Thuparivaalan():
    print("\t\t\tFilm Name:Thuparivaalan")
    print("\t\t\tCast:Vishal,Prasanna,Andrea Jeremiah")
    print("\t\t\tDirector:Mysskin")
    print("\t\t\tAvailable on:Prime video")
    print()

def Mersal():
    print("\t\t\tFilm Name:Mersal")
    print("\t\t\tCast:Vijay,Kajal Agarwal,Vadivelu,Samantha")
    print("\t\t\tDirector:Atlee")
    print("\t\t\tAvailable on:Netflix")
    print()

def Theeranadhigaramondru():
    print("\t\t\tFilm Name:Theeran Adhigaram Ondru")
    print("\t\t\tCast:Karthi,Rakul Preet Singh")
    print("\t\t\tDirector:H.Vinoth")
    print("\t\t\tAvailable on:Prime video")
    print()

def Aruvi():
    print("\t\t\tFilm Name:Aruvi")
    print("\t\t\tCast:Aditi Balan")
    print("\t\t\tDirector:Arun Prabhu")
    print("\t\t\tAvailable on:Prime video")
    print()

def Vellaikaran():
    print("\t\t\tFilm Name:Velaikkaran")
    print("\t\t\tCast:Sivakarthikeyan,Fahad Fasil,Nayanthara,Prakash raj")
    print("\t\t\tDirector:Mohan Raja")
    print("\t\t\tAvailable on:Hotstar")
    print()


def Adhekannagal():
    print("\t\t\tFilm Name:Adhe Kangal")
    print("\t\t\tCast:Kalaiyarasan,Janani Iyer")
    print("\t\t\tDirector:Rohini Venkatesan")
    print("\t\t\tAvailable on:Prime video")
    print()

def si3():
    print("\t\t\tFilm Name:Singam 3")
    print("\t\t\tCast:Suriya,Anushka,Shruthi Haasan,Soori")
    print("\t\t\tDirector:Hari")
    print("\t\t\tAvailable on:Prime video")
    print()

def Maanagaram():
    print("\t\t\tFilm Name:Maanagaram")
    print("\t\t\tCast:Sri,Sudeep Kishan,Regina Cassandra")
    print("\t\t\tDirector:Lokesh kanagaraj")
    print("\t\t\tAvailable on:Prime video")
    print()

def Katruveliyidai():
    print("\t\t\tFilm Name:Kaatru Veliyidai")
    print("\t\t\tCast:Karthi,Aditi rao Haydri")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Prime video")
    print()

def Bahubali2():
    print("\t\t\tFilm Name:Bahubali The Conclusion")
    print("\t\t\tCast:Prabhass,Tamannah,Anushka,Rana Daggubati")
    print("\t\t\tDirector:S.S.Rajamouli")
    print("\t\t\tAvailable on:Hotstar")
    print()

def MM():
    print("\t\t\tFilm Name:Meesaya Murukku")
    print("\t\t\tCast:Hiphop Tamizha'Aadhi',Aathmika")
    print("\t\t\tDirector:Hiphop Tamizha")
    print("\t\t\tAvailable on:Sunnxt")
    print()    

    
def A2018():
    img=Image.open("TSK.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("NIMIR.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("KAALA.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    
    img3=Image.open("TP2.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("KKS.JPG")
    img4=img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("GHAJINIKANTH.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("V2.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("IM.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("UTURN.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("SAAMY2.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("CCV.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("PP.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("NOTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("VC.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)

    img14=Image.open("SARKAR.JPG")
    img14 = img14.resize((200, 100), Image.ANTIALIAS)
    img14 = ImageTk.PhotoImage(img14)

    img15=Image.open("KM.JPG")
    img15 = img15.resize((200, 100), Image.ANTIALIAS)
    img15 = ImageTk.PhotoImage(img15)

    img16=Image.open("20.JPG")
    img16 = img16.resize((200, 100), Image.ANTIALIAS)
    img16= ImageTk.PhotoImage(img16)

    img17=Image.open("SEETHAKATHI.JPG")
    img17= img17.resize((200, 100), Image.ANTIALIAS)
    img17 = ImageTk.PhotoImage(img17)

    img18=Image.open("M2.JPG")
    img18 = img18.resize((200, 100), Image.ANTIALIAS)
    img18 = ImageTk.PhotoImage(img18)

    img19=Image.open("AM.JPG")
    img19 = img19.resize((200, 100), Image.ANTIALIAS)
    img19 = ImageTk.PhotoImage(img19)

    img20=Image.open("PPK.JPG")
    img20 = img20.resize((200, 100), Image.ANTIALIAS)
    img20= ImageTk.PhotoImage(img20)

    img21=Image.open("SR.JPG")
    img21 = img21.resize((200, 100), Image.ANTIALIAS)
    img21= ImageTk.PhotoImage(img21)

    img22=Image.open("96.JPG")
    img22 = img22.resize((200, 100), Image.ANTIALIAS)
    img22= ImageTk.PhotoImage(img22)

    img23=Image.open("JUNGA.JPG")
    img23 = img23.resize((200, 100), Image.ANTIALIAS)
    img23= ImageTk.PhotoImage(img23)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    Tsk=Button(smain,image=img,command=TSK)
    Tsk.pack()
    NIMIR=Button(smain,image=img1,command=Nimir)
    NIMIR.pack()
    KAALA=Button(smain,image=img2,command=Kaala)
    KAALA.pack()
    tp2=Button(smain,image=img3,command=TP2)
    tp2.pack()
    Kks=Button(smain,image=img4,command=KKS)
    Kks.pack()
    GHAJINIKANTH=Button(smain,image=img5,command=Ghajinikanth)
    GHAJINIKANTH.pack()
    
    V2=Button(smain,image=img6,command=Vishroopam2)
    V2.pack()
    Im=Button(smain,image=img7,command=IM)
    Im.pack()
    UTURN=Button(smain,image=img8,command=Uturn)
    UTURN.pack()
    SAMMY2=Button(smain,image=img9,command=Sammy2)
    SAMMY2.pack()
    Ccv=Button(smain,image=img10,command=CCV)
    Ccv.pack()
    
    pP=Button(smain,image=img11,command=PP)
    pP.pack()
    NOTA=Button(smain,image=img12,command=Nota)
    NOTA.pack()
    VC=Button(smain,image=img13,command=Vadachennai)
    VC.pack()
    SARKAR=Button(smain,image=img14,command=Sarkar)
    SARKAR.pack()
    KM=Button(smain,image=img15,command=Kaatrinmozhi)
    KM.pack()
    e20=Button(smain,image=img16,command=E20)
    e20.pack()
    SEK=Button(smain,image=img17,command=Seethakathai)
    SEK.pack()
    M2=Button(smain,image=img18,command=Maari2)
    M2.pack()
    AM=Button(smain,image=img19,command=Adangamaru)
    AM.pack()
    PPK=Button(smain,image=img20,command=ppk)
    PPK.pack()
    PPK1=Button(smain,image=img21,command=SR)
    PPK1.pack()
    PPKa1=Button(smain,image=img22,command=a96)
    PPKa1.pack()
    PPKaa1=Button(smain,image=img23,command=Junga)
    PPKaa1.pack()
    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()


#2018
def TSK():
    print("\t\t\tFilm Name:Thaanaa Serndha Koottam")
    print("\t\t\tCast:Suriya,Keerthy Suresh")
    print("\t\t\tDirector:Vignesh Shivn")
    print("\t\t\tAvailable on:prime video")
    print()

def ppk():
    print("\t\t\tFilm Name:Pyaar Prema Kaadhal")
    print("\t\t\tCast:Harish Kalyan,Raiza Wilson")
    print("\t\t\tDirector:Elan")
    print("\t\t\tAvailable on:Zee5")
    print()    

def Nimir():
    print("\t\t\tFilm Name:Nimir")
    print("\t\t\tCast:Udhayanidhi Stalin,Namita Pramod")
    print("\t\t\tDirector:Priyadarshan")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Kaala():
    print("\t\t\tFilm Name:Kaala")
    print("\t\t\tCast:Rajinikanth,Nana Patekar")
    print("\t\t\tDirector:Pa.Ranjith")
    print("\t\t\tAvailable on:prime video")
    print()

def TP2():
    print("\t\t\tFilm Name:Thamizh Padam 2")
    print("\t\t\tCast:Shiva,Iswarya Menon,Sathish")
    print("\t\t\tDirector:Amudhan")
    print("\t\t\tAvailable on:prime video")
    print()

def KKS():
    print("\t\t\tFilm Name:Kadai Kuttysingam")
    print("\t\t\tCast:Karthi,Priyabhavanishankar,Sathiaraj,Soori,Sayeesha")
    print("\t\t\tDirector:Pandiraj")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Ghajinikanth():
    print("\t\t\tFilm Name:Ghajinikanth")
    print("\t\t\tCast:Arya,Sayeesha,Sathish")
    print("\t\t\tDirector:P.Jayakumar")
    print("\t\t\tAvailable on:prime video")
    print()

def Vishroopam2():
    print("\t\t\tFilm Name:Vishwaroopam 2")
    print("\t\t\tCast:Kamal Haasan,Andrea Jermiah,Pooja Kumari")
    print("\t\t\tDirector:Kamal Haasan")
    print("\t\t\tAvailable on:Hotstar")
    print()

def IM():
    print("\t\t\tFilm Name:Imaikka Nodigal")
    print("\t\t\tCast:Vijay Sethupathy,Atharvaa ,Nayanthara,Rashi Kanna")
    print("\t\t\tDirector:Gnanamuthu")
    print("\t\t\tAvailable on:prime video")
    print()

def Uturn():
    print("\t\t\tFilm Name:U Turn")
    print("\t\t\tCast:Samantha,Adinaren")
    print("\t\t\tDirector:Pawan kumar")
    print("\t\t\tAvailable on:prime video")
    print()

def Sammy2():
    print("\t\t\tFilm Name:Saamy 2")
    print("\t\t\tCast:Chiyaan Vikram,Keerthy Suresh")
    print("\t\t\tDirector:Hari")
    print("\t\t\tAvailable on:Hotstar")
    print()

def CCV():
    print("\t\t\tFilm Name:Chekka Chivantha Vaanam")
    print("\t\t\tCast:STR,Arun Vijay,Aravindhswamy,Aishwarya Rajesh,\t\t\t\tAditi Rao Hydri,Jyothika")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Hotstar")
    print()

def PP():
    print("\t\t\tFilm Name:Pariyerum Perumal")
    print("\t\t\tCast:Kathir,Aanadhi,Yogi Babu")
    print("\t\t\tDirector:Maari Selvaraj")
    print("\t\t\tAvailable on:prime video")
    print()


def Nota():
    print("\t\t\tFilm Name:Nota")
    print("\t\t\tCast:Vijay Devarkonda,Sathiaraj,Nassar,Sanjana")
    print("\t\t\tDirector:Anand Shankar")
    print("\t\t\tAvailable on:prime video")
    print()

def Vadachennai():
    print("\t\t\tFilm Name:Vadachennai")
    print("\t\t\tCast:Dhanush,Aishwarya Rajesh,Kishore,Ameer,Radha Ravi")
    print("\t\t\tDirector:Vetrimaaran")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Sarkar():
    print("\t\t\tFilm Name:Sarkar")
    print("\t\t\tCast:Vijay,Keerthy Suresh,Yogi Babu")
    print("\t\t\tDirector:A.R.Murugadoss")
    print("\t\t\tAvailable on:Netflix")
    print()

def Kaatrinmozhi():
    print("\t\t\tFilm Name:Katrin Mozhi")
    print("\t\t\tCast:Jothika,MS Baskar,Yogi Babu")
    print("\t\t\tDirector:Radha Mohan")
    print("\t\t\tAvailable on:prime video")
    print()

def E20():
    print("\t\t\tFilm Name:2.O")
    print("\t\t\tCast:Rajinikanth,Amy Jackson,Akshay Kumar")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:Prime Video")
    print()

def Seethakathai():
    print("\t\t\tFilm Name:Seethakathi")
    print("\t\t\tCast:Vijay Sethupathy,Mahendran,Sunil Reddy")
    print("\t\t\tDirector:Balaji")
    print("\t\t\tAvailable on:Prime video")
    print()

def Maari2():
    print("\t\t\tFilm Name:Maari 2")
    print("\t\t\tCast:Dhanush,Robo Shankar,Sai Pallavi,Krishna")
    print("\t\t\tDirector:Balaji Mohan")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Adangamaru():
    print("\t\t\tFilm Name:Adanga Maaru")
    print("\t\t\tCast:Jayam Ravi,Raashi Khanna,Sampath")
    print("\t\t\tDirector:Thangavelu")
    print("\t\t\tAvailable on:hotstar")
    print()    


def A2020():
    img=Image.open("DARBAR.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("PATTAS.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("PSYCHO.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    
    img3=Image.open("VK.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("MAFIA.JPG")
    img4=img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("KKK.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("DP.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("OMK.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("NS.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("PENGUIN.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("CHENNAI282.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("D16.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("KODI.PNG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("24.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)

    img14=Image.open("AYM.JPG")
    img14 = img14.resize((200, 100), Image.ANTIALIAS)
    img14 = ImageTk.PhotoImage(img14)

    img15=Image.open("Asuran.ico")
    img15 = img15.resize((200, 100), Image.ANTIALIAS)
    img15=ImageTk.PhotoImage(img15)

    img16=Image.open("Asuran.ico")
    img16 = img16.resize((200, 100), Image.ANTIALIAS)
    img16 = ImageTk.PhotoImage(img16)

    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)
    
    
    DARBAR=Button(smain,image=img,command=Darbar)
    DARBAR.pack()
    PATTAS=Button(smain,image=img1,command=Pattas)
    PATTAS.pack()
    PSYCHO=Button(smain,image=img2,command=Psycho)
    PSYCHO.pack()
    VK=Button(smain,image=img3,command=Vaanamkottatum)
    VK.pack()
    MAFIA=Button(smain,image=img4,command=Mafia)
    MAFIA.pack()
    kkk=Button(smain,image=img5,command=KKK)
    kkk.pack()
    DP=Button(smain,image=img6,command=Dharalaprabhu)
    DP.pack()
    OMK=Button(smain,image=img7,command=OHMYK)
    OMK.pack()
    NS=Button(smain,text="nan siri",image=img8,command=NAAN)
    NS.pack()
    NS1=Button(smain,text="nan siri",image=img9,command=Penguin)
    NS1.pack()

    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()


#2020

d=[]
text="asa"
def SEARCH():
    global text
    text=e.get()
    
    #2019
    if text.upper()=='PETTA':
        petta()
    elif text.upper()=='VISWASAM':
        viswasam()
    elif text.upper()=='BIGIL':
        bigil()
    elif text.upper()=='NGK':
        ngk()
    elif text.upper()in ['NKP','NERKONDA PAARVAI']:
        nkp()
    elif text.upper() in ['VANTHA RAJAVATHAAN VARUVEN','VANTHARAJAVATHAANVARUVEN']:
        vrv()
    elif text.upper() in ["SUPER DELUXE","SUPERDELUXE"]:
        superdeluxe()
    elif text.upper() in ["HERO"]:
        hero()
    elif text.upper() in ["MR.LOCAL","MRLOCAL"]:
        mrl()    
    elif text.upper() in ["KAITHI"]:
        kaithi()
    elif text.upper() in ["GAMEOVER","GAME OVER"]:
        gameover()
    elif text.upper() in ["ASURAN"]:
        asuran()
    elif text.upper() in ["THADAM"]:
        thadam()    
    elif text.upper() in ["KOLAIGARAN"]:
        kolaigaran()
    elif text.upper() in ["THAMBI"]:
        thambi()
    elif text.upper() in ["NAMMA VETTU PILLAI","NVP"]:
        nvp()    
    elif text.upper() in ["KAAPAAN","KAAPAN","KAPPAAN","KAAPPAAN"]:
        kaappan()
    elif text.upper() in ["NATPETHUNAI","NATPE THUNAI"]:
        natpethunai()    
    elif text.upper() in ["KANCHANA 3","KANCHANA3"]:
        kanchana3()
    
    
    elif text.upper() in ["OH KADHAL KANMANI","OK KANMANI","OHKADHALKANMANI","OKKANMANI"]:
        o_kadhal_kanmani()
    elif text.upper() in ["KANCHANA2","KANCHANA 2"]:
        kanchana2()    
    elif text.upper() in ["VAI RAJA VAI","VAIRAJAVAI"]:
        vai_raja_vai()
    elif text.upper() in ["RAJATHANDIRAM","RAJATHANDRAM"]:
        rajathandiram()
    elif text.upper() in ["KAAKAMUTTAI","KAAKA MUTTAI"]:
        kaakamuttai()
    elif text.upper() in ["INDRU NETRU NAALAI","INDRUNETRUNAALAI","IIN"]:
        indru_netru_naalai()    
    elif text.upper() in ["MAARI"]:
        Maari()
    elif text.upper() in ["10ENDRATHUKULA","10 ENDRATHUKULA"]:
        E10_endrathukula()
    elif text.upper() in ["THOONGAVANAM","THOOGAVANAM"]:
        thoogavanam()
    elif text.upper() in ["ANEGAN"]:
        Anegan()
    elif text.upper() in ["THANGAMAGAN","THANGA MAGAN"]:
        Thangamagan()    
    elif text.upper() in ["KAAKI SATTAI","KAAKISATTAI"]:
        Kaaki()
    elif text.upper() in ["NAANUM ROWDYDHAAN","NAANUMROWDYDHAAN"]:
        Naanum()
    elif text.upper() in ["THANI ORUVAN","THANIORUVAN"]:
        Thanioruvan()
    #2016
    elif text.upper() in ["VISARANAI"]:
        visaranai()
    elif text.upper() in ["PUGAZH"]:
        Pugazh()    
    elif text.upper() in ["ZERO"]:
        zero()
    elif text.upper() in ["THERI"]:
        Theri()
    elif text.upper() in ["MANITHAN"]:
        Manithan()
    elif text.upper() in ["URIYADI"]:
        Uriyadi()    
    elif text.upper() in ["VELAINU VANDHUTTA VELLAIKAARAN","VVV","VELAINUVANDHUTTAVELLAIKAARAN"]:
        velainu_vanthuta_velakaran()
    elif text.upper() in ["AMMA KANAKKU","AMMAKANUKKU"]:
        E10_endrathukula()
    elif text.upper() in ["THOONGAVANAM","THOOGAVANAM"]:
        Amma_kanakku()
    elif text.upper() in ["KABALI"]:
        kabali()
    elif text.upper() in ["KADAVUL IRUKAN KUMARU","KADAVULIRUKANKUMARU"]:
        kaduvul_irukan_kumaru()    
    elif text.upper() in ["CHENNAI 28 2","CHENNAI28 2","CHENNAI282","CHENNAI 28 SECOND INNINGS"]:
        Chennai_28_2()
    elif text.upper() in ["DHRUVANGAL PATHINAARU","DHRUVANGALPATHINAARU","D16"]:
        dhruvangal_pathinaru()
    elif text.upper() in ["24"]:
        s24()
    elif text.upper() in ["KODI"]:
        Kodi()
    elif text.upper() in ["KKK"]:
        KKK()
    elif text.upper() in ["KADAVULE","OMK","OH MY GOD","OH MY"]:
        OHMYK()
    elif text.upper() in ["AYM","ACHCHAM YENBADHU MADAMAIYADHA"]:
        AYM()     
    #2017
    elif text.upper() in ["SKBT","SANGILI BUNGILI KADHAVA THORA"]:
        SKBT()
    elif text.upper() in ["AAA"]:
        AAA()    
    elif text.upper() in ["VIP2","VIP 2","VELAIYILLA PATTADHARI 2"]:
        Vip2()
    elif text.upper() in ["THUPARIVAALAN"]:
        Thuparivaalan()
    elif text.upper() in ["THEERAN","THEERAN ADHIGARAM ONDRU"]:
        Theeranadhigaramondru()
    elif text.upper() in ["URIYADI"]:
        Uriyadi()    
    elif text.upper() in ["ARUVI"]:
        Aruvi()
    elif text.upper() in ["VELAIKARAN","VELLAIKARAN","VELLAIKKARAN","VELAIKKARAN"]:
        Vellaikaran()
    elif text.upper() in ["ADHE KANGAL","ADHEKANGAL"]:
        Adhekannagal()
    elif text.upper() in ["SI3","SINGAM 3","SI3","SINGAM3"]:
        si3()
    elif text.upper() in ["MAANAGARAM"]:
        Maanagaram()    
    elif text.upper() in ["KAATRU VELIYIDAI","KAATRUVELIYIDAI","KATRUVELIYIDAI","KATRU VELIYIDAI"]:
        Katruveliyidai()
    elif text.upper() in ["BAAHUBALI 2","BAAHUBALI2","BAAHUBALI THE CONCLUSION"]:
        Bahubali2()
    elif text.upper() in ["MEESAYA MURUKKU","MEESAYAMURUKKU"]:
        MM()
    #2018
    
    elif text.upper()in ['TSK',"THAANA SERNDHA KOOTTAM"]:
        TSK()
    elif text.upper() in ['PPK',"PYAAR PREMA KAADHAL","PYAARPREMAKAADHAL"]:
        ppk()
    elif text.upper() in ["NIMIR"]:
        Nimir()
    elif text.upper() in ["KAALA"]:
        Kaala()
    elif text.upper() in ["TAMIZH PADAM 2","TAMIZHPADAM 2","TAMIZHPADAM2"]:
        TP2()    
    elif text.upper() in ["KKS","KADAIKUTTY SINGAM","KADAIKUTTYSINGAM"]:
        KKS()
    elif text.upper() in ["GHAJINIKANTH"]:
        Vishroopam2()
    elif text.upper() in ["VISHWAROOPAM 2","VISHWAROOPAM2"]:
        asuran()
    elif text.upper() in ["IN","IMAIKKA NODIGAL","IMAIKKANODIGAL","IMAIKA NODIGAL","IMAIKANODIGAL"]:
        IM()    
    elif text.upper() in ["UTURN"]:
        Uturn()
    elif text.upper() in ["SAAMY2","SAAMY 2","SAMMY2","SAMMY 2"]:
        Sammy2()
    elif text.upper() in ["CCV","CHEKKA CHIVANTHA VAANAM","CHEKKACHIVANTHAVAANAM"]:
        CCV()    
    elif text.upper() in ["PP","PARIYERUM PERUMAL","PARIYERUMPERUMAL"]:
        PP()
    elif text.upper() in ["NOTA"]:
        Nota()    
    elif text.upper() in ["VADACHENNAI","VADA CHENNAI"]:
        Vadachennai()
    elif text.upper() in ["SARKAR","SARKR"]:
        Sarkar()
    elif text.upper() in ["KAATRIN MOZHI","KAATRINMOZHI"]:
        Kaatrinmozhi()
    elif text.upper() in ["2.0","ENTHIRAN 2","ENTHIRAN2","ROBOT2"]:
        E20()
    elif text.upper() in ["SEETHAKATHI","SEETHAKAATHI"]:
        Seethakathai()
    elif text.upper() in ["MAARI2","MAARI 2"]:
        Nimir()
    elif text.upper() in ["ADANGAMARU","ADANGA MARU","ADANGAMAARU","ADANGA MAARU"]:
        Adangamaru()
    #EDITED
    elif text.upper() in ["DHARMA DURAI","DHARMADURAI"]:
        DD()
    elif text.upper() in ["96"]:
        a96()
    elif text.upper() in ["JUNGA"]:
        Junga()
    elif text.upper() in ["VIKRAM VEDHA","VIKRAMVEDHA"]:
        VV()
    elif text.upper() in ["KAKAPO","KADHALUM KADUNDHU POGUM"]:
        Kakapo()
    elif text.upper() in ["IRAIVI"]:
        Iraivi()
    elif text.upper() in ["KAVAN"]:
        Kavan()

    elif text.upper() in ["DEV"]:
        Dev()
    elif text.upper() in ["THOZHA"]:
        Thozha()
    elif text.upper() in ["KAASHMORA"]:
        Kaashmora()
    elif text.upper() in ["SEEMARAJA","SEEMA RAJA"]:
        SR()
    elif text.upper() in ["REMO"]:
        REMO()

    elif text.upper() in ["RAJINIMURUGAN","RAJINI MURUGAN"]:
        RM()
    elif text.upper() in ["SINGAM2","SINGAM 2","SI3"]:
        si2()
    elif text.upper() in ["KAAPAAN","KAAPAN","KAPAAN","KAAPPAN"]:
        Kaapaan()


    elif text.upper() in ["VIVEGAM"]:
        Vivegam()
    elif text.upper() in ["VEERAM"]:
        Veeram()
    elif text.upper() in ["VEDALAM"]:
        Vedalam()
    elif text.upper() in ["YENNAI ARINDHAAL"]:
        YA()
    elif text.upper() in ["MANKATHA"]:
        Mankatha()

    elif text.upper() in ["KATHTHI","KATHI"]:
        Kaththi()
    elif text.upper() in ["THUPAKKI"]:
        Thupakki()
    elif text.upper() in ["THALAIVAA"]:
        Thalaivaa()

    elif text.upper() in ["JILLA"]:
        Jilla()
    elif text.upper() in ["PIZZA"]:
        Pizza()
    elif text.upper() in ["JIGARTHANDA"]:
        Jigarthanda()
    elif text.upper() in ["PUDHUPETTAI"]:
        Pudhupettai()
    elif text.upper() in ["MAYAKKAM ENNA","MAYAKKAMENNA"]:
        ME()
    elif text.upper() in ["7G","7G RAINBOW COLONY","7GRAINBOWCOLONY"]:
        G7()    
    elif text.upper() in ["AAYIRATHIL ORUVAN"]:
        A1000()        
    elif text.upper() in ["IRUVAR"]:
        Iruvar()
    elif text.upper() in ["THALAPATHI"]:
        Thalapathi()
    elif text.upper() in ["NAYAGAN"]:
        Nayagan()

    elif text.upper() in ["MINNALE"]:
        Minnale()
    elif text.upper() in ["ENPT","ENNAI NOKKI PAAYUM THOTTA"]:
        ENPT()
    elif text.upper() in ["KAAKHA KAAKHA","KAAKHAKAAKHA"]:
        Kaakha()
    elif text.upper() in ["VETTAIYADU VELAIYADU","VETTAIYADUVELAIYADU"]:
        Thalapathi()
    elif text.upper() in ["ALAIPAYUTHE"]:
        AP()
    elif d==[]:
        search()

    else:
        nfilm()
              

        


        
def SEARCHACT():
  text=ACT.get()
  #RAJINIKANTH
  if text.upper() in ["RAJINI","RAJNI","RAJINIKANTH","SUPERSTAR"]:
      
    img=Image.open("DARBAR.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("PETTA.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("KAALA.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("KABALI.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("20.jpg")
    img4 = img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("ENTHIRAN.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("SIVAJI.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("THALAPATHI.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("KATHTHI.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

     
    



    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)
    
    
    DARBAR=Button(smain,image=img,command=Darbar)
    DARBAR.pack()
    pett=Button(smain,image=img1,command=petta)
    pett.pack()
    KAALA=Button(smain,image=img2,command=Kaala)
    KAALA.pack()
    KABALI=Button(smain,image=img3,command=kabali)
    KABALI.pack()
    e20=Button(smain,image=img4,command=E20)
    e20.pack()
    e21=Button(smain,image=img5,command=Enthiran)
    e21.pack()
    e22=Button(smain,image=img6,command=Sivaji)
    e22.pack()
    e23=Button(smain,image=img7,command=Thalapathi)
    e23.pack()
    
    


    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()
    #VIJAY
  elif text.upper() in ["VIJAY","THALAPATHY","ILAYATHALAPATHY","THALAPATHY VIJAY"]:
      
    img=Image.open("BIGIL.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("SARKAR.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("THERI.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("MERSAL.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("BAIRAVAA.jpg")
    img4 = img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("JILLA.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("THALAIVAA.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("THUPAKKI.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("KATHTHI.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)



    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=bigil)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=Sarkar)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Theri)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Mersal)
    MERSAL.pack()
    kat=Button(smain,image=img8,command=Kaththi)
    kat.pack()
    br=Button(smain,image=img5,command=Jilla)
    br.pack()
    br1=Button(smain,image=img6,command=Thalaivaa)
    br1.pack()
    br2=Button(smain,image=img7,command=Thupakki)
    br2.pack()
    br3=Button(smain,image=img4,command=Bairavaa)
    br3.pack()

    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()



    #AJITH KUMAR

  elif text.upper() in ["AJITH","AJITH KUMAR","THALA"]:
      
    img=Image.open("VISWASAM.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("NKP.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("VIVEGAM.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("YA.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("VEERAM.jpg")
    img4 = img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("VEDALAM.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("MANKATHA.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

 


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)
    
    
    VIS=Button(smain,image=img,command=viswasam)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=nkp)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Vivegam)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=YA)
    MERSAL.pack()
    kat=Button(smain,image=img4,command=Veeram)
    kat.pack()
    br=Button(smain,image=img5,command=Vedalam)
    br.pack()
    br1=Button(smain,image=img6,command=Mankatha)
    br1.pack()


    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()
    #DHANUSH

  elif text.upper() in ["DHANUSH"]:
      
    img=Image.open("ASURAN.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("PATTAS.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("M2.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("VC.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("VIP2.jpg")
    img4 = img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("KODI.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("TM.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("MAARI.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("ANEGAN.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("AADUKALAM.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("POLLADHAVAN.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("PUDHUPETTAI.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("ME.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)


    img13=Image.open("KKO.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)

    img14=Image.open("ENPT.JPG")
    img14 = img14.resize((200, 100), Image.ANTIALIAS)
    img14 = ImageTk.PhotoImage(img14)

    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=asuran)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=Pattas)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Maari2)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Vadachennai)
    MERSAL.pack()
    kat=Button(smain,image=img4,command=Vip2)
    kat.pack()
    br=Button(smain,image=img5,command=Kodi)
    br.pack()
    br1=Button(smain,image=img6,command=Thangamagan)
    br1.pack()
    br2=Button(smain,image=img7,command=Maari)
    br2.pack()
    br3=Button(smain,image=img8,command=Anegan)
    br3.pack()
    br3A=Button(smain,image=img9,command=Aadukalam)
    br3A.pack()
    br3V=Button(smain,image=img10,command=Polladhavan)
    br3V.pack()
    brA=Button(smain,image=img11,command=Pudhupettai)
    brA.pack()
    brb=Button(smain,image=img12,command=ME)
    brb.pack()
    brbA=Button(smain,image=img13,command=KK)
    brbA.pack()
    brbAa=Button(smain,image=img14,command=ENPT)
    brbAa.pack()



    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()
    #SURIYA
  elif text.upper() in ["SURIYA","SURIYA SIVAKUMAR","SURYA"]:
      
    img=Image.open("NGK.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("KAAPAAN.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("TSK.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("SI3.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("24.jpg")
    img4 = img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

    img5=Image.open("SI2.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("MASS.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("MAAT.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("ANEGAN.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("AYAN.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)



    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=ngk)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=Kaapaan)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=TSK)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=si3)
    MERSAL.pack()
    kat=Button(smain,image=img4,command=s24)
    kat.pack()
    br=Button(smain,image=img5,command=si2)
    br.pack()
    br1=Button(smain,image=img6,command=Mass)
    br1.pack()
    br2=Button(smain,image=img7,command=Maat)
    br2.pack()

    br2A=Button(smain,image=img9,command=Ayan)
    br2A.pack()

    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

  elif text.upper() in ["SIVAKARTHIKEYAN","SK"]:#SK
      
    img=Image.open("HERO.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("NVP.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("MRL.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("SR.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("VELAIKARAN.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("REMO.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("RM.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("KS.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)



    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=hero)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=nvp)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=mrl)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=SR)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=Vellaikaran)
    br.pack()
    br1=Button(smain,image=img6,command=REMO)
    br1.pack()
    br2=Button(smain,image=img7,command=RM)
    br2.pack()
    br3=Button(smain,image=img8,command=Kaaki)
    br3.pack()

    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()


  elif text.upper() in ["KARTHI","KARTHIK","KARTHI SIVAKUMAR","KARTHIK SIVAKUMAR"]:#KARTHI
      
    img=Image.open("THAMBI.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("KAITHI.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("DEV.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("TOA.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("KV.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("KKS.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("KAASHMORA.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("THOZHA.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("A1000.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=thambi)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=kaithi)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Dev)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Theeranadhigaramondru)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=Katruveliyidai)
    br.pack()
    br1=Button(smain,image=img6,command=KKS)
    br1.pack()
    br2=Button(smain,image=img7,command=Kaashmora)
    br2.pack()
    br3=Button(smain,image=img8,command=Thozha)
    br3.pack()
    brA=Button(smain,image=img9,command=A1000)
    brA.pack()
    

    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

  elif text.upper() in ["VJS","VIJAY SETHUPATHI","SETHUPATHI","VIJAY SETHUPATHY","MAKKAL SELVAN","SETHUPATHY"]:#VJS
      
    img=Image.open("SP.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("NR.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("SEETHAKATHI.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("DD.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("IRAIVI.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("KAKAPO.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("KAVAN.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("VV.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=superdeluxe)
    VIS.pack()
    SARKAR=Button(smain,image=img2,command=Seethakathai)
    SARKAR.pack()
    THERI=Button(smain,image=img1,command=Naanum)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=DD)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=Iraivi)
    br.pack()
    br1=Button(smain,image=img6,command=Kakapo)
    br1.pack()
    br2=Button(smain,image=img7,command=Kavan)
    br2.pack()
    br3=Button(smain,image=img8,command=VV)
    br3.pack()
    Abr3=Button(smain,image=img9,command=CCV)
    Abr3.pack()
    Vbr3=Button(smain,image=img10,command=a96)
    Vbr3.pack()
    bsr3=Button(smain,image=img11,command=Junga)
    bsr3.pack()
    br3s=Button(smain,image=img12,command=petta)
    br3s.pack()
    br3ss=Button(smain,image=img13,command=Pizza)
    br3ss.pack()
    

    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()     

  else:
    nact()
    
def Aadukalam():
    print("\t\t\tFilm Name:Aadukalam")
    print("\t\t\tCast:Dhanush,Taapsee ,Jayapalan")
    print("\t\t\tDirector:Vetrimaran")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Polladhavan():
    print("\t\t\tFilm Name:Polladhavan")
    print("\t\t\tCast:Dhanush,Kishore,Divya Spadana,Daniel Balaji")
    print("\t\t\tDirector:Vetrimaran")
    print("\t\t\tAvailable on:SunNxt")
    print()    



def DD():
    print("\t\t\tFilm Name:Dharma Dhurai")
    print("\t\t\tCast:Vijay Sethupathy,Tammanah,Aishwarya Rajesh")
    print("\t\t\tDirector:Seenu Ramaswamy")
    print("\t\t\tAvailable on:SunNxt")
    print()

def a96():
    print("\t\t\tFilm Name:96")
    print("\t\t\tCast:Vijay Sethupathy,Trisha")
    print("\t\t\tDirector:Prem Kumar")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Junga():
    print("\t\t\tFilm Name:Junga")
    print("\t\t\tCast:Vijay Sethupathy,Sayeesha,Yogi Babu")
    print("\t\t\tDirector:Gokul")
    print("\t\t\tAvailable on:ZEE5")
    print()

def VV():
    print("\t\t\tFilm Name:Vikram Vedha")
    print("\t\t\tCast:Vijay Sethupathy,Madhavan,Shradda Srinath,Kathir")
    print("\t\t\tDirector:Pushkar-Gayathri")
    print("\t\t\tAvailable on:ZEE5")
    print()

def Kakapo():
    print("\t\t\tFilm Name:Kadhalum Kadandhu Pogum")
    print("\t\t\tCast:Vijay Sethupathy,Madonna Sebastain")
    print("\t\t\tDirector:Nalan Kumarasamy")
    print("\t\t\tAvailable on:Prime Video")
    print()

def Iraivi():
    print("\t\t\tFilm Name:Iraivi")
    print("\t\t\tCast:Vijay Sethupathy,SJ Suryah,Bobby Simha,Anjali")
    print("\t\t\tDirector:Karthik Subbaraj")
    print("\t\t\tAvailable on:Netflix")
    print()

def Kavan():
    print("\t\t\tFilm Name:Kavan")
    print("\t\t\tCast:Vijay Sethupathy,T Rajendar,Madonna Sebastain")
    print("\t\t\tDirector:KV Anand")
    print("\t\t\tAvailable on:ZEE5")
    print()    


def Ayan():
    print("\t\t\tFilm Name:Ayan")
    print("\t\t\tCast:Suriya,Tammanah")
    print("\t\t\tDirector:KV Anand")
    print("\t\t\tAvailable on:Sunnxt")
    print()    
        

def KO():
    print("\t\t\tFilm Name:Ko")
    print("\t\t\tCast:Jiiva,Jagan")
    print("\t\t\tDirector:KV Anand")
    print("\t\t\tAvailable on:Prime Video")
    print()    
        
    

def Dev():
    print("\t\t\tFilm Name:Dev")
    print("\t\t\tCast:Karthi,Rakul Preet Singh")
    print("\t\t\tDirector:Rajath Ravishankar")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Thozha():
    print("\t\t\tFilm Name:Thozha")
    print("\t\t\tCast:Karthi,Tammanah,Nagarjuna")
    print("\t\t\tDirector:Vamshi Padipalley")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Kaashmora():
    print("\t\t\tFilm Name:Kaashmora")
    print("\t\t\tCast:Karthi,Nayantara,Srividya,Vivek")
    print("\t\t\tDirector:Gokul")
    print("\t\t\tAvailable on:Prime Video")
    print()    


def SR():
    print("\t\t\tFilm Name:Seema Raja")
    print("\t\t\tCast:Sivakarthikeyan,Samantha Akkieni")
    print("\t\t\tDirector:Ponram")
    print("\t\t\tAvailable on:SunNxt")
    print()

def RM():
    print("\t\t\tFilm Name:Rajini Murugan")
    print("\t\t\tCast:Sivakarthikeyan,Keerthy Suresh")
    print("\t\t\tDirector:Ponram")
    print("\t\t\tAvailable on:SunNxt")
    print()

def REMO():
    print("\t\t\tFilm Name:Remo")
    print("\t\t\tCast:Sivakarthikeyan,Keerthy Suresh")
    print("\t\t\tDirector:Ponram")
    print("\t\t\tAvailable on:Prime Video")
    print()    
    
    

def si2():
    print("\t\t\tFilm Name:Singam 2")
    print("\t\t\tCast:Suriya,Anushka Shetty,Hansika")
    print("\t\t\tDirector:Hari")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Maat():
    print("\t\t\tFilm Name:Maatraan")
    print("\t\t\tCast:Suriya,Kajal Agarwal")
    print("\t\t\tDirector:KV Anand")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Mass():
    print("\t\t\tFilm Name:Mass Engira Massilamani")
    print("\t\t\tCast:Suriya,Nayantara")
    print("\t\t\tDirector:Venkat Prabhu")
    print("\t\t\tAvailable on:SunNxt")
    print()    


def Kaapaan():
    print("\t\t\tFilm Name:Kaapaan")
    print("\t\t\tCast:Suriya,Sayyesha")
    print("\t\t\tDirector:KV Anand")
    print("\t\t\tAvailable on:SunNxt")
    print()
    
        
def Vivegam():
    print("\t\t\tFilm Name:Vivegam")
    print("\t\t\tCast:Ajith Kumar,Samantha Akkieni")
    print("\t\t\tDirector:Sirurhai Siva")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Veeram():
    print("\t\t\tFilm Name:Veeram")
    print("\t\t\tCast:Ajith Kumar,Tammanah")
    print("\t\t\tDirector:Sirurhai Siva")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Vedalam():
    print("\t\t\tFilm Name:Vedalam")
    print("\t\t\tCast:Ajith Kumar,Shruti Haasan")
    print("\t\t\tDirector:Sirurhai Siva")
    print("\t\t\tAvailable on:SunNxt")
    print()

def YA():
    print("\t\t\tFilm Name:Yennai Arindhaal")
    print("\t\t\tCast:Ajith Kumar,Trisha,Arun Vijay")
    print("\t\t\tDirector:Gautham Vasudev Menon")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Mankatha():
    print("\t\t\tFilm Name:Mankatha")
    print("\t\t\tCast:Ajith Kumar,Trisha")
    print("\t\t\tDirector:Venkat Prabhu")
    print("\t\t\tAvailable on:SunNxt")
    print()    

    
    
        
    
def Kaththi():
    print("\t\t\tFilm Name:Kaththi")
    print("\t\t\tCast:Vijay,Samantha Akkieni,Satish")
    print("\t\t\tDirector:AR Murgadoss")
    print("\t\t\tAvailable on:Prime Video")
    print()
    
def Thupakki():
    print("\t\t\tFilm Name:Thupakki")
    print("\t\t\tCast:Vijay,Kajal Agarwal")
    print("\t\t\tDirector:AR Murgadoss")
    print("\t\t\tAvailable on:Hotstar")
    print()

def Thalaivaa():
    print("\t\t\tFilm Name:Thalaivaa")
    print("\t\t\tCast:Vijay,Amala Paul,Santhanam")
    print("\t\t\tDirector:AL Vijay")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def Jilla():
    print("\t\t\tFilm Name:Jilla")
    print("\t\t\tCast:Vijay,Kajal Agarwal")
    print("\t\t\tDirector:RT Neason")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def Pizza():
    print("\t\t\tFilm Name:Pizza")
    print("\t\t\tCast:Vijay Sethupathy,Ramya Nambesan")
    print("\t\t\tDirector:Karthik Subbaraj")
    print("\t\t\tAvailable on:Sunnxt")
    print()

def Jigarthanda():
    print("\t\t\tFilm Name:Jigarthanda")
    print("\t\t\tCast:Siddharth,Lakshmi Menon,Bobby Simha")
    print("\t\t\tDirector:Karthik Subbaraj")
    print("\t\t\tAvailable on:Hotstar")
    print()

def RR():
    print("\t\t\tFilm Name:Raja Rani")
    print("\t\t\tCast:Arya,Nayantara,Nazriya,Jai,Santhanam")
    print("\t\t\tDirector:Atlee")
    print("\t\t\tAvailable on:Hotstar")
    print()
    
def Spyder():
    print("\t\t\tFilm Name:Spyder")
    print("\t\t\tCast:Mahesh Babu,Rakul Preet,SJ Suryah")
    print("\t\t\tDirector:AR Murgadoss")
    print("\t\t\tAvailable on:SunNxt")
    print()
#SHANKAR
def Enthiran():
    print("\t\t\tFilm Name:Enthiran")
    print("\t\t\tCast:Rajinikanth,Aishwarya Rai,Santhanam")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Sivaji():
    print("\t\t\tFilm Name:Sivaji The Boss")
    print("\t\t\tCast:Rajinikanth,Shriya Saran,Vivek")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Anniyan():
    print("\t\t\tFilm Name:Anniyan")
    print("\t\t\tCast:Vikram,Sadha,Prakash Raj")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:SunNxt")
    print()

def I():
    print("\t\t\tFilm Name:I")
    print("\t\t\tCast:Vikram,Amy Jackson")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:Prime Video")
    print()     

def Boys():
    print("\t\t\tFilm Name:Boys")
    print("\t\t\tCast:Siddharth,Genelia,Nakhul,Vivek")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:SunNxt")
    print()

def Jeans():
    print("\t\t\tFilm Name:Jeans")
    print("\t\t\tCast:Prashanth,Aishwarya Rai,Nassar")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:SunNxt")
    print()     

def Mudhalvan():
    print("\t\t\tFilm Name:Mudhalvan")
    print("\t\t\tCast:Arjun Sarja,Vadivelu,Manisha Koirala")
    print("\t\t\tDirector:Shankar")
    print("\t\t\tAvailable on:SunNxt")
    print()
#SELVARAGHAVAN
def Pudhupettai():
    print("\t\t\tFilm Name:Pudhupettai")
    print("\t\t\tCast:Dhanush,Sneha,Sonia Agarwal")
    print("\t\t\tDirector:Selvaraghavan")
    print("\t\t\tAvailable on:Prime Video")
    print()

def A1000():
    print("\t\t\tFilm Name:Aayirathil Oruvan")
    print("\t\t\tCast:Karthi,Reema Sen,Parthiban,Andrea")
    print("\t\t\tDirector:Selvaraghavan")
    print("\t\t\tAvailable on:SunNxt")
    print()

def ME():
    print("\t\t\tFilm Name:Mayakkam Enna")
    print("\t\t\tCast:Dhanush,Richa ")
    print("\t\t\tDirector:Selvaraghavan")
    print("\t\t\tAvailable on:SunNxt")
    print()    

def KK():
    print("\t\t\tFilm Name:Kadhal Konden")
    print("\t\t\tCast:Dhanush,Sonia Agarwal")
    print("\t\t\tDirector:Selvaraghavan")
    print("\t\t\tAvailable on:SunNxt")
    print()

def G7():
    print("\t\t\tFilm Name:7G Rainbow Colony")
    print("\t\t\tCast:Ravi Krishna,Sonia Agarwal")
    print("\t\t\tDirector:Selvaraghavan")
    print("\t\t\tAvailable on:SunNxt")
    print()

#MANI    
def AP():
    print("\t\t\tFilm Name:Alaipayuthe")
    print("\t\t\tCast:Madhavan,Shalini,Vivek")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Prime Video")
    print()

def KM():
    print("\t\t\tFilm Name:Kannathil Muthammital")
    print("\t\t\tCast:Madhavan,Simran,Prakash Raj")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Prime Video")
    print()

def Thalapathi():
    print("\t\t\tFilm Name:Thalapathi")
    print("\t\t\tCast:Rajinikanth,Maamotty,Aravind Swamy")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Prime Video")
    print()       

def Iruvar():
    print("\t\t\tFilm Name:Iruvar")
    print("\t\t\tCast:Mohan Lal,Prakash Raj")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Prime Video")
    print()

def Nayagan():
    print("\t\t\tFilm Name:Nayagan")
    print("\t\t\tCast:Kamal Hassan,Nassar,Nizhagal Ravi")
    print("\t\t\tDirector:Mani Ratnam")
    print("\t\t\tAvailable on:Prime Video")
    print()

#GVM
def VET():
    print("\t\t\tFilm Name:Vettaiyadu Velayadu")
    print("\t\t\tCast:Kamal Hassan,Jyothika,Daniel Balaji")
    print("\t\t\tDirector:Gautham Vasudev Menon")
    print("\t\t\tAvailable on:SunNxt")
    print()    

def ENPT():
    print("\t\t\tFilm Name:Enai Nokki Paayum Thotta")
    print("\t\t\tCast:Dhanush,Megha Akash")
    print("\t\t\tDirector:Gautham Vasudev Menon")
    print("\t\t\tAvailable on:Prime Video")
    print()

def Kaakha():
    print("\t\t\tFilm Name:Kaakha Kaakha")
    print("\t\t\tCast:Suriya,Jyothika,Jeevan")
    print("\t\t\tDirector:Gautham Vasudev Menon")
    print("\t\t\tAvailable on:SunNxt")
    print()    

def Minnale():
    print("\t\t\tFilm Name:Minnale")
    print("\t\t\tCast:Madhavan,Reema Sen,Vivek")
    print("\t\t\tDirector:Gautham Vasudev Menon")
    print("\t\t\tAvailable on:Prime Video")
    print()
    


    

def SEARCHDIR():
  text=DIR.get()
  #KS
  if text.upper() in ["KARTHIK SUBBARAJ","KARTHIK","KS"]:
      
    img=Image.open("IRAIVI.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("PETTA.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    

    img3=Image.open("JIGARTHANDA.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    img4=Image.open("PIZZA.jpg")
    img4 = img4.resize((200, 100), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)

     
    



    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)
    
    
    DARBAR=Button(smain,image=img,command=Iraivi)
    DARBAR.pack()
    pett=Button(smain,image=img1,command=petta)
    pett.pack()
    
    KABALI=Button(smain,image=img3,command=Jigarthanda)
    KABALI.pack()
    e20=Button(smain,image=img4,command=Pizza)
    e20.pack()
    


    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

  elif text.upper() in ["KV ANAND","KV","KVANAND","KVA"]:#KVANAND
      
    img=Image.open("MAAT.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("ANEGAN.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("KAVAN.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("KAAPAAN.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("AYAN.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("KO.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("KAVAN.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("VV.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=Maat)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=Anegan)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Kavan)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Kaapaan)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=Ayan)
    br.pack()
    br1=Button(smain,image=img6,command=KO)
    br1.pack()
  

    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

  elif text.upper() in ["ATLEE","ATLE"]:#ATLEE
      
    img=Image.open("THERI.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("MERSAL.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("BIGIL.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("RR.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("AYAN.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("KO.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("KAVAN.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("VV.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=Theri)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=Mersal)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=bigil)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=RR)
    MERSAL.pack()


    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

  elif text.upper() in ["AR","ARM","ARMURGADOSS","AR MURGADOSS"]:#ARM
      
    img=Image.open("DARBAR.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("SARKAR.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("THUPAKKI.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("KATHTHI.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("SPYDER.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("KO.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("KAVAN.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("VV.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=Darbar)
    VIS.pack()
    SARKAR=Button(smain,image=img2,command=Sarkar)
    SARKAR.pack()
    THERI=Button(smain,image=img1,command=Thupakki)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Kaththi)
    MERSAL.pack()
    aMERSAL=Button(smain,image=img4,command=Spyder)
    aMERSAL.pack()
    
    
   

    menubar = Menu(smain1)
    smain1.iconbitmap('fott.ico')
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()    

  elif text.upper() in ["VETRIMARAN","VETRI","VETRI MARAN"]:#VETRIMARAN
      
    img=Image.open("ASURAN.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("VC.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("VISARANAI.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("AADUKALAM.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("POLLADHAVAN.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("KO.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("KAVAN.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("VV.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    smain1.iconbitmap('fott.ico')
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=asuran)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=Vadachennai)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=visaranai)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Aadukalam)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=Polladhavan)
    br.pack()
   

    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()
   
  elif text.upper() in ["SHANKAR"]:#Shankar
      
    img=Image.open("20.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("I.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("ENTHIRAN.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("SIVAJI.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("ANNIYAN.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("BOYS.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("JEANS.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("MUDHALVAN.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.iconbitmap('fott.ico')
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=E20)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=I)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Enthiran)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Sivaji)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=Anniyan)
    br.pack()
    boy=Button(smain,image=img6,command=Boys)
    boy.pack()
    br1=Button(smain,image=img7,command=Jeans)
    br1.pack()
    br2=Button(smain,image=img8,command=Mudhalvan)
    br2.pack()


    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

  elif text.upper() in ["SELVARAGHAVAN","SELVA","SELVARAGHAVN"]:#SELVA
      
    img=Image.open("NGK.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("PUDHUPETTAI.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("A1000.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("ME.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("G7.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("KKO.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("KAVAN.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("VV.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.iconbitmap('fott.ico')
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=ngk)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=Pudhupettai)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=A1000)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=ME)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=G7)
    br.pack()
    br1=Button(smain,image=img6,command=KK)
    br1.pack()
  

    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

  elif text.upper() in ["MANI RATNAM","MANIRATNAM","MANI","RATNAM"]:#MANIRATNAM
      
    img=Image.open("OKK.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("CCV.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("KV.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("AP.jpeg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("KM.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("THALAPATHI.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("IRUVAR.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("NAYAGAN.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.iconbitmap('fott.ico')
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=o_kadhal_kanmani)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=CCV)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Katruveliyidai)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=AP)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=KM)
    br.pack()
    boy=Button(smain,image=img6,command=Thalapathi)
    boy.pack()
    br1=Button(smain,image=img7,command=Iruvar)
    br1.pack()
    br2=Button(smain,image=img8,command=Nayagan)
    br2.pack()


    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()    

  elif text.upper() in ["GAUTHAM MENON","GAUTHAM VASUDEV MENON","GVM","GAUTHAM"]:#GVM
      
    img=Image.open("YA.jpg")
    img = img.resize((200, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    img1=Image.open("AYM.jpg")
    img1 = img1.resize((200, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    
    img2=Image.open("MINNALE.jpg")
    img2 = img2.resize((200, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)

    img3=Image.open("KAAKHA.jpg")
    img3 = img3.resize((200, 100), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)

    

    img5=Image.open("VET.JPG")
    img5 = img5.resize((200, 100), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)

    img6=Image.open("ENPT.JPG")
    img6 = img6.resize((200, 100), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)

    img7=Image.open("IRUVAR.JPG")
    img7 = img7.resize((200, 100), Image.ANTIALIAS)
    img7 = ImageTk.PhotoImage(img7)

    img8=Image.open("NAYAGAN.JPG")
    img8 = img8.resize((200, 100), Image.ANTIALIAS)
    img8 = ImageTk.PhotoImage(img8)

    img9=Image.open("CCV.JPG")
    img9 = img9.resize((200, 100), Image.ANTIALIAS)
    img9 = ImageTk.PhotoImage(img9)

    img10=Image.open("96.JPG")
    img10 = img10.resize((200, 100), Image.ANTIALIAS)
    img10 = ImageTk.PhotoImage(img10)

    img11=Image.open("JUNGA.JPG")
    img11 = img11.resize((200, 100), Image.ANTIALIAS)
    img11 = ImageTk.PhotoImage(img11)

    img12=Image.open("PETTA.JPG")
    img12 = img12.resize((200, 100), Image.ANTIALIAS)
    img12 = ImageTk.PhotoImage(img12)

    img13=Image.open("PIZZA.JPG")
    img13 = img13.resize((200, 100), Image.ANTIALIAS)
    img13 = ImageTk.PhotoImage(img13)


    smain1=Toplevel(main)
    smain1.iconbitmap('fott.ico')
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    VIS=Button(smain,image=img,command=YA)
    VIS.pack()
    SARKAR=Button(smain,image=img1,command=AYM)
    SARKAR.pack()
    THERI=Button(smain,image=img2,command=Minnale)
    THERI.pack()
    MERSAL=Button(smain,image=img3,command=Kaakha)
    MERSAL.pack()
    
    br=Button(smain,image=img5,command=VET)
    br.pack()
    boy=Button(smain,image=img6,command=ENPT)
    boy.pack()
  

    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()    

  else:
    ndir()         
    

'''import pickle
EmpID = {1:"Zack",2:"53050",3:"IT",4:"38",5:"Flipkart"}
pickling_on = open("EmpID.pickle","wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()

pickle_off = open("EmpID.pickle", 'rb')
EmpID = pickle.load(pickle_off)
print(EmpID)


EmpID = [2109,1304]
f = open("EmpID.pickle","wb")
pickle.dump(EmpID, f)
f.close()'''
def NAAN():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='NAAN SIRITHAL':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
    f.close()

def Penguin():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='PENGUIN':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()

def Darbar():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='DARBAR':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()

def Pattas():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='PATTAS':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()

def Psycho():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='PSYCHO':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()

def Vaanamkottatum():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='VAANAM KOTTATUM':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()

def Mafia():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='MAFIA':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()

def KKK():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='KANNUM KANNUM KOLAIYADITHAAL':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()
 
def Dharalaprabhu():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='DHARALA PRABHU':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
            
    f.close()
    
def OHMYK():
    f = open("Films.json","rb")
    b=pickle.load(f)
    for i in b:
        if i[0].upper()=='OH MY KADAVULE':
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
    f.close()




def create():
    
    f = open("Updates.json","wb")
    l=[]
    while True:
        s=[]
        print("To break type Y")
        a=input("\t\t\tFilmname:")
        if a in 'Yy':
            break
        b=input("\t\t\tCast:")
        c=input("\t\t\tDirector:")
        d=input("\t\t\tAvailable on:")
        s.append(a)
        s.append(b)
        s.append(c)
        s.append(d)
        l.append(s)
        
    pickle.dump(l, f)
    
    f.close()

def show():
    f = open("Films.json","rb")
    b=pickle.load(f)
    print(b)
    f.close()

def search():
    f = open("Films.json","rb")
    b=pickle.load(f)
    kn=0
    for i in b:
        if i[0].upper()==e.get().upper():
            print("\t\t\tFilm Name:",i[0])
            print("\t\t\tCast:",i[1])
            print("\t\t\tDirector:",i[2])
            print("\t\t\tAvailable on:",i[3])
            print()
            print()
            kn=1
    if kn==0:
        nfilm()
        
    f.close()
    

def APPEND():
    
    
    f = open("Films.json","rb")
    l=pickle.load(f)
    f.close()
   
    
    
    l.append([x,y,z,w])
    f = open("Films.pickle","wb")    
    pickle.dump(l, f)
    print("\t\t\tMovie Added To Database")
    
    f.close()

    
def append():
    '''p=input("\t\t\tEnter Password to Access:")
    if p == 'KANISHK':'''
    
    f = open("Films.json","rb")
    l=pickle.load(f)
    f.close()
    
    
    while True:
        s=[]
        
        a=input("\t\t\tFilmname:")
        
        b=input("\t\t\tCast:")
        c=input("\t\t\tDirector:")
        d=input("\t\t\tAvailable on:")
        s.append(a)
        s.append(b)
        s.append(c)
        s.append(d)
        l.append(s)
        
        print("\t\t\tMovie Added To Database")
        ch=input("\t\t\tDo you want to add more movies:")
        print()
        print()
        if ch.upper() in ['NO','N']:
            break
    f = open("Films.json","wb")    
    pickle.dump(l, f) 
    
    f.close()
    '''else:
      print("\t\t\tAccess not granted")
      print()
      print()'''

def Edit():
    '''p=input("\t\t\tEnter Password to Access:")
    if p == 'KANISHK':'''
    s=[]
    f = open("Films.json","rb")
    l=pickle.load(f)
    f.close()
    
    
    edit=input("\t\t\tEnter Film Name To be Edited:")
    y=0
    j=0
    
    e1=input("\t\t\tField to be edited:")
    
    if e1.upper() not in ["FILM NAME","NAME","CAST","CAST AND CREW","CREW","ACTORS","DIRECTOR","FILM MAKER","MAKER","OTT","OTT PLATFORM","DIGITAL PLATFORM","AVAILABLE ON","PLATFORM"]:
        print("\t\t\tInvalid Field")
    for i in l:
        if i[0].upper()== edit.upper():
            y=1
        
    
    for i in l:
        if i[0].upper()== edit.upper():
            if e1.upper() in ["FILM NAME","NAME"]:
                f=input("\t\t\tNew Film Name:")
                l[j][0]=f
                print("\t\t\tFilm Name Changed")
                print()
                print()
                y=1
            elif e1.upper() in ["CAST","CAST AND CREW","CREW","ACTORS"]:
                g=input("\t\t\tNew Cast Details:")
                print("\t\t\tCast Details Changed")
                print()
                print()
                l[j][1]=g
                y=1
            elif e1.upper() in ["DIRECTOR","FILM MAKER","MAKER"]:
                h=input("\t\t\tNew Director :")
                print("\t\t\tDirector Detailis Changed")
                print()
                print()
                l[j][2]=h
                y=1
            elif e1.upper() in ["OTT","OTT PLATFORM","DIGITAL PLATFORM","AVAILABLE ON","PLATFORM"]:
                k=input("\t\t\tNew OTT Platform :")
                print("\t\t\tOTT Details Changed")
                print()
                print()
                l[j][3]=k
                y=1
                
                
        j+=1    
        
    if y==0:
        print("\t\t\tFilm not in Database")
        print()
        print()
    f = open("Films.json","wb")        
    pickle.dump(l, f) 
    
    f.close()
    '''else:
    print("\t\t\tAccess not granted")
    print()
    print()'''
          
def Delete():
    '''p=input("\t\t\tEnter Password to Access:")
    if p == 'KANISHK':'''
    
    f = open("Films.json","rb")
    l=pickle.load(f)
    f.close()
    edit=input("\t\t\tEnter Film Name To be Deleted:")
    jn=0
    y=0
    
    for i in l:
        
        if i[0].upper()== edit.upper():
            
            del l[jn]
            print("\t\t",edit,"Film deleted")
            print()
            print()
            y=1
        jn+=1
    if y==0:
        print("\t\t\tFilm not in Database")
        print()
        print()
    f = open("Films.json","wb")        
    pickle.dump(l, f) 
    
    f.close()
    '''else:
    print("\t\t\tAccess not granted")
    print()
    print()'''
                        
    
t=0
'''
def EDIT():
    smain1=Toplevel(main)
    smain1.iconbitmap('fott.ico')
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=250,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    mycanvas.congifure(yscrollcommand=scroll.set)

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    PASS=Entry(smain,bg="grey",fg="yellow")
    PASS.pack()
    global t
    t=PASS.get()
    f=Button(smain,text="ENTER PASSWORD ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=PW)
             
    f.pack()
    if PASS.get()=='KANISHK':
        print(131)

    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()'''
def Edi():
    

    def kjd():
     f = open("Films.json","rb")
     l=pickle.load(f)
     f.close()
     y=0
     j=0
     s=[]
     variable1=variable.get()
     for i in l:
        if i[0].upper()== e13.get().upper():
            if variable1 == " NEW FILM NAME":
                
                l[j][0]=e1.get()
                nedfilm()
                y=1
            elif variable1 == " NEW CAST DETAILS":
                l[j][1]=e1.get()
                nedcast()
                y=1
            elif variable1 == " NEW DIRECTOR":
                l[j][2]=e1.get()
                neddir()
                y=1
            elif variable1 == " NEW OTT PLATFORM":
                l[j][3]=e1.get()
                nedott()
                y=1
            else:
                l[j][2]=e1.get()
                neddir()
                y=1
                
                
        j+=1    
        
     if y==0:
        ined()
     f = open("Films.json","wb")        
     pickle.dump(l, f)
     f.close()

        
    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=375,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    OptionList = [
    " NEW FILM NAME",
    " NEW CAST DETAILS",
    " NEW DIRECTOR",
    " NEW OTT PLATFORM"]


    
  
    A12v=Label(smain,text="EDIT A MOVIE",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2)
    A12v['font']=myfont1
    A12v.pack()

    qsA=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")
    qsA.pack()    


    k13=Label(smain,text="FILM NAME TO BE EDITED ",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()

    e13=Entry(smain,bg="grey",fg="yellow")
    e13.pack()

    qsAA=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")
    qsAA.pack()
    qsAA=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")
    qsAA.pack()    

    A12vA=Label(smain,text="FIELD TO BE EDITED",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2)
    A12vA.pack()
    qsAAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")
    qsAAa.pack()  
    
    
    
    


 
        

    '''qsAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsAa.pack()'''
    
    e1=Entry(smain,bg="grey",fg="yellow")
    e1.pack()
    variable = StringVar(smain)
    variable.set(OptionList[0])
    opt = OptionMenu(smain, variable, *OptionList)
    opt.config(width=20,bg="black",highlightthickness=0,fg="white",activebackground="black",activeforeground="white")
    opt.pack()
    qsAAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")
    qsAAa.pack()
    
    
    
    '''e12=Entry(smain,bg="grey",fg="yellow")
    
    e12.pack()
    k2=Label(smain,text="CAST DETAILS",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea1=str(e12.get())
    e13=Entry(smain,bg="grey",fg="yellow")
    e13.pack()
    k13=Label(smain,text="DIRECTOR ",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea2=str(e13.get())
    e14=Entry(smain,bg="grey",fg="yellow")
    e14.pack()
    k1=Label(smain,text="OTT PLATFORM",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea3=str(e14.get())

    qsAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsAa.pack()
    '''
    qsAAaa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")
    qsAAaa.pack()
    f12=Button(smain,text="EDIT ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=kjd).pack()
    
        
    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

def kan():
    def kj():
        f = open("Films.json","rb")
        l=pickle.load(f)
        f.close()
        ea=e1.get()
        ea1=e12.get()
        ea2=e13.get()
        ea3=e13.get()
        b=[ea,ea1,ea2,ea3]
        l.append(b)
        f = open("Updates.json","rb")
        n=pickle.load(f)
        f = open("Updates.json","wb")
        
        n.append(b)
        pickle.dump(n, f)
        f.close()

        
        f = open("Films.json","wb")    
        pickle.dump(l, f)
        valadd()

        
    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=375,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    A12=Label(smain,text="ADD A MOVIE",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2)
    A12['font']=myfont1
    A12.pack()
    qsA=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsA.pack()
    qsAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsAa.pack()
    
    e1=Entry(smain,bg="grey",fg="yellow")
    e1.pack()
    k1=Label(smain,text="FILM NAME",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea=str(e1.get())
    e12=Entry(smain,bg="grey",fg="yellow")
    
    e12.pack()
    k2=Label(smain,text="CAST DETAILS",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea1=str(e12.get())
    e13=Entry(smain,bg="grey",fg="yellow")
    e13.pack()
    k13=Label(smain,text="DIRECTOR ",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea2=str(e13.get())
    e14=Entry(smain,bg="grey",fg="yellow")
    e14.pack()
    k1=Label(smain,text="OTT PLATFORM",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea3=str(e14.get())

    qsAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsAa.pack()
    
    f12=Button(smain,text="ADD ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=kj).pack()
    '''if ea3!='':
        f = open("Films.json","rb")
        l=pickle.load(f)
        f.close()
        #nonlocal ea,ea1,ea2,ea3
        b=[ea,ea1,ea2,ea3]
        l.append(b)
        f = open("Films.json","wb")    
        pickle.dump(l, f)'''
        
    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()

k=[]
def dele():
    def kji():
       f = open("Films.json","rb")
       l=pickle.load(f)
       f.close()
       jn=0
       y=0
    
       for i in l:
        
         if i[0].upper()== e1.get().upper():

            global k
            k.append(l[jn])
            del l[jn]
            valdel()
            
            y=1
         jn+=1
       if y==0:
           '''qsA1=Label(smain,text="!!FILM NOT FOUND!! ",activebackground="grey",activeforeground="grey",bg="black",fg="YELLOW")
           qsA1.pack()'''
           invaldel()
         
       f = open("Films.json","wb")        
       pickle.dump(l, f) 
    
       f.close()
        

        
    smain1=Toplevel(main)
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="black",height=350,width=240)
    mycanvas.pack(side=LEFT)

    scroll=Scrollbar(wrapper,orient="vertical",command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)
    
    '''mycanvas.congifure(yscrollcommand=scroll.set)'''

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    


    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    A12=Label(smain,text="DELETE A MOVIE",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2)
    A12['font']=myfont1
    A12.pack()
    qsA=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsA.pack()
    qsAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsAa.pack()
    
    e1=Entry(smain,bg="grey",fg="yellow")
    e1.pack()
    k1=Label(smain,text="FILM NAME TO BE DELETED",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea=str(e1.get())
    '''
    e12=Entry(smain,bg="grey",fg="yellow")
    
    e12.pack()
    k2=Label(smain,text="CAST DETAILS",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea1=str(e12.get())
    e13=Entry(smain,bg="grey",fg="yellow")
    e13.pack()
    k13=Label(smain,text="DIRECTOR ",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea2=str(e13.get())
    e14=Entry(smain,bg="grey",fg="yellow")
    e14.pack()
    k1=Label(smain,text="OTT PLATFORM",font=(50),activebackground="grey",activeforeground="red",bg="black",fg="white",padx=2,pady=2).pack()
    ea3=str(e14.get())'''

    qsAa=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsAa.pack()
    
    f12=Button(smain,text="DELETE ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=kji).pack()
    '''if ea3!='':
        f = open("Films.json","rb")
        l=pickle.load(f)
        f.close()
        #nonlocal ea,ea1,ea2,ea3
        b=[ea,ea1,ea2,ea3]
        l.append(b)
        f = open("Films.json","wb")    
        pickle.dump(l, f)'''
        
    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.mainloop()




klm=0
def PW1():
  word=PASS.get()  
  if word.upper() in ["KANISHK"]:
      
    smain1=Toplevel(main)
    smain1.iconbitmap('fott.ico')
    smain1.configure(bg="black")
    wrapper=LabelFrame(smain1)

    mycanvas=Canvas(wrapper,highlightbackground="grey",height=250,width=150)
    mycanvas.pack(side=LEFT)

    '''scroll=Scrollbar(wrapper,orient="vertical",jump=0,command=mycanvas.yview)
    scroll.pack(side=RIGHT,fill=Y)'''
    
    'mycanvas.congifure(yscrollcommand=scroll.set)'

    '''mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    '''
    smain=Frame(mycanvas)
    mycanvas.create_window((0,0),window=smain,anchor="nw")
    smain.configure(bg="black")
    wrapper.configure(bg="black")
    mycanvas.configure(bg="black")    
    
    

    wrapper.pack(fill="both",expand="yes",pady=5)

    f1=Button(smain,text="ADD ",activebackground="grey",activeforeground="red",bg="black",fg="yellow",command=kan)

    f1['font']=myfont1
    f1.pack()
    g1=Button(smain,text="EDIT ",activebackground="grey",activeforeground="red",bg="black",fg="yellow",command=Edi)
    g1['font']=myfont1
    

    h1=Button(smain,text="DELETE ",activebackground="grey",activeforeground="red",bg="black",fg="yellow",command=dele)
    h1['font']=myfont1
    g1.pack()
    h1.pack()
    qsv=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsv.pack()
    qsn=Label(smain,text="ADD ",activebackground="grey",activeforeground="grey",bg="black",fg="black")

    qsn.pack()
    ha1=Button(smain,text="Check List to Update ",activebackground="grey",activeforeground="red",bg="black",fg="yellow",command=update)
    ha1.pack()
    menubar = Menu(smain1)
    filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
    filemenu.add_command(label="CONFIRM", command=smain1.destroy)
    menubar.add_cascade(label="GO BACK", menu=filemenu,command=smain1.destroy)
    smain1.config(menu=menubar)
    smain1.resizable(0,0)    

    smain1.mainloop()

  else:
    inval()  
      

def update():
    f = open("Updates.json","rb")
    l=pickle.load(f)
    print()
    print()
    
    print("\t\t\tRecently Added Film:",l[-1][0])
    #i=input("\t\t\tWant Further Details:")
    '''if i.upper in ["YES","Y"]:
        print("\t\t\t",l[-1])'''
    f.close()
    
    if k==[]:
      print("\t\t\tRecently Deleted Film:",k)
    else:  
      print("\t\t\tRecently Deleted Film:",k[0][0])
    print()
    print()  
    

    
def nedfilm():
   v=messagebox.showinfo("EDIT","Film name Changed!")

def nedcast():
   v=messagebox.showinfo("EDIT","Cast Details Changed!")

def neddir():
   v=messagebox.showinfo("EDIT","Director Details Changed!")

def nedott():
   v=messagebox.showinfo("EDIT","OTT Platform Changed!")

def ined():
   v=messagebox.showinfo("FILM NOT FOUND","Check your input value")   
    
    

     
def nfilm():
   v=messagebox.showinfo("FILM SEARCH","Check your input value")

     
def nact():
   v=messagebox.showinfo("ACTOR SEARCH","Check your input value")

     
def ndir():
   v=messagebox.showinfo("DIRECTOR SEARCH","Check your input value")
   
   
def valdel():
   v=messagebox.showinfo("DELETE","Film Deleted")

def invaldel():
   v=messagebox.showinfo("DELETE","Film Does Not Exist")    
    
    
def valadd():
   v=messagebox.showinfo("ADD","Film Added Successfully")    
    
    

def inval():
   v=messagebox.showinfo("Access Denied","Password Incorrect")
   
   
def PW():
  word=PASS.get()  
  if word.upper() in ["KANISHK"]:
     
      
    

     
    



    
    
    a0=Label(main,text="ADD/EDIT",font='bold',activebackground="grey",activeforeground="red",bg="grey",fg="white",padx=2,pady=2)
    a0.pack()
    
    a1=Entry(main,bg="grey",fg="yellow")
    a1.pack()
    b1=Label(main,text="FILM NAME",font='bold',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
    b1.pack()
    a2=Entry(main,bg="grey",fg="yellow")
    a2.pack()
    b2=Label(main,text="CAST & CREW",font='bold',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
    b2.pack()
    a3=Entry(main,bg="grey",fg="yellow")
    a3.pack()
    b3=Label(main,text="DIRECTOR",font='bold',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
    b3.pack()
    a4=Entry(main,bg="grey",fg="yellow")
    a4.pack()
    b4=Label(main,text="AVAILABLE ON",font='bold',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
    b4.pack()
    global x,y,z,j
    x=x.get()
    y=y.get()
    z=z.get()
    j=j.get()
    l1=[x,y,z,j]
    b5=Button(main,text="ADD",font='bold',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2,command = APPEND)
    b5.pack()
    
    
        
    
    
    
    
    
    
    
    
new = 1
url = "https://www.netflix.com/in/"

def Netflix():
    webbrowser.open(url,new=new)

new1 = 1
url1 = "https://www.amazon.com/gp/video/storefront/ref=topnav_storetab_atv?node=2858778011"

def PV():
    webbrowser.open(url1,new=new)
    
new2 = 1
url2 = "https://www.hotstar.com/in"

def Hotstar():
    webbrowser.open(url2,new=new)

new3 = 1
url3 = "https://www.zee5.com"

def Zee5():
    webbrowser.open(url3,new=new)

new4 = 1
url4 = "https://www.sunnxt.com"

def Sunnxt():
    webbrowser.open(url4,new=new)

    
    

    
    
    


    


 


    


#print(Fore.BLUE + Back.BLACK)    
   
main=Tk()
main.title('FOTT')
main.iconbitmap('fott.ico')
main.geometry('280x670')
main.configure(bg="GREY")

myfont1=font.Font(size=15)
A1=Label(main,text="SELECT YEAR",font=(50),activebackground="grey",activeforeground="red",bg="grey",fg="white",padx=2,pady=2)
A=Button(main,text=2019,command=A2019,font='Italian',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
B=Button(main,text=2015,command=A2015,font='Italian',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
C=Button(main,text=2016,command=A2016,font='Italian',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
D=Button(main,text=2017,command=A2017,font='Italian',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
E=Button(main,text=2018,command=A2018,font='Italian',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
F=Button(main,text=2020,command=A2020,font='Italian',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2)
A1['font']=myfont1
A1.pack()
#B['font']=myfont1
B.pack()
C.pack()
D.pack()
E.pack()
A.pack()
F.pack()
qs1v=Label(main,text="ADD ",activebackground="grey",activeforeground="grey",bg="grey",fg="grey")

qs1v.pack()

e=Entry(main,bg="grey",fg="yellow")
e.pack()

f=Button(main,text="SEARCH BY FILM ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=SEARCH).pack()
ACT=Entry(main,bg="grey",fg="yellow")
ACT.pack()
ACTOR=Button(main,text="SEARCH BY ACTOR",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=SEARCHACT)
ACTOR.pack()
DIR=Entry(main,bg="grey",fg="yellow")
DIR.pack()
DIRECT=Button(main,text="SEARCH BY DIRECTOR",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=SEARCHDIR)
DIRECT.pack()

qs=Label(main,text="ADD ",activebackground="grey",activeforeground="grey",bg="grey",fg="grey")

qs.pack()
'''
qsa=Label(main,text="ADD ",activebackground="grey",activeforeground="grey",bg="grey",fg="grey")

qsa.pack()'''
qsb=Label(main,text="ADMIN MODE ",activebackground="grey",activeforeground="grey",bg="grey",fg="white")
qsb['font']=myfont1
qsb.pack()
PASS=Entry(main,bg="grey",fg="yellow")
PASS.pack()
o=PASS.get()
f=Button(main,text="ENTER PASSWORD ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=PW1)

f.pack()
qs1=Label(main,text="ADD ",activebackground="grey",activeforeground="grey",bg="grey",fg="grey")

qs1.pack()

qsa1=Label(main,text="FOR REFERENCE ",justify=LEFT,activebackground="grey",activeforeground="grey",bg="grey",fg="white")
qsa1.pack()


img=Image.open("NETFLIX.JPG")
img = img.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
    
img1=Image.open("PV.jpg")
img1 = img1.resize((50,50), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
    
img2=Image.open("HOTSTAR.png")
img2 = img2.resize((50,50), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
    
img3=Image.open("ZEE5.jpeg")
img3 = img3.resize((50,50), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)

img4=Image.open("SUNNXT.png")
img4=img4.resize((50,50), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(img4)
#main.configure(background=img)

  
Btn = Button(main, text = "Netflix",image=img,command=Netflix)
Btn.pack(side = LEFT)
Btn1= Button(main, text = "PrimeVideo",image=img1,command=PV)
Btn1.pack(side = LEFT)
Btn2 = Button(main, text = "Hotstar",image=img2,command=Hotstar)
Btn2.pack(side = LEFT)
Btn3 = Button(main, text = "Zee5",image=img3,command=Zee5)
Btn3.pack(side = LEFT)
Btn4 = Button(main, text = "SunNxt",image=img4,command=Sunnxt)
Btn4.pack(side = LEFT)
main.resizable(0,0)    

'''

f=Button(main,text="ADD ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=append)

f.pack()
g=Button(main,text="EDIT ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=Edit)

g.pack()

h=Button(main,text="DELETE ",activebackground="grey",activeforeground="red",bg="grey",fg="yellow",command=Delete)

h.pack()'''


    
'''if klm == 1:
    b5=Button(main,text="ADD",font='bold',activebackground="grey",activeforeground="red",bg="grey",fg="yellow",padx=2,pady=2,command=append())
    b5.pack()'''
    
'''
menubar = Menu(main)
filemenu = Menu(menubar, tearoff=0,fg="black",activeforeground="red",bg="white",activebackground="black",activeborderwidth=0,bd=0)
filemenu.add_command(label="CONFIRM", command=main.destroy())
menubar.add_cascade(label="CLOSE", menu=filemenu,command=main.destroy())
main.config(menu=menubar)
'''
main.mainloop()



