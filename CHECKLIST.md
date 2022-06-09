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
- create [server.py](server.py):

```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
```
- start webserver:

```bash
python server.py
```

- add [templates folder](templates/index.html) with all the html files you need for your application.


- add route:

```py
@app.route('/about')
def about():
    return render_template('about.html')
```

