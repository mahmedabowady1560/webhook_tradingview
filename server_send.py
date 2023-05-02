from flask import Flask, request,render_template
from threading import Thread
import json
import send_msg
app = Flask('')
@app.route('/webhook',methods=['POST','GET'])
def get_webhook():
    try:
        jsonRequest = request.args.get("jsonRequest")
        if request.method == 'POST':
            payload = request.data
            if jsonRequest == "true":
                payload = json.dumps(request.json,indent=4)
            print("received data: \n",payload)
            send_msg.sendMessage(payload)
            return 'success' , 200
        else:
            print("Get reques")
            return 'success' , 200
    except:    
        print("Exeption occured")
        return 'failure',500
@app.route('/')
def main():
    return 'Your Bot is Alive and Working !'
def welcome():
    return render_template('index.html')
def run():
    app.run(host='0.0.0.0',port='8080')

def start_server_async():
    server= Thread(target=run)
    server.start()

def start_server():
    app.run(host='0.0.0.0',port='8080')
