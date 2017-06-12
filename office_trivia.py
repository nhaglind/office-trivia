# Has to be run with Python 3 -> $ python3 office_trivia.py
import random

t = """
What account can't Jim close in the first episode?; Library;
Where did Michael get his World's Best Boss mug?; Spencer Gifts;
What is Jan's full name?; Janet Levinson-Gould;
Early on, what politician does Michael say he calls Jan?; Hillary Rodham Clinton;
What is Todd Packer's nickname for Jan?; Godzillary;
What are the names of the Dunder Mifflin branches?; Stamford, Scranton**;
What is the name of the person that sent Ryan from the temp agency?; Daniqua;
Who are Michael Scott's four heroes?; Bob Hope, Bono, Abraham Lincoln, and God;
What is Pam's favorite yogurt flavor?; Mixed berry;
What kind of car does Dwight drive? How much did he buy it for?; '78 280Z, $1200;
What item of Dwight's does Jim put in Jell-O?; A stapler;
How long has Pam been engaged when the series starts?; Three years;
What does Michael accuse Pam of stealing when fires her as a joke?; Post-it Notes;
What is the name of the corporate diversity consultant?; Mr. Brown;
What two races is Dwight attracted to sexually?; White and Indian;
Whose comedy routine does Michael perform that gets people to file a complaint to corporate?; Chris Rock;
What does the diversity acronym HERO stand for?; Honesty, empathy, respect, and open-mindedness;
Who does Michael sign the diversity pledge as?; Daffy Duck;
What fraction of Native American does Michael claim to be?; 2/15;
What kind of heritage does Michael say he has?; English, German, Scottish, Irish;
What card does Michael have on his head in the race guessing game?; Martin Luther King;
What cards do everyone have in the race guessing game?; Pam - Jewish, Dwight - Asian, Stanley - Black, Oscar - Eskimo, Angela - Jamaican, Kevin - Italian, Meredith - Brazil, Phyllis - Haitian;
What show is Ryan watching on Pam's computer?; Chappelle's Show;
What does Michael call collard greens?; Colored greens;
What is Jan sure of that none of the health care plans cover?; Acupuncture;
What health figure does Dwight claim to be able to raise and lower at will?; Cholesterol;
What is it called when your teeth turn to liquid and they drip down the back of your throat?; Spontaneous dental hydroplosion;
What are some of the diseases submitted to Dwight when he asks for health information?; Killer nanorobots, flesh eating bacteria, hot-dog fingers, leprosy, Count Choculitis;
What does Dwight think is removed during a hysterectomy?; The vagina;
What medical condition does Kevin say is a "real thing" that "someone has"?; Anal fissures;
What does Michael bring to apologize for worsening the health care plan?; Ice cream sandwiches;
What color does Angela think is "kind of whore-ish"?; Green;
What does Michael suggest to get for Meredith's "morale raising" birthday party, despite her lactose intolerance?; A Baskin-Robbins mint chocolate chip ice cream cake;
What age is Meredith turning in "The Alliance"?; 46;
How much does Michael donate to Oscar's nephew's charity for cerebral palsy?; $25 (per mile);
How many times has Meredith been divorced? How many kids does she have?; Twice, two;
Where does Dwight hide to spy on one of the alliances?; In a box in the warehouse;
What color does Dwight dye his hair to go spy on Stamford?; Blonde;
What gift did Pam receive at her engagement shower that she calls about the warranty for?; Toaster oven;
What name does Michael make up to tease Dwight about his nerdiness in "Basketball"?; Elwyn Dragonslayer;
Who is the safety officer?; Angela;
Who is on the basketball team for the office?; Michael, Dwight, Phyllis, Jim and Ryan;
What does Dwight's shirt say that he wears to play basketball?; World Anime Expo, Philadelphia 2002;
Who is the warehouse worker played by Patrice O'Neal?; Lonny Collins;
What is the name of the "East German gal" that works in the warehouse?; Madge Madsen;
How does Michael end the basketball game?; By taking a "flagrant personal foul" to the face;
What basketball player does Roy sarcastically compare Jim to in "Basketball"?; Larry Bird;
What does Amy Adams' character, Katy, try to sell to the office?; Handbags;
What does Michael call Katy, in comparison to Pam?; Pam 6.0;
What magazines does Michael subscribe to?; USA Today, American Way Magazine;
What kind of coffee does Michael say he's going to bring to Kay?; Starbucks, or as he calls it "the 'bucks";
What high school did Katy and Toby go to?; Bishop O'Hara (Toby graduated in '89);
Michael says he lives by one rule: no office romances. But he also lives by what rule?; Just Do It. Nike;
How does Jim describe his "type" to Roy and Kevin?; Moms;
What kind of machine does Michael buy to impress Katy?; A Starbucks digital barista;
What colors does Angela say she likes to Katy?; Grey, dark grey, charcoal;
What flavor of power drink does Michael ask Ryan to put in his car trunk (with the unopened Arctic Chill)?; Blue Blast;
What cologne does Michael wear?; Rite Aid Midnight Swept (though he calls it Drakkar Noir);
What kind of car does Jim drive in season 1?; A Corolla;
"I mean, who's gonna give Kevin an award?"; Dunkin' Donuts;
In the video of the Dundies Pam is looking through for highlights, what song does Michael sing a parody of?; Lou Bega's Mambo No. 5;
How often does 05/05/05 happen?; Once every billion years;
What Dundie does Pam win in the video she scans for highlights?; "Longest Engagement";
What Dundie does Oscar win in the video Pam scans for highlights?; "Show Me the Money" award;
In the episode "The Dundies," which annual Dundies is it?; The 8th Annual (2005);
What is Stanley's wife's name?; Terri;
What is the name of the bar that the warehouse guys and occasionally the office staff frequent?; Poor Richard's;
What is Phyllis's maiden name?; Lapin;
What Dundie does Phyllis win in "The Dundies"?; "Busiest Beaver," though the statue reads "Bushiest Beaver";
What is the name of Michael's Asian character?; Ping;
What Dundie does Ryan win in "The Dundies"?; "Hottest in the Office";
What Dundie does Angela win in "The Dundies"?; "Tight Ass";
What Dundie does Kelly win in "The Dundies"?; "Spicy Curry";
What Dundie does Kevin win in "The Dundies"?; "Don't Go in There After Me";
What Dundie does Stanley win in "The Dundies"?; "Fine Work";
What Dundie does Pam win in "The Dundies"?; "Whitest Sneakers";
What kind of sneakers does Pam wear?; Keds;
Who is never welcome in the Chili's restaurant chain again?; Pam;
What email does Michael forward Jim in "Sexual Harassment"?; "Fifty signs your priest might be Michael Jackson";
The Office is like "Friends," Michael is Chandler and Joey, Pam is Rachel, who is Dwight?; Kramer;
What is the name of the Dunder Mifflin CFO that is forced to resign because of sexual harassment?; Randall;
What does Todd Packer's license plate read?; WLHUNG;
Which former employee does Michael claim he could've slept with?; Catherine;
What is the name of the sexual harassment video that Michael and the warehouse guys watch?; Crossing the Line: Rules for the Modern Workplace;
Dwight asks Toby where what part of human anatomy is?; The clitoris;
What is Scenario 1 in the Sexual Harassment video?; The Natural Redhead;
In "Sexual Harassment," what is the name of the corporate lawyer that Jan brings in?; O'Malley;
What is the name of the lawyer Michael brings in that specializes in "Free Speech issues" (and motorcycle head injuries, worker's comp and diet pill lawsuits)?; James P. Albiny;
What does Michael ask Ryan to come in early for in "Office Olympics"?; To bring him a sausage, egg and cheese biscuit;
Dwight says Michael is like Mozart, and he's like who?; Butch Cassidy;
Michael asks Pam to move his subscriptions to his condo for what magazines?; The Small Business Man, Maxim, American Way and Cracked;
What do Oscar and Kevin call the paper football game they play while Michael is out?; Hate Ball;
What is the name of the head of the condo association?; Bill;
How many acres is Dwight's beet farm?; 60 acres;
Which medals are the same in "Office Olympics"?; Bronze (which is blue) and Gold;
What "games" does Angela say she plays, but not at work?; She sings and she dangles things in front of her cats;
What kind of mortgage does Michael get on the condo?; Ten over thirty, ten year fixed over thirty;
What is the national sport of Icelandic paper companies?; Flonkerton, in English, box of paper snowshoe racing;
How much will Michael lose if he walks away from the condo deal?; $7,000;
Who wins Flonkerton?; Phyllis over Kevin;
What is the name of the game that Angela plays where she counts how many times Jim gets up to go to reception?; Pam Pong;
How many bedrooms does Dwight's farm house have?; 9;
What is the first of the ten rules of business?; You need to play to win, but you also have to win to play;
What is the second rule of business?; Adapt. React. Re-Adapt. Act;
What games do Jim and Pam suggest playing while they're evacuated due to the fire?; Desert Island, Who Would You Do, and Would You Rather;
What three books would Angela take to a Desert Island?; The Bible, A Purpose Driven Life, and The Da Vinci Code (so she could burn it);
What books would Dwight bring to a Desert Island?; Physician's Desk Reference (hollowed out) and Harry Potter and the Prisoner of Azkaban;
What is rule number 4 of business?; Image is everything - Andre Agassi;
What 5 movies would Meredith bring to a desert island?; Legends of the Fall, My Big Fat Greek Wedding, Legally Blonde, Bridges of Madison County and Ghost;
How much more expensive is it to sign a new customer?; Ten times;
What 5 movies would Pam bring to a desert island?; Fargo, Edward Scissorhands, Dazed and Confused, The Breakfast Club and the Princess Bride;
What is Dwight's favorite movie?; The Crow;
What object of Michael's does Dwight go into the burning office building to retrieve?; His cell phone;
What food does Ryan start the fire with?; A cheese pita;
What is the first movie Katy mentions she'd bring to a desert island?; Legally Blonde;
What is rule 5 of business?; Safety first, i.e., don't burn the building down;
What is Pam dressed as in "Halloween"?; A cat;
What is Phyllis dressed as in "Halloween"?; A cat;
What is Jim dressed as in "Halloween"?; A three-hole punch version of Jim;
Who is Jan's assistant in "Halloween" that Michael suggests firing instead of him having to let someone go?; Sherri;
What is Dwight dressed as in "Halloween"?; A Sith Lord (it cost him $129!);
What is Oscar dressed as in "Halloween"?; A woman;
Kelly is dressed as Dorothy, but Michael suggests she should've dressed as someone from what movie?; Bend it like Beckham;
What does Phyllis bring to the party in "Halloween" that causes Angela to accuse her of sabotaging her?; Brownies;
What is Michael's middle name?; Gary;
What company do Pam and Jim try to get Dwight hired at (that he sends a martial arts training supplement to his resume)?; Cumberland Mills, in Maryland;
Who is the first person Michael has Dwight try to fire in "Halloween"? Who is the first person he tries to fire himself?; Stanley, Creed;
Who does Michael end up firing in "Halloween"?; Devon;
What is Devon dressed as in "Halloween"?; A hobo;
Michael lists four "topical" costumes that he had in years prior in "Halloween." What are they?; Janet Jackson's boob, Monica Lewinsky, Monica Lewinsky (again), and O.J.;
Where does Jim move Dwight's desk in "The Fight"?; The bathroom;
What kind of discounts are Dunder Mifflin giving on the 20lb. white model?; $9.78 per ream, discounts 7%;
What kind of karate is Dwight a practitioner of?; Goju-Ryu;
What belt has Dwight been recently promoted to in "The Fight"?; Purple;
On one Friday every year, Michael has to sign time cards, expense reports and purchase orders. What does Pam call it?; The Perfect Storm;
What is the name of Jim's sister that he uses as an emergency contact?; Larisa Halpert (at 117 Mount Bergin St.);
What is Toby's wife's last name now that he's divorced?; Becker;
What movie did Dwight and Michael rent that Dwight cried at the end of?; Armageddon;
Dwight's maternal grandfather killed 20 men in World War II and spent the rest of the war in an allied prison camp, what did his father battle?; Blood pressure and obesity;
What is the name of the radio station that Dwight has a sticker on his desk for?; Froggy 101;
Michael recognizes a symbol in the dojo as being Japanese for "California Roll," what does it actually mean?; Eternal discipline;
What is the name of Dwight's sensei in "The Fight"?; Ira;
Who is Michael's emergency contact?; Todd Packer;
Who does Dwight say to put as his emergency contact?; The hospital, contact number 9-1-1;
What odd piece of clothing does Michael have dry cleaned?; His Levi Jeans;
What client are Jan and Michael trying to land in "The Client"?; Lackawanna County;
Michael changes the meeting place from where to Chili's in "The Client"?; The Radisson;
Pam describes her worst first date as being left at a minor league hockey game. Who was the date with?; Roy;
What is the name of the representative that Michael and Jan meet in "The Client"?; Christian;
What does Michael call Pam to look up in "The Client"?; Jokes;
What is the name of Michael's screenplay?; Threat Level Midnight;
What is pictured on the backside of Michael's lucky tie in "The Client"?; A mouth;
What was the part made up for Dwight in his 7th grade production of Oklahoma?; Mutey the Mailman;
What part does Phyllis play in the table read for Threat Level Midnight?; Catherine Zeta-Jones;
What is the name of Michael Scarn's old partner?; Samuel L. Chang;
Who plays the villain, Goldenface, in the table read of Threat Level Midnight?; Oscar;
Michael did a search and replace to change the name of Michael Scarn's assistant, but leaves what behind?; Dwigt;
Why did Jan divorce Gould?; She wanted kids, he didn't;
Where do Jim and Pam eat grilled cheese during the intermission of the table read of Threat Level Midnight?; The roof;
Chili's is the new what, according to Small Businessman Magazine?; Golf course;
What does Dwight call exercise balls?; Fitness orbs;
What does Dwight say Jim should ask Michael to stock more of in Jim's performance review?; Double tabbed manila file folders;
What day does Dwight think it is in "Performance Review," when it's actually Thursday?; Friday;
What is the name of the accountant that committed suicide after suggesting better care for employees with depression?; Tom;
The first suggestion in the suggestion box is a question about how to prepare for what event?; Y2K;
What kind of jerky did Dwight bring in for the whole office?; Deer;
What TV show does Dwight quote in his performance review?; Smallville;
What is the name of the IT guy that Michael instructs everyone to hide from upon first seeing him?; Sadiq;
What is Michael's password; 123;
Dwight notes that his county has a high number of what medical condition, probably because they're down river from a bread factory?; Yeast infections;
What does Michael call Battlestar Galactica when trying to get Dwight to admit that he's going to Jim's party?; Battleship Galaxy;
What kind of shoes does Dwight keep an extra set of in his car for special occasions?; Birkenstocks;
What is the name of Jim's roommate in season 2?; Mark;
According to Michael, what is the most exciting thing that can happen on TV, in movies, or real life?; Someone has a gun;
What bar does Michael's improv class go to, leaving him alone?; Bernie's Tavern;
What song does Phyllis sing at Jim's party?; Here I Go Again - Whitesnake;
What song does Kevin sing at Jim's party?; I Will Survive - Gloria Gaynor;
What duet do Michael and Jim sing at Jim's party?; Islands in the Stream - Kenny Rogers, Dolly Parton;
How did Michael find out about his improv class?; A flyer;
What does Jim get for Pam in "Christmas Party"?; A teapot filled with inside jokes;
What is the size of Michael's Christmas bonus in "Christmas Party"?; $3000;
For Secret Santa, Toby gets Angela a picture of babies playing what instrument?; Saxophone;
What does Oscar get Creed for Secret Santa?; A shamrock keychain;
Who did Kevin get for Secret Santa in "Christmas Party"?; Himself;
What does Kelly get Oscar in Secret Santa?; A shower radio;
What does Michael get Ryan in Secret Santa?; A video iPod;
What does Phyllis get Michael in Secret Santa; A handmade oven mitt;
Michael suggests turning Secret Santa into what game?; Yankee Swap;
What does Dwight get Michael for Secret Santa?; Paintballs and 2 Paintball Lessons;
How many bottles of vodka does Michael buy in "Christmas Party"?; 15;
What does Roy say he's going to get for Pam for Christmas now that she's got an iPod?; A sweater (or something);
What line of work is Bob Vance in?; Refrigeration;
What gift does Kevin get for himself for Secret Santa?; A foot bath;
How does Dwight propose he's going to use Jim's teapot?; As a neti pot;
What is the name of the vending machine guy Jim gets to put Dwight's stuff in a vending machine?; Steve;
What does Michael ask people to pack for the booze cruise?; A swimsuit, a ski mask, rubber-soled shoes, and a toothbrush;
What lake is the booze cruise on?; Lake Wallenpaupack;
What part of the ship is sales, according to Michael?; The furnace;
What is the name of the captain of the booze cruise?; Captain Jack;
What activity did Katy do in high school?; Cheerleading;
What is the name of the person from corporate on the booze cruise?; Brenda;
What does the captain of the ship have Dwight pretend to do (though he doesn't know it's pretend)?; Steer the ship;
What military operation was Captain Jack in?; Desert Storm;
What day does Roy suggest setting for his and Pam's wedding?; June 10th;
What kitchen appliance does Michael burn his foot on?; A George Foreman grill;
What smell does Michael like waking up to?; Bacon;
What does Dwight run in to with his car after hearing that Michael's been injured?; A pole;
What does Michael wrap his burned foot in?; Bubble wrap;
Ryan brings Michael creamed spinach with his chicken and cornbread instead of what?; Yams (the one in Stroudsberg always has yams);
What music player does Roy get for Pam instead of an iPod?; A Prism Duro-Sport;
What does Michael ask Pam to rub on his burned foot?; Country Crock butter;
What back condition did Phyllis have as a young girl?; Scoliosis;
What did Creed claim to be in as a teenager when Michael asks about disabilities?; An iron lung;
When Michael puts up disabled icons on the wall, what actor is up there twice?; Tom Hanks;
Michael claims to have put up a picture from Philadelphia, what movie is it actually from?; Big;
What is the name of the disabled properties manager?; Billy Merchant;
Where does Ryan find the pudding cups that Michael wanted?; A gas station in Carbondale;
What does Ryan grind up and put into Michael's pudding?; 4 extra-strength aspirin;
Where does Jim tell Dwight that they're going when he's driving him to the hospital?; Chuck E. Cheese;
What is Dwight's middle name?; Kurt;
What medical procedure does Dwight undergo after having a concussion?; A CAT scan;
What month is spring cleaning?; January;
What kind of drink does Michael get for Stanley in the vending machine knowing that he'll "hate it"?; Peach iced tea;
Where does Michael take Jim for lunch when Jim is trying to get him to keep a secret about Pam?; Hooters;
What does Michael end up ordering at Hooters?; The gourmet hotdog;
What is the name of the server at Hooters?; Dana;
What is the name of Oscar's boyfriend Dwight discovers as he's investigating Oscar's sick leave?; Gil;
What Cinemax movie does Michael reference when he says that he doesn't want to keep secrets?; More Secrets of a Call Girl;
Where do Pam and Roy go on vacation?; The Poconos;
Who was the manager of the office before Michael?; Ed Truck;
Dwight is calling Rock 107 to win what band's box set?; Jethro Tull;
Who is responsible for what happens to Michael's carpet?; Todd Packer;
What is the "math equation" Michael puts on the warehouse board to see if there's a "Good Will Hunting" situation?; 13579/8724;
What is Meredith's five year goal?; To be five years sober (well, four and a half);
What branch unionized and was shut down?; Pittsfield;
According to Michael, what food is the great equalizer?; Pizza (Do black people like pizza?);
What does Angela get Dwight for Valentine's Day in "Valentine's Day"?; A bobble head of himself;
On what day do Ryan and Kelly hook up for the first time?; February 13th;
What is Michael's favorite New York pizza joint?; Sbarro;
Who does Michael say founded Rockefeller Center?; Theodore Rockefeller;
What celebrity walks by Michael when he thinks he sees Tina Fey?; Conan O'Brien;
What is name of the CFO after Randall?; David Wallace;
What is the video presentation called that Michael shows to David Wallace?; The Faces of Scranton;
What prize does Jim get for being 9th best salesman?; Cugino's Pizza;
Who was the other finalist in Dwight's 6th grade Spelling Bee?; Raj Patel;
Pam doesn't want what color invitations for her and Roy's wedding?; Orange;
Who does Dwight say got in an accident on 84 West to get the attention of the office?; Brad Pitt;
Where in Europe did Toby go after his divorce?; Amsterdam;
Jim gives Dwight a speech from what dictator?; Benito Mussolini;
Where do Roy and Pam plan to have their wedding reception?; The V.A.;
What temperature does Oscar set the thermostat to?; 66;
What temperature does Kevin set the thermostat to?; 69;
What is the one thing Roy is in charge of for his and Pam's wedding?; Music;
What kind of sandwich does Jim eat everyday for lunch?; Ham and cheese;
If Dwight could travel anywhere in the world, where would he go?; New Zealand (he can't go to Cuba);
Where does Creed suggest Jim should travel to?; Hong Kong;
Oscar suggests Jim could use his time share where?; Key West;
Where does Jim book a ticket to, leaving on June 8th, before Pam's wedding?; Australia;
Michael says on Take Your Daughter to Work Day that he's like Eddie Murphy in Raw, but that the office wants him to be like Eddie Murphy in what movie?; Daddy Daycare;
What is the name of Toby's daughter?; Sasha;
What is the name of Kevin's fiancee?; Stacy;
What is the name of Kevin's fiancee's daughter?; Abby;
What is the name of Stanley's daughter that he brings to Take Your Daughter to Work Day?; Melissa, she's in 8th grade;
What is the name of Meredith's younger son?; Jake;
What book is Abby reading on Take Your Daughter to Work Day?; From the Mixed-Up Files of Mrs. Basil E. Frankweiler;
What name does Jake, Meredith's son, call Dwight?; Mr. Poop;
Sasha, Toby's daughter, asks Phyllis if she's what children's character?; Mother Goose;
What coffee place does Stanley's daughter suggest to Ryan?; Jitters at the Steamtown Mall;
What song does Dwight play for the kids on Take Your Daughter to Work Day?; Greensleeves;
Creed tries to show the kids what body part on Take Your Daughter to Work Day?; His four-toed foot;
What kids show was Michael on as a boy?; Fundle Bundle;
Where does Michael's mother live?; Dickson City;
Who is the host of Fundle Bundle?; Miss Trudy;
What is the name of the cat puppet on Fundle Bundle?; Edward R. Meow;
What is the name of the now weatherman who was on Fundle Bundle with Michael?; Chet Montgomery;
What username does Michael say he's going to use for online dating sites?; Little kid lover;
What song do Dwight and Michael sing at the end of Take Your Daughter to Work Day?; CSNY - Teach Your Children;
Michael gets involved in a pyramid scheme to sell what?; Calling cards;
Michael shares a birthday with what actress (he has a perfect icebreaker for when he meets Teri Hatcher)?; Eva Longoria;
What does Michael want on his cake for his birthday?; Trick candles;
What condition is Kevin waiting to hear about on Michael's birthday?; Skin cancer;
Kelly never thought about death until who died?; Princess Diana;
Michael's mother rubbed cream on him for 3 hours after he got a rash from what animal brought to his birthday?; A pony;
Dwight plays what song for Michael on the recorder for his birthday?; Billy Joel - For the Longest Time;
What time was Michael born?; 11:23 AM (on March 15th);
Dwight orders an 8 ft. sub for Michael's birthday. What does he get instead?; 8 1-foot subs;
Dwight doesn't tip delivery people, taxi drivers, or hairdressers. Who did he tip?; His urologist;
What kind of sub sandwich does Dwight get the office for Michael's birthday?; Bologna, tomato and ketchup;
What is Kevin's favorite movie?; American Pie 2;
Where does Michael take the office for his birthday (and also for Kevin's skin cancer)?; An ice skating rink;
Dwight gets Michael a hockey jersey for his birthday that says what on the back?; "From Dwight";
Creed identifies a picture of marijuana as what strain?; Northern Lights Cannabis Indica;
Who did Michael go to see at the Montage Mountain Performing Arts Center?; Alicia Keys;
According to Michael, this year more people will use cocaine than do what?; Read a book to their children;
Every morning, Dwight's father would wake up at dawn to make him what breakfast?; Biscuits and gravy;
What is the name of the security officer at the office?; Hank;
Pam doesn't want to invite Angela to her and Roy's wedding because Angela has called her what?; A hussy;
Where does Michael get his hair cut?; Fantastic Sam's;
What does Oscar file a complaint about to HR about Angela?; Her baby poster;
What is the 5th style of conflict resolution?; Win/win/win;
Who complained to HR that the men's room is whites only?; Creed;
Ryan complains that Creed has a distinct old man smell - what does Creed claim it's from?; Sprouting mung beans;
What middle name is put down for Dwight on his company ID badge?; Fart;
What coin did Jim put in Dwight's phone handset to confuse him about the weight?; Nickels;
Jim puts a macro in Dwight's computer to have Dwight autocorrect to what?; Diapers;
What does Jim make move with his mind control?; A coat rack;
What organization does the Casino Night benefit?; Boy Scouts of America;
What organization does Michael say he wants his money to go to if he wins at Casino Night? What does he change it to?; Comic Relief, Afghanistanis with AIDS;
According to Michael, what topics are off-limits for comedians?; AIDS, JFK and the Holocaust (the Lincoln assassination only recently became funny);
Who is catering Casino Night?; Hooters;
What company is Dunder Mifflin leasing the office from?; Beakman Properties;
What phrases does Darryl teach Michael to help with interracial conversations?; "Dinkin' Flicka," "Fleece it Out," and "Going Mach Five";
What is the name of Kevin's Police cover band?; Scrantonicity;
What is the full name of the realtor Michael dates?; Carol Stills;
Dwight establishes codenames for Carol and Jan at Casino Night, what are they?; Re/Max and Lan Jevinson;
Where did Billy, the property manager, meet his girlfriend?; Chili's;
Michael goes all-in on the first hand of hold 'em - who calls his bluff?; Toby;
What drink does Ryan get for Kelly at Casino Night?; A 7 and 7 with 8 maraschino cherries with sugar on the rim;
Kevin won a Tournament at the World Series of Poker in Vegas in what year?; 2002;
Who does Kevin lose to in poker during casino night?; Phyllis;
Who wins the mini-fridge at Casino Night?; Creed;
Whose Job does Ryan get at the start of season 3?; Jim;
What does Michael call everyone in the office that Oscar finds offensive?; "Faggie";
Michael calls Oscar "faggie" for liking what movie more than Die Hard?; Shakespeare in Love;
What is Andy's nickname for Jim?; Big Tuna;
What is the name of Andy's college acapella group?; Here Comes Treble;
Where did Andy go to college?; Cornell;
How does Dwight tell if someone is gay?; Whether they're dressed in women's clothes;
Where does Jim suggest Dwight could buy a gay-dar?; Sharper Image;
What did Stanley get for Roy and Pam's wedding that he can no longer return?; A toaster;
What item of Andy's does Jim put in Jell-O?; Calculator;
Who does Michael think might be having a gay affair?; Oscar and Angela;
What does Jan offer Oscar after Michael kisses him?; A 3 month paid vacation and a company car;
What does Jim send Dwight as a "gay-dar"?; A metal detector;
What is the name of Jim's boss at Stamford?; Josh Porter;
What does Michael call a booze-fueled sex romp where anything goes?; The Annual Northeastern Mid-Market Office Supply Convention;
What job does Kelly's neighbor Alan have (whom she set up with Pam)?; Cartoonist for the local paper;
What does SWAG stand for?; Stuff we all get;
What football player does Michael invite to his party at the convention?; Jerome Bettis;
What room number does Michael have at the convention?; 308 - it's close to the elevator;
What state is the Stamford branch in?; Connecticut;
What company's products does Michael get a deal for at the convention?; HammerMill;
When Angela shows up at the convention for Dwight, who does Jim think she is?; A prostitute;
What movie does Michael show the office to cure the "Monday blues"?; Varsity Blues;
What video game do people in the office at Stamford play?; Call of Duty;
When Jim and Pam would both hum the same high-pitched note, what did Pam call it?; Pretendenitus;
Where does Dwight ask Jan to meet him to talk about Michael?; A Liz Claiborne outlet;
What name does Dwight make up for his fake dentist?; Crentist;
What kind of car does Michael drive?; A Sebring;
What do men say to each other after a fight, according to Michael?; Hug it out, bitch;
How does Michael punish Dwight for trying to execute a coup?; He has to do Michael's laundry for a year;
What kind of chips does Jim make a large effort to get for Karen?; Herr's chips;
How did Ed Truck die?; Decapitation;
What store number does Jim say for the West Side Market when he's trying to get salt and vinegar chips?; Six;
Where does Jim ultimately get the chips for Karen?; The building next door;
What song does Pam sing for the bird funeral?; On the Wings of Love - Jeffrey Osborne;
Where does Dwight take Ryan for his first sales call?; Schrute Farm;
What song does Jim sing to the sound of his squeaky chair?; Lovefool - The Cardigans;
How many different toppings do they have at the pretzel cart?; 18;
According to Dwight, what is the greatest danger facing Dunder-Mifflin?; Flash floods;
According to Dwight, what is the true cause of Robert Mifflin's suicide?; He hated himself;
According to Dwight, what is Michael Scott's greatest fear?; Nothing, also snakes;
How many words per minute does Jim type? Pam?; 65, 90;
What movie does Pam confuse with 28 Days?; 28 Days Later;
How many days until the next Pretzel Day?; 364;
What does Michael say is essentially a "Hindu Halloween"?; Diwali;
What does Carol dress up as for Diwali, thinking its a costume party?; A cheerleader;
What does Michael mistake for s'mores at Diwali?; Samosas;
What are the names of Kelly's sisters?; Rupa, Nipa, Tiffany;
On what date does Michael propose to Carol?; The ninth;
What Indigo Girls song do Jim and Andy sing together at Stamford on form consolidation day?; Closer to Fine;
What song does Michael sing a parody of at Diwali?; The Chanukah Song;
Jim faxes Dwight as Future Dwight warning him that what is poisoned?; Coffee;
What does Ryan receive in the mail on the day he hears that Scranton branch is to be shut down?; 1,000 business cards;
How does Dwight have David Wallace's home address?; Christmas card list;
Michael thought that Bowling for Columbine was going to be like what bowling movie?; Kingpin;
Josh leaves Dundler-Mifflin to work a senior management position for whom?; Staples;
How did Michael haze Dwight on his first day?; He sprayed him with a fire extinguisher;
How fast can Toby run a mile?; In about 7 minutes;
Dwight estimates his speed as between what three animals?; Snake, mongoose and a panther;
What is Karen's full name?; Karen Filippelli;
Besides Karen and Jim, who are the other three employees that transfer from Stamford?; Tony Gardner, Hannah Smoterich-Barr, and Martin Nash;
"They call it Scranton. What?"; The Electric City;
While watching Lazy Scranton, Jim recalls watching his orientation video of what name?; The Scranton Witch Project;
Scranton has a museum for what kind of coal?; Anthracite;
On merger day, what song do Andy and Michael sing together?; Haddaway - What is Love;
Who is fired on the merger day, and why are they fired?; Tony Gardner, because he tried to quit;
What kind of car does Dwight start driving in season 3?; A Trans Am;
What kind of car does Andy drive?; An XTerra;
Who from Stamford is the ex-convict and what was he in prison for?; Martin Nash, insider trading;
What black guy does Michael trust more than Pam's mom?; Danny Glover;
What black guy does Michael trust more than Justin Timberlake?; Colin Powell;
What black guy does Michael trust more than Jesus?; Apollo Creed;
What do they serve in prison according to Michael?; Gruel;
According to Michael, what is the worst thing about prison?; The Dementors;
What song does Andy sing to Pam in a sexy falsetto voice in an attempt to woo her?; The Rainbow Connection;
What kind of roadkill does Dwight bring to the office for Christmas?; A goose;
Why does Carol break up with Michael?; He Photoshops himself into a picture with her and her two kids on a ski trip;
What does Michael put into the gift box for kids?; His old bike;
What gift does corporate give everyone in "A Benihana Christmas"?; Bathrobes;
What snippet of a song does Michael keep replaying when Carol breaks up with him?; Goodbye My Lover - James Blunt;
In "A Benihana Christmas," Angela now claims what color is whore-ish?; Orange;
What is Angela's theme for the Christmas party in season 3?; "A Nutcracker Christmas";
What party planning splinter group do Karen and Pam form?; The Committee to Plan Parties;
What does Michael call Benihana?; Asian Hooters;
How do you make a noga-sake?; One part eggnog, three parts sake;
Dwight claims that the Nakiri knife is better than what knife the Benihana chef is using?; Usuba;
Angela hasn't talked to her sister in how many years?; 16;
What is the name of the waitress Michael brings to the Christmas Party?; Cindy;
What song do Michael and Andy sing for karaoke in "A Benihana Christmas"?; John Mayer - Your Body is a Wonderland;
What song does Kelly sing for karaoke in "A Benihana Christmas"?; Pat Benatar - We Belong;
What movie does Jim get Karen for Christmas?; Bridget Jones' Diary;
What song does Angela sing for karaoke in "A Benihana Christmas"?; Little Drummer Boy;
Where does Michael take Jan for Christmas vacation?; Sandals, Jamaica;
What German woman's name does Michael make up to cover up the fact that he was with Jan in Jamaica?; Urkel Grue;
What is the name of the picture of Jan in Jamaica that Michael sends to packaging@DunderMifflin.com?; Jamaican Jan Sun Princess;
What hotel is Karen staying at in Scranton until she finds a place?; A Day's Inn;
What is the name of Jan's psychiatrist?; Dr. Perry;
What is the name of Michael's computer-voiced "friend"?; Harvey;
What are the partnerships in the Traveling Salesman episode?; Karen/Phyllis, Michael/Andy, Jim/Dwight, Ryan/Stanley;
Andy knows how to fold laundry from his time working at what clothing store?; Abercrombie;
How many attacks out of ten are from the rear?; 7;
When he drops off the tax forms for Angela in New York, what does Dwight write under "State Your Business"?; Beeswax. Not Yours, Inc.;
When Dwight is forced to quit, he gives Michael all of his desk items except what?; His bobbleheads;
Dwight breaks his resume into three parts (for convenience!) - what are they?; Professional, Athletic and Special Skills, and Dwight Schrute trivia;
How would Dwight describe himself in three words?; Hard-working, alpha male, jackhammer, merciless, insatiable;
Where does Dwight get a job after he is forced to quit Dunder-Mifflin?; Staples;
What song does Andy record himself singing all four parts to?; Rockin' Robin;
Who watered the plant in the office?; Dwight;
What is the name of the anger management counselor Andy meets with?; Marcy;
What is the name of the sales associate Dwight works with at Staples?; Paris;
Michael refers Jim to a strip club called Banana Slings to get a male stripper - instead he calls the Scholastic Speakers of Pennsylvania and gets an impersonator of whom?; Ben Franklin;
What is the name of the stripper that Dwight gets for Bob Vance's bachelor party?; Elizabeth;
What is the name of the Ben Franklin impersonator who definitely does not have syphillis?; Gordon;
What gift do Stanley and Karen both get Phyllis for her wedding?; A toaster;
Schrutes marry standing in their own what?; Graves;
Dwight saw Wedding Crashers accidentally after buying a ticket for what movie?; Grizzly Man;
What color does Kelly wear to Phyllis' wedding?; White;
What is the name of Phyllis' dad?; Albert;
Who goes missing at Phyllis' wedding?; Uncle Al;
In a wedding toast, Michael says Phyllis' nickname back in high school was what?; Easy Rider;
What is Pam and Roy's song?; Jewel - You Were Meant For Me;
Who gets the bouquet at Phyllis' wedding?; Toby's date;
What business class of Ryan's does Michael go to give a guest lecture at?; Emerging Enterprises;
What was the name of Michael's 8th grade teacher that hung out with kids, told awesome jokes... and molested 12 of them?; Mr. Handell;
What piece of advice changed Dwight's life?; "Don't be an idiot";
"""

