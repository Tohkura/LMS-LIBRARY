import os
import pathlib
from tabnanny import check
from datetime import datetime, date, timedelta

class LoginSystem:
    def __init__(self):
        self.file = pathlib.Path("Login_Credentials.csv")

        if not self.file.exists():
            with open(self.file, "w") as f:
                f.write("name,password\n")
                f.write("Owen Ward,Owen2205\n")

    def updateName(self, old_name, new_name):
        lines = []
        with open(self.file, "r") as f:
            for line in f:
                lines.append(line)

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            file_name, file_password = info[0], info[1]

            if file_name == old_name:
                file_name = new_name
                found = True

            updated_rows.append(f"{file_name},{file_password}\n")

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        if found:
            print("Name updated successfully.")
        else:
            print("Name not found — no changes made.")

    def changePassword(self, name, new_password):
        lines = []
        with open(self.file, "r") as f:
            for line in f:
                lines.append(line)

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            file_name, file_password = info[0], info[1]

            if file_name == name:
                file_password = new_password
                found = True

            updated_rows.append(f"{file_name},{file_password}\n")

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        if found:
            print("Password updated successfully.")
        else:
            print("Name not found — no changes made.")

    def checkLogin(self):
        print("Welcome to the login system.")
        name = input("Please enter your name: ")
        password = input("Please enter your password: ")

        lines = []
        with open(self.file, "r") as f:
            for line in f:
                lines.append(line)

        rows = lines[1:]

        for line in rows:
            info = line.strip().split(",")
            file_name, file_password = info[0], info[1]

            if file_name == name and file_password == password:
                print(f"Login successful! Welcome, {file_name}.")
                return True
            
        print("Incorrect name or password, please try again.")
        return False

