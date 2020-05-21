#Jesus write for me

#import functions

from urllib.request import urlopen
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar
from re import findall, finditer, MULTILINE, DOTALL
from sqlite3 import *

image_file = 'product_images.html'

#Coffee -LIVE 1
 # Define url for the live web document
url = 'https://www.ebay.com.au/b/Coffee/185036/bn_99762518?rt=nc&_sop=10'
    # Get a link to the web page from the server
coffee_page = urlopen(url)
    # Extract the web page's content as a Unicode string
html1_code1 = coffee_page.read().decode('UTF-8')


instore_today_thing =0
oldstock_onorder_thing=0

def call_product_function():
    if instore_today_thing == 1:
        product1()
    elif instore_today_thing == 2:
        product2()
    elif instore_today_thing == 3:
        product3()
    elif instore_today_thing == 4:
        product4()




def product1():
    # Define url for the live web document
    url = 'https://www.ebay.com.au/b/Coffee/185036/bn_99762518?rt=nc&_sop=10'
    # Get a link to the web page from the server
    coffee_page = urlopen(url)
    # Extract the web page's content as a Unicode string
    html1_code = coffee_page.read().decode('UTF-8')
    # close the connection to the web server
    coffee_page.close()
    #open new html file
    sf_coffee_file = open(image_file, 'w', encoding = 'UTF-8')
    # HTML header
    coffee_code='''<!DOCTYPE html>
    <html>
      <head>
          <title>Coffee</title>
      </head>
      <body>
          <h1 align="center">Pandamic Products: on Offer </h1>
          <p align="center">
          Coffee <a href="https://www.ebay.com.au/b/Coffee/185036/bn_99762518?rt=nc&_sop=10"><em>https://www.ebay.com.au/b/Coffee/185036/bn_99762518?rt=nc&_sop=10</em></a>
          </p>

          <table align="center" border="2"style="width:70%">\n

    '''
    coffeematch=findall('alt="([A-Z a-z 0-9 , . -]*)"',html1_code)
    coffeem=coffeematch[5:10]
    coffimg=findall('<img class([]A-Za-z0-9-"()=:./ _?\s]*)>',html1_code)
    ci=coffimg[0:5]
    for index in range(min(len(coffeem),len(ci))):
        coffee_code+=f"<tr >\n<th>{coffeem[index]}<br><img class{ci[index]}width=200 height=300/></th></tr>"
    coffee_code+="\n</table>\n</body>\n</html>"
    # Write the standard HTML "footer" markups into your file
    # to complete the document
    sf_coffee_file .write(coffee_code)
    # Close your HTML file (which you can now view in a web browser)
    sf_coffee_file .close()

#find title using findall
coffeematch=findall('alt="([A-Z a-z 0-9 , . -]*)"',
                  html1_code1)
coffeem=coffeematch[5:10]

#find price using findall
coffeeprice=findall('<span class="s-item__price">([AU $[0-9]+\.[0-9]+)</span>',html1_code1)
coffeep=coffeeprice[0:5]

#GAMES AND TOYS DEAL-LIVE 2

 # Define url for the live web document of Games and toys deal
url1 = 'https://www.dealnews.com/c186/Gaming-Toys/?sort=time'

    # Get a link to the web page from the server, using one
    # of the URLs above
game_page = urlopen(url1)

    # Extract the web page's content as a Unicode string
