#importing the required modules 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

#creating function for generating recipt
def generatereciept(cust_name , items_purchased , items_price , total_amount , reciept_number):
    filename=f"receipt.{reciept_number}.pdf"
    
    #creating canvas and setting the font
    c = canvas.Canvas(filename,pagesize=A4)
    c.setFont("Helvetica" , 12)
    
    #setting the header
    c.drawString(220,790,"VAISHALI MEDICAL STORE")
    c.drawString(220,750,"Transaction Reciept")
    c.drawString(175,730,"-"*70)
    
    #writting the time and date and reciept number
    c.drawString(50 , 710 , f"Date:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50 , 690 , f"Reciept number : {reciept_number}")
    c.drawString(50 , 670 , f"Customer Name: {cust_name}")
    
    c.drawString(50,650,"Items Purchased:")
    c.drawString(300,650,"Items Price:")
    y_position=630
    for items in items_purchased:
        c.drawString(70,y_position,f"- {items}")
        y_position -= 20
    for items in items_price:
        c.drawString(320,y_position - -60,f"- {priceofitems}")
        y_position -= 20
     
     
    c.drawString(50, y_position-20,"-"*60)
    c.drawString(50, y_position - 40 ,f"Total Amount : Rs.{total_amount}")
     
     #saving the file
    c.save()
     
    print(f"Receipt generated : {filename}")
     
customername="ishaan"
itemspurchased=["lays","redpepper"]
priceofitems=[20,75]
totalprice=95
reciept_number=123456
generatereciept(customername , itemspurchased , priceofitems , totalprice , reciept_number)    
     
