from guizero import App, Text, TextBox, PushButton, Window
import ipaddress
import re

def check_regex():
    reg = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/(?:[1-9]|1[0-9]|2[0-9]|3[0-2])$"
    if not ip_input_box.value:
        return
    x = re.match(reg, ip_input_box.value)
    if x == None:
        test_button.hide()
    else:
        test_button.show()
        ip_input_box.cancel(check_regex)

def show_next_window():
    window = Window(app, title="Wynik")
    Text(window, text=ip_input_box.value)

app = App(title="Liczenie adresów IP")
entry_text = Text(app, text="Podaj adres IP wraz z maską w formacie x.x.x.x/x")
ip_input_box = TextBox(app, width=20)
test_button = PushButton(app, command=show_next_window)
ip_input_box.repeat(1000, check_regex)
app.display()