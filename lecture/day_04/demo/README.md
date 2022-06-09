# Flask Checklist

- [ ] make a new directory
- [ ] run command

```bash
pipenv install flask
```
- [ ] activate virtual env

```
pipenv shell
```
- create [server.py](first_flask/server.py):

```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
```
- start our webserver:

```bash
python server.py
```

- add route:

```py
@app.route('/about')
def about():
    return render_template('about.html')
```
- add templates folder

- inside templates folder, create html files
