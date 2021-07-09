from flask import Flask, render_template, request


app = Flask(__name__)

wd = 0
rh = 0
ws = 0
wg = 0
t = 0
p = 0
pt = 0
dp = 0

@app.route("/")
def home():
    """
    return '''
              <h1>The wind dir value is: {}</h1>
              <h1>The humidity value is: {}</h1>
              <h1>The wind speed value is: {}</h1>
              <h1>The wind gust value is: {}</h1>
              <h1>The air temp value is: {}</h1>
              <h1>The pressure value is: {}</h1>
              <h1>The precipitation value is: {}</h1>
              <h1>The dewpoint value is: {}'''.format(wd,rh,ws,wg,t,p,pt,dp)
    """
    #return "Hello World (please work)"
    return render_template('index.html', wd=wd, rh=rh, ws=ws, wg=wg, t=t, p=p, pt=pt, dp=dp)

@app.route('/weather_update')
def weather_update():
    #return 'Query String Example'
    #if key doesn't exist, returns None
    global wd
    global rh
    global ws
    global wg
    global t
    global p
    global pt
    global dp
    wd = request.args.get('winddir')
    rh = request.args.get('rh')
    ws = request.args.get('wind')
    wg = request.args.get('gust')
    t = request.args.get('temp')
    p = request.args.get('pressure')
    pt = request.args.get('precip')
    dp = request.args.get('dewpoint')
    return '''
              <h1>The wind dir value is: {}</h1>
              <h1>The humidity value is: {}</h1>
              <h1>The wind speed value is: {}</h1>
              <h1>The wind gust value is: {}</h1>
              <h1>The air temp value is: {}</h1>
              <h1>The pressure value is: {}</h1>
              <h1>The precipitation value is: {}</h1>
              <h1>The dewpoint value is: {}'''.format(wd,rh,ws,wg,t,p,pt,dp)