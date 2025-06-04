from flask import Flask

from threading import Thread


app = Flask('')


@app.route('/')

def home():

    return "I'm alive"


def run():

  app.run(host='0.0.0.0',port=8080)


def keep_alive():

    t = Thread(target=run)

    t.start()

prefix = 'f?'#prefix here
token = "MTEyNTA1OTE2Mzc4MTg3NzkwMQ.G_V2aH.Zp5FzNke1vr2a3rHN2Y0ni-ZT94g_9vzb_Kh5k"#your token here
