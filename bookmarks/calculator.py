# Modules
try: from bookmarks import Bookmarks_HTML, Bookmark_Toolbar, Folder, Bookmark
except: print("Bookmarks module not found, download at https://raw.githubusercontent.com/Coder4360/RandomProyects/main/bookmarks/bookmarks.py")

# Variables
html = Bookmarks_HTML("Bookmarks") # Bookmarks HTML object
toolbar = Bookmark_Toolbar("Bookmarks Toolbar", personal_toolbar = True) # Bookmarks toolbar object
bookmarks = Folder("Calculator") # Bookmarks folder object

# Main code
for i in range(10):
    folder = Folder(str(i * 10))
    for i2 in range(10):
        folder2 = Folder(str(i * 10 + i2))
        for operator in ["+", "-", "*", "/", "%"]:
            operator_display = operator.replace("*", "\xD7").replace("/", "\xF7").replace("%", "mod")
            folder3 = Folder(operator_display)
            for i3 in range(10):
                folder4 = Folder(str(i3 * 10))
                for i4 in range(10):
                    folder5 = Folder(str(i3 * 10 + i4))
                    folder5.add(Bookmark(eval(str(i * 10 + i2) + operator + str(i3 * 10 + i4)) if i3 + i4 > 0 else "NaN", "chrome://newtab"))
                    folder4.add(folder5)
                folder3.add(folder4)
            folder2.add(folder3)
        folder3 = Folder("^")
        for power in [1 / 3, 1 / 2, 2, 3]:
            power_display = str(power).replace("0.5", "\xBD").replace("0.3333333333333333", "\u2153")
            folder4 = Folder(power_display)
            folder4.add(Bookmark(eval(str(i * 10 + i2) + "**" + str(power)), "chrome://newtab"))
            folder3.add(folder4)
        folder2.add(folder3)
        folder.add(folder2)
    bookmarks.add(folder)
toolbar.add(bookmarks)
html.add(toolbar)
file = open(input("File name: "), "w")
file.write(str(html))