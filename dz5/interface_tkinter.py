
import tkinter as tk
from tkinter import messagebox

# проверка данных регистрации
def check_registration():
  nick = entry_nick.get()
  email = entry_email.get()
  password = entry_pass.get()

  if len(nick) < 3:
    messagebox.showerror("ошибка", "ник должен быть не короче 3 символов")
    return

  if "@" not in email or "." not in email:
    messagebox.showerror("ошибка", "проверь правильность почты")
    return

  if len(password) < 5:
    messagebox.showerror("ошибка", "пароль должен содержать минимум 5 символов")
    return

  messagebox.showinfo(
      "регистрация",
      f"привет, {nick}! регистрация прошла успешно.\n"
      "теперь можешь выбрать подписку на открытки.",
  )

  frame_reg.pack_forget()
  frame_sub.pack(expand=True)


# оформление подписки
def buy_subscription():
  card = entry_card.get()
  plan = sub_var.get()

  if len(card) != 16 or not card.isdigit():
    messagebox.showerror("ошибка оплаты", "номер карты должен состоять из 16 цифр")
    return

  messagebox.showinfo(
      "подписка оформлена",
      f"ты оформил подписку ОткрыткиПлюс ({plan})!\n"
      "теперь тебе доступны все открытки на сайте.",
  )


# создаем главное окно
window = tk.Tk()
window.title("подписка на ОткрыткиПлюс")
window.geometry("600x600")

frame_reg = tk.Frame(window)
frame_reg.pack(expand=True)

# форма регистрации
label_title = tk.Label(
    frame_reg, text="регистрация на ОткрыткиПлюс", font=("Arial", 16, "bold")
)
label_title.pack(pady=10)

# ввод никнейма
tk.Label(frame_reg, text="твой никнейм:").pack()
entry_nick = tk.Entry(frame_reg)
entry_nick.pack(pady=5)

# ввод почты
tk.Label(frame_reg, text="твоя почта:").pack()
entry_email = tk.Entry(frame_reg)
entry_email.pack(pady=5)

# ввод пароля
tk.Label(frame_reg, text="придумай пароль:").pack()
entry_pass = tk.Entry(frame_reg, show="*")
entry_pass.pack(pady=5)

# выбор пола
tk.Label(frame_reg, text="выбери пол:").pack(pady=5)
gender_var = tk.StringVar(value="женский")

tk.Radiobutton(
    frame_reg, text="женский", variable=gender_var, value="женский"
).pack()

tk.Radiobutton(
    frame_reg, text="мужской", variable=gender_var, value="мужской"
).pack()

# кнопка регистрации
btn_reg = tk.Button(
    frame_reg,
    text="зарегистрироваться",
    bg="lightblue",
    command=check_registration,
)
btn_reg.pack(pady=15)


# окно выбора подписки
frame_sub = tk.Frame(window)

tk.Label(
    frame_sub,
    text="выбери тариф ОткрыткиПлюс:",
    font=("Arial", 12, "bold"),
).pack(pady=5)

sub_var = tk.StringVar(value="1 месяц за 199 рублей")

tk.Radiobutton(
    frame_sub,
    text="на 1 месяц - 199 рублей",
    variable=sub_var,
    value="1 месяц за 199 рублей",
).pack()

tk.Radiobutton(
    frame_sub,
    text="на 3 месяца - 499 рублей",
    variable=sub_var,
    value="3 месяца за 499 рублей",
).pack()

tk.Radiobutton(
    frame_sub,
    text="на 1 год - 1499 рублей",
    variable=sub_var,
    value="1 год за 1499 рублей",
).pack()

# поле для номера карты
tk.Label(frame_sub, text="введи номер карты (учебный пример):").pack(pady=10)
entry_card = tk.Entry(frame_sub)
entry_card.pack(pady=5)

# кнопка оформления подписки
btn_buy = tk.Button(
    frame_sub,
    text="оформить подписку",
    bg="lightgreen",
    command=buy_subscription,
)
btn_buy.pack(pady=15)

# запуск программы
window.mainloop()
