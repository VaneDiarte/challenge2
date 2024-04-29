#importar la libreria para poder construir la aplicacion 

from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

from modelos import Usuario


#crear la clase mesas
class mesas:
    def _init_(self):
        self.cantidad_mesas = []
        self.mesas_reservadas = {}


    def reservas_mesas(self, numero):
        if numero not in self. mesas_reservadas:
            self.mesas_reservadas[numero] 
            return f"La reserva de la mesa {numero} se ha hecho correctamente"

        else:
            print(f"La mesa {numero} esta reservada")

    def cancelar_reserva(self, numero):
        if numero in self.mesas_reservadas:
            del self.mesas_reservadas[numero]
            return f"La reserva de la mesa {numero} ha sido cancelada"
        else:
            return f"No hay una reserva para la mesa {numero}"
        
    def imprimir_reservas(self):
        print(self.mesas_reservadas)

mesa = mesas()
mesa.reservas_mesas()

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/nosotros')
def inicio():
    return render_template('nosotros.html')

@app.route('/registro')
def inicio():
    return render_template('registro.html')


#crear la clase usuario
class Usuario:
    def _init_(self):
        self.usuario = []
        self.usuario_nombre = {}

@app.route('/cancelar_reserva', methods=['POST'])
def cancelar_reserva():
    numero_mesa = int(request.form['numero_mesa'])
    mensaje = mesa.cancelar_reserva(numero_mesa)
    return jsonify({'cancelar reserva de la mesa': mensaje})

@app.route('/reservas')
def obtener_reservas():
    reservas = mesa.obtener_reservas()
    return jsonify(reservas)

if __name__ == '_main_':
    app.run(debug=True)

mesa.imprimir_reservas()