import urllib

def read_file():
    input_file = open('input.txt', 'r')
    content_of_file = input_file.read()
    print(content_of_file)

def check_curse_words(content):
    print('hi')
    # open url and use inpput text
    connection = urllib.urlopen('http://google.com')
    bar = connection.read()
    print(bar)


    #print out

    #if condition for readability


read_file()
