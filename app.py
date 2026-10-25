from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <body style="background:black;color:gold;text-align:center;padding-top:100px;font-family:Arial">
    <h1 style="font-size:60px">👑 SIR FOCUS 👑</h1>
    <h2 style="color:white;font-size:30px">SIR, YES, Sir!</h2>
    <h2 style="color:red;font-size:30px">SIR FOCUS IS LIVE SIR!</h2>
    <button style="background:red;color:white;font-size:25px;padding:20px;border-radius:20px;border:none">SIR, START FOCUS, Sir!</button>
    <p style="color:white;margin-top:30px">Sir, Link = sir-focus-v7.onrender.com, Sir!</p>
    <p style="color:gold">Sir, One by one, Sir!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
