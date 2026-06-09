import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_ECCCipher
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ECCCipher()
        self.ui.setupUi(self)

        # Debug: in ra các attribute của ui để biết tên nút/field thực tế
        print("UI attributes (sample):", [a for a in dir(self.ui) if not a.startswith('_') and (a.startswith('btn') or a.startswith('push') or a.startswith('txt') or a.startswith('line') or a.startswith('plain'))])

        # Kết nối các signal như trước (đã hoạt động)
        try:
            if hasattr(self.ui, 'btn_generate_keys'):
                self.ui.btn_generate_keys.clicked.connect(self.call_api_gen_keys)
            if hasattr(self.ui, 'btn_sign'):
                self.ui.btn_sign.clicked.connect(self.call_api_sign)
            if hasattr(self.ui, 'btn_verify'):
                self.ui.btn_verify.clicked.connect(self.call_api_verify)
        except Exception as e:
            print("Error connecting signals:", e)

    # Helpers an toàn để lấy/đặt text từ widget (hỗ trợ QTextEdit / QLineEdit)
    def _get_ui_text(self, name):
        if not hasattr(self.ui, name):
            return ''
        w = getattr(self.ui, name)
        if hasattr(w, 'toPlainText'):
            return w.toPlainText()
        if hasattr(w, 'text'):
            return w.text()
        return ''

    def _set_ui_text(self, name, value):
        if not hasattr(self.ui, name):
            return False
        w = getattr(self.ui, name)
        try:
            if hasattr(w, 'setPlainText'):
                w.setPlainText(value)
            elif hasattr(w, 'setText'):
                w.setText(value)
            else:
                return False
            return True
        except Exception as e:
            print(f"Failed to set text on {name}: {e}")
            return False

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)
            if response.status_code == 200:
                data = response.json()
                # Nếu API trả keys, hãy gán vào các field nếu có tên tương ứng
                if 'private_key' in data:
                    self._set_ui_text('txt_signature', data.get('private_key', ''))  # ví dụ: đổi tên nếu cần
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data.get("message", "Keys generated"))
                msg.exec_()
            else:
                # Hiện lỗi chi tiết để bạn kiểm tra server
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Error {response.status_code}")
                msg.setInformativeText(response.text)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Request exception:", e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Network error")
            msg.setInformativeText(str(e))
            msg.exec_()

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        message = self._get_ui_text('txt_information')  # tên đúng từ debug
        payload = {"message": message}
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)
            if response.status_code == 200:
                data = response.json()
                sig = data.get("signature", "")
                # đặt vào txt_signature (tên đúng)
                self._set_ui_text('txt_signature', sig)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Sign error {response.status_code}")
                msg.setInformativeText(response.text)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Request exception:", e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Network error")
            msg.setInformativeText(str(e))
            msg.exec_()

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        message = self._get_ui_text('txt_information')
        signature = self._get_ui_text('txt_signature')
        payload = {"message": message, "signature": signature}
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)
            if response.status_code == 200:
                data = response.json()
                ok = data.get("is_verified", False)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information if ok else QMessageBox.Warning)
                msg.setText("Verified Successfully" if ok else "Verified Fail")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Verify error {response.status_code}")
                msg.setInformativeText(response.text)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Request exception:", e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Network error")
            msg.setInformativeText(str(e))
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())