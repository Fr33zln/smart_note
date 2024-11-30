from interface import *
from create_json import *

name_file = "data.json"


#обробка винятка
try:
    data = read_json(name_file)
except:
    data = dict()


def error(txt):
    ms =QMessageBox()
    ms.setText(txt)
    ms.exec_()

def show_note():
    note_list_widget.addItems(list(data.keys()))


def add_note():
    name_note = QInputDialog().getText(QInputDialog(), "Назва нотатка", " Введіть назву нотатка")[0]
    data[name_note] = {"TEXT": "", "TAG": []}
    write_json(name_file, data)
    note_list_widget.addItem(name_note)

def save_file():
    try:
        name_note = note_list_widget.currentItem().text()
        data[name_note]["TEXT"] = text_edit.toPlainText()
        write_json(name_file, data)
    except:
        error("Щоб зберегти, спочатку виберіть нотаток")

def show_text():
    name_note = note_list_widget.currentItem().text()
    text_edit.setPlainText(data[name_note]["TEXT"])

create_note.clicked.connect(add_note)
create_note.clicked.connect(save_file)
note_list_widget.clicked.connect(show_text)





show_note()
app.exec_()