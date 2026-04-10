import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import AppUser

def create_demo_users():
    users = [
        ('admin', '1234', 'System Admin', 'admin'),
        ('doctor', '1234', 'Dr. House', 'doctor'),
        ('nurse', '1234', 'Nurse Jackie', 'nurse'),
        ('front', '1234', 'Receptionist', 'reception'),
        ('patient', '1234', 'John Wick', 'patient'),
    ]

    for username, password, name, role in users:
        if not AppUser.objects.filter(username=username).exists():
            AppUser.objects.create(username=username, password=password, name=name, role=role)
            print(f"Created user: {username}")
        else:
            print(f"User {username} already exists.")

if __name__ == "__main__":
    create_demo_users()