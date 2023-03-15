import cgi
import mysql.connector


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Program 3</title>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link rel="stylesheet" href="../css/w3.css">')
print("</head>")
print("<body>")
try:
    db = mysql.connector.connect(
    host="localhost",
    user="etudiant",
    password="Promo2024",
    database="test"
    )
    cursor = db.cursor()


    form = cgi.FieldStorage()
    dept_num = form.getvalue("dept_num")

    query = "SELECT departement_code, departement_nom FROM departement WHERE departement_code = "+dept_num
    cursor.execute(query)

    result = cursor.fetchone()

    print(f"""<div class="w3-container">
            <div class="w3-card-4" style="width:50%;">
                <header class="w3-container w3-blue">
                <h1>{result[0]}</h1>
                </header>

                <div class="w3-container">
                <p>{result[1]}</p>
                </div>
            </div>
            </div>""")

    db.close()
except Exception as e:
    print(e)
