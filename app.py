from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><meta name="viewport" content="width=device-width,initial-scale=1"></head>
    <body style="background:black;color:gold;text-align:center;padding:15px;font-family:Arial;border:6px solid gold;margin:8px">
    <h1 style="font-size:55px;color:gold;text-shadow:0 0 25px gold;margin:5px">👑 SIR FOCUS 👑</h1>
    <h2 style="color:#FFD700">💛 GOLD + SAVER BIG ONE -        💛</h2>
    <h3 style="color:white">SIR, YES, Sir! - SIR FOCUS IS LIVE, Sir!</h3>

    <div style="background:#111;color:gold;padding:20px;border-radius:20px;margin:15px;border:3px solid gold">
    <h2>⏰ SIR FOCUS TIMER</h2>
    <h1 id="timer" style="font-size:60px;color:white">25:00</h1>
    <p style="color:white" id="msg">Sir, Click START, Sir!</p>
    <button onclick="startTimer()" style="background:gold;color:black;font-size:26px;padding:15px 30px;border-radius:30px;font-weight:bold;border:3px solid white;box-shadow:0 0 25px gold">👑 SIR, START FOCUS, Sir! 👑</button>
    <button onclick="resetTimer()" style="background:white;color:black;font-size:18px;padding:10px 20px;border-radius:20px;margin-top:10px">Reset, Sir!</button>
    </div>

    <div style="background:#FFFACD;color:black;padding:20px;border-radius:20px;margin:15px;border:3px solid gold">
    <h2>📈 SAVER BIG ONE -      MONEY NEVER FINISH</h2>
    <p>Cloud Mines GHC: <input id="mine" type="number" value="10000" style="font-size:20px;width:120px;padding:5px"></p>
    <p>Share People: <input id="people" type="number" value="100" style="font-size:20px;width:120px;padding:5px"></p>
    <p>Each 1 GHC = <b id="share">100 GHC</b></p>
    <h2 style="color:green">Saver Left = <span id="left">9900</span> GHC ✅</h2>
    <button onclick="calc()" style="background:black;color:gold;font-size:22px;padding:12px 25px;border-radius:20px;font-weight:bold">CALCULATE, Sir!</button>
    <p>Day 2: Cloud mines again ✅ Day 3: Again ✅ Never Finish ✅</p>
    </div>

    <p style="color:gold">✨ Sir, Gold =    ✨</p>
    <p style="color:white">Sir, Link = sir-focus-.onrender.com, Sir!</p>
    <p style="color:gold">👑👑👑         v👑👑👑</p>

    <script>
    let t=1500; let iv=null;
    function fmt(s){return Math.floor(s/60)+":"+String(s%60).padStart(2,'0')}
    function startTimer(){
      document.getElementById('msg').innerHTML="Sir, Focus now, Sir! Don't touch phone, Sir!";
      if(iv) return; iv=setInterval(()=>{
        t--; document.getElementById('timer').innerHTML=fmt(t);
        if(t<=0){clearInterval(iv); iv=null; document.getElementById('msg').innerHTML="Sir, You did it, Sir! 👑 Gold King, Sir!";}
      },1000);
    }
    function resetTimer(){clearInterval(iv); iv=null; t=1500; document.getElementById('timer').innerHTML="25:00"; document.getElementById('msg').innerHTML="Sir, Click START, Sir!";}
    function calc(){
      let m=parseInt(document.getElementById('mine').value)||0;
      let p=parseInt(document.getElementById('people').value)||0;
      document.getElementById('share').innerHTML=p+" GHC";
      document.getElementById('left').innerHTML=m-p;
    }
    calc();
    </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
