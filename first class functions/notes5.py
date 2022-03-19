# You can return the function from a function (practical example)
def html_tag(tag):
    # function within a function
    def wrap_text(message):
        print("<{0}>{1}</{0}>".format(tag, message))

    return wrap_text


html_line = html_tag("h1")
print(html_line)
html_line("Title headline")

# it's easy to do the same thing with simple class
