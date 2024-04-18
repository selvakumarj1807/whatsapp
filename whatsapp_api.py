#pip install pywhatkit

import pywhatkit

def send_message(phone_number, message):
    pywhatkit.sendwhatmsg_instantly(f"+{phone_number}", message)

# Example usage
phone_number = "919500912258"  # Replace with recipient's phone number
message = "Hello! This is an automated message."

send_message(phone_number, message)
