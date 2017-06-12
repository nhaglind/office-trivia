var questions = [

"What account can't Jim close in the first episode?",
"Where did Michael get his World's Best Boss mug?",
"What is Jan's full name?",
"Early on, what politician does Michael say he calls Jan?",
"What is Todd Packer's nickname for Jan?",
"What are the names of the Dunder Mifflin branches?",
"What is the name of the person that sent Ryan from the temp agency?",
"Who are Michael Scott's four heroes?",
"What is Pam's favorite yogurt flavor?",
"What kind of car does Dwight drive? How much did he buy it for?",
"What item of Dwight's does Jim put in Jell-O?",
"How long has Pam been engaged when the series starts?",
"What does Michael accuse Pam of stealing when fires her as a joke?",
"What is the name of the corporate diversity consultant?",
"What two races is Dwight attracted to sexually?",
"Whose comedy routine does Michael perform that gets people to file a complaint to corporate?",
"What does the diversity acronym HERO stand for?",
"Who does Michael sign the diversity pledge as?",
"What fraction of Native American does Michael claim to be?",
"What kind of heritage does Michael say he has?",
"What card does Michael have on his head in the race guessing game?",
"What cards do everyone have in the race guessing game?",
"What show is Ryan watching on Pam's computer?",
"What does Michael call collard greens?",
"What is Jan sure of that none of the health care plans cover?",
"What health figure does Dwight claim to be able to raise and lower at will?",
"What is it called when your teeth turn to liquid and they drip down the back of your throat?",
"What are some of the diseases submitted to Dwight when he asks for health information?",
"What does Dwight think is removed during a hysterectomy?",
"What medical condition does Kevin say is a \"real thing\" that \"someone has?\"",
"What does Michael bring to apologize for worsening the health care plan?",
"What color does Angela think is \"kind of whore-ish\"?",
"What does Michael suggest to get for Meredith's \"morale raising\" birthday party, despite her lactose intolerance?",
"What age is Meredith turning in \"The Alliance\"?",
"How much does Michael donate to Oscar's nephew's charity for cerebral palsy?",
"How many times has Meredith been divorced? How many kids does she have?",
"Where does Dwight hide to spy on one of the alliances?",
"What color does Dwight dye his hair to go spy on Stamford?",
"What gift did Pam receive at her engagement shower that she calls about the warranty for?",
"What name does Michael make up to tease Dwight about his nerdiness in \"Basketball\"?",
"Who is the safety officer?",
"Who is on the basketball team for the office?",
"What does Dwight's shirt say that he wears to play basketball?",
"Who is the warehouse worker played by Patrice O'Neal?",
"What is the name of the \"East German gal\" that works in the warehouse?",
"How does Michael end the basketball game?",
"What basketball player does Roy sarcastically compare Jim to in \"Basketball\"?",
];

var answers = [

"Library",
"Spencer Gifts",
"Janet Levinson-Gould",
"Hillary Rodham Clinton",
"Godzillary",
"Stamford, Scranton**",
"Daniqua",
"Bob Hope, Bono, Abraham Lincoln, and God",
"Mixed berry",
"'78 280Z, $1200",
"A stapler",
"Three years",
"Post-it Notes",
"Mr. Brown",
"White and Indian",
"Chris Rock",
"Honesty, empathy, respect, and open-mindedness",
"Daffy Duck",
"2/15",
"English, German, Scottish, Irish",
"Martin Luther King",
"Pam - Jewish, Dwight - Asian, Stanley - Black, Oscar - Eskimo, Angela - Jamaican, Kevin - Italian, Meredith - Brazil, Phyllis - Haitian",
"Chappelle's Show",
"Colored greens",
"Acupuncture",
"Cholesterol",
"Spontaneous dental hydroplosion",
"Killer nanorobots, flesh eating bacteria, hot-dog fingers, leprosy, Count Choculitis",
"The vagina",
"Anal fissures",
"Ice cream sandwiches",
"Green",
"A Baskin-Robbins mint chocolate chip ice cream cake",
"46",
"$25 (per mile)",
"Twice, two",
"In a box in the warehouse",
"Blonde",
"Toaster oven",
"Elwyn Dragonslayer",
"Angela",
"Michael, Dwight, Phyllis, Jim and Ryan",
];

var magicQuestion = questions[0];
var magicAnswer = answers[0];

function getQuestion () {
  var magicNumber = Math.floor(Math.random() * questions.length);
  magicQuestion = questions[magicNumber];
  magicAnswer= answers[magicNumber];
}

function swapQuestion() {
  getQuestion();
  var questionStr = document.getElementById("displayQuestion").innerHTML;
  var answerStr = document.getElementById("displayAnswer").innerHTML;
  var newquestionStr = magicQuestion;
  var newanswerStr = magicAnswer;
  document.getElementById("hidden").style.display = 'none';
  document.getElementById("displayQuestion").innerHTML = newquestionStr;
  document.getElementById("displayAnswer").innerHTML = newanswerStr;
}

function showAnswer() {
  document.getElementById("hidden").style.display = 'block';
}
