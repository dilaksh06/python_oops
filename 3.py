class Book:
    def __init__(self,book=None):
        self.book={}
        self.count=0
    def show_details(self):
        if self.book:
            print("books details are below")
            for key,value in self.book.items():
                self.count+=1
                print(self.count,".","Title:",key,"  copies:",value[0],"  Author:",value[1])
        else:
            print("no books are available:")
            
       
class Library(Book):
    
    def add_book(self,books):
        self.book.update(books)
        print("\nbooks added successfully.....\n")
        self.show_details()
        
    def borrow_book(self,title):
        if title in self.book:
            if self.book[title][0] > 0:
                print("\nborrowing",title,"successfull....\n")
                self.book[title]=[self.book[title][0]-1,self.book[title][1]]
            else:
                print("book out of stock")
        else:
            print("no book found")
        (self.show_details())
        
    def return_books(self,title):
        if title in self.book:
            print("\nreturning",title,"successfull....\n")
            self.book[title]=[self.book[title][0]+1,self.book[title][1]]
        (self.show_details())

print("\n",format("*","*<10"),"welcome to library management system",format("*","*>10"))

x={"a":[5,"dilaksha"],"b":[15,"abi"]}
update=Library()
update.add_book(x)
update.borrow_book("a")

print("press 1 to add book")
print("press 2  to borrow book")
print("press 3 to return book")
print("press 4 to display books")
print("5 to exit")
book={}
while(True):
    choice=int(input("enter your choice :"))
    if(choice==1):  
        title=input(("enter the title of the book :"))
        copies=int(input("enter the number of copies :"))
        author=input("enter the name of the author :")
        book[title]=[copies,author]
        update.add_book(book)
    elif(choice==2):
         title=input("enter the title of the book : ")
         update.borrow_book(title)
    elif(choice==3):
         title=input("enter the title of the book : ")
         update.return_books(title)
    
    elif(choice==4):
         update.show_details()
        
    elif(choice==5):
         print("we are exiting.....")
         break
    else:
        print("INVALID CHOICE")
    
         
        
    
