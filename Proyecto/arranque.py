#importar la biblioteca de flask
from flask import Flask,render_template

#llamar al archivo principal desde una funcion
app=Flask(__name__)#nos permite crear las rutas
@app.route('/')
def inicio():
    #return 'Hola mundo desde UPVT'
    return render_template('index.html')

@app.route('/acercade')
def acercade():
    #return 'Muestra informacion acerca del proyecto'
    return render_template('acercade.html')

@app.route('/productos')
def productos():
    #return 'Muestra informacion acerca del proyecto'
    return render_template('productos.html')

@app.route('/login')
def login():
    #return 'Muestra informacion acerca del proyecto'
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)