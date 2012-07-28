#!/usr/bin/env python
import os
import glob
import datetime
import New_Record
import Search_Records


MenuLength = 11



def MainMenu(): 
    print "Please select a menu entry:\n"
    print "Exit (0)"
    print "Add new entry (1)"
    print "Add new entry by series (2)"
    print "Add new entry by series of existing author (3)"
    print "List series by author (4)"
    print "List unread books by author (5)"
    print "List books read by author (6)"
    print "List all unread books (7)"
    print "List unread books by genre (8)"
    print "List author names (9)"
    print "Count number of books read (10)"
    print "List current genres (11)\n"
    UserSelection = raw_input("Selection: ")
    return UserSelection



###########################################################
#  Main Loop
###########################################################

print "\n\nWelcome to Jesse's Book Management Program!!!\n\n"
while 1:
    UserSelection = int(MainMenu())
    while UserSelection < 0 or UserSelection > MenuLength:
        print "\n\nInvalid choice, choose again:\n\n"
        UserSelection = int(MainMenu())
    
    
    if UserSelection == 0:
        break
    elif UserSelection == 1:
        New_Record.Add_New_Book()
    elif UserSelection == 2:
        New_Record.Add_New_Books_By_Series()
    elif UserSelection == 3:
        New_Record.Add_New_Books_By_Series_Existing_Author()
    elif UserSelection == 4:
        Search_Records.Search_Author_Series()
        Junk = raw_input("Press Enter key to continue")
    elif UserSelection == 5:
        Search_Records.Search_Author_Series_Unread()
        Junk = raw_input("Press Enter key to continue")
    elif UserSelection == 6:
        Search_Records.Search_Author_Series_Read()
        Junk = raw_input("Press Enter key to continue")
    elif UserSelection == 7:
        Search_Records.Search_All_Unread()
        Junk = raw_input("Press Enter key to continue")
    elif UserSelection == 8:
        Search_Records.Search_Genre_Unread()
        Junk = raw_input("Press Enter key to continue")
    elif UserSelection == 9:
        Search_Records.Search_List_Authors()
        Junk = raw_input("Press Enter key to continue")
    elif UserSelection == 10:
        Search_Records.Search_Count_Read()
        Junk = raw_input("Press Enter key to continue")
    elif UserSelection == 11:
        Search_Records.Search_Get_Genres()
        Junk = raw_input("Press Enter key to continue")
