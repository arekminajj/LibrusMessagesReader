from librus_tricks import create_session
import time

email = input("Your email: ")
passw = input("Your password: ")
session = create_session(email, passw)

while(True):
    time.sleep(10)
    try:
        messages = session.message_reader.read_messages()
        print(messages[0].text)
    except:
        session = create_session(email, passw)
