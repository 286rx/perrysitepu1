from flask import Flask, render_template

app = Flask(__name__, template_folder='Tugas', static_folder='Tugas_img')

@app.route('/')
def Percobaan():
    return render_template('Percobaan.html')

@app.route('/about')
def About():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(debug=True)
