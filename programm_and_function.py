# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:00:19 2022

@author: Patrick Ablinger
"""
import time

KMHTOMS = True

def printHelpText():
    if KMHTOMS:
        string = '[km/h] -> [m/s]'
    else:
        string = '[m/s] -> [km/h]'
    print('==================================== \n ')
    print('Die aktuelle Umrechnung ist {}.'.format(string))
    print('[exit] Beenden Sie das Programm indem sie "exit" eingeben.')
    print('[/help] Rufen Sie diese Hilfe Funktion auf.')
    print('[/toggle] Ändern Sie die Umrechnungsrichtung.')
    print('[/rotate] Für echte Geniesser!')
    print('[/m/s] Umrechnen in [m/s].')
    print('[/s/m] Umrechnen in [s/m].')
    print('\n==================================== \n ')
    
def CommandHandler(input_string):
    global KMHTOMS
    lwrd = input_string.lower()
    if lwrd in ['/', '/h', 'help', '/help', '/hilfe', 'hilfe', '/info']:
        printHelpText()
        return 2 #exit code 'Change Needed'
    
    if lwrd in ['/toggle', '/t']:
        if KMHTOMS:
             KMHTOMS = True
             print('Nun wird von km/h in m/s umgerechnet.')
        else:
             KMHTOMS = False
             print('Nun wird von km/h in s/m umgerechnet.')        
        return 2 #exit code 'Change Needed'
    
    if lwrd in ['/exit', 'exit', 'e', '/e']:
        print('Vielen Dank für das Nutzen dieses Tools.')
        print('© Patrick Ablinger, 2022')
        return 0 #0 is exit key
    
    if lwrd in ['/rotate', 'rotate', '/r', 'r']:
        
        return 2
    
    if lwrd in ['m/s', '/m/s', '[/m/s]', '/[/m/s]']:
        KMHTOMS = True
        print('Nun wird von [km/h] in [m/s] umgerechnet.')
        return 2
    
    if lwrd in ['s/m', '/s/m', '[/s/m]', '/[/s/m]']:
        KMHTOMS = False
        print('Nun wird von [km/h] in [s/m] umgerechnet.')
        return 2
    return 1 #if no keyword --> try continuing processing


def loading_function():
    print("Processing Input: ##", end = ' ', flush=True)
    for i in range(6):
        time.sleep(0.2)
        print("##", end=' ', flush=True)
    print(" ")
    time.sleep(0.2)
    print("Calculation Finished!")
    time.sleep(1)
    return
    

def kmh2ms(input_float, round = 0):
    """
    This function converts km/h to m/s and s/m
    returns a tuple of (m/s, s/m).
    
    Note that this function itself does not check wheter your inputs are of
    correct data type.

    Parameters
    ----------
    input_float : FLOAT or INT (Number)
        input: kilometers/h which you want to calculate to m/s or s/m

    Returns
    -------
    ms : FLOAT
        result in meter/seconds.
    sm : FLOAT
        result in seconds/meter.

    """
    
    ms = input_float / 3.6
    sm = 1/ms
    return ms, sm

def prepareString(input_string):
    """
    

    Parameters
    ----------
    input_string : string of input

    Returns
    -------
    out_str : prepared string

    comma_n : int number of float values (int)
        
    """
    kmh_f = input_string[::-1] #reversing the input string to easier find number of values before comma
    out_str = '' #defining empty string which is going to be filled with useble '.'
    comma_n = 0 #if there is no , or . than the value is just 0
    for i, char in enumerate(kmh_f): #finding missleading ',' in string and finding out the number of float values (for rounding afterwards)
        if char in [',','.']: #checking if floating value is reached
            comma_n = i #get the index of , or . (That's how many values are after , because of reverse iteration through string)
            if char == ',': #correction check
                char = '.' #correction step
        out_str += char #out string is always without , but whith . (good!)
    return out_str, comma_n #returning fast tuple
            
def validateString(input_string, comma_n):
    """
    

    Parameters
    ----------
    input_string : adapted prepared string
       
    comma_n : int comma from 'prepareString' function

    Returns
    -------
    out_float : validated float from input_string

    comma_n : (recalculated) int number of float values (int)

    """
    
    while True: #endless loop until string is validated as float
        
        try :
            
            out_float = float(input_string)   # try to cast to float type 
            break          #break if out_float is casted correctly   
        except ValueError:
            print('Bitte gib eine richtige Zahl ein z.B.: 7,2 oder 7.2 ')
            raw = input() #restart process
            input_string, comma_n = prepareString(raw) #prepare new input
            

    return out_float, comma_n
        

def TransTo():
    meter_sec = (abs(float_valid / 3.6)) #actual calculation into m/s --> abs value because speed is always abs compared to velocity
    if KMHTOMS:          
        return meter_sec
    else:
        sec_meter = 1/meter_sec #invert
        return sec_meter
    
#=============================================================================

    

print('Falls Sie Hilfe benötigen, geben Sie /help ein.')   
print('Beenden Sie das Programm indem sie "exit" eingeben.')
print('Bitte geben Sie die gegebenen km/h ein: ')
while True:  
    kmh = input()
    continueValue = CommandHandler(kmh)
    if continueValue == 0:
        break    #exit main loop
    if continueValue == 1:
        pass #do nothing (continue value == 1)
    if continueValue == 2:
        print('Entern Sie bitte ihre neue Eingabe.')
        continue #repeat Process

   

    prepared_str, nFloat = prepareString(kmh) #prepare string and number of float values
    float_valid, nFloat = validateString(prepared_str, nFloat) #converting string or restart

    calculated = TransTo()
    

    loading_function()
    if KMHTOMS:
        unit = ['[m/s]']
    else:
        unit = ['[s/m]']
    print('Ihre Eingabe beträgt umgerechnet {} {}. \n'.format(round(calculated, nFloat+1), unit[0]))     #round + 1 because you want to know n+1 comma values
    




