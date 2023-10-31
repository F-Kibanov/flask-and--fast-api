from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page='Main page')


@app.route('/outerwear/')
def outerwear():
    wear = [
        {"title": "coat_1", "desc": "some_coat_1_desc", "price": "$111"},
        {"title": "coat_2", "desc": "some_coat_2_desc", "price": "$222"},
        {"title": "coat_3", "desc": "some_coat_3_desc", "price": "$333"},
        {"title": "coat_4", "desc": "some_coat_4_desc", "price": "$444"},
    ]
    return render_template('index.html', items=wear, page='Outwear')


@app.route('/shoes/')
def shoes():
    shoe = [
        {"title": "shoes_1", "desc": "some_shoes_1_desc", "price": "$555"},
        {"title": "shoes_2", "desc": "some_shoes_2_desc", "price": "$666"},
        {"title": "shoes_3", "desc": "some_shoes_3_desc", "price": "$777"},
        {"title": "shoes_4", "desc": "some_shoes_4_desc", "price": "$888"},
    ]
    return render_template('index.html', items=shoe, page='Shoes')


@app.route('/hats/')
def hats():
    hat = [
        {"title": "hat_1", "desc": "some_hat_1_desc", "price": "$100"},
        {"title": "hat_2", "desc": "some_hat_2_desc", "price": "$200"},
        {"title": "hat_3", "desc": "some_hat_3_desc", "price": "$300"},
        {"title": "hat_4", "desc": "some_hat_4_desc", "price": "$400"},
    ]
    return render_template('index.html', items=hat, page="Hats")


if __name__ == '__main__':
    app.run(debug=True)
