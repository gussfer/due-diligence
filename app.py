from flask import Flask, request, render_template

app = Flask(__name__)

def valida_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    cpf = [int(digit) for digit in cpf]
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((10 * value) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


@app.route('/', methods=['GET', 'POST'])
def check_cpf():
    if request.method == 'POST':
        cpf = request.form['cpf']
        valido = valida_cpf(cpf)
        return render_template('result.html', valido=valido)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
