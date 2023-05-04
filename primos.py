from flask import Flask

app = Flask(__name__)

@app.route('/')
def primo():
    inicioPrimo = 3
    qtdTotal = 98
    nPrimo = 1
    primos = '1,2'
    qtdEncontrada = 2

    while qtdTotal > 0:
        for i in range(2, inicioPrimo):
            if inicioPrimo % i == 0:
                nPrimo = 0
                pass
        if nPrimo == 1:
            primos = primos + str(inicioPrimo) + ","
            qtdTotal -= 1
            qtdEncontrada += 1

            if qtdEncontrada % 10 == 0:
                primos += "<br>"

        inicioPrimo += 2
        nPrimo = 1

    return primos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)