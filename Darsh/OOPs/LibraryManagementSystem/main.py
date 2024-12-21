from configurationHelper import __config__
from service import BookService, MemberService, StaffService, LibraryService


def main():
    # region Initiate Services
    bookService = BookService()
    memberservice = MemberService()
    staffService = StaffService()
    libraryService = LibraryService()
    # endregion


# Synchronously done programming
# Asynchronously done programming  -> 


def downloadImage(url): 
    pass


for url in urls:
    downloadImage(url)