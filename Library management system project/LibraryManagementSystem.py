def allBooksInfo():
    fh_r = open("booksInfo.txt",'r')
    s = fh_r.readlines()
    print("\nTotal "+str(len(s))+" books:")
    print("-------------------------")
    for i in range (0,len(s)):
        L = s[i].split(",")
        L1 = L[2].split(":")
        totalBooks = int(L[4]) + int(L[5])
        print("serial#:  "+L[0])
        print("\ntitle:  "+L[1])
        print("\nnumber of authors:  "+str(len(L1)))
        print("\nprice:  "+L[3])
        print("\ntotal copies:  "+str(totalBooks))
        print("-------------------------")
    fh_r.close()

    
    
def searchBooks():
    option = input("\nEnter (t) to search by title or (a) to search by author name: ")
    if option == 't' or option == 'T':
        fh_r = open("booksInfo.txt",'r')
        key = input("Enter the title: ")
        count=0
        s = fh_r.readlines()
        print("\nMatched records:")
        for i in range (0,len(s)):
            L = s[i].split(",")
            if key.lower() in L[1].lower():
                print("serial#:  "+L[0])
                print("\ntitle:  "+L[1])
                print("\nauthors:")
                author = L[2].split(":")
                for j in range (0,len(author)):
                    print("\n\t-"+author[j])

                print("\nprice:  "+L[3])
                print("\ncopies in library:  "+L[4])
                print("\nborrowed copies:  "+L[5])
                print("---------------------------------")
            else:
                count+=1

        if count==len(s):
            print("\nNo matched record found.")
        fh_r.close()  

    elif option == 'a' or option == 'A':
        fh_r = open("booksInfo.txt",'r')
        key = input("Enter author name: ")
        count=0
        s = fh_r.readlines()
        print("\nMatched records:")
        for i in range (0,len(s)):
            L = s[i].split(",")
            author = L[2].split(":")
            auth = ""
            for j in range (0,len(author)):
                auth += author[j]
                auth += " "
            if key.lower()in auth.lower():
                print("serial#:  "+L[0])
                print("\ntitle:  "+L[1])
                print("\nauthors:")
                author = L[2].split(":")
                for j in range (0,len(author)):
                    print("\n\t-"+author[j])

                print("\nprice:  "+L[3])
                print("\ncopies in library:  "+L[4])
                print("\nborrowed copies:  "+L[5])
                print("---------------------------------")
            else:
                count+=1

        if count==len(s):
            print("\nNo matched record found.")
        fh_r.close()
    else:
        print("\nError: Invalid input")

        
        
def removeEmptyLine():        
    import os

    fh_r = open("booksInfo.txt",'r')
    fh_w = open("temp2.txt",'w')
    s = fh_r.readlines()

    for i in range (0,len(s)):
        if s[i] != '\n':
            fh_w.write(s[i])

    fh_r.close()
    fh_w.close()
    os.remove("booksInfo.txt")
    os.rename("temp2.txt","booksInfo.txt")       
        
def checkSerial(serialNo):
    fh_r = open("booksInfo.txt",'r')
    s = " "
    while(s):
        s = fh_r.readline()
        L = s.split(",")
        if serialNo == L[0]:
            return 1
            break
        else:
            continue
    fh_r.close()      
    return 0
def addNewBook():
    fh_w = open("booksInfo.txt",'a+')
    serialNo = input("\nEnter a serial no.: ")
    if len(serialNo) == 5:
        if checkSerial(serialNo) == 0:
            Title = input("\nEnter a valid title of the book: ")
            if len(Title)>1 or Title != ' ':
                ch = 'y'
                listOfname = []
                while(ch=='y' or ch=="Y"):
                    name = input("Enter author name: ")
                    if len(name)!=0 or name != '':
                        listOfname.append(name)
                    else:
                        print("\nAuthor name cannot be empty")
                    ch = input("\nDo you want to add another author name(y/n): ")

                if len(listOfname) > 0:
                    priceOfbook = float(input("\nEnter price of the book: "))
                    numberOfCopies  = int(input("\nEnter no. of copies: "))
                    authorNames=""
                    count = len(listOfname)

                    for i in range(len(listOfname)):
                        if listOfname[i] != '':
                            authorNames += listOfname[i]
                            if count>1:
                                authorNames += ":"
                        count -= 1
                    newEntry = (serialNo+","+Title+","+authorNames+","+str(priceOfbook)+","+str(numberOfCopies)+","+"0")
                    fh_w.write("\n"+newEntry)
                    
                    print("\nNew book has been successfully added.")
                else:
                    print("\nError: names of all authors should not be empty")
            else:
                print("\nError: Title should not be empty")
        else:
            print("\nError: serial number is already used")
    else:
        print("\nError: Invalid serial number. Serial number should be 5 digits.")
    fh_w.close()
    removeEmptyLine()

