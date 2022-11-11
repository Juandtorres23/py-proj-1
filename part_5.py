### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def adding_book():

    book_name = input('Name of book?  ')

    book_author = input('Name of author?  ')
    try:
        book_pages = int(input('Number of pages in book?  '))
    except:
        book_pages = int(input("Please use numbers for the pages"))
    try:
        book_year = int(input('Year the book was published?  '))
    except:
        book_year = int(input("Please use number for year"))
    try:
        book_rating = float(input('Rating on book from 0 - 5?  '))
    except:
        book_rating = float(input("Please use numbers and decimals to rate this book from 0 - 5"))

    with open("library.txt", "a") as f:
        f.write(f"{book_name}, {book_author}, {book_year}, {book_rating}, {book_pages} \n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def all_books():
    book_library = []
    with open("library.txt", "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }
            book_library.append(book_dictionary)

    return book_library
        


def print_books(book_list):
    for book in book_list:
        print(f"{book['title']} by {book['author']}")


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script
def main_menu():
    open_menu = True

    while open_menu == True:
        user_input = input("What would you like to do?  1-add a book   2-check library  3-filter by rating  4-filter by largest book  5-filter by smallest book  6-exit -> ")

        if user_input == "1":
            adding_book()
            print("Book added successfully")
        elif user_input == "2":
            print_books(all_books())
        elif user_input == "3":
            filter_by_rating(all_books())
        elif user_input == "4":
            print(largest_book(all_books()))
        elif user_input == "5":
            print(smallest_book(all_books()))
        elif user_input == "6":
            open_menu = False


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
def largest_book(book_list):
    large_book = ''
    page_num = 0
    for book in book_list:
        if book['pages'] > page_num:
            page_num = book['pages']
            large_book = book['title']
        else:
            pass
    return f"The largest book in your list is {large_book} which contains {page_num} pages!"


def smallest_book(book_list):
    small_book = ''
    page_num = 100000
    for book in book_list:
        if book['pages'] < page_num:
            page_num = book['pages']
            small_book = book['title']
        else:
            pass
    return f"The largest book in your list is {small_book} which contains {page_num} pages!"

def filter_by_rating(book_list):
    user_input = float(input("What rating are you interested in? -> "))
    rating_match = []

    for book in book_list:
        if user_input == book['rating']:
            rating_match.append(book["title"])
        else:
            pass
    if len(rating_match) > 0:
        for book in rating_match:
            print(f"{book} matches that rating.")
    else:
        print("There are no books that match that rating!")


# print(largest_book(all_books()))
# print(smallest_book(all_books()))



if __name__ == "__main__":
    main_menu()
