# ------------------------------------
# libraries required for bot running
# --------------------------------------

import csv
from os import error, path
import re
import time
import pyautogui
from pyautogui import *
import pandas as pd
import random
import json
import pyperclip

# ----------------------------------

def leave_website_popup_appear(): 

    """
    This function is used to click on the Leave Website pop up , if it was appear then simply click or press enter and returns  False
    """

    if LocateImageOnScreen('./Screenshots/leave.png') == True: 

        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter') 

        return True 
    
    else: 
        return False
    

def FindImagesOnScreen(ListOfImages):

    """
    This function is used to find the multiple images on the screen, when any of the image was find it contains
    it returns the (x,y) cordinates where image was found.
    """
    cordinates = []

    for image in ListOfImages:

        if LocateImageOnScreen(image) == True:
            cordinates = Locate_PNGImageOnScreen(image)
            break 
    
    return cordinates


def Find_Maximum_Images_On_Screen(ListOfImages): 

    image_names = []

    for image in ListOfImages:

        if LocateImageOnScreen(image) == True:            
            image_names.append(image)
            
    
    return image_names

def redirect_url(link):

    """
    This function is used to redirect the group link...
    """

    # Press Ctrl + L to selsect the address bar
    pyautogui.hotkey('ctrl', 'l')

    # Wait for the address bar to become active
    time.sleep(1)

    # print("link to write is ",link)
    
    # Type the URL and press Enter
    # pyautogui.typewrite(link,interval=0.05)
    pyautogui.write(link)
    pyautogui.press('space')
    # time.sleep(1)
    pyautogui.press('enter')
    please_wait_for_sometime('./Screenshots/redirect.png')

def ClickImageOnScreen(image_png,total_clicks):
    # this function is used to search the image on screen and returns the co-ordinates

    cordinates = pyautogui.locateCenterOnScreen(image_png, grayscale=True, confidence=0.8)
    pyautogui.click(cordinates[0],cordinates[1],clicks=total_clicks)


def find_image_on_screen(image_png): 

    """
    This function is used to find image on screen, 
    If it was find return True otherwise False
    """
    if len(Locate_PNGImageOnScreen(image_png)) > 0: 
        return True  

    else: 
        return False


def find_specific_image(image_png):

    """
    This function is used to find the specific image on the screen by pressing the Number of tabs on the screen 
    when the image was found then it simply break the function 
    """

    while(True):

        if LocateImageOnScreen(image_png) == True:         
            break 
        time.sleep(0.5)
        pyautogui.press('tab')

def open_new_tab_with_inspect_element():

    """
    this function is used to open new tab in google chrome and with inspect element
    """
    time.sleep(1)
    pyautogui.hotkey('ctrl','t')
    time.sleep(2)

    pyautogui.hotkey('ctrl','shift','i')

# def Locate_PNGImageOnScreen(image_png):

#     # this function is used to search the imsage on screen and returns the co-ordinates
#     # time.sleep(4)

#     if pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8) != None:
#         cordinates = pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8)
#         position = []
#         position.append(cordinates[0])
#         position.append(cordinates[1])
#         return position
#     else:
#         return []

def ClickAllImagesOnScreen(image_path):
    pass


def Locate_PNGImageOnScreen(image_png):

    # this function is used to search the imsage on screen and returns the co-ordinates
    # time.sleep(4)

    try:

        if pyautogui.locateCenterOnScreen(image_png, grayscale=True, confidence=0.8) != None:
            cordinates = pyautogui.locateCenterOnScreen(image_png, grayscale=True, confidence=0.8)
            position = []
            position.append(cordinates[0])
            position.append(cordinates[1])
            return position
        else:
            return [] 
    
    except pyautogui.ImageNotFoundException: 
        return []


def move_cursor():

    """    
    This function is used to move the cursor to left side of screen where Twitter Icon was place
    """ 

    pyautogui.moveTo(100,100)

    # cordinates = Locate_PNGImageOnScreen('.//Images/ICON.png') 
    # pyautogui.click(cordinates[0]+120,cordinates[1])
    # time.sleep(1)