html_code1 = game_page.read().decode('UTF-8')
def product2():
    # Define url for the live web document of Games and toys deal
    url1 = 'https://www.dealnews.com/c186/Gaming-Toys/?sort=time'

    # Get a link to the web page from the server, using one
    # of the URLs above
    game_page = urlopen(url1)

    # Extract the web page's content as a Unicode string
    html_code = game_page.read().decode('UTF-8')

    # close the connection to the web server
    game_page.close()

    #open new HTML file
    sf_game_file = open(image_file, 'w', encoding = 'UTF-8')

    # HTML header
    game_code='''<!DOCTYPE html>
    <html>
      <head>
          <title>Games and Toys</title>
      </head>
      <body>
          <h1 align="center">Pandamic Products: on Offer </h1>
          <p align="center">
          Games & Toys<a href="https://www.dealnews.com/c186/Gaming-Toys/?sort=time"><em>https://www.dealnews.com/c186/Gaming-Toys/?sort=time</em></a>
          </p>

          <table align="center" border="2"style="width:70%">\n

    '''
    gamematch=findall('title="([A-Z a-z 0-9 , . - ! ()]*)">',html_code)
    gamem=gamematch[12:17]
    gameimg=findall('data-bg-src=([A-Za-z0-9-"()=:./ $;,_?~\'\s]*).jpg',html_code)
    gi=gameimg[12:17]
    for index in range(min(len(gamem),len(gi))):
        game_code+=f"<tr >\n<th>{gamem[index]}<br><img src={gi[index]}.jpg'width=200 height=300/></th></tr>"
    game_code+="\n</table>\n</body>\n</html>"

    # Write the standard HTML "footer" markups into your file
    # to complete the document
    sf_game_file .write(game_code)

    # Close your HTML file (which you can now view in a web browser)
    sf_game_file .close()

#find title using findall
gamematch=findall('title="([A-Z a-z 0-9 , . - ! ()]*)">',html_code1)
gamem=gamematch[12:17]

#find title using findall
gameprice=findall('<span class="callout-comparison">([0-9,$]*)</span>',html_code1)
gamep=gameprice[0:5]

#VINTAGE RUGS-STATIC 1

#opens and reads the html source file
vintage_contents1=open('Vintage Rugs.html',errors='ignore').read()

def product3():    
    #opens and reads the html source file
    vintage_contents=open('Vintage Rugs.html',errors='ignore').read()

    #open new file
    sf_vintage_file = open(image_file, 'w', encoding = 'UTF-8')

    #HTML header
    html2_code='''<!DOCTYPE html>
    <html>
      <head>
          <title>Coffee</title>
      </head>
      <body>
          <h1 align="center">Pandamic Products: on Offer </h1>
          <p align="center">
          Vintage Rugs <a href="file:///https://www.persianrugs.com.au/vintage-rugs"><em>https://www.persianrugs.com.au/vintage-rugs</em></a>
          </p>

          <table align="center" border="2"style="width:70%">\n

    '''
    vintmatch=findall('data-product-title="([A-Z a-z 0-9 , . - ! ()]*)" data-product-id',vintage_contents)
    vm=vintmatch[0:5]
    vinimg=findall('<img class([]A-Za-z0-9-"()=:./ _?\s]*)/>',vintage_contents)
    vi=vinimg[0:5]
    for index in range(min(len(vm),len(vi))):
        html2_code+=f"<tr >\n<th>{vm[index]}<br><img class{vi[index]}width=200 height=300/></th></tr>"
    html2_code+="\n</table>\n</body>\n</html>"

    # Write the standard HTML "footer" markups into your file
    # to complete the document
    sf_vintage_file.write(html2_code)

    # Close your HTML file (which you can now view in a web browser)
    sf_vintage_file.close()

#find title using findall
vintmatch=findall('data-product-title="([A-Z a-z 0-9 , . - ! ()]*)" data-product-id',vintage_contents1)
vm=vintmatch[0:5]

#find title using findall
vintprice=findall('<span class="price-value">([0-9,$]*)</span>',vintage_contents1)
vp=vintprice[0:5]

