from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def main():
    posty = [
        {
            'dat_loc': {'date': '05.01.2019', 'location': 'Gdańsk'},
            'body': 'Tekst1'
        },
        {
            'dat_loc': {'date': '12.01.2019', 'location': 'Gdańsk'},
            'body': 'Tekst2'
        },
        {
            'dat_loc': {'date': '13.01.2019', 'location': 'Frombork'},
            'body': 'Tekst3'
        }
    ]
    return render_template('index.html', tytul='Artykuły', posty=posty)





if __name__ == "__main__":
    app.run()
