from pip import main


class Library:
    def __init__(self, list, name):

        self.booklist = list
        self.name = name
        self.lendDict = {}
        
    def displayBook(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")   
        else:
            print(f"Book is already being used by {self.lendDict[book]}")


    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")
    
    def returnBook(self, book):
        self.lendDict.pop(book)
    
    
if __name__ == '__main__':
    harry = Library(['Python', 'Rich dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by Clrs'], "CodeWithHarry")
    
    while(True):
        print(f"Wlcome to the {harry.name} library. Enter Your choice to continue")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Enter a Book")
        user_choice = input("--> ")

        if user_choice not in ['1','2','3','4']:
            print("please select a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.displayBook()
            
        elif user_choice == 2:
            book = input("Enter the name of the book ypu want to lend: ")
            user = input("Enter your name: ")
            harry.lendBook(user, book)
        
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            harry.addBook(book)
        
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            harry.returnBook(book)
        
        else:
            print("Note a valid option")
            
        print("Press q to quit and c to continue: ")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input("--> ")
            if user_choice2 == "q":
                exit()
            
            elif user_choice2 == "c":
                continue

            else:
                print("Please enter a valid input")
            