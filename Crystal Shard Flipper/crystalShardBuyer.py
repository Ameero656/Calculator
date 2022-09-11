from pydoc import locate
import pyautogui as pg
import time
import pytesseract
from PIL import ImageGrab
import imutils
import random
import keyboard

crystal_location =1766, 813
gold_block = 1774, 886
purchase = 1919, 957
confirm_purch = 1776, 916

def locate_position(t):
    time.sleep(t)
    print(pg.position())


def open_gui(mi,ma):
    t=random.randint(mi,ma)
    t/=10
    time.sleep(t)
    pg.click(button='right')

def click_gold_block(mi,ma):
    t=random.randint(mi,ma)
    t/=10
    time.sleep(t)
    pg.moveTo(1774, 886)
    pg.click()

def hover_crystal(mi, ma, shift):
    t=random.randint(mi,ma)
    t/=10
    time.sleep(t)
    if shift ==4:
        pg.moveTo(2061, 804)
    if shift ==3:
        pg.moveTo(1986, 782)
    if shift ==2:
        pg.moveTo(1894, 1140)
    if shift ==1:
        print('Shiftone!')
        pg.moveTo(1825, 798)
    else:
        pg.moveTo(1766, 813)
        time.sleep(t)
    pg.click()
    pg.moveTo(1919, 957)
    time.sleep(.2)
    
def purchase(mi,ma):
    t=random.randint(mi,ma)
    t/=10
    pg.click()
    pg.moveTo(1776, 916),
    time.sleep(t)
    pg.click()



def main():
    budget = input('Max cost per crystal:')
    time.sleep(3)
    shift =0
    floatcount = 0
    
    for x in range(35):
        print("""
Cycle: {x}
===========>""")

        floatcount+=1
        if floatcount >= 2:
            if floatcount == 4:
                floatcount =0
            shift = floatcount-1
        print('Shift:', shift)
        open_gui(4, 7)
        click_gold_block(4, 7) 
        hover_crystal(4,7, shift)
        time.sleep(1)
        img =pg.screenshot()
        img.save(r"G:\programStuff\Calculator\ReadScreen.png")
        print("Screenshot Saved.")
        bin_location =pg.locateOnScreen("pricetag.png",confidence =.6, grayscale=False)
        print(bin_location)

        pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe") 
        try:
            price_img = pg.screenshot(region=(bin_location.left+100, bin_location.top-5, 250, 60))
        except:
            print("Unable to read price tag, continuing routine.")
            continue
        price_img.save(r"G:\programStuff\Calculator\PurchaseCostSnip.png")
        Output=pytesseract.image_to_string(price_img)
        Output = Output.split()
        price = Output[0]
        print('Price registered:',Output[0])
        price=price.replace(',', '')

        if float(price) < float(budget):
            print('purchase Requirements Fufilled.')
            print('Attempting Purchase...')
            purchase(2,2)
            print('Purchase Macro Sucessful.')
        else:
            pg.press('escape')
            print('Too High price, aborting...')
            shift =0
            floatcount=0
            print('Shift and Floatcount have been reset.')
        
        
        
main()
#locate_position(3)