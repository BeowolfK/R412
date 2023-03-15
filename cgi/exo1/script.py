import cgi, cgitb
from re import match
import time


form = cgi.FieldStorage()
name = form.getvalue('name')
sex = form.getvalue('sex')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Program 1</title>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link rel="stylesheet" href="../css/w3.css">')
print("</head>")
print("<body>")

if not match("[A-Z][a-z]+", name):
    print("""<div class="w3-container w3-center">
            <h2>ERREUR</h2>
            <h3>Votre nom n'est pas bon</h3>
          </div>""")
elif sex not in ['M', 'F']:
    print("""<div class="w3-container w3-center">
            <h2>ERREUR</h2>
            <h3>Votre sexe n'est pas bon</h3>
          </div>""")
else:
    string = ""
    if 18 <= int(time.strftime("%H")) <= 2:
        string += "Bonsoir "
    else:
        string += "Bonjour "

    if sex == "M":
        string += "Monsieur"
    else:
        string += "Madame"

    print(f"""<div class="w3-container w3-teal">
            <p>{string} {name}, il est {time.strftime("%H:%M")}</p>
          </div>""")


print("</body>")
print("</html>")