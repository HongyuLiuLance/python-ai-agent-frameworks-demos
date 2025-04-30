import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLabel
)
from PyQt5.QtCore import Qt


class Main_App:
    def __init__(self):

        self.url_submit_callback = None  # Callback function for after user submits

        # setting the window
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle('Cooking Agent')
        self.window.resize(900, 600)
        

        # creating the tool boxes
        # basic layouts
        self.v_base = QVBoxLayout()
        self.h_url_input = QHBoxLayout()
        self.h_output = QHBoxLayout()
        self.v_ingredient = QVBoxLayout()
        self.v_recipe = QVBoxLayout()

        # widgets for url input
        self.txt_url_input = QTextEdit()
        self.btn_url_submit = QPushButton()

        self.txt_url_input.setPlaceholderText("Type your url here...")
        self.txt_url_input.setFixedSize(700, 50)
        self.btn_url_submit.setText("Submit")
        self.btn_url_submit.setFixedHeight(50)
        self.btn_url_submit.clicked.connect(self.on_submit_clicked)

        self.setattr_ingredient()
        
        self.setattr_recipe()

        self.set_layout_structure()


        

        self.window.setLayout(self.v_base)

    def set_layout_structure(self):
        self.v_base.addLayout(self.h_url_input)
        self.v_base.addLayout(self.h_output)
        self.h_output.addLayout(self.v_ingredient)
        self.h_output.addLayout(self.v_recipe)
        
        self.h_url_input.addWidget(self.txt_url_input)
        self.h_url_input.addWidget(self.btn_url_submit)
        self.v_ingredient.addWidget(self.lbl_ingredient)
        self.v_ingredient.addWidget(self.lstview_ingredient)
        self.v_recipe.addWidget(self.lbl_recipe)
        self.v_recipe.addWidget(self.lstview_recipe)


    def execute(self):
        self.window.show()
        self.app.exec_()


    def on_submit_clicked(self) -> str: 
        self.user_url = self.txt_url_input.toPlainText()
        print(self.user_url)
        if self.url_submit_callback:
            self.url_submit_callback(self.user_url)  # Call external logic here

    def on_url_submit(self, callback):
        self.url_submit_callback = callback
    

    def setattr_ingredient(self):
        # widgets for ingredient part
        self.lbl_ingredient = QLabel("Ingredients")

        # Create scroll area and content widget
        self.lstview_ingredient = QScrollArea()
        self.lstview_ingredient.setWidgetResizable(True)

        # Create a container widget to hold the layout
        self.lst_content_ingredient = QWidget()
        self.lst_layout_ingredient = QVBoxLayout(self.lst_content_ingredient)

        # Set the container widget into the scroll area
        self.lstview_ingredient.setWidget(self.lst_content_ingredient)

    def setattr_recipe(self):
        # widgets for recipe part
        self.lbl_recipe = QLabel("Cooking Steps")
        self.lstview_recipe = QScrollArea()
        self.lstview_recipe.setWidgetResizable(True)

        self.lst_content_recipe = QWidget()
        self.lst_layout_recipt = QVBoxLayout(self.lst_content_recipe)

        self.lstview_recipe.setWidget(self.lst_content_recipe)


    
    def add_ingredient(self, ingredient): 
        tmp_ingredient = QLabel(ingredient)
        tmp_ingredient.setAlignment(Qt.AlignLeft)
        self.lst_layout_ingredient.insertWidget(-1, tmp_ingredient)  # insert at top

    def add_steps(self, step):
        tmp_step = QLabel(step)
        tmp_step.setAlignment(Qt.AlignLeft)
        self.lst_layout_recipt.insertWidget(-1, tmp_step)


