from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import darkcyan, lightsalmon
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import A4
import datetime
from SampleData import sample_list
from invoice_values import Name, Adress_Line_1, Adress_Line_2, Adress_Line_3, Adress_Line_4, client_name,\
    client_adress_line_1, client_adress_line_2, client_adress_line_3, client_adress_line_4

date_data = datetime.datetime.now().strftime("%Y-%m-%d")

y = A4[1] - 135
x = A4[0]
space = 14

document = canvas.Canvas("Example Invoice.pdf", pagesize=A4)


def set_header(seller_name='Sebastian'):

    document.setLineWidth(5)
    document.setStrokeColor(lightsalmon)
    document.setFillColor(darkcyan)
    document.rotate(10)
    document.rect(90, A4[1]-120, 800, 250, 1, 1)
    document.rotate(-10)

    document.setFont("Helvetica-Bold", 16)
    document.drawString(50, y, seller_name)
    document.setFont("Helvetica", 11)
    document.drawString(50, y - space, Adress_Line_1)
    document.drawString(50, y - space * 2, Adress_Line_2)
    document.drawString(50, y - space * 3, Adress_Line_3)
    document.drawString(50, y - space * 4, Adress_Line_4)

    document.drawRightString(x - 50, y - space * 9, "Prepared date")
    document.drawRightString(x - 50, y - space * 10, date_data)

    document.drawString(50, y - space * 7, "Invoice to:")
    document.setFont("Helvetica-Bold", 16)
    document.drawString(50, y - space * 9, client_name)
    document.setFont("Helvetica", 11)
    document.drawString(50, y - space * 10, client_adress_line_1)
    document.drawString(50, y - space * 11, client_adress_line_2)
    document.drawString(50, y - space * 12, client_adress_line_3)
    document.drawString(50, y - space * 13, client_adress_line_4)


def set_footer():
    document.setFillColor(darkcyan)
    document.drawCentredString(x / 2, y - space * 46, "Bank Details:")
    document.drawCentredString(x / 2, y - space * 47, "Sort Code: 11-22-33")
    document.drawCentredString(x / 2, y - space * 48, "Account Number: 12345789")
    document.drawCentredString(x / 2, y - space * 49, "Name: Mack Sebastian")


def create_table(list_of_items, items_per_page=13):

    [i.insert(1, '') for i in list_of_items]

    list_of_items = [
        i + [i[2] * i[3]] for i in list_of_items
    ]
    total = sum(i[4] for i in list_of_items)
    for i in range(0, len(list_of_items), items_per_page):
        list_of_items.insert(i, [
            'ITEM NAME ', '', 'QTY',
            'PRICE PER UNIT', 'TOTAL'
        ])

    list_of_items = [
        list_of_items[i:i + items_per_page]
        for i in range(0, len(list_of_items), items_per_page)
    ]
    list_of_items[-1].append([
        'TOTAL: ' + str(total)
    ])

    print(list_of_items)

    t = Table(list_of_items[0], 5 * [1.4 * inch], len(list_of_items[0]) * [0.5 * inch])

    if len(list_of_items) == 1:
        t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
                               ('ALIGN', (0, -1), (0, -1), 'RIGHT'),
                               ('BACKGROUND', (0, 0), (-1, 0), colors.lightgoldenrodyellow),
                               ('BACKGROUND', (0, -1), (0, -1), colors.lightgrey),
                               ('SPAN', (0, -1), (-1, -1)),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.grey),
                               ('BOX', (0, 0), (-1, -1), 1, colors.grey)]))

        for i in range(len(list_of_items[0]) - 1):
            t.setStyle(TableStyle([('SPAN', (0, i), (1, i))]))

    else:
        t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
                               ('BACKGROUND', (0, 0), (-1, 0), colors.lightgoldenrodyellow),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.grey),
                               ('BOX', (0, 0), (-1, -1), 1, colors.grey)]))

        for i in range(len(list_of_items[0])):
            t.setStyle(TableStyle([('SPAN', (0, i), (1, i))]))

    row_space = 0.5 * inch * (len(list_of_items[0]) - 2)
    t.wrapOn(document, 60, y - 300)
    t.drawOn(document, 50, y - space * 20 - row_space)

    for i in range(1, len(list_of_items)):
        document.showPage()
        t_new = Table(list_of_items[i], 5 * [1.4 * inch], len(list_of_items[i]) * [0.5 * inch])
        if i == len(list_of_items) - 1:
            t_new.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
                                      ('ALIGN', (0, -1), (0, -1), 'RIGHT'),
                                      ('BACKGROUND', (0, 0), (-1, 0), colors.lightgoldenrodyellow),
                                      ('BACKGROUND', (0, -1), (0, -1), colors.lightgrey),
                                      ('SPAN', (0, -1), (-1, -1)),
                                      ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.grey),
                                      ('BOX', (0, 0), (-1, -1), 1, colors.grey)]))
            for j in range(len(list_of_items[i]) - 1):
                t_new.setStyle(TableStyle([('SPAN', (0, j), (1, j))]))
        else:
            t_new.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                       ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
                                       ('BACKGROUND', (0, 0), (-1, 0), colors.lightgoldenrodyellow),
                                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.grey),
                                       ('BOX', (0, 0), (-1, -1), 1, colors.grey)]))
            for j in range(len(list_of_items[i])):
                t_new.setStyle(TableStyle([('SPAN', (0, j), (1, j))]))

        row_space = 0.5 * inch * (len(list_of_items[i]) + 2)
        t_new.wrapOn(document, 60, y - 300)
        t_new.drawOn(document, 50, A4[1] - row_space)


# set_header()

# create_table(sample_list)

# set_footer()


document.save()
