import re
from datetime import datetime

from tabulate import tabulate


def file_reader(filename):
    table = []
    with open(filename) as file:
        log = file.read().split('\n')
        date_exp = r"\w{1,3}\s{1,3}\w{1,3}\s{1,3}\d{1,2}\s\d{1,2}\:\d{1,5}\:\d{1,5}\s\d{1,4}"
        regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}"
        for line in log:
            if re.search(regexp, line):
                ip_address = (re.findall(regexp, line))
                date = (re.findall(date_exp, line))
                formatted_date = datetime.strptime(date[0], '%c').strftime('%m/%d/%y %H:%M:%S %p')

                lst = [formatted_date, ip_address[0]]
                table.append(lst)
    return table


def show_tabulated_data():
    table = file_reader('log.txt')
    print(tabulate(table, headers=['Date', 'Client IP']))


def main():
    show_tabulated_data()


main()
