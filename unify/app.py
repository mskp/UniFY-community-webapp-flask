# Importing required modules and packages
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from os import remove, urandom, path
from bcrypt import hashpw, checkpw, gensalt
from function import time_ago, resize_image
from sqlite3 import connect
from datetime import datetime

# SQLite db connection
connection = connect('/home/mycomunity/mysite/unify.sqlite', check_same_thread=False)

# Initializing flask app
app = Flask(__name__)

# Generating secret key for session
app.secret_key = urandom(24)

# Flask app config variables
app.config['PROFILE_PHOTO'] = "/home/mycomunity/mysite/static/img/profile-photo"
app.config['UPLOADS'] = "/home/mycomunity/mysite/static/img/uploads"

# For session
app.config['SESSION_TYPE'] = "filesystem"
app.config['SESSION_PERMANENT'] = True
Session(app)

# -----Signup end point-----
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if 'logged_in' in session:
        return redirect(url_for('index'))

    try:
        cursor = connection.cursor()

        if request.method == 'POST':
            name = request.form.get('name').strip()
            email = request.form.get('email').strip()
            password = request.form.get('password').strip()
            confirm_password = request.form.get('c-password').strip()
            profile_photo = request.files.get('profile-photo')

            profile_photo_extension = path.splitext(profile_photo.filename)[1];
            profile_photo.filename = f"mycommunity_profilePhoto_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}{profile_photo_extension}" if profile_photo.filename.strip() else "user.jpg";

            if password != confirm_password:
                return redirect(url_for('signup'))

            # Checking if the user already exists
            query_to_fetch_user = f"SELECT * FROM user WHERE email='{email}'"
            cursor.execute(query_to_fetch_user)
            row = cursor.fetchall()

            if row:
                return redirect(url_for('signup'))

            if profile_photo.filename != "user.jpg":
                profile_photo.save(path.join(app.config['PROFILE_PHOTO'], profile_photo.filename))
                resize_image(f"{path.join(app.config['PROFILE_PHOTO'])}/{profile_photo.filename}").save((path.join(app.config['PROFILE_PHOTO'], profile_photo.filename)))


            password_hash = hashpw(password.encode('utf-8'), gensalt())

            query_to_create_new_account = f"""INSERT INTO user(name, email, password, profile_photo, date) VALUES('{name}', '{email}', '{password_hash.decode()}', '{profile_photo.filename}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')"""
            cursor.execute(query_to_create_new_account)
            connection.commit()

            return redirect(url_for('login'))

        return render_template('signup.html')

    finally:
        cursor.close()

# -----Login end point-----
@app.route('/login', methods=['GET', 'POST'])
def login():

    if 'logged_in' in session:
        return redirect(url_for('index'))

    try:
        cursor = connection.cursor()

        if request.method == 'POST':
            email = request.form.get('email').strip()
            password = request.form.get('password').strip()

            query_to_fetch_user = f"SELECT * FROM user WHERE email='{email}'"
            cursor.execute(query_to_fetch_user)
            row = cursor.fetchall()

            if row and checkpw(password.encode('utf-8'), row[0][3].encode('utf-8')):
                session['logged_in'] = True
                session['id'] = row[0][0];
                session['name'] = row[0][1]
                session['email'] = row[0][2]
                session['profile_photo'] = row[0][4]

                return redirect(url_for('index'))

            return redirect(url_for('login'))

        return render_template('login.html')

    finally:
        cursor.close()

# -----Home end point-----
@app.route('/', methods=['GET', 'POST'])
def index():

    if 'logged_in' not in session:
        return redirect(url_for('login'))

    try:
        cursor = connection.cursor()

        if request.method == 'POST':
            id = session['id'];
            post = request.form.get('post').strip().replace("'", "''")
            photo = request.files.get('photo')
            extension = path.splitext(photo.filename)[1];
            photo.filename = f"mycommunity_uploaded_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}{extension}" if photo.filename.strip() else "";

            if post or photo.filename:
                if photo.filename:
                    photo.save(path.join(app.config['UPLOADS'], photo.filename))
                    resize_image(f"{path.join(app.config['UPLOADS'])}/{photo.filename}").save((path.join(app.config['UPLOADS'], photo.filename)))

                query_to_create_post = f"""INSERT INTO posts(id, post, photo, created_at) VALUES({id}, '{post}', '{photo.filename}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')"""
                cursor.execute(query_to_create_post)
                connection.commit()

                return redirect(url_for('index'))

        # Deleting post
        if request.form.get('delete'):
            time = request.form.get('delete');
            query_to_fetch_photo = f"SELECT photo FROM posts WHERE created_at='{time}'";
            cursor.execute(query_to_fetch_photo)
            photo = cursor.fetchone()

            if photo[0]:
                remove(path.join(app.config['UPLOADS'], photo[0]))

            query_to_delete_post = f"DELETE FROM posts WHERE created_at='{time}'";
            cursor.execute(query_to_delete_post)
            connection.commit()

            return redirect(url_for('index'))

        # Fetching members
        query_to_fetch_users = "SELECT * FROM user ORDER BY date DESC"
        cursor.execute(query_to_fetch_users)
        members = cursor.fetchall()
        users_count = len(members)

        # Fetching posts
        query_to_fetch_posts = "SELECT user.id, name, email, profile_photo, post, photo, created_at, is_verified FROM user INNER JOIN posts ON user.id = posts.id ORDER BY created_at DESC";
        cursor.execute(query_to_fetch_posts)
        posts = cursor.fetchall()

        return render_template('index.html', users_count=users_count, members=members, posts=posts, time_ago=time_ago)

    finally:
        cursor.close()