def Click_PNGImageOnScreen(image_png,_x,_y,total_clicks):
    # this function is used to search the image on screen and returns the co-ordinates

    if len(Locate_PNGImageOnScreen(image_png)) > 0:

        cordinates = pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8)
        pyautogui.click(cordinates[0]+_x,cordinates[1]+_y,clicks=total_clicks) # (x,y) 

    else:
        pass

# def LocateImageOnScreen(image_png):

#     # this function is used to search the image on screen and returns the co-ordinates
#     # time.sleep(4)

#     if pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8) != None:
#         return True
#     else:
#         return False

def LocateImageOnScreen(image_png):

    # this function is used to search the image on screen and returns the co-ordinates
    # time.sleep(4)

    try:

        if pyautogui.locateCenterOnScreen(image_png, grayscale=True, confidence=0.8) != None:
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException as e:
        # print("exception block") 
        return False


def locate_when_appear(png_image):
    """
    This function is used to find image when it appears...
    It prevents the unwanted time sleeps
    """
    counter = 0
    while(True):
        
        try:

            if LocateImageOnScreen(png_image) == True: 
                break
            else: 
                time.sleep(1)

            counter += 1
            if counter == 7:
                break
        
        except pyautogui.ImageNotFoundException:
            pass


def click_when_appear(png_image):
    """
    This function is used to click on image when it appears...
    It prevents the unwanted time sleeps
    """

    while(True): 
        if LocateImageOnScreen(png_image) == True: 
            ClickImageOnScreen(png_image,1)
            break
        else: 
            time.sleep(0.5)

def press_up_key(n_times):
    """
    Press UP key on keyboard
    """
    for i in range(0,n_times):
        pyautogui.press('up')

def press_arrow_keys(arrow_,times):

    for i in range(0,times):
        pyautogui.hotkey(arrow_)

def press_down_keys(n_times):

    for i in range(0,n_times):
        pyautogui.press('down')

def press_up_key(n_times):

    for i in range(0,n_times):
        pyautogui.press('up')

def press_tab_key(times):

    for i in range(0,times):
        pyautogui.press('tab')


def please_wait(png_image):

    """
    Wait until appear... 
    """
    while(True):

        try:

            if LocateImageOnScreen(png_image) == True: 
                break  

            time.sleep(1)
        
        except pyautogui.ImageNotFoundException: 
            pass


def please_wait_for_multi_images(list_of_images):

    """
    this function is used to handle the multiple images on the screen... 
    once they appears on the screen ...
    """

    while(True):

        try:
            
            if len(FindImagesOnScreen(list_of_images)) > 0:
                break  

            time.sleep(1)
        
        except pyautogui.ImageNotFoundException: 
            pass

        # print("error...")


def please_wait_for_sometime(png_image):

    """
    This function is used to wait for sometime if image wasn't appear then it simply break the function , this is very useful in case of dynamic images, especially in such cases when due to slow internet connection or slow computer speed due to lack of good hardware... 
    """
    counter = 0
    while(True):

        try:

            if LocateImageOnScreen(png_image) == True: 
                break 

            else:
                time.sleep(0.5)
                counter += 1 
        
            if counter > 5:
                break
        
        except pyautogui.ImageNotFoundException:
            pass
    
    if counter < 5: 
        return True
    
    else:
        return False

def click_on_inspect_element_scrollbar():

    axes = Locate_PNGImageOnScreen('./Images/settings.png')

    for i in range(0,7):
        pyautogui.click(axes[0]+75,axes[1]+25)

def regulate_chrome_browser():

    time.sleep(2)

    if LocateImageOnScreen('./Screenshots/redirect.png') == True or LocateImageOnScreen('./Screenshots/redirect_icognito.png') == True: 
        return True 
    
    else:
        return False

def find_head_tag():

    axes = Locate_PNGImageOnScreen('./Screenshots/settings.png')


    while(True):

        if find_image_on_screen('./Screenshots/body.png') == True:
            break

        else:
            pyautogui.click(axes[0]+75,axes[1]+245)


        time.sleep(1)


# def scrolling_function(cordinates,total_clicks):

