# Swed News

Swedish News Hub is an online platform that offers the latest news updates from Sweden. It allows users to read news articles and actively engage with the content through comments and likes.

Additionally, the Code Institute hosts various Python-based projects on their mock terminal platform on Heroku, providing a diverse range of educational and interactive experiences.

 [View the live site here](https://swed-news-cf4db223443b.herokuapp.com/)

![Mockup](docs/readme_images/mockup.jpg)

## Description

Swed News, is a go-to platform for comprehensive insights on Sweden. The user can explore a diverse range of topics, personalize news feed, and engage with a vibrant community. Trust in our accurate and unbiased reporting to enhance understanding of Sweden. Users have the option to register for an account, and anyone is welcome to subscribe to our email newsletter.

## Features 

### Navigation Section

* The navigation here is visible to all users before the user sign in, it includes:
  * Home  
  * Register
  * Login

![Nav Before](docs/readme_images/nav-before.jpg)

* The navigation here is exclusively visible to logged-in users and includes:
  * Home  
  * Logout

![Nav After](docs/readme_images/nav-after.jpg)

* Home
  * This will lead to the landing page containing all the essential information.

![Home](docs/readme_images/home.jpg)

* Register
  * This will redirect the user to the registration page where they can input all the necessary information to create an account.

![Register](docs/readme_images/register.jpg)

* Login
  * This will direct the user to the login page, where they can enter their details to access the functions available for logged-in users.

![Login](docs/readme_images/login.jpg)

* Logout
  * This will direct the user to the logout page, allowing them to log out from the system.
  
![Logout](docs/readme_images/logout.jpg)

### Message Notification

* Message notifications deliver important information to users when they take significant actions. For instance, these messages will appear briefly for 2.5 seconds few exampels:
  * Signing in or out  
  * Entering their email to subscribe
  * Entering their email to subscribe while they already did

![Sign In](docs/readme_images/sign-in.jpg)

![Sign Out](docs/readme_images/sign-out.jpg)

![Already Subscribed](docs/readme_images/already-subscribed.jpg)

### Newsletter Subscription

* Newsletter subscription enables users to enter their email address to subscribe and receive the latest news updates from Swed News.
  
![Newsletter](docs/readme_images/newsletter.jpg)

### Footer

* The footer contains a variety of information which include:
  * Quick links  
  * Newsletter subscription
  * Social media links
  * Contact email
  
![Footer](docs/readme_images/footer.jpg)

### Posting and Liking Comments

* Below, there are two types of users: one who is signed in, allowing them to post, like comments, and interact with posts, while the other type can only read the posts, but they can see the number of likes each post has.
  
![Post 1](docs/readme_images/post-1.jpg)

![Post 2](docs/readme_images/post-2.jpg)

* Signed-in users can post comments, but their comments require approval from the admin before they are published.

![Approval](docs/readme_images/approval.jpg)



### Future Features 

* Allow player to select categories
* Give more chances for the player

## Technologies

* Python
    * The Website was animated using custom Python in an external file.    
* GitHub
    * Source code is hosted on GitHub and delpoyed using Git Pages.
* Git 
    * Used to commit and push code during the development opf the Website
* Heroku
    * Source code is hosted on Heroku and delpoyed.
* Tinyjpg
    * https://tinyjpg.com/ was used to reduce the size of the images used throughout the website

## Data Model 

The data model for the Hangman game consists of several attributes and methods. The Hangman class has a constructor that takes a list of words as a parameter and initializes several attributes, including the word to be guessed, the list of guessed letters, the number of allowed guesses, the number of incorrect guesses made by the player, the display word with underscores representing unguessed letters, and a list of art representations of the hangman as it is being drawn.

The class has methods to introduce the game to the user, choose a word at random from the list of possible words, and get a guess from the player. The guess method updates the display_word and guesses attributes based on the guess. The play method calls the intro, word_choose, and guess methods until the game is won or lost.

Overall, the data model represents a simple game with a clear objective: guessing a word before the hangman is fully drawn. The game's state is updated based on the player's input, and the game ends when the player has used all their guesses or correctly guessed the word. The class's attributes and methods encapsulate the game's state and behavior, making it easy to reuse and extend the code.

* Below it shows my Flow Chart for the Hangman Game

![flow chart](docs/readme_images/flow_chart.jpeg)

### Testing

I have manually tested this game by doing the following:

* I ran the game by running the script in my local terminal and the Code Institute Heroku terminal.
* The game displayed a welcome message, rules of the game, and a hint to guess a fruit.
* I was prompted to guess a letter.
* I guessed a letter that was in the word.
* The game displayed the updated word with the correct letters filled in and the number of guesses left.
* I repeated steps 3-5 until I guessed the entire word or ran out of guesses.
* If I guessed the entire word, the game displayed a congratulations message.
* If I ran out of guesses, the game displayed a sorry message with the correct word.
* I was prompted if I wanted to play again.
* If I chose to play again, the game started over from the beginning with a new word to guess.
* I repeated steps 3-10 until you were finished playing.

I tested several situations:

* I wrote number and I got error message as expected.

![number error](docs/testing/number_error.jpg)

* I wrote multiple letters and also I got error as expected.

![multiple letters error](docs/testing/multiple_letters_error.jpg)

* I wrote capital letter and got answer as expected.

![writting capital letter](docs/testing/writting_capital_letter.jpg)


Overall, I manually tested the game by playing it multiple times and verifying that it functioned correctly according to the rules and gameplay.

### Bugs

### Solved Bugs

* Player was able to put numbers also for guessing the word. I fixed it by adding guess.isalpha() so incase the player input number will get error saying "Invalid input. Please enter a letter." 
* The game was not running and I discover it was because my indication for game.play() was not right. I fixed it and it started working
* When the game ends and I reset the game and I was getting the welcome message however it was showing me already that I am lost. I fix it by adding def reset_variables.
* When player write letter in capital letter it was not working and player was able to write multiple letters without issue. I fix it by adding .lower() to the guess variabile and adding "or len(guess) > 1" for the "if not guess.isalpha()"

### Remaining Bugs

* No bugs remaining

### Validator Testing

* PEP8
  * Two errors were returned from pep8ci.herokuapp.com for line too long will fix it in the new release.

![pep8 test](docs/testing/pep8_test.jpg)

### Deployment

This project was deoplyed using Code Institut's mock terminal for Heroku

* Steps for deployment:
    * Fork or clone this repository
    * Create a new Heroku app
    * Set the buildbacks to Python and NodeJS in that order
    * Link the Heroku app to the repository
    * Click on Deploy

### Credits

* Code Institute for the deployment terminal.
* Code Institute Love Sandwishes Project for inspiration and practice.
* Code Institute Battleship Game Project for inspiration and practice.
* Slack groups it gives me good inspiration.  







