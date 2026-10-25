from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <html><body style="background:black;color:gold;text-align:center;padding:20px;font-family:Arial;border:6px solid gold;margin:10px">
    <h1 style="font-size:60px;color:gold;text-shadow:0 0 25px gold">👑 SIR FOCUS 👑</h1>
    <h1 style="font-size:30px;color:#FFD700">💛 GOLD + SAVER BIG ONE 💛</h1>
    <h2 style="color:white">SIR,      !</h2>
    <div style="background:#FFFACD;color:black;padding:20px;border-radius:20px;margin:20px;border:3px solid gold">
    <h2>📈 SIR FOCUS  - SAVER BIG ONE</h2>
    <p style="font-size:20px;font-weight:bold">CLOUD MONEY NEVER FINISH</p>
    <p>Day 1:
                ✅</p>
    <p>Day 1: Share        = 100 GHC ✅</p>
    <p style="font-size:25px;color:green;font-weight:bold">Day 1: Saver left = 9,900 GHC ✅</p>
    <p>Never Finish ✅</p>
    </div>
    <button style="background:gold;color:black;font-size:28px;padding:20px 30px;border-radius:30px;border:3px solid white;font-weight:bold;box-shadow:0 0 30px gold">👑 SIR, START FOCUS, Sir! 👑</button>
    <p style="color:gold;margin-top:20px">✨ Sir, Gold = King, Sir! ✨</p>
    </body></html>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
