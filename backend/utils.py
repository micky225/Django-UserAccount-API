import random
from django.core.mail import send_mail

def generate_six_random_numbers():
    return str(random.randint(100000, 999999))

def send_raw_email(subject: str, message: str, sender: str, recipients: list):
    send_mail(subject, message, sender, recipients)