class StudentID:
    def __init__(self):
            self.file = pathlib.Path("Student_IDs.csv")
    
            if not self.file.exists():
                with open(self.file, "w") as f:
                    f.write("ID,fullname,yearlevel,course,books,penalties\n")

    def SearchID(self):
        ID = input("Enter the student ID to search: ")

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip().split(",")[0] == ID:
                    info = line.strip().split(",")
                    print(f"Student ID: {info[0]}")
                    print(f"Full Name: {info[1]}")
                    print(f"Year Level: {info[2]}")
                    print(f"Course: {info[3]}")
                    print(f"Books: {info[4]}")
                    print(f"Penalties: {info[5]}")
                    return

    def UpdateID(self):
        ID = input("Enter the student ID to update: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False

        for line in lines:
            if line.strip().split(",")[0] == ID:
                found = True
                info = line.strip().split(",")
                print(f"Current Full Name: {info[1]}")
                new_fullname = input("Enter new full name (leave blank to keep current): ")
                if new_fullname:
                    info[1] = new_fullname

                print(f"Current Year Level: {info[2]}")
                new_yearlevel = input("Enter new year level (leave blank to keep current): ")
                if new_yearlevel:
                    info[2] = new_yearlevel

                print(f"Current Course: {info[3]}")
                new_course = input("Enter new course (leave blank to keep current): ")
                if new_course:
                    info[3] = new_course

                updated_lines.append(",".join(info) + "\n")
            else:
                updated_lines.append(line)

        if not found:
            print(f"No student found with ID {ID}.")
            return

        with open(self.file, "w") as f:
            for line in updated_lines:
                f.write(line)

        print("Student information updated successfully.")
                
    def addid(self):
        ID = input("Enter the new student ID: ")

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip().split(",")[0] == ID:
                    print(f"Student ID {ID} already exists.")
                    return

        fullname = input("Enter the student's full name: ")
        yearlevel = input("Enter the student's year level: ")
        course = input("Enter the student's course: ")

        with open(self.file, "a") as f:
            f.write(f"{ID},{fullname},{yearlevel},{course},,\n")

        print("Student ID added successfully.")

    def SearchByName(self):
        name = input("Enter the student's full name to search: ")

        with open(self.file, "r") as f:
            found = False
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[1].lower() == name.lower():
                    found = True
                    print(f"Student ID: {info[0]}")
                    print(f"Full Name: {info[1]}")
                    print(f"Year Level: {info[2]}")
                    print(f"Course: {info[3]}")
                    print(f"Books: {info[4]}")
                    print(f"Penalties: {info[5]}")

        if not found:
            print(f"No student found with name '{name}'.")

    def deleteID(self):
        ID = input("Enter the student ID to delete: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == ID:
                found = True
                continue
            updated_rows.append(line)

        if not found:
            print(f"No student found with ID {ID}.")
            return

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        print("Student record deleted successfully.")

    def getStudentRow(self, ID):
        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[0] == ID:
                    return info
        return None

    def updateBooksField(self, ID, book_ids):
        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == ID:
                found = True
                info[4] = ";".join(book_ids)
                updated_rows.append(",".join(info) + "\n")
            else:
                updated_rows.append(line)

        if found:
            with open(self.file, "w") as f:
                f.write(header)
                for row in updated_rows:
                    f.write(row)

        return found

    def updatePenaltyField(self, ID, new_total):
        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == ID:
                found = True
                info[5] = str(new_total)
                updated_rows.append(",".join(info) + "\n")
            else:
                updated_rows.append(line)

        if found:
            with open(self.file, "w") as f:
                f.write(header)
                for row in updated_rows:
                    f.write(row)

        return found

class Library:
    def __init__(self):
        self.file = pathlib.Path("Library_Catalogue.csv")
    
        if not self.file.exists():
            with open(self.file, "w") as f:
                f.write("ID,title,author,year,copies,copies available\n")

    def SearchBook(self):
        ID = input("Enter the book ID, title, or author to search: ")
        title = ID
        author = ID

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip().split(",")[0] == ID or line.strip().split(",")[1] == title or line.strip().split(",")[2] == author:   
                    found = True  
                    info = line.strip().split(",")
                    print(f"Book ID: {info[0]}")
                    print(f"Title: {info[1]}")
                    print(f"Author: {info[2]}")
                    print(f"Genre: {info[3]}")
                    print(f"Year: {info[4]}")
                    print(f"Total Copies: {info[5]}")
                    print(f"Available Copies: {info[6]}")
            else: print(f"No book found with ID, title, or author '{ID}'.")

    def addBook(self):
        ID = input("Enter the new book ID: ")

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip().split(",")[0] == ID:
                    print(f"Book ID {ID} already exists.")
                    return

        title = input("Enter the book's title: ")

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip().split(",")[1] == title:
                    print(f"Book title '{title}' already exists.")
                    return
                
        author = input("Enter the book's author: ")
        genre = input("Enter the book's genre: ")
        year = input("Enter the book's year of publication: ")
        copies = input("Enter the total number of copies: ")

        with open(self.file, "a") as f:
            f.write(f"{ID},{title},{author},{genre},{year},{copies},{copies}\n")

        print("Book added successfully.")

    def UpdateBook(self):
        ID = input("Enter the book ID to update: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False

        for line in lines:
            if line.strip().split(",")[0] == ID:
                found = True
                info = line.strip().split(",")
                print(f"Current Title: {info[1]}")
                new_title = input("Enter new title (leave blank to keep current): ")
                if new_title:
                    info[1] = new_title

                print(f"Current Author: {info[2]}")
                new_author = input("Enter new author (leave blank to keep current): ")
                if new_author:
                    info[2] = new_author

                print(f"Current Genre: {info[3]}")
                new_genre = input("Enter new genre (leave blank to keep current): ")
                if new_genre:
                    info[3] = new_genre

                print(f"Current Year: {info[4]}")
                new_year = input("Enter new year (leave blank to keep current): ")
                if new_year:
                    info[4] = new_year

                print(f"Current Total Copies: {info[5]}")
                new_total_copies = input("Enter new total copies (leave blank to keep current): ")
                if new_total_copies:
                    info[5] = new_total_copies

                updated_lines.append(",".join(info) + "\n")
            else:
                updated_lines.append(line)

        if not found:
            print(f"No book found with ID {ID}.")
            return

        with open(self.file, "w") as f:
            for line in updated_lines:
                f.write(line)

    def BorrowBook(self):

        ID = input("Enter the book ID to borrow: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False

        for line in lines:
            if line.strip().split(",")[0] == ID:
                found = True
                info = line.strip().split(",")
                available_copies = int(info[6])
                if available_copies > 0:
                    info[6] = str(available_copies - 1)
                    print(f"You have successfully borrowed '{info[1]}'.")
                else:
                    print(f"Sorry, '{info[1]}' is currently unavailable.")
                updated_lines.append(",".join(info) + "\n")
            else:
                updated_lines.append(line)

        if not found:
            print(f"No book found with ID {ID}.")
            return

        with open(self.file, "w") as f:
            for line in updated_lines:
                f.write(line)

    def ReturnBook(self):
        ID = input("Enter the book ID to return: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False

        for line in lines:
            if line.strip().split(",")[0] == ID:
                found = True
                info = line.strip().split(",")
                total_copies = int(info[5])
                available_copies = int(info[6])
                if available_copies < total_copies:
                    info[6] = str(available_copies + 1)
                    print(f"You have successfully returned '{info[1]}'.")
                else:
                    print(f"All copies of '{info[1]}' are already in the library.")
                updated_lines.append(",".join(info) + "\n")
            else:
                updated_lines.append(line)

        if not found:
            print(f"No book found with ID {ID}.")
            return

        with open(self.file, "w") as f:
            for line in updated_lines:
                f.write(line)

    def removeBook(self):
        ID = input("Enter the book ID to remove: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == ID:
                found = True
                continue
            updated_rows.append(line)

        if not found:
            print(f"No book found with ID {ID}.")
            return

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        print("Book removed successfully.")

    def getBookRow(self, ID):
        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[0] == ID:
                    return info
        return None

class BorrowRecord:
    def __init__(self):
        self.file = pathlib.Path("Borrowed_Books.csv")

        if not self.file.exists():
            with open(self.file, "w") as f:
                f.write("bookID,studentID,borrowdate,duedate,returned\n")

    def addRecord(self, bookID, studentID, borrowdate, duedate):
        with open(self.file, "a") as f:
            f.write(f"{bookID},{studentID},{borrowdate.isoformat()},{duedate.isoformat()},N\n")

    def getOpenRecordsForStudent(self, studentID):
        open_records = []

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[1] == studentID and info[4] == "N":
                    open_records.append(info)

        return open_records

    def countOpenForStudent(self, studentID):
        return len(self.getOpenRecordsForStudent(studentID))

    def markReturned(self, bookID, studentID):
        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        returned_duedate = None

        for line in rows:
            info = line.strip().split(",")
            if info[0] == bookID and info[1] == studentID and info[4] == "N" and returned_duedate is None:
                returned_duedate = info[3]
                info[4] = "Y"
                updated_rows.append(",".join(info) + "\n")
            else:
                updated_rows.append(line)

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        if returned_duedate is not None:
            year, month, day = returned_duedate.split("-")
            return date(int(year), int(month), int(day))
        return None

class PenaltyRecord:
    def __init__(self):
        self.file = pathlib.Path("Penalties.csv")

        if not self.file.exists():
            with open(self.file, "w") as f:
                f.write("studentID,bookID,amount,reason,paid\n")

    def addPenalty(self, studentID, bookID, amount, reason):
        with open(self.file, "a") as f:
            f.write(f"{studentID},{bookID},{amount},{reason},N\n")

    def getOpenPenaltiesForStudent(self, studentID):
        open_penalties = []

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[0] == studentID and info[4] == "N":
                    open_penalties.append(info)

        return open_penalties

    def getUnpaidTotal(self, studentID):
        total = 0
        for info in self.getOpenPenaltiesForStudent(studentID):
            try:
                total += float(info[2])
            except ValueError:
                continue
        return total

    def clearPenalties(self, studentID):
        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        cleared = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == studentID and info[4] == "N":
                info[4] = "Y"
                cleared = True
            updated_rows.append(",".join(info) + "\n")

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        return cleared

    def adjustPenalty(self, studentID, bookID, new_amount):
        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == studentID and info[1] == bookID and info[4] == "N" and not found:
                info[2] = str(new_amount)
                found = True
            updated_rows.append(",".join(info) + "\n")

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        return found

def calculateDueDate(borrow_date, weekdays=5):
    current = borrow_date
    added = 0
    while added < weekdays:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current

def calculateLateDays(due_date, return_date):
    late_days = 0
    current = due_date
    while current < return_date:
        current += timedelta(days=1)
        if current.weekday() < 5:
            late_days += 1
    return late_days

BORROW_LIMIT = 3
LATE_FEE_PER_DAY = 10

def StudentCatalogue():
    print("Student Catalogue selected.")
    print("1. Search Student by ID")
    print("2. Update Student Information")
    print("3. Add New Student ID")
    print("4. Quit")
    print("5. Delete Student Record")
    print("6. Search Student by Name")

    choice = input("Please select an option: ")

    if choice == "1":
        student_catalogue = StudentID()
        student_catalogue.SearchID()

    if choice == "2":
        student_catalogue = StudentID()
        student_catalogue.UpdateID()

    if choice == "3":
        student_catalogue = StudentID()
        student_catalogue.addid()

    if choice == "4":
        return

    if choice == "5":
        student_catalogue = StudentID()
        student_catalogue.deleteID()

    if choice == "6":
        student_catalogue = StudentID()
        student_catalogue.SearchByName()

def LibraryCatalogue():
    print("Library Catalogue selected.")
    print("1. Search Book by ID")
    print("2. Update Book Information")
    print("3. Add New Book")
    print("4. Quit")
    print("5. Remove Book")

    choice = input("Please select an option: ")

    if choice == "1":
        library_catalogue = Library()
        library_catalogue.SearchBook()

    if choice == "2":
        library_catalogue = Library()
        library_catalogue.UpdateBook()

    if choice == "3":
        library_catalogue = Library()
        library_catalogue.addBook()

    if choice == "4":
        return

    if choice == "5":
        library_catalogue = Library()
        library_catalogue.removeBook()

def UpdateLoginCredentials():
    print("Update Login Credentials selected.")
    print("1. Update Name")
    print("2. Change Password")
    print("3. Quit")
    choice = input("Please select an option: ")
        
    if choice == "1":
        old_name = input("Enter your current name: ")
        new_name = input("Enter your new name: ")
        lms.updateName(old_name, new_name)
    elif choice == "2":
        name = input("Enter your name: ")
        new_password = input("Enter your new password: ")
        lms.changePassword(name, new_password)
    else:
        print("Invalid option, please try again.")

    if choice == "3":
        return

def ViewOpenTransactions(studentID=None):
    student_catalogue = StudentID()
    borrow_records = BorrowRecord()
    penalty_records = PenaltyRecord()

    if studentID is None:
        studentID = input("Enter the student ID to view open transactions: ")

    student_row = student_catalogue.getStudentRow(studentID)
    if student_row is None:
        print(f"No student found with ID {studentID}.")
        return None

    print(f"--- Open Transactions for {student_row[1]} (ID: {studentID}) ---")

    open_books = borrow_records.getOpenRecordsForStudent(studentID)
    if open_books:
        print("Books currently borrowed:")
        for record in open_books:
            print(f"  Book ID: {record[0]} | Borrowed: {record[2]} | Due: {record[3]}")
    else:
        print("Books currently borrowed: none")

    open_penalties = penalty_records.getOpenPenaltiesForStudent(studentID)
    unpaid_total = penalty_records.getUnpaidTotal(studentID)
    if open_penalties:
        print("Unpaid penalties:")
        for penalty in open_penalties:
            print(f"  Book ID: {penalty[1]} | Amount: ₱{penalty[2]} | Reason: {penalty[3]}")
    else:
        print("Unpaid penalties: none")
    print(f"Total unpaid penalties: ₱{unpaid_total}")

    return student_row, open_books, unpaid_total

def BorrowBookProcess():
    print("Borrow Book selected.")
    studentID = input("Enter the student's ID: ")

    student_catalogue = StudentID()
    library_catalogue = Library()
    borrow_records = BorrowRecord()
    penalty_records = PenaltyRecord()

    student_row = student_catalogue.getStudentRow(studentID)
    if student_row is None:
        print(f"No student found with ID {studentID}.")
        return

    result = ViewOpenTransactions(studentID)
    if result is None:
        return
    _, open_books, unpaid_total = result

    if unpaid_total > 0:
        print("This student has unpaid penalties. Please settle penalties before borrowing.")
        return

    if borrow_records.countOpenForStudent(studentID) >= BORROW_LIMIT:
        print(f"Borrow limit reached ({BORROW_LIMIT} books). Cannot borrow more books.")
        return

    bookID = input("Enter the Book ID to borrow: ")
    book_row = library_catalogue.getBookRow(bookID)

    if book_row is None:
        print(f"No book found with ID {bookID}.")
        return

    try:
        available_copies = int(book_row[6])
    except (ValueError, IndexError):
        print("Book catalogue data is corrupted for this entry.")
        return

    if available_copies <= 0:
        print(f"Sorry, '{book_row[1]}' is currently unavailable.")
        return

    with open(library_catalogue.file, "r") as f:
        lines = f.readlines()
    header = lines[0]
    updated_lines = []
    for line in lines[1:]:
        info = line.strip().split(",")
        if info[0] == bookID:
            info[6] = str(available_copies - 1)
        updated_lines.append(",".join(info) + "\n")
    with open(library_catalogue.file, "w") as f:
        f.write(header)
        for line in updated_lines:
            f.write(line)

    borrow_date = date.today()
    due_date = calculateDueDate(borrow_date, 5)
    borrow_records.addRecord(bookID, studentID, borrow_date, due_date)

    current_books = student_row[4].split(";") if student_row[4] else []
    current_books.append(bookID)
    student_catalogue.updateBooksField(studentID, current_books)

    print(f"'{book_row[1]}' successfully borrowed by {student_row[1]}. Due date: {due_date.isoformat()}")

def ReturnBookProcess():
    print("Return Book selected.")
    studentID = input("Enter the student's ID: ")

    student_catalogue = StudentID()
    library_catalogue = Library()
    borrow_records = BorrowRecord()
    penalty_records = PenaltyRecord()

    student_row = student_catalogue.getStudentRow(studentID)
    if student_row is None:
        print(f"No student found with ID {studentID}.")
        return

    open_books = borrow_records.getOpenRecordsForStudent(studentID)
    if not open_books:
        print("This student has no currently borrowed books.")
        return

    print("Currently borrowed books:")
    for record in open_books:
        print(f"  Book ID: {record[0]} | Borrowed: {record[2]} | Due: {record[3]}")

    bookID = input("Enter the Book ID being returned: ")
    book_row = library_catalogue.getBookRow(bookID)

    if book_row is None:
        print(f"No book found with ID {bookID}.")
        return

    due_date = borrow_records.markReturned(bookID, studentID)
    if due_date is None:
        print(f"No open borrow record found for Book ID {bookID} and Student ID {studentID}.")
        return

    try:
        total_copies = int(book_row[5])
        available_copies = int(book_row[6])
    except (ValueError, IndexError):
        print("Book catalogue data is corrupted for this entry.")
        return

    with open(library_catalogue.file, "r") as f:
        lines = f.readlines()
    header = lines[0]
    updated_lines = []
    for line in lines[1:]:
        info = line.strip().split(",")
        if info[0] == bookID and available_copies < total_copies:
            info[6] = str(available_copies + 1)
        updated_lines.append(",".join(info) + "\n")
    with open(library_catalogue.file, "w") as f:
        f.write(header)
        for line in updated_lines:
            f.write(line)

    return_date = date.today()
    late_days = calculateLateDays(due_date, return_date)

    if late_days > 0:
        penalty_amount = late_days * LATE_FEE_PER_DAY
        penalty_records.addPenalty(studentID, bookID, penalty_amount, f"{late_days} day(s) late")

        try:
            current_total = float(student_row[5]) if student_row[5] else 0
        except ValueError:
            current_total = 0
        student_catalogue.updatePenaltyField(studentID, current_total + penalty_amount)

        print(f"'{book_row[1]}' returned {late_days} day(s) late. Penalty of ₱{penalty_amount} applied.")
    else:
        print(f"'{book_row[1]}' returned on time. No penalty.")

    current_books = student_row[4].split(";") if student_row[4] else []
    if bookID in current_books:
        current_books.remove(bookID)
    student_catalogue.updateBooksField(studentID, current_books)

def ManagePenalties():
    print("Manage Penalties selected.")
    print("1. View Unpaid Penalties for a Student")
    print("2. Add Penalty")
    print("3. Clear Penalties for a Student")
    print("4. Adjust a Penalty Amount")
    print("5. Quit")

    choice = input("Please select an option: ")
    penalty_records = PenaltyRecord()
    student_catalogue = StudentID()

    if choice == "1":
        studentID = input("Enter the student ID: ")
        open_penalties = penalty_records.getOpenPenaltiesForStudent(studentID)
        if open_penalties:
            for penalty in open_penalties:
                print(f"  Book ID: {penalty[1]} | Amount: ₱{penalty[2]} | Reason: {penalty[3]}")
        else:
            print("No unpaid penalties for this student.")
        print(f"Total unpaid: ₱{penalty_records.getUnpaidTotal(studentID)}")

    if choice == "2":
        studentID = input("Enter the student ID: ")
        if student_catalogue.getStudentRow(studentID) is None:
            print(f"No student found with ID {studentID}.")
            return
        bookID = input("Enter the related Book ID (leave blank if none): ")
        try:
            amount = float(input("Enter the penalty amount: "))
        except ValueError:
            print("Invalid amount entered.")
            return
        reason = input("Enter the reason for the penalty: ")
        penalty_records.addPenalty(studentID, bookID, amount, reason)

        student_row = student_catalogue.getStudentRow(studentID)
        try:
            current_total = float(student_row[5]) if student_row[5] else 0
        except ValueError:
            current_total = 0
        student_catalogue.updatePenaltyField(studentID, current_total + amount)
        print("Penalty added successfully.")

    if choice == "3":
        studentID = input("Enter the student ID: ")
        cleared = penalty_records.clearPenalties(studentID)
        if cleared:
            student_catalogue.updatePenaltyField(studentID, 0)
            print("All unpaid penalties cleared for this student.")
        else:
            print("No unpaid penalties found for this student.")

    if choice == "4":
        studentID = input("Enter the student ID: ")
        bookID = input("Enter the Book ID for the penalty to adjust: ")
        try:
            new_amount = float(input("Enter the new penalty amount: "))
        except ValueError:
            print("Invalid amount entered.")
            return
        if penalty_records.adjustPenalty(studentID, bookID, new_amount):
            print("Penalty adjusted successfully.")
        else:
            print("No matching unpaid penalty found.")

    if choice == "5":
        return

def StartMenu():
        print("Select the desired process:")
        print("1. Check Student Catalogue")
        print("2. Check Library Catalogue")
        print("3. Update Login Credentials")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Open Transactions")
        print("7. Manage Penalties")
        print("8. Quit")

        choice = input("Please select an option: ")

        if choice == "1":
            StudentCatalogue()

        if choice == "2":
            LibraryCatalogue()

        if choice == "3":
            UpdateLoginCredentials()

        if choice == "4":
            BorrowBookProcess()

        if choice == "5":
            ReturnBookProcess()

        if choice == "6":
            ViewOpenTransactions()

        if choice == "7":
            ManagePenalties()
        
        if choice == "8":
            return
        
if __name__ == "__main__":
    lms = LoginSystem()
    if lms.checkLogin() == True:
        StartMenu()