#JIGSAW PUZZLE-STATIC 2
#opens and reads the html source file
jigsaw_contents1=open('Jigsaw Puzzles.html',errors='ignore').read()
def product4():   
    #opens and reads the html source file
    jigsaw_contents=open('Jigsaw Puzzles.html',errors='ignore').read()

    #open new file
    sf_puzzle_file = open(image_file, 'w', encoding = 'UTF-8')

    # HTML header
    html3_code='''<!DOCTYPE html>
    <html>
      <head>
          <title>Jigsaw Puzzles</title>
      </head>
      <body>
          <h1 align="center">Pandamic Products: on Offer </h1>
          <p align="center">
          Jigsaw Puzzles <a href="https://www.etsy.com/au/search?q=jigsaw+puzzles&order=date_desc"><em>https://www.etsy.com/au/search?q=jigsaw+puzzles&order=date_desc</em></a>
          </p>

          <table align="center" border="2"style="width:70%">\n

    '''
    jigmatch=findall('title="([A-Z a-z 0-9 , . - !]*)',jigsaw_contents)
    jm=jigmatch[3:8]
    jigimg=findall('<img([]A-Za-z0-9-"()=:./ _?\s]*)/>',jigsaw_contents)
    ji=jigimg[0:5]
    #print(ji)
    #for html_code in range(sf_puzzle_1):
    for index in range(min(len(jm),len(ji))):
        html3_code+=f"<tr >\n<th>{jm[index]}<br><img{ji[index]}width=200 height=300/></th></tr>"
    html3_code+="\n</table>\n</body>\n</html>"

    # Write the standard HTML "footer" markups into your file
    # to complete the document
    sf_puzzle_file.write(html3_code)

    # Close your HTML file (which you can now view in a web browser)
    sf_puzzle_file.close()

#find title using findall
jigmatch=findall('title="([A-Z a-z 0-9 , . - !]*)',jigsaw_contents1)
jm=jigmatch[3:8]

#find title using findall
#print("price:")
jigprice=findall('([0-9]+\.[0-9]+)</span>',jigsaw_contents1)
jp=jigprice[0:7]
del jp[4:6]

#Fuction to display the top 5 products in box_1

def displaybox_1():
    global instore_today_thing
    instore_today_thing = 1
    # print(instore_today_thing)
    box_1.delete('1.0', END)
    box_1.insert(END,'Coffee:')
    #order the items in a list
    for idx,(name,price) in enumerate(zip(coffeem,coffeep),1):
        box_1.insert(END,f"\n{idx}. {name} ({price})")
    box_1.insert(END,f"\n\nhttps://www.ebay.com.au/b/Coffee/185036/bn_99762518?rt=nc&_sop=10")

def displaybox_2():
    global instore_today_thing
    instore_today_thing = 2
    box_1.delete('1.0', END)
    box_1.insert(END,'Games and Toys:')
    #order the items in a list
    for idx,(name,price) in enumerate(zip(gamem,gamep),1):
        box_1.insert(END,f"\n{idx}. {name} (AU{price})")
    box_1.insert(END,f"\n\nhttps://www.dealnews.com/c186/Gaming-Toys/?sort=time")

def displaybox_3():
    global instore_today_thing
    instore_today_thing = 3
    box_1.delete('1.0', END)
    box_1.insert(END,'Vintage Rugs:')
    #order the items in a list
    for idx,(name,price) in enumerate(zip(vm,vp),1):
        box_1.insert(END,f"\n{idx}. {name} (AU{price})")
    box_1.insert(END,f"\n\nhttps://www.persianrugs.com.au/vintage-rugs")
    
def displaybox_4():
    global instore_today_thing
    instore_today_thing = 4
    box_1.delete('1.0', END)
    box_1.insert(END,'Jigsaw Puzzles:')
    #order the items in a list
    for idx,(name,price) in enumerate(zip(jm,jp),1):
        box_1.insert(END,f"\n{idx}. {name} (AU${price})")
    box_1.insert(END,f"\n\nhttps://www.etsy.com/au/search?q=jigsaw+puzzles&order=date_desc")
    #sf_puzzle_file = open(image_file, 'w', encoding = 'UTF-8')
    
#function to define the current choice when add to list is pressed
def shopper_choice():
    #box_2.delete("2.0",START)
    #box_2.delete('1.0'," 1 lines" )
    box_2.insert(END,'Your shopping cart:\n\n')
    #box_2.delete('3.0',END)
    box_2.insert(INSERT, box_1.get("2.0","end- 1 lines")+'\n')
    #box_2.append
    #box_2.insert(END,radio_button4.get(command=displaybox_4))
    #box_2.insert(END,f"* {box_1}")
    #box_2.insert(END,box_1.get())
    #j.append(the_button2.get())

#function to define the radiobutton
#def radio_button():
 #   if instore_today_coffeestatus.get()==1:
  #  elif instore_today_gamesstatus()==2:
   # elif oldstock_onorder_vintagestatus.get()==3:
    #else status.get()==4:

