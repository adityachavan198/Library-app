from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 592)
        MainWindow.setStyleSheet("background-color: rgb(240, 255, 248);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.box = QtWidgets.QStackedWidget(self.centralwidget)
        self.box.setGeometry(QtCore.QRect(70, 20, 751, 501))
        self.box.setWhatsThis("")
        self.box.setAccessibleName("")
        self.box.setAutoFillBackground(False)
        self.box.setStyleSheet("border-color: rgb(255, 35, 64);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.box.setObjectName("box")
        self.page1_login = QtWidgets.QWidget()
        self.page1_login.setObjectName("page1_login")
        self.membershipno_login = QtWidgets.QLineEdit(self.page1_login)
        self.membershipno_login.setGeometry(QtCore.QRect(280, 70, 231, 20))
        self.membershipno_login.setObjectName("membershipno_login")
        self.label = QtWidgets.QLabel(self.page1_login)
        self.label.setGeometry(QtCore.QRect(280, 40, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page1_login)
        self.label_2.setGeometry(QtCore.QRect(280, 110, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.password_login = QtWidgets.QLineEdit(self.page1_login)
        self.password_login.setGeometry(QtCore.QRect(280, 140, 231, 20))
        self.password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_login.setObjectName("password_login")
        self.login_pushButton = QtWidgets.QPushButton(self.page1_login)
        self.login_pushButton.setGeometry(QtCore.QRect(280, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setObjectName("login_pushButton")
        self.register_pushButton = QtWidgets.QPushButton(self.page1_login)
        self.register_pushButton.setGeometry(QtCore.QRect(420, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.register_pushButton.setFont(font)
        self.register_pushButton.setObjectName("register_pushButton")
        self.box.addWidget(self.page1_login)
        self.page_2_register = QtWidgets.QWidget()
        self.page_2_register.setObjectName("page_2_register")
        self.name_input_regi = QtWidgets.QLineEdit(self.page_2_register)
        self.name_input_regi.setGeometry(QtCore.QRect(260, 60, 251, 20))
        self.name_input_regi.setObjectName("name_input_regi")
        self.label_3 = QtWidgets.QLabel(self.page_2_register)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dob_input_regi = QtWidgets.QDateEdit(self.page_2_register)
        self.dob_input_regi.setGeometry(QtCore.QRect(260, 120, 251, 22))
        self.dob_input_regi.setObjectName("dob_input_regi")
        self.label_4 = QtWidgets.QLabel(self.page_2_register)
        self.label_4.setGeometry(QtCore.QRect(260, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2_register)
        self.label_5.setGeometry(QtCore.QRect(260, 140, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.password_regi = QtWidgets.QLineEdit(self.page_2_register)
        self.password_regi.setGeometry(QtCore.QRect(260, 170, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.password_regi.setFont(font)
        self.password_regi.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_regi.setObjectName("password_regi")
        self.label_6 = QtWidgets.QLabel(self.page_2_register)
        self.label_6.setGeometry(QtCore.QRect(260, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2_register)
        self.label_7.setGeometry(QtCore.QRect(260, 260, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.email_regi = QtWidgets.QLineEdit(self.page_2_register)
        self.email_regi.setGeometry(QtCore.QRect(260, 300, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.email_regi.setFont(font)
        self.email_regi.setObjectName("email_regi")
        self.label_8 = QtWidgets.QLabel(self.page_2_register)
        self.label_8.setGeometry(QtCore.QRect(260, 330, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.phone_regi = QtWidgets.QLineEdit(self.page_2_register)
        self.phone_regi.setGeometry(QtCore.QRect(260, 360, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.phone_regi.setFont(font)
        self.phone_regi.setObjectName("phone_regi")
        self.submit_regi = QtWidgets.QPushButton(self.page_2_register)
        self.submit_regi.setGeometry(QtCore.QRect(260, 410, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.submit_regi.setFont(font)
        self.submit_regi.setObjectName("submit_regi")
        self.pushbutton_regi_back = QtWidgets.QPushButton(self.page_2_register)
        self.pushbutton_regi_back.setGeometry(QtCore.QRect(420, 410, 81, 23))
        self.pushbutton_regi_back.setObjectName("pushbutton_regi_back")
        self.gender_input_regi = QtWidgets.QComboBox(self.page_2_register)
        self.gender_input_regi.setGeometry(QtCore.QRect(260, 230, 251, 22))
        self.gender_input_regi.setObjectName("gender_input_regi")
        self.label_5.raise_()
        self.name_input_regi.raise_()
        self.label_3.raise_()
        self.dob_input_regi.raise_()
        self.label_4.raise_()
        self.password_regi.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.email_regi.raise_()
        self.label_8.raise_()
        self.phone_regi.raise_()
        self.submit_regi.raise_()
        self.pushbutton_regi_back.raise_()
        self.gender_input_regi.raise_()
        self.box.addWidget(self.page_2_register)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.book1_diplay_browse = QtWidgets.QLabel(self.page_3)
        self.book1_diplay_browse.setGeometry(QtCore.QRect(80, 60, 561, 20))
        self.book1_diplay_browse.setText("")
        self.book1_diplay_browse.setObjectName("book1_diplay_browse")
        self.book1_issue_pushButton = QtWidgets.QPushButton(self.page_3)
        self.book1_issue_pushButton.setGeometry(QtCore.QRect(660, 60, 75, 23))
        self.book1_issue_pushButton.setObjectName("book1_issue_pushButton")
        self.book2_diplay_browse = QtWidgets.QLabel(self.page_3)
        self.book2_diplay_browse.setGeometry(QtCore.QRect(80, 130, 561, 16))
        self.book2_diplay_browse.setText("")
        self.book2_diplay_browse.setObjectName("book2_diplay_browse")
        self.book2_issue_pushButton = QtWidgets.QPushButton(self.page_3)
        self.book2_issue_pushButton.setGeometry(QtCore.QRect(660, 120, 75, 23))
        self.book2_issue_pushButton.setObjectName("book2_issue_pushButton")
        self.book3_diplay_browse = QtWidgets.QLabel(self.page_3)
        self.book3_diplay_browse.setGeometry(QtCore.QRect(70, 190, 571, 20))
        self.book3_diplay_browse.setText("")
        self.book3_diplay_browse.setObjectName("book3_diplay_browse")
        self.book4_diplay_browse = QtWidgets.QLabel(self.page_3)
        self.book4_diplay_browse.setGeometry(QtCore.QRect(70, 250, 571, 16))
        self.book4_diplay_browse.setText("")
        self.book4_diplay_browse.setObjectName("book4_diplay_browse")
        self.book5_diplay_browse = QtWidgets.QLabel(self.page_3)
        self.book5_diplay_browse.setGeometry(QtCore.QRect(76, 310, 561, 20))
        self.book5_diplay_browse.setText("")
        self.book5_diplay_browse.setObjectName("book5_diplay_browse")
        self.book3_issue_pushButton = QtWidgets.QPushButton(self.page_3)
        self.book3_issue_pushButton.setGeometry(QtCore.QRect(660, 180, 75, 23))
        self.book3_issue_pushButton.setObjectName("book3_issue_pushButton")
        self.book4_issue_pushButton = QtWidgets.QPushButton(self.page_3)
        self.book4_issue_pushButton.setGeometry(QtCore.QRect(660, 240, 75, 23))
        self.book4_issue_pushButton.setObjectName("book4_issue_pushButton")
        self.book5_issue_pushButton = QtWidgets.QPushButton(self.page_3)
        self.book5_issue_pushButton.setGeometry(QtCore.QRect(660, 300, 75, 23))
        self.book5_issue_pushButton.setObjectName("book5_issue_pushButton")
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setGeometry(QtCore.QRect(140, 450, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.search_book_input = QtWidgets.QLineEdit(self.page_3)
        self.search_book_input.setGeometry(QtCore.QRect(150, 390, 431, 20))
        self.search_book_input.setObjectName("search_book_input")
        self.browse_search_pushButton = QtWidgets.QPushButton(self.page_3)
        self.browse_search_pushButton.setGeometry(QtCore.QRect(650, 390, 75, 23))
        self.browse_search_pushButton.setObjectName("browse_search_pushButton")
        self.box.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.Registration_sucessfull = QtWidgets.QLabel(self.page_4)
        self.Registration_sucessfull.setGeometry(QtCore.QRect(60, 20, 531, 441))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Registration_sucessfull.setFont(font)
        self.Registration_sucessfull.setObjectName("Registration_sucessfull")
        self.back_pushButton = QtWidgets.QPushButton(self.page_4)
        self.back_pushButton.setGeometry(QtCore.QRect(70, 470, 131, 23))
        self.back_pushButton.setObjectName("back_pushButton")
        self.box.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(110, 40, 121, 31))
        self.label_9.setObjectName("label_9")
        self.Book1_label = QtWidgets.QLabel(self.page)
        self.Book1_label.setGeometry(QtCore.QRect(110, 130, 451, 16))
        self.Book1_label.setObjectName("Book1_label")
        self.Book2_label = QtWidgets.QLabel(self.page)
        self.Book2_label.setGeometry(QtCore.QRect(110, 180, 451, 16))
        self.Book2_label.setObjectName("Book2_label")
        self.Book3_label = QtWidgets.QLabel(self.page)
        self.Book3_label.setGeometry(QtCore.QRect(110, 230, 451, 16))
        self.Book3_label.setObjectName("Book3_label")
        self.Book1_return_pushButton = QtWidgets.QPushButton(self.page)
        self.Book1_return_pushButton.setGeometry(QtCore.QRect(610, 120, 111, 23))
        self.Book1_return_pushButton.setObjectName("Book1_return_pushButton")
        self.Book2_return_pushButton = QtWidgets.QPushButton(self.page)
        self.Book2_return_pushButton.setGeometry(QtCore.QRect(610, 170, 111, 23))
        self.Book2_return_pushButton.setObjectName("Book2_return_pushButton")
        self.Book3_return_pushButton = QtWidgets.QPushButton(self.page)
        self.Book3_return_pushButton.setGeometry(QtCore.QRect(610, 220, 111, 23))
        self.Book3_return_pushButton.setObjectName("Book3_return_pushButton")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(110, 310, 141, 16))
        self.label_10.setObjectName("label_10")
        self.Book_name_search = QtWidgets.QLineEdit(self.page)
        self.Book_name_search.setGeometry(QtCore.QRect(130, 370, 411, 20))
        self.Book_name_search.setObjectName("Book_name_search")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(130, 340, 231, 16))
        self.label_11.setObjectName("label_11")
        self.Book_search_pushButton = QtWidgets.QPushButton(self.page)
        self.Book_search_pushButton.setGeometry(QtCore.QRect(620, 370, 111, 23))
        self.Book_search_pushButton.setObjectName("Book_search_pushButton")
        self.Book_found_label = QtWidgets.QLabel(self.page)
        self.Book_found_label.setGeometry(QtCore.QRect(130, 440, 411, 16))
        self.Book_found_label.setObjectName("Book_found_label")
        self.Issue_book_pushButton = QtWidgets.QPushButton(self.page)
        self.Issue_book_pushButton.setGeometry(QtCore.QRect(620, 440, 111, 23))
        self.Issue_book_pushButton.setObjectName("Issue_book_pushButton")
        self.browse_pushbutton = QtWidgets.QPushButton(self.page)
        self.browse_pushbutton.setGeometry(QtCore.QRect(630, 300, 75, 23))
        self.browse_pushbutton.setObjectName("browse_pushbutton")
        self.box.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.label)

        self.retranslateUi(MainWindow)
        self.box.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bookstore"))
        self.membershipno_login.setPlaceholderText(_translate("MainWindow", "Enter your Membership No."))
        self.label.setText(_translate("MainWindow", "Membership No. :"))
        self.label_2.setText(_translate("MainWindow", "Password : "))
        self.password_login.setPlaceholderText(_translate("MainWindow", "Enter your Password"))
        self.login_pushButton.setText(_translate("MainWindow", "Login"))
        self.register_pushButton.setText(_translate("MainWindow", "Register"))
        self.name_input_regi.setPlaceholderText(_translate("MainWindow", "Enter Your Full Name Here"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Birthday"))
        self.label_5.setText(_translate("MainWindow", "Create a password "))
        self.password_regi.setPlaceholderText(_translate("MainWindow", "Enter password"))
        self.label_6.setText(_translate("MainWindow", "Gender"))
        self.label_7.setText(_translate("MainWindow", "Email Address "))
        self.email_regi.setPlaceholderText(_translate("MainWindow", "Enter Your Email Address"))
        self.label_8.setText(_translate("MainWindow", "Mobile Phone"))
        self.phone_regi.setPlaceholderText(_translate("MainWindow", "Enter YourMobile Phone Number"))
        self.submit_regi.setText(_translate("MainWindow", "Submit"))
        self.pushbutton_regi_back.setText(_translate("MainWindow", "Back"))
        self.book1_issue_pushButton.setText(_translate("MainWindow", "Issue"))
        self.book2_issue_pushButton.setText(_translate("MainWindow", "Issue"))
        self.book3_issue_pushButton.setText(_translate("MainWindow", "Issue"))
        self.book4_issue_pushButton.setText(_translate("MainWindow", "Issue"))
        self.book5_issue_pushButton.setText(_translate("MainWindow", "Issue"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.search_book_input.setPlaceholderText(_translate("MainWindow", "Enter name of the book"))
        self.browse_search_pushButton.setText(_translate("MainWindow", "Search"))
        self.Registration_sucessfull.setText(_translate("MainWindow", "sucessfully registered"))
        self.back_pushButton.setText(_translate("MainWindow", "Back"))
        self.label_9.setText(_translate("MainWindow", "Books Taken"))
        self.Book1_label.setText(_translate("MainWindow", "Book1"))
        self.Book2_label.setText(_translate("MainWindow", "Book2"))
        self.Book3_label.setText(_translate("MainWindow", "Book3"))
        self.Book1_return_pushButton.setText(_translate("MainWindow", "Return"))
        self.Book2_return_pushButton.setText(_translate("MainWindow", "Return"))
        self.Book3_return_pushButton.setText(_translate("MainWindow", "Return"))
        self.label_10.setText(_translate("MainWindow", "Book Search"))
        self.Book_name_search.setPlaceholderText(_translate("MainWindow", "Enter the Name of the Book to be Searched"))
        self.label_11.setText(_translate("MainWindow", "Name of the Book"))
        self.Book_search_pushButton.setText(_translate("MainWindow", "Search"))
        self.Book_found_label.setText(_translate("MainWindow", "Book Found"))
        self.Issue_book_pushButton.setText(_translate("MainWindow", "Issue"))
        self.browse_pushbutton.setText(_translate("MainWindow", "Browse"))
