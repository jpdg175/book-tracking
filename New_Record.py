import os
import glob
from Book_Variables import Book
import Search_Records


def Add_New_Book():
    print "\n\n\n\n\n\n\n"
    print "Adding New Book"
    print "Enter date in \"YYYYMMDD\" format. Use \"00000000\" if not read yet, and \"99999999\" if unknown date."
    print "Enter \"+++\" to exit without saving anytime.\n\n"
    NewEntry = Book()
    NewEntry.Title = raw_input("Book Title: ")
    if NewEntry.Title == "+++":
        return
    NewEntry.Author_First = raw_input("Author First Name: ")
    if NewEntry.Author_First == "+++":
        return
    NewEntry.Author_Last = raw_input("Author Last Name: ")
    if NewEntry.Author_Last == "+++":
        return
    NewEntry.Series = raw_input("Book Series: ")
    if NewEntry.Series == "+++":
        return
    NewEntry.Date = raw_input("Date: ")
    if NewEntry.Date == "+++":
        return
    if not NewEntry.Date:
        NewEntry.Date = "99999999"
    NewEntry.Genre = raw_input("Genre: ")
    if NewEntry.Genre == "+++":
        return
    

    print "\n\n\n\n\n\n\n"
    print "Verify your entry:"
    print "Title: " + NewEntry.Title
    print "Author First: " + NewEntry.Author_First
    print "Author Last: " + NewEntry.Author_Last
    print "Series: " + NewEntry.Series
    print "Date: " + NewEntry.Date
    print "Genre: " + NewEntry.Genre

    Ver = raw_input("\nCorrect (y/n): ")
    while not (Ver == "y")  and not (Ver == "n"):
        Ver = raw_input("\nCorrect (y/n): ")
    
    if Ver == "n":
        return
    
    os.chdir("Records")
    SearchString = NewEntry.Author_Last + "_" + NewEntry.Author_First
    NewAuthor = 1
    for FileName in glob.glob("*"):
        if FileName == SearchString:
            os.chdir(FileName)
            NewAuthor = 0
            break
    #### Easy one, make a new folder and entry
    if NewAuthor == 1:
        os.mkdir(SearchString)
        os.chdir(SearchString)
        fid = open(NewEntry.Series + ".txt",'w')
        fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last + ","\
             + NewEntry.Author_First + "," + NewEntry.Date + "\n")
        fid.close()
        os.chdir("..")
        os.chdir("..")
        return 
        
    #### Harder one, have to check if this entry exists 
    for FileName in glob.glob("*.txt"):
        ### Check if this series is already started 
        if FileName == (NewEntry.Series+".txt"):
            ### Yep, now check if this entry exists
            fid = open(FileName,'r')
            UserInput = "z"
            LineCount = 0
            for line in fid:
                LineCount = LineCount + 1
                Existing = line.split(',')
                if Existing[0] == NewEntry.Title and Existing[1] == NewEntry.Genre:
                    print "WARNING: An entry exists under this author, series, and title:"
                    print line
                    UserInput = raw_input("\nAdd Another Entry (a), Overwrite Entry (o), Do Nothing (n): ")
                    while not (UserInput == "a") and not (UserInput == "o") and not (UserInput == "n"):
                        UserInput = raw_input("\nAdd Another Entry (a), Overwrite Entry (o), Do Nothing (n): ")
                    break
            fid.close()
            if UserInput == "n":
                os.chdir("..")
                os.chdir("..")
                return
            elif UserInput == "a":
                fid = open(FileName,'a')
                fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last +\
                     "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
                fid.close()
                os.chdir("..")
                os.chdir("..")
                return
            elif UserInput == "o":
                LineCount2 = 0;
                fid = open(FileName,'r')
                OldData = fid.readlines()
                fid.close
                fid = open(FileName,'w')
                for line in OldData:
                    LineCount2 = LineCount2 + 1
                    if LineCount2 == LineCount:
                        fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last\
                             + "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
                    else: 
                        fid.write(line)
                fid.close
                os.chdir("..")
                os.chdir("..")
                return

            else:
                fid = open(FileName,'a')
                fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last\
                     + "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
                fid.close()
                os.chdir("..")
                os.chdir("..")
                return

    ###If we're here, this series doesn't exist for this author
    fid = open(NewEntry.Series + ".txt",'w')
    fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last + ","\
         + NewEntry.Author_First + "," + NewEntry.Date + "\n")
    fid.close()
    os.chdir("..")
    os.chdir("..")
    return


