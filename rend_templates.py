from flask import render_template, Flask
import smtplib
import requests


app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('contact.html', name=name)

@app.route('/send-email/', methods=['GET','POST'])
def contact():
    return render_template('contact.html')


def email(name=None):
    s = smtplib.SMTP("smpt.gmail.com",587)
    name = requests.get("sender-name")
    sender = requests.get("sender-email")
    receiver = requests.get("receiver-email")
    topic = requests.get("sub")
    para = requests.get("message")
    s.starttls()
    s.login(sender)
    s.sendmail(name,sender,receiver,topic,para)
    s.quit()




if __name__ == "__main__":
    app.run()
