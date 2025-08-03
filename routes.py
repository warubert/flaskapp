from flask import Flask, flash, jsonify, redirect, request, render_template, url_for
from models import Person, User
from flask_login import login_user, logout_user, current_user, login_required


def register_routes(app, db, bcrypt):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        # myvalue = "AIOOOOOOOOOOOu"
        # mylist = [1, 2, 3, 4, 5]
        people = Person.query.all()

        if request.method == 'GET':
            return render_template('index.html', people=people)
        elif request.method == 'POST':
            name = request.form.get('name')
            age = request.form.get('age')
            job = request.form.get('job')
            if not name or not age:
                return redirect(url_for('index'), people=people)
            new_person = Person(name=name, age=int(age), job=job)
            db.session.add(new_person)
            db.session.commit()
            return redirect(url_for('index'), people=people)
        
    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete_person(pid):
        person = Person.query.get(pid)
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': 'Person deleted successfully'}), 200
        else:
            return jsonify({'message': 'Person not found'}), 404
        
    @app.route('/details/<pid>')
    def detail_person(pid):
        person = Person.query.get(pid)
        if person:
            return render_template('detail.html', person=person)
        else:
            return "Person not found", 404
        
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
    
    @app.route('/people', methods=['GET'])
    def get_people():
        people = Person.query.all()
        return str(people)
    
    @app.route('/login_users', methods=['GET'])
    def index_users():
        if not current_user.is_authenticated:
            return "User is not logged in", 401
        else:
            return str(current_user.username)
    
    @app.route('/login_user/<uid>', methods=['GET'])
    def login_users(uid):
        user = User.query.get(uid)
        login_user(user)
        return f"User logged in successfully."
    
    @app.route('/logout', methods=['GET'])
    def logout2():
        logout_user()
        return redirect(url_for('index'))
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            hashed_password = bcrypt.generate_password_hash(password)

            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
        
    @app.route('/login2', methods=['GET', 'POST'])
    def login2():
        if request.method == 'GET':
            return render_template('login2.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'Invalid username or password', 401
            
    @app.route('/secret')
    @login_required
    def secret():
        return f"Secret page for {current_user.username} with role {current_user.role}"