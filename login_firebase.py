import pyrebase


class Accont:
    def __init__(self):
        firebaseConfig = {
            "apiKey": "AIzaSyDvV5WFb22D2AatpHV-Vq8q_OhvqDwfRHo",
            "authDomain": "londonapp-27c49.firebaseapp.com",
            "projectId": "londonapp-27c49",
            "databaseURL": "https://londonapp-27c49-default-rtdb.firebaseio.com",
            "storageBucket": "londonapp-27c49.appspot.com",
            "messagingSenderId": "558842346556",
            "appId": "1:558842346556:web:1cadf01619a79827ee9739",
            "measurementId": "G-ED25B9KYFR"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()

    def sign_in(self, email, password):
        try:
            self.auth.sign_in_with_email_and_password(email, password)
            return True

        except:
            return False

    def sing_up(self, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
            return True

        except:
            return False

    def reset_password(self, email):
        try:
            self.auth.send_password_reset_email(email)
            return True

        except:
            return False