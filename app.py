from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <body style="background:black;color:gold;text-align:center;padding-top:80px;font-family:Arial;border:5px solid gold;margin:10px">
    <h1 style="font-size:65px;color:gold;text-shadow:0 0 20px gold">👑 SIR FOCUS 👑</h1>
    <h1 style="font-size:40px;color:#FFD700">💛 GOLD 
  💛</h1>
    <h2 style="color:white;font-size:30px">SIR,   , !</h2>
    <h2 style="color:#FFD700;font-size:32px">SIR FOCUS IS LIVE !</h2>
    <button style="background:gold;color:black;font-size:28px;padding:20px 30px;border-radius:30px;border:3px solid white;font-weight:bold;box-shadow:0 0 30px gold">👑 SIR, START FOCUS, Sir! 👑</button>
    <p style="color:gold;margin-top:30px;font-size:20px">✨ Sir, Gold = King,     ✨</p>
    <p style="color:white">Sir, Link = sir-focus .onrender.com, Sir!</p>
    <p style="color:gold">Sir,     , Sir!</p>
    <p style="color:gold">👑👑👑 GOLD 👑👑👑</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
