from guizero import App, Text, TextBox, PushButton, Window
import ipaddress
import re

# część zabezpieczająca przed podaniem złego adresu ip lub podania go w zlym formacie
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
# okienko pokazujące wykonane obliczenia
def show_next_window():
    window = Window(app, title="Wynik")
    network = ipaddress.IPv4Network(ip_input_box.value)
    network_net_text = "Adres sieci: " + str(network.network_address)
    network_text = Text(window, network_net_text)
    network_broad_text = "Adres broadcast: " + str(network.broadcast_address)
    network_broad = Text(window, network_broad_text)
    network_mask_text = "Maska sieci: " + str(network.netmask)
    network_mask = Text(window, network_mask_text)
    network_host_text = "Maksymalna liczba hostów: " + str(network.num_addresses)
    network_host = Text(window, network_host_text)
    network_bit_text = "Długość prefixu sieci w bitach:" + str(network.prefixlen)
    network_bit = Text(window, network_bit_text)
    def close_window():
        window.hide()
    close = PushButton(window, text="Zamknij", command = close_window)



# główna część aplikacji pozwalająca na wpisanie adresu ip
app = App(title="Liczenie adresów IP")
entry_text = Text(app, text="Podaj adres IP wraz z maską w formacie x.x.x.x/x")
example_text = Text(app, text="Przykład: 192.161.1.0/25")
ip_input_box = TextBox(app, width=20)
test_button = PushButton(app, command=show_next_window)
ip_input_box.repeat(1000, check_regex)
app.display()



