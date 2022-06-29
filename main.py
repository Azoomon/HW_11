"""Импортив фласк и все ранее прописанные функции из utils.py"""
from flask import Flask, render_template
from utils import get_candidates_by_skill, get_candidate, get_candidates_by_name, load_candidates_from_json

"""Заводим представления для каждой странички (url)"""
app = Flask(__name__)

@app.route("/")
def index_page():
    """записываем все данные из джейсона в переменную, для работы с этими данными"""
    candidates = load_candidates_from_json('candidates.json')
    """используем темплейт (шаблон html), указываем файл html, ссылаемся на candidates из функции чтобы была связь этих данных с html"""
    return render_template("list.html", candidates=candidates)

"""Повторяем все с поправкой на требуемые нам данные и url"""
@app.route("/candidate/<int:id>")
def page_per_id(id):
    person = get_candidate(id)
    return render_template("single.html", candidate=person)


@app.route("/search/<candidate_name>")
def page_per_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, search_name=candidate_name)

@app.route("/skill/<skill_name>")
def page_per_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name)


"""Предохранитель от случайного запуска"""
if __name__ == "__main__":
    app.run()