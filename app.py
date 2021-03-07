from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/chart2')
def chart2():

  legend = "Argent du joueur sur toutes les parties"  
  conn = sqlite3.connect('BDD_argent_joueur.db')  # nom de la base de données
  cursor = conn.cursor()
  try:
        cursor.execute("SELECT partie from total_argent") #choix de la table
        rows = cursor.fetchall()
        labels = list() #récupération des valeurs
        i = 0
        for row in rows:
            labels.append(row[i])
        
        cursor.execute("SELECT argent from total_argent") #choix de la table
        rows = cursor.fetchall()
        
        values = list() #récupération des valeurs
        i = 0
        for row in rows:
            values.append(row[i])
        cursor.close()    
        conn.close()
        
  except:
        print("Error: unable to fetch items")
  return render_template("chart2.html", values=values, labels=labels, legend=legend) #envoie des valeurs à l'html

@app.route('/chart3')
def chart3():

  legend = "Argent du joueur sur 5 parties"  
  conn = sqlite3.connect('BDD_argent_joueur.db')  # nom de la base de données
  cursor = conn.cursor()
  try:
        cursor.execute("SELECT partie from total_argent LIMIT 5") #choix de la table
        rows = cursor.fetchall()
        labels = list() #récupération des valeurs
        i = 0
        for row in rows:
            labels.append(row[i])
        
        cursor.execute("SELECT argent from total_argent LIMIT 5") #choix de la table
        rows = cursor.fetchall()
        
        values = list() #récupération des valeurs]
        i = 0
        for row in rows:
            values.append(row[i])
        cursor.close()    
        conn.close()


  except:
        print("Error: unable to fetch items")
  return render_template("chart3.html", values=values, labels=labels, legend=legend) #envoie des valeurs à l'html


app.run(debug=True, use_reloader=False)
