
import sys 
from Cimpl import *
from photo_filters import *

def get_image():
    file = choose_file()
    if file == "":
        sys.exit("File Open cancelled, exiting program")
    img = load_image(file)
    return img

def command_input():
    print('\nL)oad Image\nN)egative G)Grayscale',end='')
    print(' S)olarize 2)-tone 3)-tone\nQ)uit\n')
    i = input(': ')
    return i

if __name__ == "__main__":
    
    i = command_input()
    
    while i != 'Q' and i != 'L':
        if i in ['N','G','S','2','3']:
            print('\n"No Image Loaded"')
        else:
            print('\nNo such command')
        i = command_input()
        
    while i == 'L':
        img = get_image()
        show(img)    
        i = command_input()
        while not i in ['N','G','S','2','3','Q','L']:
            print('\n"No such Command"')
            i = command_input()        
        
    while i != 'Q':    
        if i == 'N':
            img = negative(img)
            show(img)
        elif i == 'G':
            img = grayscale(img)
            show(img)
        elif i == '2':
            img = black_and_white(img)
            show(img)
        elif i == '3':
            img = black_and_white_and_gray(img)
            show(img)  
        elif i == 'S':
            t = int(input('Threshold? (0-256): '))
            while t<0 or t>256:
                print('\n"Invalid threshold',end='')
                print(' Value. Please try again"\n')
                t = int(input('Threshold? (0-256): '))
            img = solarize(img,t)
            show(img)
            
        i = command_input() 
        
        while not i in ['N','G','S','2','3','Q']:
            print('"\nNo such Command"')
            i = command_input()
                      
    print('\nThanks for using Photo Editor, have a nice day :) ----created by Tejash Patel')
     
        
    
    
        
