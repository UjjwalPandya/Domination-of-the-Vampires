# Domination of the Vampires
About the game:
“Domination of the Vampires” is a simple board game in which you will be the “Hunter” who is on a mission to kill the Vampires with the help of the God of Traps, “Silas”.


Rules of the game:
1.	The objective of the game is to kill all the vampires by making their experience = 0 xp.
2.	Silas is the “God of Traps” who is going to allow you to create obstacles by using your experience.
3.	You will be assisted by your old friends on friend space which might get you to earn more xps.
4.	It is up to you, how you deal with fighters, boxers, and police.
5.	If the vampires move ahead of you, they might have set trap for you. 
6.	Opportunities are set by Silas which might get you to earn or lose xps.
7.	You can get out of Jail by...
a)	Escaping the Jail: Throwing doubles on any of your next three turns, if you succeed in doing this you immediately move forward the number of spaces shown by your doubles throw. Even though you had thrown doubles, you do not take another turn.
b)	The help of Silas: Using the "Get Out of Jail Free Card"
c)	Risking your life to vampires: Purchasing the "Get Out of Jail Free Card" from another player and playing it.
d)	Bribing the officer: Paying 50 xp before you roll the dice on either of your next two turns. If you do not throw doubles by your third turn, you must pay the 50 xp fine. You then get out of Jail and immediately move forward the number of spaces shown by your throw.
8.	No man’s land is just a resting place.
9.	If you clear the evidence, you will get half the xps back from Silas which you spent on the obstacles.


Summary:
We were instructed to ideate an original board game with proper logic and functioning. We had help from the instructor throughout the project which helped a lot through the process. To make the game I used the usual approach of first decomposing the problem and then going ahead solving them, which made the problem much more approachable. After decomposing the problem, I researched the packages that I can use and then realized that I do not need any packages, so I went ahead to write the code.
 
Decomposition of Problem:
1.	Complete the ideation and conceptualising of your game.
2.	Create a rough plan for your game by analysing the concept.
3.	Define how your game is going to work.
4.	Define the rules of the game.
5.	Create a prototype of your idea.
6.	Developing a logic of your game.
7.	Doing proper research about the technical requirements of your game.
8.	Properly arrange your code so that it works.


Pattern Recognition:
After properly studying all the decomposed problems and the logic of the game I realized that the logics in my game are repetitive, like every time questions with similar answers have been asked. This logic has been repeated in every question.


Algorithm:
1.	First called the random and sys function to serve the purpose.
2.	Created a class called ‘Snag’ to create obstacles at relevant places.
3.	Defined other useful classes which are required for each space(title).
4.	Created cards to assist player in uncertain conditions.
5.	Created a class called ‘Player’ to define the addition of obstacles and similar purposes.
6.	Created a class called ‘Board’ to define all the locations (tiles) of the board and player’s move and addressing where to create obstacles on the board.
7.	Defined ‘premove’ to handle the player escape from jail and clearing evidences.
8.	Defined ‘main’ function to direct the flow of the game with welcome message, rules, selection of opponents and playing the game.


Abstraction:
We do not have to concentrate on the broad concept of the game as it can make us confused. We just need to follow the decomposition of the game that we have done, i.e., focus on smaller sub problems and solving them in sequence as they are based on the main logic of the game which has been derived from the concept of the game.
 
Code design:
The code has been designed in a very basic manner and is easy to understand, every process is clearly explained and performed, every part of the code is interconnected to each other. And the user defined functions have been named such that their function can be understood just by looking at the name.


Logics:
1.	A random character from the list will be selected based on the user’s input.
2.	It will ask every time to create obstacle at the relevant places after each move.
3.	If already created an obstacle, it will ask every time to clear the evidence and return half the original value of the obstacle before each move.
4.	Game will over if any player lost all the xps. 
