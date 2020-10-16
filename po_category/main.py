import sys
import csv
import os


def parse_table(path):
    table = []
    with open(path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, quotechar='"')
        for row in spamreader:
            table.append(row)
    return table


def deal_csv(path):
    print("input: " + path)
    output_path = os.path.dirname(path)+'\output.csv'
    print("input: " + output_path)
    table = parse_table(path)
    # PO Document+PO Item # Confirmation Category with AB without LA
    checktable = {}
    cb = table[0].index("PO Item")
    pd = table[0].index("PO Document")
    cc = table[0].index("Confirmation Category")

    for row in table[1:]:
        key = row[cb] + '/' + row[pd]
        try:
            checktable[key]
        except KeyError:
            if row[cc] == "LA":
                checktable[key] = 1
    with open(output_path, 'wb') as csvfile:
        writer = csv.writer(csvfile, quotechar='"')
        writer.writerow(table[0])
        for row in table[1:]:
            key = row[cb] + '/' + row[pd]
            try:
                checktable[key]
            except KeyError:
                writer.writerow(row)


if len(sys.argv) > 1:
    if sys.argv[1].endswith(".csv"):
        deal_csv(sys.argv[1])
