import json
import os

file_ary = []
text = ""
for filename in os.listdir("."):
    if filename.endswith(".txt"):
        file_ary.append(filename)
for fname in file_ary:
    with open(fname, 'r') as f:
        text += f.read()

questions = []
answers = []

text = text.split("\n")
for p in text:
    pair = p.rstrip(";")
    pair = pair.split("; ")
    try:
        answers.append(pair[1])
        questions.append(pair[0])
    except IndexError:
        continue


f = open("../office_trivia.js", "w")
print("var questions=", file=f)
json.dump(questions, f)
print(";\n\nvar answers=", file=f)
json.dump(answers, f)
print(""";\n\nvar magicQuestion = questions[0];
var magicAnswer = answers[0];
var replacement = false;

function getQuestion () {
  var magicNumber = Math.floor(Math.random() * questions.length);
  magicQuestion = questions[magicNumber];
  magicAnswer= answers[magicNumber];
  return magicNumber;
}

function swapQuestion() {
    var newquestionStr = "";
    var newanswerStr = "";
    if (questions.length > 0) {
      var mn = getQuestion();
      if (replacement == false) {
        questions.splice(mn, 1);
        answers.splice(mn, 1);
      }
      newquestionStr = magicQuestion;
      newanswerStr = magicAnswer;
    } else {
      newquestionStr = "You've reached the end!";
      newanswerStr = "Go home!";
    }
    document.getElementById("hidden").style.display = 'none';
    document.getElementById("displayQuestion").innerHTML = newquestionStr;
    document.getElementById("displayAnswer").innerHTML = newanswerStr;
}

function showAnswer() {
  document.getElementById("hidden").style.display = 'block';
}""", file=f)
f.close()
