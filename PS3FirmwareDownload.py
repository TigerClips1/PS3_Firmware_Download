#!/usr/bin/env python3
from PS3Firmwares.PS3Firmware import PS3
import os
import webbrowser

username = input("Please Enter your linux or Windows User name: ")

print("Welcome to my Script this script install PS3 Firmware for WSL or Windows or Linux\n")
print("PS3 Slim and supe slims can only install firmware that 3.75 or higher\n")
print("PS3 Fat can install firmware 1.02-4.90\n")
print("Also Make Sure you set your default browser if you dont do that whale it will open about a lot of cmd or Terminal\n")
print("Make sure to not run as root or it wont work\n")

def open_url(url):
    webbrowser.open(url, new=2)

path =  f"/home/{username}/Downloads"
make = "mkdir PS3"
make4 = f"mkdir UPDATE"
path2 = "PS3"
make2 = "md PS3"
make3 = "md UPDATE"
path3 = "UPDATE"
path4 = f"c:/USER/{username}/Downloads/"

def first():
    if path:
        os.chdir(path)
    else:
        os.chdir(path4)

    if make:
        os.system(make)
    else:
        os.chdir(make2)
    if path2:
        os.chdir(path2)

    if make3:
        os.system(make4)
    else:
        os.system(make3)
    if path3:
        os.system(path3)

def menu_1():
    while True:
        print("[1] PS3_Firmware_489")
        print("[2] PS3_Firmware_488")
        print("[3] PS3_Firmware_487")
        print("[4] PS3_Firmware_486")
        print("[5] PS3_Firmware_485")
        print("[6] PS3_Firmware_484")
        print("[7] PS3_Firmware_482")
        print("[8] PS3_Firmware_481")
        print("[9] PS3_Firmware_480")
        print("[10] PS3_Firmware_478")
        print("[11] PS3_Firmware_476")
        print("[12] PS3_Firmware_475")
        print("[13] PS3_Firmware_470")
        print("[14] PS3_Firmware_466")
        print("[15] PS3_Firmware_465")
        print("[16] PS3_Firmware_460")
        print("[17] Next page 1/6")
        print("[0] Exit")
        option = input("Enter the PS3 firmware you want to install: ") #get input from user
        if option == "1":
            os.system(PS3_Firmware_489)
        elif option == "2":
            os.system(PS3_Firmware_488)
        elif option == "3":
            os.system(PS3_Firmware_487)
        elif option == "4":
            webbrowser.open(PS3.PS3_Firmware_486)
        elif option == "5":
            webbrowser.open_new_tab(PS3_Firmware_485)
        elif option == "6":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_484)
        elif option == "7":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_482)
        elif option == "8":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_481)
        elif option == "9":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_480)
        elif option == "10":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_478)
        elif option == "11":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_476)
        elif option == "12":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_475)
        elif option == "13":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_470)
        elif option == "14":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_466)
        elif option == "15":
            PS3Firmware.webbrowser.open_new_tab(PS3.PS3_Firmware_465)
        elif option == "16":
            webbrowser.open_new_tab(PS3.test)
        elif option == "17":
            menu_2()
        elif option == "0":
            break
        else:
            print("Invalid option")
def menu_2():
    while True:
        print("[18] PS3_Firmware_455")
        print("[19] PS3_Firmware_453")
        print("[20] PS3_Firmware_450")
        print("[21] PS3_Firmware_446")
        print("[22] PS3_Firmware_445")
        print("[23] PS3_Firmware_441")
        print("[24] PS3_Firmware_440")
        print("[25] PS3_Firmware_431")
        print("[26] PS3_Firmware_430")
        print("[27] PS3_Firmware_425")
        print("[28] PS3_Firmware_421")
        print("[29] PS3_Firmware_420")
        print("[30] PS3_Firmware_411")
        print("[31] PS3_Firmware_410")
        print("[32] PS3_Firmware_400")
        print("[33] PS3_Firmware_374")
        print("[34] Next page 2/6")
        print("[35] Back")
        option = input("Enter the PS3 firmware you want to install: ") #get input from user
        if option == "18":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_455)
        elif option == "19":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_453)
        elif option == "20":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_450)
        elif option == "21":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_446)
        elif option == "22":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_445)
        elif option == "23":
            PS3Firmware.webbrowser.open_new_tab(Firmware_441)
        elif option == "24":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_440)
        elif option == "25":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_431)
        elif option == "26":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_430)
        elif option == "27":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_425)
        elif option == "28":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_421)
        elif option == "29":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_420)
        elif option == "30":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_411)
        elif option == "31":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_410)
        elif option == "32":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_400)
        elif option == "33":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_374)
        elif option == "34":
            menu_3()
        elif option == "35":
            menu_1()
        else:
            print("Invalid option")

def menu_3():
    while True:
        print("[36] PS3_Firmware_373")
        print("[37] PS3_Firmware_372")
        print("[38] PS3_Firmware_370")
        print("[39] PS3_Firmware_366")
        print("[40] PS3_Firmware_365")
        print("[41] PS3_Firmware_361")
        print("[42] PS3_Firmware_360")
        print("[43] PS3_Firmware_356_v2")
        print("[44] PS3_Firmware_356_v1")
        print("[45] PS3_Firmware_355")
        print("[46] PS3_Firmware_350")
        print("[47] PS3_Firmware_342")
        print("[48] PS3_Firmware_341_v2")
        print("[49] PS3_Firmware_341_v1")
        print("[50] PS3_Firmware_340")
        print("[51] PS3_Firmware_321")
        print("[52] Next page 3/6")
        print("[53] Back")
        option = input("Enter the PS3 firmware you want to install: ") #get input from user
        if option == "36":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_373)
        elif option == "37":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_372)
        elif option == "38":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_370)
        elif option == "39":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_366)
        elif option == "40":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_365)
        elif option == "41":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_361)
        elif option == "42":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_360)
        elif option == "43":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_356_v2)
        elif option == "44":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_356_v1)
        elif option == "45":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_355)
        elif option == "46":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_350)
        elif option == "47":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_342)
        elif option == "48":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_341_v2)
        elif option == "49":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_341_v1)
        elif option == "50":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_340)
        elif option == "51":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_321)
        elif option == "52":
            menu_4()
        elif option == "53":
            menu_2()
        else:
            print("Invalid option")

