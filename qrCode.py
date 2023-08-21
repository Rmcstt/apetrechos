import pyqrcode

# Informações do Wi-Fi
SSID = input("Digite o SSID da sua rede Wi-Fi: ")
PASS = input("Digite a senha da sua rede Wi-Fi: ")

# Monta o código Wi-Fi no formato adequado
wifi_data = f"WIFI:T:WPA;S:{SSID};P:{PASS};;"

# Cria o código QR
qr_code = pyqrcode.create(wifi_data)

# Salva o código QR como imagem PNG
qr_code.png("wifi_qrcode.png", scale=8)

print("Código QR do Wi-Fi gerado com sucesso!")
