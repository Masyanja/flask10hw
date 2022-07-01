from flask import Flask
import json
with open("candidates.json") as f: #открываем и читаем файл
    candidates_json = json.load(f) #записываем в переменную candidates_json

print(candidates_json)#проверка, что в переменной
print(candidates_json[1])#по первому словарю
print(candidates_json[2]["position"])

app = Flask(__name__)

@app.route("/")
def page_index():
    output_string = '<pre>'
    for candidate in candidates_json:
        output_string+=('Имя кандидата -'+candidate['name'] + '\n'+candidate['position']+ '\n'+candidate['skills']+'\n\n')
    print(output_string)
    return output_string+'<pre>'

@app.route("/candidates/<int:uid>")
def page_candidate(uid):
    output_string = ''
    for candidate in candidates_json:
        if candidate['id'] == uid:
            output_string += ('<img src = "'+candidate['picture']+'">')
            output_string+=('<pre>'+'Имя кандидата -'+candidate['name'] + '\n'+candidate['position']+ '\n'+candidate['skills']+'\n\n')
    print(output_string)
    return output_string+'<pre>'

@app.route("/skills/<x>")
def page_skills(x):
    output_string = '<pre>'
    for candidate in candidates_json:
        if x in candidate['skills'].lower():
            output_string+=('Имя кандидата -'+candidate['name'] + '\n'+candidate['position']+ '\n'+candidate['skills']+'\n\n')
    print(output_string)
    return output_string+'<pre>'

app.run()