from html.parser import HTMLParser
import os

paragraphs = 0
# Create a subclass and override the handler methods
# These methods are called when the parser encounters
# an HTML tag, comment, etc.
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment:", data)
        pos = self.getpos()
        print("At line", pos[0], "position", pos[1])

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        pos = self.getpos()
        print("At line", pos[0], "position", pos[1])

        # Count number of <p> tags
        global paragraphs
        if tag == "p":
            paragraphs += 1

        if len(attrs) > 0:
            print("Attributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered text data:", data)
        pos = self.getpos()
        print("At line", pos[0], "position", pos[1])

def main():
    parser = MyHTMLParser()
    
    os.chdir("internet")
    file = open("sample.html")
    if file.mode == "r":
        contents = file.read()
        parser.feed(contents)

    print ("Number of <p> tags:", paragraphs)

if __name__ == "__main__":
    main()