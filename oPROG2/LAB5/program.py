from schema import factory, User
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

session = factory()

@app.route('/')
@app.route('/index')
def show_all_users():
    users = session.query(User).all()
    return render_template('all_users.html', users=users)


@app.route('/add-user')
def add_new_user():
    return render_template('registration.html')


@app.route('/edit-user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = session.query(User).get(user_id)
    if request.method == 'POST':
        user.first_name = request.form.get('name')
        user.last_name = request.form.get('surname')
        user.email = request.form.get('email')
        user.username = request.form.get('username')
        user.password = request.form.get('pwd')
        try:
            session.commit()
            return redirect(url_for('show_all_users'))
        except Exception as e:
            session.rollback()
            return f"Failed to update user: {e}"
    return render_template('edit_user.html', user=user)


@app.route('/user-reg', methods=['POST'])
def user_form():
    u = User(
        first_name=request.form["name"],
        last_name=request.form["surname"],
        email=request.form["email"],
        username=request.form["username"],
        password=request.form["pwd"]
    )
    confirm_pwd = request.form["confirm_pwd"]

    if u.password != confirm_pwd:
        return "Password confirmation does not match"

    try:
        session.add(u)
        session.commit()
        return redirect(url_for('show_all_users'))
    except Exception as e:
        session.rollback()
        return f"Failed: {e}"


@app.route('/user-log', methods=['GET', 'POST'])
def user_log_in():
    if request.method == 'POST':
        user = session.query(User).filter_by(username=request.form["username"]).first()
        if user is None:
            return "Username not found"
        elif user.password == request.form["pwd"]:
            return "Success"
        else:
            return "Wrong password"
    return render_template('log_in.html')


if __name__ == 'main':
    app.run(host="127.0.0.1", port=4322)