#CREATING GUI
        
#Create a root window
pan_window=Tk()

#define the geometry of the window
pan_window.geometry('450x500')

#provide title to the root window
pan_window.title('Pandemic Products: Shop at Home')

#Create a label widget(fixed text)
the_label=Label(pan_window,text='Pandemic Products:Shop at Home',
                font=('Arial',15),fg='navy blue')

#Import image to the root window
online_shopping=PhotoImage(file='logo1.gif')

#create a button widgets for parent container
the_button1=Button(pan_window,text='Show images',font=('Arial',10),
                   fg='green',command=call_product_function)
the_button2=Button(pan_window,text='Add products to cart',
                   font=('Arial',10),fg='green',command=shopper_choice)
the_button3=Button(pan_window,text='Submit order',
                   font=('Arial',10),fg='green')
                   #command=shopper_choice)

#Boolean variable status
instore_today_coffeestatus = IntVar()
instore_today_gamesstatus = IntVar()
oldstock_onorder_vintagestatus = IntVar()
oldstock_onorder_jigsawstatus = IntVar()

#function to define a single product selection
#def product():
 #   if instore_today_coffeestatus.get()==1:
  #      print 
    
  #  if instore_today_chocolatestatus.get()==2:
   # if oldstock_onorder_vintagestatus.get()==3:
    #if oldstock_onorder_jigsawstatus.get()==4:

            
#create LabelFrame widgets to hold the radiobuttons
instore_today=LabelFrame(pan_window,relief='groove',
                         font=('Arial',10),borderwidth=2,
                         text='In store today',fg='navy blue')
oldstock_onorder=LabelFrame(pan_window,relief='groove',
                         font=('Arial',10),borderwidth=2,
                         text='Old stock on order',fg='navy blue')

#Create radiobutton for the items

radio_button1=Radiobutton(instore_today,text='Coffee',value=1,
                          variable=instore_today_thing,
                          font=('Arial',10),fg='green',command=displaybox_1)
# print(instore_today_coffeestatus)
radio_button2=Radiobutton(instore_today,text='Games & Toys',value=2,
                          variable=instore_today_thing,
                          font=('Arial',10),fg='green',command=displaybox_2)
radio_button3=Radiobutton(oldstock_onorder,text='Vintage Rugs',value=3,
                          variable=instore_today_thing,
                          font=('Arial',10),fg='green',command=displaybox_3)
radio_button4=Radiobutton(oldstock_onorder,text='Jigsaw puzzles',value=4,
                          variable=instore_today_thing,
                          font=('Arial',10),fg='green',command=displaybox_4)

#Create 2 text area to display the list
#text area1 for viewing item
box_1=ScrolledText(pan_window,
           width=27,height=11, font = ('Arial',10),wrap=WORD,
          borderwidth = 2, relief = 'groove',fg='navy blue',
           yscrollcommand=set())

#text1="Please select a product category"
box_1.insert(END,'Please select a product category')
         
#text area2 for diplaying item of shopper's choice
box_2=ScrolledText(pan_window,
           width=27,height=11, font = ('Arial',10),wrap=WORD,
          borderwidth = 2, relief = 'groove',fg='navy blue',
           yscrollcommand=set())
box_2.insert(INSERT,"Nothing ordered yet")

#pack the labels and widgets
the_label.place(x=70,y=5)
Label(pan_window,image=online_shopping).place(x = 15, y = 40)
the_button1.place(x = 290, y = 210)
the_button2.place(x = 55, y = 450)
the_button3.place(x = 275, y = 450)

#grid geometry manger for placing the radiobuttons
radio_button1.grid(row = 1, sticky = 'w')
radio_button2.grid(row = 2, sticky = 'w')
radio_button3.grid(row = 1, sticky = 'w')
radio_button4.grid(row = 2, sticky = 'w')

#grid geometry manger for placing the widgets
instore_today.place(x = 270, y = 55)
oldstock_onorder.place(x = 270, y = 130)
box_1.place(x=15,y=253)
box_2.place(x=230,y=253)

#Start the event loop to react to user inputs
pan_window.mainloop()

