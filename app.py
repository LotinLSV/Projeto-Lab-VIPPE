from flask import Flask, render_template, request
import webview
import threading
import os
import time


def inject_floating_button():
    js = """
    (function() {
        if (document.getElementById('floating-btn')) return;

        const btn = document.createElement('button');
        btn.id = 'floating-btn';
        btn.innerText = '↪️';

        Object.assign(btn.style, {
            position: 'fixed',
            bottom: '20px',
            right: '20px',
            zIndex: '9999',
            padding: '15px',
            borderRadius: '50%',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            cursor: 'pointer',
            fontSize: '18px',
            boxShadow: '0 4px 10px rgba(0,0,0,0.3)'
        });

        btn.onclick = function() {
          window.location.href='/home'
        };

        document.body.appendChild(btn);
    })();
    """
    return js




app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/central')
def p2():
    return render_template('central.html')


@app.route('/agente')
def abrir_agente():
    return render_template('agente.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploadArquivos', methods=['POST'])
def upload_arquivo():
    if 'usuario' not in globals():
        return "Usuário não logado", 403
    
    file = request.files.get('files')
    if not file or file.filename == '':
        return "Nenhum arquivo enviado", 400
    
    username = usuario
    user_folder = os.path.join(app.config["UPLOAD_FOLDER"], username)
    os.makedirs(user_folder, exist_ok=True)
    
    filepath = os.path.join(user_folder, file.filename)
    file.save(filepath)
    
    return "Upload realizado com sucesso"


@app.route('/logar', methods=['POST'])
def realiza_login():
    global urln8n
    global usuario
    global senha

    usuario = request.form['usuario']
    senha = request.form['senha']

    if usuario == 'paollo' and senha == '123':
        urln8n = "https://labvippeplus.app.n8n.cloud/projects/hH8IKvKqSVtsseeD/workflows"
        return render_template('central.html', titulo='central')
    elif usuario == 'messias' and senha == '123':
        urln8n = ""
        return render_template('central.html', titulo='central')
    elif usuario == 'lucas' and senha == '123':
        urln8n = "https://labvippeplus.app.n8n.cloud/projects/kXLih3RyOAkbdnF8/workflows"
        return render_template('central.html', titulo='central')
    else:
        return "Login inválido"


# 🔥 API controlando navegação externa
class API:
    # def abrir_google(self):
    #     webview.windows[0].load_url('https://www.google.com')

    # def abrir_uol(self):
    #     webview.windows[0].load_url('https://www.uol.com.br')

    def abrir_n8n(self):
        if urln8n:
            webview.windows[0].load_url(urln8n)
        else:
            webview.windows[0].load_url("http://127.0.0.1:5000/home")


def start_flask():
    app.run(port=5000)


if __name__ == '__main__':
    t = threading.Thread(target=start_flask)
    t.daemon = True
    t.start()

    window = webview.create_window(
        "App",
        "http://127.0.0.1:5000/home",
        js_api=API(),
        width=1200,
        height=800
    )





def keep_button_alive(window):
    while True:
        try:
            window.evaluate_js(inject_floating_button())
        except:
            pass
        time.sleep(1)


def start_webview():
    keep_button_alive(window)

webview.start(start_webview)