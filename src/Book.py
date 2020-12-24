import json
import datetime
import uuid

class Book:
    """ 
    A class used to represent a book.
    ...

    Attributes:
    ----------
    title: str
    description: str
    id: int
    """
    def __init__(self):
        self.title = ""
        self.description = ""
        self.id = uuid.uuid4()

    def setTitle(self, title):
        self.title = title
        return True

    def setDescription(self, description):
        self.descrition= description
        return True

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def saveAsJSON(self):
        bookAsDict = {
                f'{self.id}': {
                    'title': f'{self.title}',
                    'description': f'{self.description}'
                }
        }
        noWhiteSpaceTitle = self.title.replace(" ", "")
        timeStamp = datetime.datetime.now().strftime("%Y-%m-%d")
        bookName = f'{noWhiteSpaceTitle}_{timeStamp}.json'
        # TODO: save the file into data folder
        with open(bookName, 'w') as book:
            json.dump(bookAsDict, book, indent=4)
        return True












