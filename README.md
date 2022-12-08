# Wordle

This is an implementation of Wordle terminal game written in Python. It was a final project for a ReDI Digital Women Programm - Coding Fundamentals Course.

## What is ReDI?

[ReDI School of Digital Integration](https://www.redi-school.org/) is a non-profit tech school providing access to free digital education. From ReDI Website: *Since 2016, we offer a variety of courses; from Computer Basics to more advanced tech courses. Additionally, we offer a unique career program incl. mentorship, career workshops, company visits, job matching and much more. A semester takes 3-4 months (part time) and the teachers are volunteer tech experts.* Check them out and support!

## What is wordle?

Wordle is a daily puzzle word-game. The original version can be playd [here](https://www.nytimes.com/games/wordle/index.html). This version has been adapted visually (red squares instead of grey ones) due to colorama colour constrains.

## How to play wordle?

* Guess the 5 letter word (wordle) in 6 tries
* If you guess the word, all letters are green, you won.
* If you guess wrong, you get hints based on the wordle (word to guess):
	- A green hint is displayed if the letter in your guess is also in the wordle and at the same position.
	- A yellow hint is displayed if the letter in your guess is also in the wordle but at the wrong position
	- If the letter in your guess is not in the wordle - a red hint is displayed.
* If you have not guessed the word after 6 tries, you lost.
* If you have not guessed the word after 6 tries, the wordle is revealed.

## Credits
Thanks to all the ReDI teachers!\
The words lists come from:\
[cfreshman/wordle-nyt-allowed-guesses.txt](https://gist.github.com/cfreshman/40608e78e83eb4e1d60b285eb7e9732f)\
[cfreshman/wordle-nyt-answers-alphabetical.txt](https://gist.github.com/cfreshman/a7b776506c73284511034e63af1017ee)