class Bookmark: # Bookmark class
    def __init__(self, name, url, add_date = 0):
        self.name = name
        self.url = url
        self.add_date = add_date
    def __str__(self): # HTML representation of the bookmark
        return f"<DT><A ADD_DATE=\"{self.add_date}\" HREF=\"{self.url}\">{self.name}</A>"

class Folder: # Bookmark folder class
    def __init__(self, name, add_date = 0, last_modified = 0):
        self.name = name
        self.add_date = add_date
        self.last_modified = last_modified
        self.structure = []
    def add(self, item): # Add an item to the folder
        self.structure.append(item)
    def __str__(self): # HTML representation of the folder
        global indentation_string, line_separator
        string = f"<DT><H3 ADD_DATE=\"{self.add_date}\" LAST_MODIFIED=\"{self.last_modified}\">{self.name}</H3>{line_separator}<DL><p>{line_separator}"
        for item in self.structure:
            string += indentation_string + str(item) + line_separator
        return string + "</DL><p>"

class Bookmark_Toolbar:
    def __init__(self, name, add_date = 0, last_modified = 0, personal_toolbar = False):
        self.name = name
        self.add_date = add_date
        self.last_modified = last_modified
        self.structure = []
        self.personal_toolbar = personal_toolbar
    def add(self, item): # Add an item to the bookmark toolbar
        self.structure.append(item)
    def __str__(self): # HTML representation of the bookmark toolbar
        global indentation_string
        string = f"<DT><H3 ADD_DATE=\"{self.add_date}\" LAST_MODIFIED=\"{self.last_modified}\">{self.name}</H3>{line_separator}<DL><p>{line_separator}"
        for item in self.structure:
            string += indentation_string + str(item) + line_separator
        return string + "</DL><p>"

class Bookmarks_HTML: # Bookmarks HTML class
    def __init__(self, title):
        self.title = title
        self.structure = []
    def add(self, item): # Adds a toolbar to the bookmarks
        self.structure.append(item)
    def __str__(self): # HTML representation of the bookmarks
        global indentation_string, line_separator
        string = f"<!DOCTYPE NETSCAPE-Bookmark-file-1>{line_separator}<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\">{line_separator}<TITLE>{self.title}</TITLE>{line_separator}<H1>{self.title}</H1>{line_separator}<DL><p>"
        for item in self.structure:
            string += indentation_string + str(item) + line_separator
        return string + "</DL><p>"

indentation_string = "    " # Indentation string
line_separator = "\n" # Line separator