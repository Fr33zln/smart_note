from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,
                             QTextEdit,QListWidget,QLineEdit,QInputDialog,QMessageBox)
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.setFixedSize(900,650)
window.setWindowTitle("Smartnote")

create_note = QPushButton("Створити нотатку")
save_note = QPushButton("Зберігти нотатку")
delete_note = QPushButton("Видалити нотатку")
create_tag = QPushButton("Додати до тегу")
delete_tag = QPushButton("Вилучити з тегу")
search_tag = QPushButton("Шукати тег")
label_note = QLabel("Створити замітки")
label_tag  = QLabel("Створити теги")
note_list_widget = QListWidget()
tag_list_widget = QListWidget()
searching_tag_input = QLineEdit()
text_edit = QTextEdit()
text_edit.setDisabled(True)

layout1 = QHBoxLayout()
layout1.addWidget(create_note)
layout1.addWidget(save_note)

layout2 = QHBoxLayout()
layout2.addWidget(create_tag)
layout2.addWidget(delete_tag)


panel_layout = QVBoxLayout()
panel_layout.addWidget(label_note)
panel_layout.addWidget(note_list_widget)
panel_layout.addLayout(layout1)
panel_layout.addWidget(delete_note)
panel_layout.addWidget(label_tag)
panel_layout.addWidget(tag_list_widget)
panel_layout.addLayout(layout2)
panel_layout.addWidget(searching_tag_input)
panel_layout.addWidget(text_edit)

main_layout= QHBoxLayout()
main_layout.addWidget(text_edit)
main_layout.addLayout(panel_layout)



window.setLayout(main_layout)
window.show()



#скачати з першого сайту get.pip
#далі там буде боотстрап і зберегти його в програму
#python get-pip.py написати в терміналі вс коду