def Add_New_Books_By_Series():
    print "\n\n\n\n\n\n\n"
    print "Adding New Books"
    print "Enter date in \"YYYYMMDD\" format. Use \"00000000\" if not read yet, and \"99999999\" if unknown date."
    print "Enter \"+++\" to exit without saving anytime.\n\n"
    NewEntry = Book()
    NewEntry.Author_First = raw_input("Author First Name: ")
    if NewEntry.Author_First == "+++":
        return
    NewEntry.Author_Last = raw_input("Author Last Name: ")
    if NewEntry.Author_Last == "+++":
        return
    NewEntry.Series = raw_input("Book Series: ")
    if NewEntry.Series == "+++":
        return
    NewEntry.Genre = raw_input("Genre: ")
    if NewEntry.Genre == "+++":
        return
    

    print "\n\n\n\n"
    
    os.chdir("Records")
    SearchString = NewEntry.Author_Last + "_" + NewEntry.Author_First
    NewAuthor = 1
    for FileName in glob.glob("*"):
        if FileName == SearchString:
            os.chdir(FileName)
            NewAuthor = 0
            break
    #### Easy one, make a new folder and entry
    if NewAuthor == 1:
        os.mkdir(SearchString)
        os.chdir(SearchString)
        fid = open(NewEntry.Series + ".txt",'w')
        Choice = "y"
        while Choice == "y":
            
            NewEntry.Title = raw_input("Book Title: ")
            if NewEntry.Title == "+++":
                fid.close()
                os.chdir("..")
                os.chdir("..")
                return
            NewEntry.Date = raw_input("Date: ")
            if NewEntry.Date == "+++":
                fid.close()
                os.chdir("..")
                os.chdir("..")
                return
            if not NewEntry.Date:
                NewEntry.Date = "99999999"
            fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last + ","\
                + NewEntry.Author_First + "," + NewEntry.Date + "\n")
            Choice = raw_input("\nAdd Another Book (y/n): ")
            while not (Choice == "y")  and not (Choice == "n"):
                Choice = raw_input("\nAdd Another Book (y/n): ")
        fid.close()
        os.chdir("..")
        os.chdir("..")
        return 
        
    #### Harder one, have to check if this entry exists 
    for FileName in glob.glob("*.txt"):
        ### Check if this series is already started 
        if FileName == (NewEntry.Series+".txt"):
            Choice = "y"
            while Choice == "y":
                NewEntry.Title = raw_input("Book Title: ")
                if NewEntry.Title == "+++":
                    fid.close()
                    os.chdir("..")
                    os.chdir("..")
                    return
                NewEntry.Date = raw_input("Date: ")
                if NewEntry.Date == "+++":
                    fid.close()
                    os.chdir("..")
                    os.chdir("..")
                    return
                if not NewEntry.Date:
                    NewEntry.Date = "99999999"

                ### Yep, now check if this entry exists
                fid = open(FileName,'r')
                UserInput = "z"
                LineCount = 0
                for line in fid:
                    LineCount = LineCount + 1
                    Existing = line.split(',')
                    if Existing[0] == NewEntry.Title and Existing[1] == NewEntry.Genre:
                        print "WARNING: An entry exists under this author, series, and title:"
                        print line
                        UserInput = raw_input("\nAdd Another Entry (a), Overwrite Entry (o), Do Nothing (n): ")
                        while not (UserInput == "a") and not (UserInput == "o") and not (UserInput == "n"):
                            UserInput = raw_input("\nAdd Another Entry (a), Overwrite Entry (o), Do Nothing (n): ")
                        break
                fid.close()
                if UserInput == "n":
                    print "No changes made"
                elif UserInput == "a":
                    fid = open(FileName,'a')
                    fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last +\
                         "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
                    fid.close()
                elif UserInput == "o":
                    LineCount2 = 0;
                    fid = open(FileName,'r')
                    OldData = fid.readlines()
                    fid.close
                    fid = open(FileName,'w')
                    for line in OldData:
                        LineCount2 = LineCount2 + 1
                        if LineCount2 == LineCount:
                            fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last\
                                 + "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
                        else: 
                            fid.write(line)
                    fid.close

                else:
                    fid = open(FileName,'a')
                    fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last\
                         + "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
                    fid.close()
                Choice = raw_input("\nAdd Another Book (y/n): ")
                while not (Choice == "y")  and not (Choice == "n"):
                    Choice = raw_input("\nAdd Another Book (y/n): ")
            os.chdir("..")
            os.chdir("..")
            return

    ###If we're here, this series doesn't exist for this author
    fid = open(NewEntry.Series + ".txt",'w')
    Choice = "y"
    while Choice == "y":
        NewEntry.Title = raw_input("Book Title: ")
        if NewEntry.Title == "+++":
            fid.close()
            os.chdir("..")
            os.chdir("..")
            return
        NewEntry.Date = raw_input("Date: ")
        if NewEntry.Date == "+++":
            fid.close()
            os.chdir("..")
            os.chdir("..")
            return
        if not NewEntry.Date:
            NewEntry.Date = "99999999"
        fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last + ","\
            + NewEntry.Author_First + "," + NewEntry.Date + "\n")
        Choice = raw_input("\nAdd Another Book (y/n): ")
        while not (Choice == "y")  and not (Choice == "n"):
            Choice = raw_input("\nAdd Another Book (y/n): ")
    fid.close()
    os.chdir("..")
    os.chdir("..")
    return