# -----Profile end point-----
@app.route('/profile', methods=['GET', 'POST'])
def profile():

    if 'logged_in' not in session:
        return redirect(url_for('login'))

    try:
        cursor = connection.cursor()
        id = session['id'];

        if request.method == 'POST':
            profile_photo = request.files.get('profile-photo')

            profile_photo_extension = path.splitext(profile_photo.filename)[1];
            profile_photo.filename = f"profile-photo_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}{profile_photo_extension}" if profile_photo.filename.strip() else ...

            profile_photo.save(path.join(app.config['PROFILE_PHOTO'], profile_photo.filename))
            resize_image(f"{path.join(app.config['PROFILE_PHOTO'])}/{profile_photo.filename}").save((path.join(app.config['PROFILE_PHOTO'], profile_photo.filename)))
            if session['profile_photo'] != 'user.jpg':
                remove(path.join(app.config['PROFILE_PHOTO'], session['profile_photo']))


            query_to_update_profile_photo = f"UPDATE user SET profile_photo='{profile_photo.filename}' WHERE id={id}";
            cursor.execute(query_to_update_profile_photo)
            connection.commit()

            return redirect(url_for('profile'))


        # Fetching profile photo
        query_to_fetch_profile_photo = f"SELECT profile_photo FROM user WHERE id={id}"
        cursor.execute(query_to_fetch_profile_photo)
        session['profile_photo'] = cursor.fetchone()[0];

        # Fetching posted photos
        query_to_fetch_photos = f"SELECT photo FROM posts where id={id} order by created_at desc"
        cursor.execute(query_to_fetch_photos)
        photos = cursor.fetchall()

        return render_template('profile.html', photos=photos)

    finally:
        cursor.close()

# -----Other profile end point-----
@app.route('/profile/<email>', methods=['GET', 'POST'])
def other_profile(email):

    # if 'logged_in' not in session:
    #     return redirect(url_for('login'))

    try:
        cursor = connection.cursor()

        query_to_fetch_user_data = f"SELECT * FROM user WHERE email='{email}'"
        cursor.execute(query_to_fetch_user_data)
        user_data = cursor.fetchall()
        print(user_data)

        query = f"SELECT photo FROM posts where id={user_data[0][0]} order by created_at desc"
        cursor.execute(query)
        photos = cursor.fetchall()

        return render_template('other-profile.html', photos=photos, user_data=user_data)

    finally:
        cursor.close()

# -----Contact end point-----
@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if 'logged_in' not in session:
        return redirect(url_for('login'))

    try:
        cursor = connection.cursor()

        if request.method == 'POST':
            subject = request.form.get('subject').strip().replace("'", "''")
            message = request.form.get('message').strip().replace("'", "''")

            if subject and message:
                query_to_insert_into_contact_table = f"""INSERT INTO contact(id, subject, message) VALUES({session['id']}, '{subject}', '{message}')"""
                cursor.execute(query_to_insert_into_contact_table)
                connection.commit()

                return redirect(url_for('contact'))

        return render_template('contact.html')

    finally:
        cursor.close()

# -----About Us end point-----
@app.route('/about', methods=['GET', 'POST'])
def about():
    # if 'logged_in' not in session:
    #     return redirect(url_for('login'))

    return render_template('about.html')

# -----Logout end point-----
@app.route('/logout')
def logout():
    session.pop('logged_in', None)

    return redirect(url_for('login'))

# ----------END----------

if __name__ == '__main__':
    app.run(debug=True)