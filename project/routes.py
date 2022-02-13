import decimal

from flask import render_template, flash, request, redirect, url_for, session
from project import app, db
from project.models.schema import UserModel, CommentModel
from project.form.forms import LoginForm, CommentForm, ResetForm, RegisterForm


@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html')


@app.route('/login/', methods=['POST','GET'])
def login():
    form = LoginForm()
    if "user" in session:
        return redirect(url_for('comment'))
    if form.validate_on_submit():
        user_data = UserModel.query.filter_by(email=form.email.data).first()
        if user_data is None or form.password.data != user_data.password:
            flash(f'Email or Password is wrong', 'danger')
        else:
            session["user"] = [user_data.id,user_data.email]
            return redirect(url_for('comment'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegisterForm()
    if "user" in session:
        return redirect(url_for('comment'))
    if form.validate_on_submit():
        user_data = UserModel.query.filter_by(email=form.email.data).first()
        if user_data is not None:
            flash(f'This email id already exists', 'danger')
        else:
             
            data = UserModel(
                email=form.email.data,
                password=form.password.data,
                secret=form.secret.data,
                is_delete=0
            )

            db.session.add(data)
            db.session.commit()

            flash(f'Account created successfully', 'success')
            return redirect(url_for('login'))
            
    return render_template('register.html', form=form)

@app.route('/reset', methods=['POST','GET'])
def reset():
    form = ResetForm()
    if "user" in session:
        return redirect(url_for('comment'))
    if form.validate_on_submit():
        user_data = UserModel.query.filter_by(email=form.email.data).first()
        if user_data is None or form.secret.data != user_data.secret:
            flash(f'email or password is wrong', 'danger')
        else:
            flash(f'The password is {user_data.password}', 'success')
            
    return render_template('reset.html', form= form)

@app.route('/comment', methods=['POST','GET'])
def comment():
    form = CommentForm()
    if "user" not in session:
        return redirect(url_for('login'))
    
    if "filter" not in session:
        session['filter'] = False
        
    if form.validate_on_submit():
        data = CommentModel(
            message=form.comment.data,
            created_by=session["user"][0],
            modified_by=session["user"][0]
        )

        db.session.add(data)
        db.session.commit()
    
    comment_data = CommentModel.query.filter_by(created_by=session["user"][0]).all() if session['filter'] else CommentModel.query.all()
    
    new_dict = []
    for comment in comment_data:
        new_dict.append({
            'comment': comment.message,
            'created_by': repr(UserModel.query.filter_by(id=comment.created_by).first()),
            'created_at': comment.created_at.isoformat(),
            'modified_by': repr(UserModel.query.filter_by(id=comment.modified_by).first()),
            'modified_at': comment.modified_at.isoformat()

    })
        
    return render_template('comment.html', comment_data=new_dict, form=form)


@app.route('/change_filter/')
def change_filter():
    if session['filter']:
        session['filter'] = False
    else:
        session['filter'] = False if session['filter'] else True
    
    return redirect(url_for('comment'))




@app.route('/logout/', methods=['POST','GET'])
def logout() :
    if "user" not in session:
        return redirect(url_for('login'))
    else:
        session.pop("user", None)
        return redirect(url_for('login'))

@app.errorhandler(404)
def invalid(txt):
    txt = "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    return render_template('invalid.html',text = txt)

