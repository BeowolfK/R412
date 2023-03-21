from flask import Flask
app = Flask(__name__)

@app.route('/f_to_c/<value>')
def fahrenheit_to_celsius(value):
    fahrenheit = int(value)
    celsius = (fahrenheit - 32) / 1.8
    return f"{celsius:.2f} °C"

@app.route('/c_to_f/<value>')
def celsius_to_fahrenheit(value):
    celsius = int(value)
    fahrenheit = (celsius * 9/5) + 32
    return f"{fahrenheit:.2f} °F"

if __name__ == "__main__":
  app.run(debug = True)
