import json

text = """
"""

questions = []
answers = []

text = text.split("\n")
for p in text:
    pair = p.rstrip(";")
    pair = pair.split("; ")
    try:
        questions.append(pair[0])
        answers.append(pair[1])
    except IndexError:
        continue

f = open("sanitized_office.txt", "w")
print("questions=", file=f)
json.dump(questions, f)
print("\nanswers=", file=f)
json.dump(answers, f)
f.close()
