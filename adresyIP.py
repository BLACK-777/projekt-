from guizero import App, Text, TextBox, PushButton, Window
import ipaddress
import re

# część zabezpieczająca przed podaniem złego adresu ip lub podania go w zlym formacie
def is_proper_input(typed_value):
    reg = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/(?:[1-9]|1[0-9]|2[0-9]|3[0-2])$"  #szablon adresu ip
    if re.match(reg, typed_value):      # funkcja pozwalajaca na korzystanie z zabezpieczenia wiecej niz jeden raz
        try:
            ipaddress.IPv4Network(ip_input_box.value) # przy podaniu poprawnego adresu ip zostaje on przejety przez funkcje python 'ipaddress'
        except ValueError:
            return False
        else:
            return True

# okienko pokazujące wykonane obliczenia
def show_next_window():
    window = Window(app, title="Wynik")
    network = ipaddress.IPv4Network(ip_input_box.value)
    network_net_text = "Adres sieci: " + str(network.network_address)
    network_text = Text(window, network_net_text)
    network_broad_text = "Adres broadcast: " + str(network.broadcast_address)
    network_broad = Text(window, network_broad_text)
    network_us = Text(window, text = "Użytkowe adresy znajdują sie między adresem ip a adresem broadcast")
    network_mask_text = "Maska sieci: " + str(network.netmask)
    network_mask = Text(window, network_mask_text)
    network_host_text = "Maksymalna liczba hostów: " + str(network.num_addresses)
    network_host = Text(window, network_host_text)
    network_bit_text = "Długość prefixu sieci w bitach:" + str(network.prefixlen)
    network_bit = Text(window, network_bit_text)
    def close_window():    #funkcja pozwalajaca na zamkniecie okienka wynikow bez koniecznosci zamykania calego prgramu
        window.hide()
    close = PushButton(window, text="Zamknij", command = close_window)


def show_element(element):
    element.show()


def verify_proper_ip_address_and_mask_were_passed():
    if is_proper_input(ip_input_box.value):
        test_button.show()
        error_text.hide()                                                                        # funkcja pokazujaca i
    else:                                                                                        # ukrywajaca przycisk
        error_text.value = f'Błędnie wpisana sieć/maska - obliczenie nie możliwe'                # chroniąca przed próbą
        error_text.show()                                                                        # obliczen przy zlym
        test_button.hide()                                                                       # formacie adresu

# główna część aplikacji pozwalająca na wpisanie adresu ip
app = App(title="Liczenie adresów IP")
entry_text = Text(app, text="Podaj adres IP wraz z maską w formacie x.x.x.x/x")
example_text = Text(app, text="Przykład: 192.161.1.0/25")
ip_input_box = TextBox(app, width=20)
ip_input_box.update_command(verify_proper_ip_address_and_mask_were_passed)
test_button = PushButton(text='Oblicz', master=app, command=show_next_window)
error_text = Text(app, text='Zacznij pisać...', color='red')
test_button.hide()
app.display()


