import pywhatkit as kit

phone_number = "+923067024733"
message = "Hello! This is an automated message sent using Python."

try:
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
    print("Message sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
