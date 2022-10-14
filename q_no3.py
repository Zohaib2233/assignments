import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def write_file(url, file_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    file = open(file_name, 'w')
    file.write(soup.find('p').text)
    file.close()


def file_reader(file_name):
    file = open(file_name, 'r')
    data = file.read()
    file.close()
    dic = {}
    table = []
    for chapter in range(1, 13):
        chapter_number = ("CHAPTER " + data.split('CHAPTER')[chapter].split('\n')[0])
        chapter_name = (data.split('CHAPTER')[chapter].split('\n')[4].strip())
        paragraph = data.split('CHAPTER')[chapter].split('\n')[5:]
        try:
            while True:
                paragraph.remove("")
        except ValueError:
            pass

        words = ''.join(paragraph).strip().split(" ")
        while "" in words:
            words.remove("")

        stop_words = read_stop_words()
        words = list(set(words) - set(stop_words))
        dic[chapter_number + " : " + chapter_name] = set(words)
        name = [chapter_number, chapter_name, len(set(words))]
        table.append(name)

    for key, value in dic.items():
        print(key, ' : ', value)
    return table


def show_tabulated_data():
    table = file_reader('book.txt')
    print("\n\t\tOutput")
    print("\n" + tabulate(table, headers=["CHAPTER", "CHAPTER TITLE", "UNIQUE WORDs"]))


def read_stop_words():
    file = open('stop_words.txt', 'r')
    words = ''.join(file.read()).strip('[ \n] , \"\"').replace('"', '').replace('    ', '').split('\n')
    return words


def main():
    write_file("https://www.gutenberg.org/files/11/old/alice30.txt", 'book.txt')
    write_file('https://cse2050.drfitz.fit/data/very/stop_words.txt', 'stop_words.txt')
    show_tabulated_data()


main()
