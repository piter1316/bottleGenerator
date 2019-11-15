import random
import string

from bottle import route, run, post, request, template


@route('/generate')
def hello():
    return """ 
    <form action="/generate" method="post">
        <div class="">
            <label for="chars">Password length</label>
            <input type="number" name="chars" id="chars" value="8"/>
        </div>
        <div class="">
            <label for="specials">Scpecial chracters</label>
            <input type="checkbox" name="specials" id="specials" />
        </div>
    
        <div class="">
            <button type="submit" name="generate">GENERATE</button>
        </div>
    </form>
  """

@post('/generate') # or @route('/login', method='POST')
def do_generate():
    passwd = ''
    chars_with_specials = string.ascii_letters + string.punctuation
    passw_length = int(request.forms.get('chars'))
    specials = request.forms.get('specials')
    if specials:
        for i in range(passw_length):
            passwd += random.choice(chars_with_specials)
    else:
        for i in range(passw_length):
            passwd += random.choice(string.ascii_letters)
    return "<p>{}</p>".format(passwd)

run(host='localhost', port=8080, debug=True)