def menu_4():
    while True:
        print("[54] PS3_Firmware_316")
        print("[55] PS3_Firmware_315")
        print("[56] PS3_Firmware_310")
        print("[57] PS3_Firmware_301")
        print("[58] PS3_Firmware_300")
        print("[59] PS3_Firmware_280")
        print("[60] PS3_Firmware_276")
        print("[61] PS3_Firmware_270")
        print("[62] PS3_Firmware_260")
        print("[63] PS3_Firmware_253")
        print("[64] PS3_Firmware_252")
        print("[65] PS3_Firmware_250")
        print("[66] PS3_Firmware_243")
        print("[67] PS3_Firmware_242")
        print("[68] PS3_Firmware_241")
        print("[69] PS3_Firmware_240")
        print("[70] Next page 4/6")
        print("[71] Back")
        option = input("Enter the PS3 firmware you want to install: ") #get input from user
        if option == "54":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_316)
        elif option == "55":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_315)
        elif option == "56":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_310)
        elif option == "57":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_301)
        elif option == "58":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_300)
        elif option == "59":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_280)
        elif option == "60":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_276)
        elif option == "61":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_270)
        elif option == "62":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_260)
        elif option == "63":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_253)
        elif option == "64":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_252)
        elif option == "65":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_250)
        elif option == "66":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_243)
        elif option == "67":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_242)
        elif option == "68":
            PS3_Firmware.webbrowser.open_new_tab(PS3_Firmware_241)
        elif option == "69":
            PS3Firmware.webbrowser.open_new_tab(PS3.PS3_Firmware_240)
        elif option == "70":
            menu_5()
        elif option == "71":
            menu_3()
        else:
            print("Invalid option")

def menu_5():
    while True:
        print("[72] PS3_Firmware_236")
        print("[73] PS3_Firmware_235")
        print("[74] PS3_Firmware_230")
        print("[75] PS3_Firmware_220")
        print("[76] PS3_Firmware_217")
        print("[77] PS3_Firmware_216")
        print("[78] PS3_Firmware_210")
        print("[79] PS3_Firmware_201")
        print("[80] PS3_Firmware_200")
        print("[81] PS3_Firmware_194")
        print("[82] PS3_Firmware_193")
        print("[83] PS3_Firmware_192")
        print("[84] PS3_Firmware_190")
        print("[85] PS3_Firmware_182")
        print("[86] PS3_Firmware_181")
        print("[87] PS3_Firmware_180")
        print("[88] Next page 5/6")
        print("[89] Back")
        option = input("Enter the PS3 firmware you want to install: ") #get input from user
        if option == "72":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_236)
        elif option == "73":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_235)
        elif option == "74":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_230)
        elif option == "75":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_220)
        elif option == "76":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_217)
        elif option == "77":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_216)
        elif option == "78":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_210)
        elif option == "79":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_201)
        elif option == "80":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_200)
        elif option == "81":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_194)
        elif option == "82":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_193)
        elif option == "83":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_192)
        elif option == "84":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_190)
        elif option == "85":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_182)
        elif option == "86":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_181)
        elif option == "87":
            webbrowser.open_new_tab(PS3.PS3_Firmware_180)
        elif option == "88":
            menu_6()
        elif option == "89":
            menu_4()
        else:
            print("Invalid option")

def menu_6():
    while True:
        print("[90] PS3_Firmware_170")
        print("[91] PS3_Firmware_160")
        print("[92] PS3_Firmware_154")
        print("[93] PS3_Firmware_151")
        print("[94] PS3_Firmware_150")
        print("[95] PS3_Firmware_132")
        print("[96] PS3_Firmware_130")
        print("[97] PS3_Firmware_111")
        print("[98] PS3_Firmware_110")
        print("[99] PS3_Firmware_102")
        print("[100] Back")
        option = input("Enter the PS3 firmware you want to install: ") #get input from user
        if option == "90":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_170)
        elif option == "91":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_160)
        elif option == "92":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_154)
        elif option == "93":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_151)
        elif option == "94":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_150)
        elif option == "95":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_132)
        elif option == "96":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_130)
        elif option == "97":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_111)
        elif option == "98":
            PS3Firmware.webbrowser.open_new_tab(PS3_Firmware_110)
        elif option == "99":
            PS3Firmware.webbrowser.open_new_tab(PS3Firmware.PS3.PS3_Firmware_102)
        elif option == "100":
            menu_5()
        else:
            print("Invalid option")
def credit():
    print("Script By TigerClips1\n")
    print("I will now force your Computer to open a link to my github my twitter and my kofi\n")
    print("ps4linux.com\n")
    open_url("https://ko-fi.com/tigerclips1")
    open_url("https://twitter.com/TugerClips1")
    open_url("https://github.com/TigerClips1")
first()
menu_1()
credit()




