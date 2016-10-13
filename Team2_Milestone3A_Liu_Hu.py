import re
import sys

# Created by Junjie Liu(AndrewID: junjiel1)
# Created by Qianyi Hu(AndrewID: qianyih)
def getAbstract(paragraph):

    if paragraph.find("keywords:") != -1:
        abstract = re.findall(r'Abstract:(.*)keywords:', paragraph)[0]
    elif "URL:" in paragraph:
        abstract = re.findall(r'Abstract:(.*)URL:', paragraph)[0]
    else:
        abstract = paragraph.split("Abstract:")[1]

    return abstract

def getAuthor_Title(paragraph):

    list = paragraph.split('"')
    author = list[0]
    title = list[1]
    author = author.strip()
    title = title.strip()
    if len(author) > 1 and author[len(author) - 1] == ',':
        author = author[0: len(author) - 1]
    if title[len(title) - 1] == ',':
        title = title[0: len(title) - 1]
    return author, title

def generateHTML(author, title, abstract, name):
    name = name + ".html"
    file = open(name, 'a')

    message = """
    <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            </head>

            <body>
                <div class="container" style="margin-top: 30px">
                    <div class="jumbotron">
                        <h2> """ + title + """</h2>
                        <h4 style="margin-left: 20px">""" + author + """</h4>
                        <p>Abstract: """ + abstract + """</p>
                    </div>
                </div>
            </body>
        </html>
    """
    file.write(message)
    file.close()

def verify(paragraph):
    if paragraph.find("[Front cover],") == -1 and paragraph.find("[Front matter],") == -1:
        return True
    return False

def main():

    sys.stdout.encoding = 'utf-8'
    url = input("Please enter the address of the file: ")
    reachable = True
    while reachable:
        reachable = False
        try:
            file = open(url, 'r', encoding="utf-8")
        except FileNotFoundError:
            reachable = True
            url = input("Please make sure you enter a right address:")

    paragraph = ""
    filename = 0
    for line in file.readlines():
        if line != "\n":
            paragraph += line.replace("\n", " ")
        else:
            if verify(paragraph):
                filename += 1
                author, title = getAuthor_Title(paragraph)
                abstract = getAbstract(paragraph)
                generateHTML(author, title, abstract, str(filename))
            paragraph = ""
    file.close()


main()
