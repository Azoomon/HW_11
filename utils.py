import json


def load_candidates_from_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate_id == candidate["id"]:
            return candidate

def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json('candidates.json')
    to_return = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            to_return.append(candidate)
    return to_return

def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json('candidates.json')
    approved = []
    for candidate in candidates:

    #     if skill_name in map(lambda skill: skill.lower().strip(), candidate['skills'].split(',')):
    #         approved.append(candidate)
    # return approved


        skills_str = candidate["skills"].lower()
        skills_list = skills_str.split(",")
        for index, skill in enumerate(skills_list):
            skills_list[index] = skill.strip()

        if skill_name in skills_list:
            approved.append(candidate)
    return approved

x = get_candidates_by_skill("go")
pass