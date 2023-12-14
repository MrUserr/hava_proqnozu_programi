import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import requests

class HavaProqnozuProgramı(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hava Proqnozu Programı')

        self.label_sehir = QLabel('Şəhər:')
        self.entry_sehir = QLineEdit()
        self.button_getir = QPushButton('Hava Məlumatlarını Gətir')
        self.label_sonuc = QLabel('')

        self.button_getir.clicked.connect(self.hava_durumu_getir)

        layout = QVBoxLayout()
        layout.addWidget(self.label_sehir)
        layout.addWidget(self.entry_sehir)
        layout.addWidget(self.button_getir)
        layout.addWidget(self.label_sonuc)

        self.setLayout(layout)

    def hava_durumu_getir(self):
        sehir = self.entry_sehir.text()
        if sehir:
            try:
                api_key = "Your_APİ"  # OpenWeatherMap açarını buraya əlavə edin
                api_url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric"

                response = requests.get(api_url)
                response.raise_for_status()

                weather_data = response.json()

                istilik = weather_data['main']['temp']
                hava = weather_data['weather'][0]['description']

                self.label_sonuc.setText(f"{sehir} - İstilik: {istilik}°C, Hava: {hava}")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, 'Xəta', f'Hava məlumatı alarkən bir xəta oldu: {str(e)}')
        else:
            QMessageBox.warning(self, 'Xəta', 'Xahiş edirik bir şəhər adı girin.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uygulama = HavaProqnozuProgramı()
    uygulama.show()
    sys.exit(app.exec_())
