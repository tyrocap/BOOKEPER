#!/usr/bin/python3

from src.Book import Book

def main():
    curBook = Book()
    curBook.setTitle("Cracking the Coding Interview")
    curBook.setDescription("Good book")
    curBook.saveAsJSON()


if __name__ == "__main__":
    main()



