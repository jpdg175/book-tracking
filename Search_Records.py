import os
import glob
from Book_Variables import Book

####################################################################
def Search_Author_Series():
    print "\n\n\n\n\n\n\n"
    print "Searching for Series by Author name"
    print "Enter \"+++\" to exit without saving anytime.\n\n"
    NewEntry = Book()
    NewEntry.Author_First = raw_input("Author First Name: ")
    if NewEntry.Author_First == "+++":
        return
    NewEntry.Author_Last = raw_input("Author Last Name: ")
    if NewEntry.Author_Last == "+++":
        return

    print "\n\n\n\n"
    os.chdir("Records")
    SearchString = NewEntry.Author_Last + "_" + NewEntry.Author_First
    for FileName in glob.glob("*"):
        if FileName == SearchString:
            os.chdir(FileName)
            for SeriesName in glob.glob("*.txt"):
                ForPrint = SeriesName.split(".")
                print ForPrint[0]
            os.chdir("..")
    os.chdir("..")
    print "\n\n"



####################################################################
def Search_Author_Series_Unread():
    print "\n\n\n\n\n\n\n"
    print "Searching for Unread by Author name"
    print "Enter \"+++\" to exit without saving anytime.\n\n"
    NewEntry = Book()
    NewEntry.Author_First = raw_input("Author First Name: ")
    if NewEntry.Author_First == "+++":
        return
    NewEntry.Author_Last = raw_input("Author Last Name: ")
    if NewEntry.Author_Last == "+++":
        return

    print "\n\n\n\n"
    os.chdir("Records")
    SearchString = NewEntry.Author_Last + "_" + NewEntry.Author_First
    for FileName in glob.glob("*"):
        if FileName == SearchString:
            os.chdir(FileName)
            for SeriesName in glob.glob("*.txt"):
                SeriesName_p = SeriesName.split('.')
                PrintList = []
                fid = open(SeriesName,'r')
                for line in fid:
                    line_p = line.split(',')
                    if line_p[4] == "00000000\n":
                        PrintList.append(line)        
                fid.close()
                if PrintList:
                    AuthorName = FileName.split('_')
                    print SeriesName_p[0] + ",  " + AuthorName[1] + " " + AuthorName[0]
                    for line in PrintList:
                        line_p = line.split(',')
                        print "\t" + line_p[0]
                    print
            os.chdir("..")
    os.chdir("..")

    print "\n\n"


####################################################################
def Search_Author_Series_Read():
    print "\n\n\n\n\n\n\n"
    print "Searching for Books Read by Author name"
    print "Enter \"+++\" to exit without saving anytime.\n\n"
    NewEntry = Book()
    NewEntry.Author_First = raw_input("Author First Name: ")
    if NewEntry.Author_First == "+++":
        return
    NewEntry.Author_Last = raw_input("Author Last Name: ")
    if NewEntry.Author_Last == "+++":
        return

    print "\n\n\n\n"
    os.chdir("Records")
    SearchString = NewEntry.Author_Last + "_" + NewEntry.Author_First
    for FileName in glob.glob("*"):
        if FileName == SearchString:
            os.chdir(FileName)
            for SeriesName in glob.glob("*.txt"):
                SeriesName_p = SeriesName.split('.')
                PrintList = []
                fid = open(SeriesName,'r')
                for line in fid:
                    line_p = line.split(',')
                    if line_p[4] != "00000000\n":
                        PrintList.append(line)
                fid.close()
                if PrintList:
                    AuthorName = FileName.split('_')
                    print SeriesName_p[0] + ",  " + AuthorName[1] + " " + AuthorName[0]
                    for line in PrintList:
                        line_p = line.split(',')
                        print "\t" + line_p[0]
                    print
            os.chdir("..")
    os.chdir("..")

    print "\n\n"


####################################################################
def Search_All_Unread():
    print "\n\n\n\n\n\n\n"
    print "Searching for all unread books."

    print "\n\n\n\n"
    os.chdir("Records")
    for FileName in glob.glob("*"):
            os.chdir(FileName)
            for SeriesName in glob.glob("*.txt"):
                SeriesName_p = SeriesName.split('.')
                PrintList = []
                fid = open(SeriesName,'r')
                for line in fid:
                    line_p = line.split(',')
                    if line_p[4] == "00000000\n":
                        PrintList.append(line)
                fid.close()
                if PrintList:
                    AuthorName = FileName.split('_')
                    print SeriesName_p[0] + ",  " + AuthorName[1] + " " + AuthorName[0]
                    for line in PrintList:
                        line_p = line.split(',')
                        print "\t" + line_p[0]
                    print
            os.chdir("..")
    os.chdir("..")
    print "\n\n"


####################################################################
def Search_Genre_Unread():
    Search_Get_Genres()
    print "\n"
    print "Searching for Unread Books by Genre"
    print "Enter \"+++\" to exit without saving anytime.\n\n"
    NewEntry = Book()
    NewEntry.Genre = raw_input("Genre: ")
    if NewEntry.Author_First == "+++":
        return
    print "\n\n\n\n"

    os.chdir("Records")
    for FileName in glob.glob("*"):
            os.chdir(FileName)
            for SeriesName in glob.glob("*.txt"):
                SeriesName_p = SeriesName.split('.')
                fid = open(SeriesName,'r')
                for line in fid:
                    line_p = line.split(',')
                    if line_p[4] == "00000000\n" and line_p[1] == NewEntry.Genre:
                        print line_p[0] + ", " + line_p[3] + " " + line_p[2]        
                fid.close()
            os.chdir("..")
    os.chdir("..")
    print "\n\n"

    
####################################################################
def Search_List_Authors():
    print "\n\n\n\n\n\n\n"
    print "Searching for Series by Author name"
    print "Input first letter of author's last name or \"0\" for all authors."
    SearchLetter = raw_input("Search Letter: ")
    print "\n\n\n\n"

    os.chdir("Records")
    for FileName in glob.glob("*"):
        FileName_p = FileName.split("_")
        LastName = list(FileName_p[0])
        if LastName[0] == SearchLetter or SearchLetter == "0":
            print FileName_p[0] + ", " + FileName_p[1]
    os.chdir("..")
    print "\n\n"


####################################################################
def Search_Count_Read():
    print "\n\n\n\n\n\n\n"
    print "Counting all read books."
    BookCount = 0
    print "\n\n\n\n"
    os.chdir("Records")
    for FileName in glob.glob("*"):
            os.chdir(FileName)
            for SeriesName in glob.glob("*.txt"):
                fid = open(SeriesName,'r')
                for line in fid:
                    line_p = line.split(',')
                    if line_p[4] != "00000000\n":
                        BookCount = BookCount + 1
                fid.close()
            os.chdir("..")
    os.chdir("..")

    print "Total number of books read: " + str(BookCount)
    print "\n\n"


####################################################################
def Search_Get_Genres():
    print "\n\n\n\n\n\n\n"
    print "Getting all genres."
    print "\n\n\n\n"
    os.chdir("Records")
    ShortList = []
    for FileName in glob.glob("*"):
            os.chdir(FileName)
            for SeriesName in glob.glob("*.txt"):
                fid = open(SeriesName,'r')
                for line in fid:
                    line_p = line.split(',')
                    ShortList.append(line_p[1])
                fid.close()
            os.chdir("..")
    os.chdir("..")
    PrintList = sorted(set(ShortList))
    for Genres in PrintList:
        print Genres
    print "\n\n"
