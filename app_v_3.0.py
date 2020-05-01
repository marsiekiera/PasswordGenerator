import string
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QCheckBox


class PasswordGenerator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):

        # Labels
        label_char = QLabel("Enter length of generated password:", self)
        label_uppercase = QLabel("Is the password should consist of Upper Case (A, B, C, ...)", self)
        label_lowercase = QLabel("Is the password should consist of Lower Case (a, b, c, ...)", self)
        label_digits = QLabel("Is the password should consist of Digits (1, 2, 3, ...)", self)
        label_interlude = QLabel("Is the password should consist of Minus and Under Line(-, _)", self)
        label_special = QLabel("""Is the password should consist of Special (!, $, %, &, ", ... )""", self)
        label_brackets = QLabel("Is the password should consist of Brackets ([, ], {, }, (, ), <, >)", self)
        label_password = QLabel("Your password is:", self)

        # Labels to tab
        TabLayout = QGridLayout()
        TabLayout.addWidget(label_char, 0, 0)
        TabLayout.addWidget(label_uppercase, 1, 0)
        TabLayout.addWidget(label_lowercase, 2, 0)
        TabLayout.addWidget(label_digits, 3, 0)
        TabLayout.addWidget(label_interlude, 4, 0)
        TabLayout.addWidget(label_special, 5, 0)
        TabLayout.addWidget(label_brackets, 6, 0)
        TabLayout.addWidget(label_password, 8, 0)

        # Checkboxes

        self.charEdt = QLineEdit()
        self.uppercaseEdt = QCheckBox()
        self.lowercaseEdt = QCheckBox()
        self.digitsEdt = QCheckBox()
        self.interludeEdt = QCheckBox()
        self.specialEdt = QCheckBox()
        self.bracketsEdt = QCheckBox()
        self.passwordEdt = QLineEdit()

        self.charEdt.setText("32")
        self.uppercaseEdt.setChecked(True)
        self.lowercaseEdt.setChecked(True)
        self.digitsEdt.setChecked(True)
        self.interludeEdt.setChecked(True)
        self.specialEdt.setChecked(True)
        self.bracketsEdt.setChecked(True)

        self.passwordEdt.readonly = True

        TabLayout.addWidget(self.charEdt, 0, 1)
        TabLayout.addWidget(self.uppercaseEdt, 1, 1)
        TabLayout.addWidget(self.lowercaseEdt, 2, 1)
        TabLayout.addWidget(self.digitsEdt, 3, 1)
        TabLayout.addWidget(self.interludeEdt, 4, 1)
        TabLayout.addWidget(self.specialEdt, 5, 1)
        TabLayout.addWidget(self.bracketsEdt, 6, 1)
        TabLayout.addWidget(self.passwordEdt, 9, 0)

        # Generate password button

        generatepasswordbutton = QPushButton("&Generate password", self)
        ButLayout = QHBoxLayout()
        ButLayout.addWidget(generatepasswordbutton)

        TabLayout.addLayout(ButLayout, 7, 0)

        # Added to window

        self.setLayout(TabLayout)

        generatepasswordbutton.clicked.connect(self.main_function)

        self.charEdt.setFocus()
        self.setGeometry(500, 500, 50, 50)
        self.setWindowTitle("Password generator")
        self.show()

    def main_function(self):

        # List of characters
        uppercase_list = list(string.ascii_uppercase)
        lowercase_list = list(string.ascii_lowercase)
        digits_list = list(string.digits)
        interlude_list = ["-", "_"]
        special_list = ['!', '"', '#', '$', '%', '&', "'", '*', '+', ',', '.', '/',
                        ':', ';', '=', '?', '@', '^', '`', '|']
        brackets_list = ["[", "]", "{", "}", "(", ")", "<", ">"]

        user_char = int(self.charEdt.text())

        # main function
        char_list = []
        if self.uppercaseEdt.isChecked() == True:
            char_list = char_list + uppercase_list
        if self.lowercaseEdt.isChecked() == True:
            char_list = char_list + lowercase_list
        if self.digitsEdt.isChecked() == True:
            char_list = char_list + digits_list
        if self.interludeEdt.isChecked() == True:
            char_list = char_list + interlude_list
        if self.specialEdt.isChecked() == True:
            char_list = char_list + special_list
        if self.bracketsEdt.isChecked() == True:
            char_list = char_list + brackets_list

        password = ""
        i = 0
        while i < user_char:
            password = password + random.choice(char_list)
            i += 1

        self.passwordEdt.setText(str(password))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec_())