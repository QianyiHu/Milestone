# Team2_Milestone3B
# Team member: Junjie Liu (junjiel1)
# Team member: Qianyi Hu (qianyih)

# Requirement: keywords be sorted in ascending order on the index.html page.
# inventory file, file I/O, read the file, delete junk words and substitution

import csv
import re
import sys

# separate the file into a list of each paragraphs
def generateParagraph(file):
    paragraph = ""
    paragraphList=[]
    for line in file.readlines():
        if line != "\n":
            paragraph += line.replace("\n", " ")
        else:
            paragraphList.append(paragraph)
            paragraph=""
    return paragraphList


def substitute(string):
    # separate the paragraph into a list of words
    wordlist = re.split('\W+', string)

    csvfile = open("Team2_Milestone3 BSub_Liu_Hu.csv", newline='', encoding="utf-8")
    wordReader = csv.reader(csvfile)
    # each row is a list of string now

    #substitue the list
    for i in range(len(wordlist)):
        for row in wordReader:
            if wordlist[i].lower() == row[0]:
                wordlist[i] = row[1]

    # remove junk word
    noise_word_file = open("TeamX_Milestone3 BDel_ Liu_ Hu.txt", "r", encoding="utf-8")
    noise_word = []
    for line in noise_word_file:
        noise_word.append(line[0:len(line)-1])

    for word in wordlist:
        for item in noise_word:
            if word.lower() == item:
                wordlist.remove(word)
                break

    for word in wordlist:
        for item in noise_word:
            if word.lower() == item:
                wordlist.remove(word)
                break

    return wordlist
    # now you get the list of each paragraph words after removing the junk and misspelling words


def selectElement(paragraph):
    # get title
    title = paragraph.split('"')[1][0:-1]

    # get abstract
    if paragraph.find("keywords:") != -1:
        abstract = re.findall(r'Abstract:(.*)keywords:', paragraph)[0]
    elif "URL:" in paragraph:
        abstract = re.findall(r'Abstract:(.*)URL:', paragraph)[0]
    else:
        abstract = paragraph.split("Abstract:")[1]


    # select author
    temp_author = paragraph.split('"')[0][0:-2]
    author_list=[]
    if "and" in temp_author:
        auth = temp_author.split(" and ")
        if "," in auth[0]:
            author_list = auth[0].split(", ")
            author_list.append(auth[1])
        else:
            author_list = auth
    else:
        author_list.append(temp_author)

    # select keywords
    keyword_start = paragraph.index("keywords: {") + 11
    keyword_end = paragraph.index("},")
    keyword_given = paragraph[keyword_start:keyword_end].split(";")


    # select url
    url_start = paragraph.index("URL:")+4
    url = paragraph[url_start:]

    return title, abstract, author_list, keyword_given, url

def display(list):
    content = ""

    for item in list:
        content += "<a href=\"www.google.com\">" + item + "</a><br>"
    return content


def generate_HTML(list):
    name = "index.html"
    file = open(name, 'w', encoding="utf-8")

    message = """
        <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8" >
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                </head>
                <body>
                    <div class="container" style="margin-top: 30px; word-wrap: break-word; word-break: normal">
                        <div class="jumbotron">
                            <h2> Keywords: </h2>
                            <div>"""+display(list)+""""</div>
                        </div>
                    </div>
                </body>
            </html>
        """
    file.write(message)
    file.close()

def main():

    # sys.stdout.encoding = 'utf-8'
    url = input("Please enter file name(pls type \"sample.txt\" as the inventory file name: ")
    reachable = True
    while reachable:
        reachable = False
        try:
            file = open("sample.txt", 'r', encoding="utf8")
        except FileNotFoundError:
            reachable = True
            url = input("Please make sure you enter a right address:")

    paragraphlist = generateParagraph(file)

    total_keyword = []
    for paragraph in paragraphlist[2:]:
        title, abstract, author_list, keyword_given, url = selectElement(paragraph)

        abs_list = substitute(abstract)
        title_list = substitute(title)
        keyword_list = list(set(abs_list + title_list + keyword_given + author_list))

        total_keyword += keyword_list

    print(sorted(list(set(total_keyword))))
    generate_HTML(sorted(list(set(total_keyword))))
    print("Please refer to the \'index.html\' file in the directory.")


main()