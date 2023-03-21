 
import random
import cgi

nb = [random.randint(0, 99) for _ in range(20)]

def sort(nb):
    n = len(nb)
    flag = True
    while flag:
        flag = False
        for i in range(n-1):
            if nb[i] > nb[i+1]:
                temp = nb[i+1]
                nb[i+1] = nb[i]
                nb[i] = temp
                flag = True
    return nb


print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Tri à bulles</title>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')
print("</head>")
print("<body>")
print("""<div class="w3-container w3-grey">
  <h1>Tri à bulle</h1>
</div>""")
print("""<div class="w3-container w3-light-grey">
  <h2 style="text-shadow:1px 1px 0 #444">Série d'origine</h2>
</div>""")
print(f"""<div class="w3-panel w3-border-left">
    <p>{str(nb)}</p>
  </div>""")
print("""<div class="w3-container w3-light-grey">
  <h2 style="text-shadow:1px 1px 0 #444">Série triée</h2>
</div>""")
print(f"""<div class="w3-panel w3-border-left">
    <p>{str(sort(nb))}</p>
  </div>""")
print("</body>")
print("</html>")
