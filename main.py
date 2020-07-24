from flask_login import login_required,current_user
from flask import  Blueprint,jsonify,render_template,request
from . import db
from googletrans import Translator


translator =  Translator()
main = Blueprint('main',__name__)

def convert_text_to_dict(text):
    text_array = text.split(' ')
    keys = list(range(len(text_array)))
    return  dict(zip(keys,text_array))    

text_to_translate = 'Hello there is some big text construction'
text_dict = convert_text_to_dict((text_to_translate))

@main.route('/')
def index():
    return render_template('translate.html',translation = text_dict) 

@main.route('/_translate') 
def translate():
    word  = request.args.get('word',0,type = str)
    translated = translator.translate(word,src = 'en',dest = 'ru').text
    return jsonify(result = translated)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