class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
trivia = []

t = t.split("\n")
for q in t:
    temp = q.rstrip(";")
    temp = temp.split("; ")
    try:
        trivia.append(Question(temp[0],temp[1]))
    except IndexError:
        continue

trivia_bad = []

def serveQuestion():
    global trivia, trivia_bad
    random.shuffle(trivia)
    print("\n" + trivia[0].question)
    input()
    print(">>> " + trivia[0].answer)
    if set_follow == "Y" or set_follow == "y":
        check_right = input("\nDid you get it right? Y or N? ")
        if check_right != "Y" or check_right != "y":
            trivia_bad.append(trivia[0])
            trivia.remove(trivia[0])
        else:
            trivia.remove(trivia[0])
    else:
        trivia.remove(trivia[0])

def startQuestions(trivia_ary):
    global trivia, trivia_bad
    total = len(trivia_ary)
    while len(trivia_ary) > 0:
        serveQuestion()
    wrong = len(trivia_bad)
    if set_follow == "Y":
        print("You got " + str(((total - wrong)/total)*100) + "% of questions (" + str(total - wrong) + "/" + str(total) + ") right. Now we'll review the ones you got wrong.")
        trivia = trivia_bad
        trivia_bad = []
        startQuestions(trivia)

print("OFFICE TRIVIA: Press ENTER to see answers.\n")
set_follow = input("Track responses? Y/N? ")
startQuestions(trivia)
