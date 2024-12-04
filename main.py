from flask import Flask, redirect, url_for, abort, request, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('unstyled.html'), 200

@app.route('/hello1/')
def hello1():
  return "Hello Napier!!! :D"

@app.route('/private/')
def private():
    # Test for user logged in failed
    # so redirect to login URL
   return redirect(url_for('login'))

@app.route('/login/')
def login():
   return "Now we should get a username & password"

@app.route('/static-example/img')
def static_example_img():
   start = '<img src= "'
   url = url_for('static', filename='vmask.jpg')
   end = '">'
   return start+url+end, 200

@app.route("/account1/", methods=['GET', 'POST'])
def account1():
    if request.method == 'POST':
        return "POST'ed to /account root\n" # use cmd to POST AS CURL NEEDED IN TERMINAL IS DEIFFERENT
    else:
        return "GET /account root"

@app.route("/account2/", methods=['GET', 'POST'])
def account2():
    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        return "Hello %s" %name
    else:
        page ='''
        <html><body>
          <form action="" method="post" name="form">
          <label for="name">Name:</label>
          <input type="text" name="name" id="name"/>
          <input type="submit" name="submit" id="submit"/>
          </form>
        </body><html>'''

        return page

@app.errorhandler(404)
def page_not_found(error):
   return "Couldn't find the page you requested.", 404

@app.route('/force404')
def force404():
   abort(404)

@app.route('/goodbye/')
def goodbye():
   return "Goodbye cruel world :("

#VARIABLE USE
@app.route('/hello2/<name>') #replavce <name> with yours in the url and it returns that.
def hello2(name):
   return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first,second):
    return str(first+second)

#PARAMATER USE
@app.route('/hello3/')
def hello3():
    name = request.args.get('name', '')
    if name == '':
        return "no param supplied"
    else: # in the url you type ?name= the name you want displayed
        return "Hello %s" % name

#FILE UPLOAD
@app.route("/upload/", methods=['GET', 'POST'])
def account3():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/vmask.jpg')
        return "File Uploaded"
    else:
        page ='''
        <html><body>
          <form action="" method="post" name="form" enctype="multipart/form-data">
          <input type="file" name="datafile" />
          <input type="submit" name="submit" id="submit"/>
          </form>
        </body><html>'''

        return page, 200

@app.route("/display/")
def display():
    return '<img src="'+url_for('static', filename='uploads/vmask.jpg')+'"/>'

#TEMPLATE USE
@app.route('/hello4/<name>')
def hello4(name=None):
    user = {'name': name}
    return render_template('hello.html', user=user)

@app.route('/hello5/<name>')
def hello5(name=None):
    user = {'name': name}
    return render_template('hello.html', user=user)

@app.route('/hello6/')
@app.route('/hello6/<name>')
def hello6(name=None):
    return render_template('conditional.html', name=name)

#TEMPLATE AND COLLECTIONS
@app.route('/users/')
def users():
    names = ['simon', 'thomas', 'lee', 'jamie', 'sylvester']
    return render_template('loops.html', names=names)

#TEMPLATE INHERITANCE
@app.route('/inherits/')
def inherits():
    return render_template('base.html')

@app.route('/inherits/one/')
def inherits_one():
    return render_template('inherits1.html')

@app.route('/inherits/two/')
def inherits_two():
    return render_template('inherits2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




