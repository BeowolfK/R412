import cgi
form = cgi.FieldStorage()

ft = form.getvalue('altitude_ft')
m = form.getvalue('altitude_m')

def ft_to_m(altitude_pied):
    return altitude_pied * 0.3048


def m_to_ft(altitude_metre):
    return altitude_metre / 0.3048

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Program 2</title>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link rel="stylesheet" href="../css/w3.css">')
print("</head>")
print("<body>")

if ft is None and m is None:
    print("""<div class="w3-container w3-center">
            <h2>ERREUR</h2>
            <h3>Merci de saisir au moins une valeur</h3>
          </div>""")
elif not(ft is None) and not(m is None):
    print("""<div class="w3-container w3-center">
            <h2>ERREUR</h2>
            <h3>Merci de ne saisir qu'une valeur</h3>
          </div>""")
else:
    value = ""

    if m is None:
        m = ft_to_m(int(ft))
        value = f"{round(m, 2)} m"
    if ft is None:
        value = f"{round(m_to_ft(int(m)), 2)} ft"
        m = int(m)
    image = ""
    if m < 1000:
        print("""<div class="w3-container w3-teal">
            <p>Vous êtes trop bas!</p>
        </div>""")
        exit()
    if 1000 <= m <= 4999:
        image="tourisme"
    elif 5000 <= m <= 5999:
        image="question"
    elif 5100 <= m <= 6999:
        image="regional"
    elif 7000 <= m <= 9999:
        image="moyen-courrier"
    elif 10000 <= m <= 13000:
        image="long-courrier"
    elif m <= 15500:
        image="business-jet"
    elif m > 15500:
        print("""<div class="w3-container w3-teal">
            <p>Vous êtes trop haut!</p>
        </div>""")
        exit()

    print(f"""<div class="w3-container">
            <div class="w3-card-4">
                <img src="../image/{image}.jpg" style="width:100%">
                <div class="w3-container w3-center">
                <h4><b>{image.replace("-", " ").title()}</b></h4>
                <p>{value}</p>
                </div>
            </div></div>""")
print("</body>")
print("</html>")
