# Flask Checklist

- [ ] make a new directory
- [ ] move this document inside the new directory.
- [ ] create virtual environment:

```bash
pipenv install flask
```
- [ ] activate virtual environment:

```
pipenv shell
```
- [ ] create [server.py](server.py):

```py
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods = ['POST'])
def handle_data():
    print(request.form['info'])
    session['session_info'] = request.form['info']
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
```
- [ ] start webserver:

```bash
python server.py
```

- [ ] add [templates](templates/index.html) folder with all the html files you need for your application.


- [ ] add routes as needed:

```py
@app.route('/about')
def about():
    return render_template('about.html')
```
- [ ] add [index.html](templates/index.html):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>flask form</title>
</head>
<body>
    {{session}}
    <h1>Form Demo</h1>
    <form action="/data" method="post">
        <label for="info">info</label>
        <input type="text" name="info" id="info">
        <input type="submit" value="submit">
    </form>

    <h2>{{session['session_info']}}</h2>
</body>
</html>
```