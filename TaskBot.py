import pyautogui as pg
import time as t
import os

def AltTab(): #Ready
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')

def ClickAutoClickChannel(): #Ready
    pg.moveTo(2057,178) #Change these values according to the server screen resolution akiid.
    pg.click()

def ClickAndSubmitReview(): #Use after opening the browser tab with the location. Works
    t.sleep(3)
    pg.moveTo(2246,438)
    pg.click()
    t.sleep(3)
    pg.moveTo(2194,531)
    pg.click()
    t.sleep(6)
    #Click the 1st set of stars
    pg.moveTo(3296,268)
    pg.click()
    #Click the 2nd set of stars
    pg.moveTo(3442,359)
    pg.click()
    #Click the 3rd set of stars
    pg.moveTo(3442,437)
    pg.click()
    #Click the 4th set of stars
    pg.moveTo(3442,504)
    pg.click()
    #Move to the textbox write something and hit Post
    pg.moveTo(2971,583)
    pg.click()
    pg.typewrite('Very Nice Spot. I strongly recommend it!')#Will create a list containing various strings for this.
    pg.moveTo(3432,1361)
    pg.click()
    t.sleep(3)

def CloseCurrentWindow():
    pg.keyDown('alt')
    pg.press('f4')
    pg.keyUp('alt')

def MoveToTelegramLink():
    try:
        linkLocation=pg.locateOnScreen('Link8.png') ##Search for it according to an image. IT RECOGNIZES THE A RED HTTPS STRING BEST
        linkCoords=pg.center(linkLocation)
    except pg.ImageNotFoundException:
        return 'ImageNotFoundException: image not found'
    pg.moveTo(linkCoords.x,linkCoords.y)
    return 'OK'

def DeleteSameReview():
    print("IN PROGRESS :)")

def ProgramLoop():
    t.sleep(1)
    counter=1
    while True:
        result=MoveToTelegramLink()
        if result=='OK':
            pg.click()
            AltTab()
            AltTab()
            t.sleep(20)
            ClickAndSubmitReview()
            counterStr=str(counter)
            pg.screenshot(counterStr+".png")
            counter=counter+1
            CloseCurrentWindow()
            quit()
        elif result=='ImageNotFoundException: image not found':
            print('Link Not Found ... Scrolling Down')
            pg.scroll(-1)
        

if __name__ == "__main__":
    #AltTab()
    #clickAutoClickChannel()
    #img=pg.screenshot()
    #img.save('/home/hummus/Desktop/ImageYaBro.png') #Works
    #ClickAndSubmitReview()Works
    t.sleep(3)
    ProgramLoop()
    print(os.getcwd())
    print('This works')