#     """
#     This function is used to scroll down the screen
#     """

#     height = win32api.GetSystemMetrics(1)
#     y = height - 82 

#     pyautogui.click(cordinates[0]+184,y,clicks=total_clicks)
#     # pyautogui.click(cordinates[0]+50,cordinates[1]-13,clicks=total_clicks)

def press_backspace(number):

    for i in range(0,number):
        pyautogui.press("backspace")


def redirect_file_path(filename,folder_path):
    
    axes = pyautogui.locateOnScreen('.//Images/up.png') 
    pyautogui.click(axes[0]+700,axes[1],clicks=1)

    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)

    pyautogui.typewrite(folder_path,interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)

    # click on filename...
    axes = pyautogui.locateOnScreen('.//Images/filename.png')
    pyautogui.click(axes[0]+300,axes[1],clicks=1)
    time.sleep(1)

    pyautogui.typewrite(filename,interval=0.05)
    pyautogui.press('enter')

    # auto-check condition to terminate the 
    time.sleep(7)

    if find_image_on_screen('.//Images/post.png') == False:

        # print("Post image not found...")

        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab') 
        pyautogui.press('tab') 
        time.sleep(1)

        pyautogui.press('enter')

def if_this_image_appear_on_screen(png_image):

    """
    This function wait for 3 secs to check the certain image was appear on screen or not...
    """

    flag = False
    counter = 0

    while(True):
        if find_image_on_screen(png_image) == True:
            flag = True
            pyautogui.press('enter')
            time.sleep(1)
            break 

        counter += 1 
        time.sleep(1)

        if counter == 3:
            break    
    
    return flag

def maximimize_chrome():

    ClickImageOnScreen('./Images/maximum.png',1)


def copy_url():
    # Bring the Chrome window to the front
    # pyautogui.hotkey('alt', 'tab')

    # Give the window a moment to come to the front
    time.sleep(1)

    # Select the address bar
    pyautogui.hotkey('ctrl', 'l')

    # Copy the URL
    pyautogui.hotkey('ctrl', 'c')

    # Give the clipboard a moment to update
    time.sleep(1)

    # Get the URL from the clipboard
    url = pyperclip.paste()

    # ClickImageOnScreen

    return url

def copy_text():

    # Bring the Chrome window to the front
    # pyautogui.hotkey('alt', 'tab')
    # Give the window a moment to come to the front
    time.sleep(1)

    # Select the address bar
    pyautogui.hotkey('ctrl', 'a')

    # Copy the URL
    pyautogui.hotkey('ctrl', 'c')

    # Give the clipboard a moment to update
    time.sleep(1)

    # Get the URL from the clipboard
    text = pyperclip.paste()
    # pyautogui.press('left')
    time.sleep(1)

    # axes = pyautogui.position()

    # ClickImageOnScreen

    return text

def cancel_google_translate_popup():

    """
    this function is used to cancel the google translate pop up and see more facebook pop up in case of appearence on a page due to icognito mode ...
    """

    # boolean = please_wait_for_sometime('./Screenshots/google_trans.png')

    # if boolean == True:
    if LocateImageOnScreen('./Screenshots/google_trans.png') == True: 

        time.sleep(1)
        pyautogui.press('esc')

    if LocateImageOnScreen('./Screenshots/see_more_on_fb.png') == True: 
        pyautogui.press('esc')
        

# print("start /_")
# time.sleep(4)
# text = copy_text()
# print(text) 

# ClickImageOnScreen('./Images/elements.png',1)

# click_on_inspect_element_scrollbar()
# axes = Locate_PNGImageOnScreen('./Images/all_filters.png')
# scrolling_function(axes,1)
# find_head_tag()

# print("starts /_")
# time.sleep(5)
# redirect_url('https://www.google.com.pk/')
# open_new_tab_with_inspect_element()
# redirect_url('https://ventsmagazine.com/2022/08/30/aaron-sand-releases-emotional-new-single-still-here/')
# flag = please_wait_for_sometime('./Screenshots/posts.png')
# print(flag)

# URL = copy_url()
# print(URL)

# time.sleep