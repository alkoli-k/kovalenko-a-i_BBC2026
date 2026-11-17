
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

# проверка регистрации
def check_registration():
  nick = entry_nick.text()
  email = entry_email.text()
  password = entry_pass.text()

  if len(nick) < 3:
    QMessageBox.warning(window, "ошибка", "никнейм слишком короткий")
    return

  if "@" not in email or "." not in email:
    QMessageBox.warning(window, "ошибка", "введи почту правильно")
    return

  if len(password) < 5:
    QMessageBox.warning(window, "ошибка", "пароль слишком короткий")
    return

  QMessageBox.information(
      window,
      "регистрация завершена",
      f"привет, {nick}! ты успешно зарегистрировался.\nтеперь выбери тариф"
      " подписки на открытки!",
  )

  frame_reg.hide()
  frame_sub.show()


# проверка карты и покупка
def buy_subscription():
  card = entry_card.text()
  if radio_1m.isChecked():
    plan = "1 месяц за 199 рублей"
  elif radio_3m.isChecked():
    plan = "3 месяца за 499 рублей"
  else:
    plan = "1 год за 1499 рублей"

  if len(card) != 16 or not card.isdigit():
    QMessageBox.warning(window, "ошибка оплаты", "неверный номер карты")
    return

  QMessageBox.information(
      window,
      "поздравляем!",
      f"ты успешно оформил подписку на ОткрыткиПлюс ({plan})!\n"
      "теперь тебе доступны все открытки нашего сайта!",
  )


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Подписка на ОткрыткиПлюс")
window.resize(700, 700)  # ширина 700, высота 700

window.setStyleSheet("""
    QWidget {
        background-color: #f4f6f9;
        font-family: 'Segoe UI', Arial;
        font-size: 14px;
        color: #2c3e50;
    }
    QLabel#title {
        font-size: 20px;
        font-weight: bold;
        color: #1a252f;
    }
    QLineEdit {
        background-color: white;
        border: 2px solid #dcdfe6;
        border-radius: 8px;
        padding: 8px;
        font-size: 14px;
    }
    QLineEdit:focus {
        border: 2px solid #4a90e2;
    }
    QPushButton {
        background-color: #4a90e2;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        font-size: 15px;
    }
    QPushButton:hover {
        background-color: #357abd;
    }
    QPushButton#buy_btn {
        background-color: #2ecc71;
    }
    QPushButton#buy_btn:hover {
        background-color: #27ae60;
    }
""")

main_layout = QVBoxLayout(window)
main_layout.setAlignment(Qt.AlignCenter)

frame_reg = QWidget()
layout_reg = QVBoxLayout(frame_reg)
layout_reg.setSpacing(10)

label_title = QLabel("регистрация на сайте ОткрыткиПлюс")
label_title.setObjectName("title")
label_title.setAlignment(Qt.AlignCenter)
layout_reg.addWidget(label_title)

entry_nick = QLineEdit()
entry_nick.setPlaceholderText("твой никнейм")
layout_reg.addWidget(entry_nick)

entry_email = QLineEdit()
entry_email.setPlaceholderText("твоя почта")
layout_reg.addWidget(entry_email)

entry_pass = QLineEdit()
entry_pass.setPlaceholderText("придумай пароль")
entry_pass.setEchoMode(QLineEdit.Password)
layout_reg.addWidget(entry_pass)

label_gender = QLabel("выбери пол:")
layout_reg.addWidget(label_gender)

radio_female = QRadioButton("женский")
radio_female.setChecked(True)
layout_reg.addWidget(radio_female)

radio_male = QRadioButton("мужской")
layout_reg.addWidget(radio_male)

btn_reg = QPushButton("зарегистрироваться")
btn_reg.clicked.connect(check_registration)
layout_reg.addWidget(btn_reg)

main_layout.addWidget(frame_reg)

frame_sub = QWidget()
layout_sub = QVBoxLayout(frame_sub)
layout_sub.setSpacing(12)

label_sub = QLabel("выбери тариф ОткрыткиПлюс\nдля доступа ко всем открыткам:")
label_sub.setObjectName("title")
label_sub.setAlignment(Qt.AlignCenter)
layout_sub.addWidget(label_sub)

radio_1m = QRadioButton("на 1 месяц — 199 рублей")
radio_1m.setChecked(True)
layout_sub.addWidget(radio_1m)

radio_3m = QRadioButton("на 3 месяца — 499 рублей")
layout_sub.addWidget(radio_3m)

radio_1y = QRadioButton("на 1 год — 1499 рублей")
layout_sub.addWidget(radio_1y)

entry_card = QLineEdit()
entry_card.setPlaceholderText("номер карты (16 цифр, учебный пример)")
layout_sub.addWidget(entry_card)

btn_buy = QPushButton("оформить подписку")
btn_buy.setObjectName("buy_btn")
btn_buy.clicked.connect(buy_subscription)
layout_sub.addWidget(btn_buy)

main_layout.addWidget(frame_sub)
frame_sub.hide()

window.show()
sys.exit(app.exec_())
