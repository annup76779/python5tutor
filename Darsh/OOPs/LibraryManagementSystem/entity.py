class Book:
    def __init__(self, id, name, author, edition, genre):
        self.id = id
        self.name = name
        self.author = author
        self.edition = edition
        self.genre = genre
        self.member = None
        self.durationAlloted = None
        self.dateTimeAlloted = None
        self.staffId = None


class Member:
    def __init__(self, id, name, durationOfMembership, dateTimeOfMembership, staffId):
        self.id = id
        self.name = name
        self.books = []
        self.durationOfMembership = durationOfMembership
        self.dateTimeOfMembership = dateTimeOfMembership
        self.staffId = staffId


class Staff:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Library:
    def __init__(self, name):
        self.name = name
        self.staffs = []
        self.books = []
        self.members = []