import random

def tri_selection(t):
    n = len(t)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if t[j] < t[min_index]:
                min_index = j
        if min_index != i:
            temp = t[min_index]
            t[min_index] = t[i]
            t[i] = temp
    return t

liste = [random.randint(0, 99) for _ in range(20)]

print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Tri par sélection</title>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link rel="stylesheet" href="../css/w3.css">')
print("</head>")
print("<body>")
print("""<div class="w3-container w3-grey">
  <h1>Tri par sélection</h1>
</div>""")
print("""<div class="w3-container w3-light-grey">
  <h2 style="text-shadow:1px 1px 0 #444">Série d'origine</h2>
</div>""")
print(f"""<div class="w3-panel w3-border-left">
    <p>{str(liste)}</p>
  </div>""")
print("""<div class="w3-container w3-light-grey">
  <h2 style="text-shadow:1px 1px 0 #444">Série triée</h2>
</div>""")
print(f"""<div class="w3-panel w3-border-left">
    <p>{str(tri_selection(liste))}</p>
  </div>""")
print("</body>")
print("</html>")
