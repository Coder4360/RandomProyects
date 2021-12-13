f = open("calculator_bookmarks.html", "w")
f.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3 ADD_DATE="0" LAST_MODIFIED="0" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks bar</H3>
    <DL><p>
        <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">Calculator</H3>
        <DL><p>
""")
for i in range(10):
    f.write(f"""            <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">{i}0</H3>
            <DL><p>
""")
    for i2 in range(10):
        f.write(f"""                <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">{i}{i2}</H3>
                <DL><p>
""")  # First number
        for operator in ["+", "-", "\xD7", "\xF7", "mod"]:
            f.write(f"""                    <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">{operator}</H3>
                    <DL><p>
""") # Operator
            for i3 in range(10):
                f.write(f"""                        <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">{i3}0</H3>
                        <DL><p>
""")
                for i4 in range(10):
                    f.write(f"""                            <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">{i3}{i4}</H3>
                            <DL><p>
""") # Second number
                    result = {"+": (i * 10 + i2) + (i3 * 10 + i4), "-": (i * 10 + i2) - (i3 * 10 + i4),
                    "\xD7": (i * 10 + i2) * (i3 * 10 + i4), "\xF7": ((i * 10 + i2) / (i3 * 10 + i4)) \
                    if (i3 + i4) > 0 else "NaN", "mod": ((i * 10 + i2) % (i3 * 10 + i4)) \
                    if (i3 + i4) > 0 else "NaN"}[operator]
                    f.write(f"""                                <DT><A HREF="chrome://new-tab-page/" ADD_DATE="0">{result}</A>
                            </DL><p>
""")
                f.write("                        </DL><p>\n")
            f.write("                    </DL><p>\n")
            continue
        f.write("""                    </DL><p>
                    <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">^</H3>
                    <DL><p>
""")
        for power in [1/3, 1/2, 2, 3]:
            power_display = str(power).replace("0.5", "\xBD").replace("0.3333333333333333", "\u2153")
            f.write(f"""                        <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">{power_display}</H3>
                    <DL><p>
                        <DT><A HREF="chrome://new-tab-page/" ADD_DATE="0">{(i * 10 + i2) ** power}</A>
                    </DL><p>
""")
        f.write("                    </DL><p>\n")
        f.write("                </DL><p>\n")
    f.write("            </DL><p>\n")
f.write("        </DL><p>\n")
f.write("    </DL><p>\n")
f.write("</DL><p>\n")