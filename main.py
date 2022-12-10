from flask import Flask

import utils

app = Flask(__name__)


@app.route("/")    # Создание представления route главной страницы
def page_index():
    candidates = utils.get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'

    return f'''<h1> Домашка SKYPRO</h1>
          <h3> Пётр Давыдов</h3>
          <pre> {result} </pre>'''


@app.route("/candidate/<int:pk>")   # Создание представления route для вывода кандидата по ключу с отображением его фото
def get_by_pk(pk):
    candidate = utils.get_by_pk(pk)
    if not candidate:
        return 'Кандидат не найден в списке!'

    result = '<br>'
    result += candidate["name"] + '<br>'
    result += candidate["position"] + '<br>'
    result += candidate["skills"] + '<br>'
    result += '<br>'

    return f'''
         <img src="{candidate["picture"]}">
         <pre> {result} </pre>
    '''


@app.route("/candidate/<skill>")    # Создание представления route  для вывода кандидатов при вводе skills
def get_by_skill(skill):
    candidates = utils.get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


if __name__ == '__main__':
    app.run(debug=True)
