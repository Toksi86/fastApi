from fastApi import FastApi

app = FastApi()

@app.get('/')
def hello():
    return 'Hello world'
