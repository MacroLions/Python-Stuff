import random as r
import time as t

#random-list-function
def randomizer(a=[]):
    chosenone=(r.randrange(1,len(a),1))
    print(a[chosenone])
        
def main():
    #Variables#
    a=0
    menu=str("n")

    #Title
    print("Fucking randomizer of movies and series\nBy MacroLions\n\n1)Random movie\n2)Random serie\n3)Exit")

    #Lists
    movielist=["The Naked Gun","Alice in wonderland","As Good as it gets",
               "The Circle (Emma Watson one)","Sweet Science","Mulan",
               "The Lego movie","Lego Batman","Wedding Crashers",
               "Scott Pilgrim vs The world","Not Cool"]
    serielist=["Fuck that's Delicious","Parks and Recreation","How I met your mother",
           "Camp Camp"]

    #option thingie
    a=input("\nOption:")


    #Valid options   
    if(int(a)==1):
        print("\nThe chosed movie is: ")
        t.sleep(0.5)
        print(".")
        t.sleep(0.5)
        print(".")
        t.sleep(0.5)
        print(".")
        t.sleep(0.5)
        randomizer(movielist)
        t.sleep(0.8)
        print("\n")
        menu=str(input("Return to menu? y/n "))
        menu=menu.upper()
        if(str(menu)=="Y"):
            print ("\n" * 31)
            main()
        if(str(menu)=="N"):
            print("Welp, bye!")
            t.sleep(0.)
            quit()
        
    if(int(a)==2):
        print("\nThe chosed serie is: ")
        t.sleep(0.5)
        print(".")
        t.sleep(0.5)
        print(".")
        t.sleep(0.5)
        print(".")
        t.sleep(0.5)
        randomizer(serielist)
        t.sleep(0.8)
        print("\n")
        menu=str(input("Return to menu? y/n "))
        menu=menu.upper()
        if(str(menu)=="Y"):
            print ("\n" * 31)
            main()
        if(str(menu)=="N"):
            print("Welp, bye!")
            t.sleep(0.7)
            quit()
            
    if(int(a)==3):
        print("Welp, bye!")
        t.sleep(0.7)
        quit()
        
    #NotValidOption        
    print("\nNot valid option")
    t.sleep(0.8)
    print ("\n" * 31)
    main()

main()