def Add_New_Books_By_Series_Existing_Author():
    print "\n\n\n\n\n\n\n"
    print "Adding New Books to Existing Series"
    print "Enter date in \"YYYYMMDD\" format. Use \"00000000\" if not read yet, and \"99999999\" if unknown date."
    print "Enter \"+++\" to exit without saving anytime.\n\n"
    NewEntry = Book()
    NewEntry.Author_First = raw_input("Author First Name: ")
    if NewEntry.Author_First == "+++":
        return
    NewEntry.Author_Last = raw_input("Author Last Name: ")
    if NewEntry.Author_Last == "+++":
        return
    #NewEntry.Series = raw_input("Book Series: ")
    #if NewEntry.Series == "+++":
    #    return
    #NewEntry.Genre = raw_input("Genre: ")
    #if NewEntry.Genre == "+++":
    #    return
    

    print "\n\n\n\n"
    
    os.chdir("Records")
    SearchString = NewEntry.Author_Last + "_" + NewEntry.Author_First
    NewAuthor = 1
    for FileName in glob.glob("*"):
        if FileName == SearchString:
            NewAuthor = 0
            break
    
    #### If this author doesn't exist
    if NewAuthor == 1:
        print "That author doesn't exist!!!"
        os.chdir("..")
        return
   
   
    #### List the series available for the author
    SeriesList = Search_Records.Search_Author_Series_Return(SearchString)
    c = 1
    print "(0) Series Not Started"
    for Name in SeriesList:
       print "("+str(c)+") " + Name 
       c = c+1
    
    
    UserEntry = raw_input("Choose series: ")
    if UserEntry == "+++" or UserEntry == "0":
        os.chdir("..")
        return

    NewEntry.Title = raw_input("Title: ")
    if NewEntry.Title == "+++":
        os.chdir("..")
        return
    
        
    NewEntry.Date = raw_input("Date: ")
    if NewEntry.Date == "+++":
        fid.close()
        os.chdir("..")
        return
    if not NewEntry.Date:
        NewEntry.Date = "99999999"

    os.chdir(SearchString)

    ### Yep, now check if this entry exists
    FileName = SeriesList[int(UserEntry)-1]+".txt"
    fid = open(FileName,'r')
    UserInput = "z"
    LineCount = 0
    for line in fid:
        LineCount = LineCount + 1
        Existing = line.split(',')
        NewEntry.Genre = Existing[1]
        if Existing[0] == NewEntry.Title and Existing[1] == NewEntry.Genre:
            print "WARNING: An entry exists under this author, series, and title:"
            print line
            UserInput = raw_input("\nAdd Another Entry (a), Overwrite Entry (o), Do Nothing (n): ")
            while not (UserInput == "a") and not (UserInput == "o") and not (UserInput == "n"):
                UserInput = raw_input("\nAdd Another Entry (a), Overwrite Entry (o), Do Nothing (n): ")
            break
    fid.close()
    if UserInput == "n":
        print "No changes made"
    elif UserInput == "a":
        fid = open(FileName,'a')
        fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last +\
            "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
        fid.close()
    elif UserInput == "o":
        LineCount2 = 0;
        fid = open(FileName,'r')
        OldData = fid.readlines()
        fid.close()
        fid = open(FileName,'w')
        for line in OldData:
            LineCount2 = LineCount2 + 1
            if LineCount2 == LineCount:
                fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last\
                  + "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
            else: 
                fid.write(line)
        fid.close()

    else:
        fid = open(FileName,'a')
        fid.write(NewEntry.Title + "," + NewEntry.Genre + "," + NewEntry.Author_Last\
            + "," + NewEntry.Author_First + "," + NewEntry.Date + "\n")
        fid.close()

    os.chdir("..")
    os.chdir("..")
    return

