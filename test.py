import pdftotext

CONFIG = {
        'From': {
            'row': [7, 8],
            'column': [29, 91],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'To': {
            'row': [7, 8],
            'column': [113, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'Booking No.': {
            'row': [9, 10],
            'column': [29, 91],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'Date': {
            'row': [8, 9],
            'column': [29, 91],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'Shipper Name & Address': {
            'row': [12, 18],
            'column': [4, 91],
            'startFlex': False,
            'endObject': 'Notify Party',
            'verticalFlex': True
        },
        'Consignee Name & Address': {
            'row': [12, 18],
            'column': [92, None],
            'startFlex': False,
            'endObject': 'Port of Loading',
            'verticalFlex': True
        }
}

CURR_CONFIG = {}
fileName = "VN101466/SI_HANV07496600.pdf"

if __name__ == '__main__':
    with open(fileName, "rb") as f:
        pdf = pdftotext.PDF(f)
    page = pdf[0].split("\n")

    # for i in range(len(page)):
    #     print(i)
    #     print([str(k) + page[i][k] for k in range(len(page[i]))])
    data = {}
    for key in CONFIG:
        # print(key)
        row = CONFIG[key]['row']
        column = CONFIG[key]['column']
        # print(row)
        # print(column)
        lines = page[row[0]:row[1]]
        data[key] = '\n'.join([x[column[0]:column[1]] for x in lines])

    for key in data:
        print("%s: %s" % (key, data[key]))
