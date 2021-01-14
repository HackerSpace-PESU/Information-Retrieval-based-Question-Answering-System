from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from app import qamodel
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'


class QuestionForm(FlaskForm):
    question = StringField('Question:',
                         validators = [
                             InputRequired(message='Field is required!')
                             ])

    
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = QuestionForm()
    answer=0
    if form.validate_on_submit():
        question = form.question.data
        answer = qamodel.query(question).split('\n')
    return render_template('index.html', form = form, answer=answer)


if __name__ == '__main__':
    app.run(debug=True)

