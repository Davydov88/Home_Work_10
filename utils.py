import json


def load_candidates():
    """Функция, которая загружает все данные из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_all():
    """Функция, которая покажет всех кандидатов"""
    return load_candidates()


def get_by_pk(pk):
    """Функция, которая возвращает кандидатов по pk"""
    for candidate in load_candidates():
        if candidate["pk"] == pk:
            return candidate
    return


def get_by_skill(skill):
    """Функция, которая возвращает кандидатов по навыку"""
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate["skills"].split(', '):
            candidates.append(candidate)
    return candidates