from flask import Flask, flash, jsonify, redirect, request, render_template, url_for

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     return "This is a POST request", 201
    # return "Hello, World!"
    myvalue = "AIOOOOOOOOOOO"
    mylist = [1, 2, 3, 4, 5]
    return render_template('index.html', myvalue=myvalue, mylist=mylist)

@app.route('/other')
def other():
    some_text = "This is some text"
    return render_template('other.html', some_text=some_text)

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('other'))

@app.route('/add/<int:a>/<int:b>')
def add():
    return f"The sum is {a + b}"

@app.route('/handle_url_params')
def handle_url_params():
    if 'greetings' not in request.args.keys() and 'name' not in request.args.keys():
        return "Missing required parameters: 'greetings' and 'name'", 400
    greetings = request.args['greetings']
    name = request.args.get('name')
    return f"{greetings}, {name}!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123':
            return render_template('index.html', message="")
        else:
            return render_template('login.html', message="")
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    if file.content_type == 'text/plain':
        return f"File {file.filename} uploaded successfully!\n" + file.read().decode('utf-8'), 200

    return

@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f"{greeting}, {name}!\n")

    return jsonify({'message': f"{greeting}, {name}!"})


@app.template_filter('reverse_string')
def reverse_string(s):
    """Reverses a string."""
    return s[::-1]