def infoOfAbook(serialNo):
    fh_r = open("booksInfo.txt",'r')
    s=" "
    while(s):
        s = fh_r.readline()
        L = s.split(",")
        if serialNo == L[0]:
            return s
        else:
            continue
    fh_r.close()
def removeAbook():
    import os
    fh_r = open("booksInfo.txt",'r')
    fh_w = open("temp.txt",'w')
    serialNo = input("\nEnter a serial no.: ")
    getBook = infoOfAbook(serialNo)
    if getBook != None:
        print("\nThe book info: "+getBook)
        book = getBook.split(",")
        if int(book[5]) == 0:
            print("\nMatched records:")
            print("serial#:  "+book[0])
            print("\ntitle:  "+book[1])
            print("\nauthors:")
            author = book[2].split(":")
            for j in range (0,len(author)):
                print("\n\t-"+author[j])

            print("\nprice:  "+book[3])
            print("\ncopies in library:  "+book[4])
            print("\nborrowed copies:  "+book[5])
            print("---------------------------------")
            deleteChoice = input("Deleting the book .. Are you sure (y/n): ")
            if deleteChoice == 'y' or deleteChoice == 'Y':
                k = fh_r.readlines()
                for i in range (0,len(k)):
                    L = k[i].split(",")
                    if L[0]!=serialNo:
                        fh_w.write(k[i])

                fh_r.close()
                fh_w.close()
                os.remove("booksInfo.txt")
                os.rename("temp.txt","booksInfo.txt")
                print("\nThe book has removed successfully.")
            else:
                print("operation is cancelled")
        else:
            print("\nBook cannot be removed: borrowed copies must be 0")
    else:
        print("\nNot found. Please enter a valid serial number.")

def checkUserId(userID):

    fh_r = open("borrowedInfo.txt",'r')
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(userID) == int(L[1]):
            return 1
            break
        else:
            continue
    fh_r.close()
    return 0

def countBorrowBook(userID):
    count = 0
    fh_r = open("borrowedInfo.txt",'r')
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(userID) == int(L[1]):
            count += 1
    fh_r.close()
    return count

def checkBorrowByUser(serialNo,userID):
    fh_r = open("borrowedInfo.txt",'r')
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(userID) == int(L[1]) and int(serialNo) == int(L[0]):
            return 1
            break
        else:
            continue
    fh_r.close()
    return 0

def booksIsAvailable(serialNo):
    fh_r = open("booksInfo.txt",'r')
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(serialNo) == int(L[0]) and int(L[4]) > 0:
            return 1
            break
    fh_r.close()
    return 0
    
def updateInBorrowInfo(serialNo,userID):
    fh_w = open("borrowedInfo.txt",'a+')
    fh_w.write("\n"+serialNo+","+userID)
    fh_w.close()

def updateBooksInfo(serialNo):
    import os
    fh_r = open("booksInfo.txt",'r')
    fh_w = open("temp.txt",'w')
    
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(L[0]) == int(serialNo):
            availableBooks = int(L[4]) - 1
            borrowedBooks = int(L[5]) + 1
            fh_w.write(L[0]+","+L[1]+","+L[2]+","+L[3]+","+str(availableBooks)+","+str(borrowedBooks)+"\n")
         
        else:
            fh_w.write(s[i])
    fh_r.close()
    fh_w.close()
    os.remove("booksInfo.txt")
    os.rename("temp.txt","booksInfo.txt")  
