from PySide2.QtGui import *
from PySide2.QtWidgets import *
import csv
from Classes import *
from datetime import datetime

user_list = []
product_list = []
sale_records = []
giftCards = []

app = QApplication([])  # Start an application.


def clockOut(user):
    clock_in_time = datetime.strptime(user.clock_in, '%H:%M')
    hoursWorked = datetime.now() - clock_in_time
    hoursWorked = round(hoursWorked.total_seconds() / 3600)
    user.hoursWorked += hoursWorked


def exitApp():
    app.exit
    saveData()


def saveData():
    with open('csv_files/user_file.csv', mode='w', newline='') as user_file:
        fieldnames = ['user_id', 'name', 'pin', 'accessLevel', 'payrate', 'hoursWorked', 'clock-in']

        user_writer = csv.writer(user_file)
        user_writer.writerow(fieldnames)
        for user in user_list:
            user_writer.writerow(
                (user.user_id, user.name, user.pin, user.accessLevel, user.payrate, user.hoursWorked, user.clock_in))
    with open('csv_files/product_file.csv', mode='w', newline='') as product_file:
        fieldnames = ['product_id', 'name', 'price', 'costToMake', 'tax']

        product_writer = csv.writer(product_file)
        product_writer.writerow(fieldnames)
        for product in product_list:
            product_writer.writerow((product.product_id, product.name, product.price, product.costToMake, product.tax))
    with open('csv_files/giftcards_file.csv', mode='w', newline='') as giftcards_file:
        fieldnames = ['cardNum', 'startAmount', 'currentBalance']

        giftcard_writer = csv.writer(giftcards_file)
        giftcard_writer.writerow(fieldnames)
        for cards in giftCards:
            giftcard_writer.writerow((cards.cardNum, cards.startAmount, cards.currentBalance))


with open('csv_files/sales_file.csv', mode='w', newline='') as sales_file:
    fieldnames = ['checkNum', 'date', 'time', 'products', 'user', 'paymentType', 'paymentAmount', 'tax', 'discount',
                  'refunded']

    sales_writer = csv.writer(sales_file)
    sales_writer.writerow(fieldnames)
    for sale in sale_records:
        sales_writer.writerow((sale.checkNum, sale.date, sale.time, sale.products, sale.user, sale.paymentType,
                               sale.paymentAmount, sale.tax, sale.discount, sale.refunded))


def readData():
    with open('csv_files/user_file.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = []
        rows = []
        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        for row in rows:
            user_list.append(User(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    with open('csv_files/product_file.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = []
        rows = []
        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        for row in rows:
            product_list.append(Product(row[0], row[1], row[2], row[3], row[4]))
    with open('csv_files/sales_file.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = []
        rows = []
        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        for row in rows:
            sale_records.append(Sale(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    with open('csv_files/giftcards_file.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = []
        rows = []
        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        for row in rows:
            giftCards.append(GiftCard(row[0], row[1], row[2]))


def setLightMode():
    default_palette = QPalette()


def setDarkMode():
    app.setStyle('Fusion')
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)


readData()

window = QWidget()  # Create a window.
product_buttons = []
sale_items = []
layout = QHBoxLayout()
exit_button = QPushButton("Exit")  # Define a button
exit_button.clicked.connect(exit)
layout.addWidget(exit_button)
def homeScreen():
    layout.addWidget(QLabel('Pin:'))  # Add a label
    pin = QLineEdit()
    Clock_in_button = QPushButton("Clock in/out")  # Define a button
    Clock_in_button.clicked.connect(homeScreen)
    Sign_in_button = QPushButton("Sign In")  # Define a button
    Sign_in_button.clicked.connect(orderScreen)
    layout.addWidget(pin)
    layout.addWidget(Sign_in_button)
    layout.addWidget(Clock_in_button)



def orderScreen():
    for products in product_list:
        product_buttons.append(QPushButton(products.name + "\n$" + products.price))
    for buttons in product_buttons:
        layout.addWidget(buttons)


homeScreen()
window.setLayout(layout)
window.show()  # Show window
app.exec_()  # Execute the App
