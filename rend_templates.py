from flask import render_template,request, Flask
import smtplib


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/send-email/', methods=["POST"])
def send_email():
    s = smtplib.SMTP("smpt.gmail.com",587)
    try:
        sender = request.form("sender-email-address")
        receiver = ""
        password = ""
        topic = request.form("subject")
        message = request.form("messages")
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender,receiver,message)


    except Exception as err:
        print("Something went wrong", err)
    finally:
        s.close()

    return "Message has been sent"





if __name__ == "__main__":
    app.run()