def removeEmptylineFromBorrow():
    import os
    fh_r = open("borrowedInfo.txt",'r')
    fh_w = open("temp2.txt",'w')
    s = fh_r.readlines()

    for i in range (0,len(s)):
        if s[i] != '\n':
            fh_w.write(s[i])

    fh_r.close()
    fh_w.close()
    os.remove("borrowedInfo.txt")
    os.rename("temp2.txt","borrowedInfo.txt")
def borrowAbook():
    userID = input("Enter your User ID: ")
    if checkUserId(userID) == 1:
        if countBorrowBook(userID) < 3:
            serialNo = input("\nEnter serial no of the book: ")
            if len(serialNo) == 5:
                if checkBorrowByUser(serialNo,userID) == 0:
                    if booksIsAvailable(serialNo) == 1:
                        print("\nSuccessfully borrowed by the user")
                        updateInBorrowInfo(serialNo,userID)
                        updateBooksInfo(serialNo)
                    else:
                        print("\nThe book isn't available.")
                else:
                    print("\nError: user already borrowed a copy of the book")
            else:
                print("\nError: serial number should be 5 digits")
        else:
            print("\nError: user cannot borrow more than 3 books.")
    else:
        serialNo = input("\nEnter serial no of the book: ")
        if len(serialNo) == 5:
            if booksIsAvailable(serialNo) == 1:
                print("\nSuccessfully borrowed by the user")
                updateInBorrowInfo(serialNo,userID)
                updateBooksInfo(serialNo)
            else:
                print("\nThe book isn't available")
        else:
                print("\nError: serial number should be 5 digits")
                
    removeEmptylineFromBorrow()
                
def checkBorrowByUser(serialNo,userID):
    fh_r = open("borrowedInfo.txt",'r')
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(userID) == int(L[1]) and int(serialNo) == int(L[0]):
            return 1
            break
        else:
            continue
    fh_r.close()
    return 0

def removeBorrowedRecordAfterReturn(serialNo,userID):
    import os
    fh_r = open("borrowedInfo.txt",'r')
    fh_w = open("temp.txt",'w')
    
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(userID) == int(L[1]) and int(serialNo) == int(L[0]):
            continue
        else:
            fh_w.write(s[i])
    fh_r.close()
    fh_w.close()
    os.remove("borrowedInfo.txt")
    os.rename("temp.txt","borrowedInfo.txt") 

def updateBooksInfoAfterReturn(serialNo):
    import os
    fh_r = open("booksInfo.txt",'r')
    fh_w = open("temp.txt",'w')
    
    s = fh_r.readlines()
    for i in range (0,len(s)):
        L = s[i].split(",")
        if int(L[0]) == int(serialNo):
            availableBooks = int(L[4]) + 1
            borrowedBooks = int(L[5]) - 1
            fh_w.write(L[0]+","+L[1]+","+L[2]+","+L[3]+","+str(availableBooks)+","+str(borrowedBooks)+"\n")
         
        else:
            fh_w.write(s[i])
    fh_r.close()
    fh_w.close()
    os.remove("booksInfo.txt")
    os.rename("temp.txt","booksInfo.txt")
    
def returnAbook():
    serialNo = input("Enter book serial number to return: ")
    userID = input("Enter User ID: ")
    if checkBorrowByUser(serialNo,userID) == 1:
        removeBorrowedRecordAfterReturn(serialNo,userID)
        updateBooksInfoAfterReturn(serialNo)
        print("\nBook has returned successfully")
    else:
        print("\nError: no matched record found in borrowedInfo.txt")

while(1):
    print("Library Management System")
    print("=========================")
    print("1. Print books info \n2. Search a book \n3. Add new book \n4. Remove a book \n5. Borrow a book \n6. Return a book \n7. Exit")
    print("=========================")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        allBooksInfo()
        input("\nPress any key to continue...")
        continue
    elif ch == 2:
        searchBooks()
        input("\nPress any key to continue...")
        continue
    elif ch == 3:
        addNewBook()
        input("\nPress any key to continue...")
        continue
    elif ch == 4:
        removeAbook()
        input("\nPress any key to continue...")
        continue
    elif ch == 5:
        borrowAbook()
        input("\nPress any key to continue...")
        continue
    elif ch == 6:
        returnAbook()
        input("\nPress any key to continue...")
        continue
    elif ch == 7:
        break
    else:
        print("Error: Invalid choice")
        input("\nPress any key to continue...")
        continue