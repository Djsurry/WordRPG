##-- This module is to hadle all the print screens for the menus --##

##-- All Imports --##
from colorama import init, Fore, Back, Style
import os, time, sys
import Mobs


##-- Font Colors --##

init(convert=True)

white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
light_red = Fore.LIGHTRED_EX
cyan = Fore.CYAN

##-- Clear Function --##

def clear():
    
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

##-- Main Menu --##

def main_menu_screen():
    
    first = light_red + 'WELECOME TO THE WASTE LAND'
    num1 = green + '1'
    num2 = green + '2'
    num3 = green + '3'
    num4 = green + '4'
    start = yellow + 'START'
    load = yellow + 'LOAD'
    help = yellow + 'HELP'
    quit = yellow + 'QUIT'

    line1 = f"{cyan}####################################################################################################"
    line2 = f"#-                                   {first}                                   {cyan}-#"
    line3 = "#-                                                                                                -#"
    line4 = f"#-                                           ({num1}{cyan}): {start}                                           {cyan}-#"
    line5 = f"#-                                           ({num2}{cyan}): {load}                                            {cyan}-#"
    line6 = f"#-                                           ({num3}{cyan}): {help}                                            {cyan}-#"
    line7 = f"#-                                           ({num4}{cyan}): {quit}                                            {cyan}-#"
    line8 = f"#-                                                                                                -#"
    line9 = f"#-                                   {red}SELECT A NUMBER TO CONTINE                                   {cyan}-#"
    line10 = f"#-                                       {red}Copy Write 2018                                          {cyan}-#"
    line11 = f"#-                                  {red}Writen by Bobby & Fernando                                    {cyan}-#"
    line12 = f"####################################################################################################"

    lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    
    clear()
    
    for i in lines:
        print(i)

def char_options():

    first = light_red + 'SELECT A CLASS TO BE'
    num1 = green + '1'
    num2 = green + '2'
    num3 = green + '3'
    num4 = green + '4'
    mage = yellow + 'MAGE'
    warrior = yellow + 'WARRIOR'
    archer = yellow + 'ARCHER'
    assassin = yellow + 'ASSASSIN'

    line1 = f"{cyan}####################################################################################################"
    line2 = f"#-                                       {first}                                     {cyan}-#"
    line3 = "#-                                                                                                -#"
    line4 = f"#-                                           ({num1}{cyan}): {mage}                                            {cyan}-#"
    line5 = f"#-                                           ({num2}{cyan}): {warrior}                                         {cyan}-#"
    line6 = f"#-                                           ({num3}{cyan}): {archer}                                          {cyan}-#"
    line7 = f"#-                                           ({num4}{cyan}): {assassin}                                        {cyan}-#"
    line8 = f"#-                                                                                                -#"
    line9 = f"#-                                   {red}SELECT A NUMBER TO CONTINE OR                                {cyan}-#"
    line10 = f"#-                     {red}TYPE 'INFO' THEN SPACE AND A NUMBER, FOR INFORMATION ON CLASS              {cyan}-#"
    line11 = f"#-                                           {red}EXSAMPLE: INFO 1                                     {cyan}-#"
    line12 = f"####################################################################################################"

    lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    
    clear()
    
    for i in lines:
        print(i)
    

##-- This is for the start of the story and to get the players name --##

def name_player(player_class):

    line1 = '#' * len(player_class) + '#' * 30
    line2 = '#- ' + f'So you want to be a {player_class} hu?' + ' -#' 
    line3 = '#- ' + 'What shall I call you?' + (' ' * len(player_class)) + '   -#'
    line4 = '#' * len(player_class) + '#' * 30

    lines = [line1, line2, line3, line4]
    
    clear()
    
    for i in lines:
        print(i)
##-- This is for the main story line and to update the player what is happening --##
##-- Needs work but we can come back to it when we get to adding story          --##

def main_game_screen(story):

    line1 = '#' * len(story) + '#' * 30
    line2 = f'# {story} #'
    line3 = '#' * len(story) + '#' * 30

    lines = [line1, line2, line3]
    
    clear()
    
    for i in lines:
        print(i)

##-- This shows who is fighing and there stats --##

def combat_screen(player, mob):

    width = (len(player.name) + len(mob.name) + 43) ##  Width sets how big the screen is no matter
    print('#' * width)                              ##  How big the names or stats are
    print(f"#              {player.name}  -- VS --  {mob.name}               #")
    print('#' * (len(player.name) + len(mob.name) + 43))

    left = f"{player.name}    "                                   ##  Left side is for player
    right = f"    {mob.name}"                                     ##  Right side is for Enemy
    line = left + ' ' * (width - (len(left) + len(right))) + right##  Line puts the Left and Right 
                                                                  ##  Sides together and uses width
    left1 = f"Level: {player.level}    "                          ##  varible to know how many space
    right1 = f"    {mob.level} :Level"                            ##  to print
    line1 = left1 + ' ' * (width - (len(left1) + len(right1))) + right1

    left2 = f"Health: {player.max_health}    "
    right2 = f"    {mob.max_health} :Health"
    line2 = left2 + ' ' * (width - (len(left2) + len(right2))) + right2

    left3 = f"Armor: {player.armor}    "
    right3 = f"    {mob.armor} :Armor"
    line3 = left3 + ' ' * (width - (len(left3) + len(right3))) + right3

    left4 = f"Mana: {player.mana}    "
    right4 = f"    {mob.mana} :Mana"
    line4 = left4 + ' ' * (width - (len(left4) + len(right4))) + right4

    left5 = f"Stamina: {player.stamina}    "
    right5 = f"    {mob.stamina} :Stamina"
    line5 = left5 + ' ' * (width - (len(left5) + len(right5))) + right5

    left6 = f"Luck: {player.luck}    "
    right6 = f"    {mob.luck} :Luck"
    line6 = left6 + ' ' * (width - (len(left6) + len(right6))) + right6
    
    print(line)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
