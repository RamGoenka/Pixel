#IMPORTING NEEDED LIBRARIES AND SETTING UP THE CLIENT
import discord
import os
import random
from discord.ext import commands
import math
import datetime
#from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

client = discord.Client()
client = commands.Bot(command_prefix=['pmath', 'pt'])
#DiscordComponents(client)

#LISTS
embed_footers = [
    'Thanks for using pixel :)',
    'You must be tired from being so purr-fect :D', 'You are very pawsome :)',
    'Are you from Tennessee? Because you are the only ten I see :D',
    'If you were a burger at McDonalds, you would be the McAmazing :)',
    'You seem to have a nice cat-titude :D',
    'Thanks for checking out my commands :)', 'Hope you have a great day :D',
    'Your back must hurt from carrying all that amazingness :)'
]

sad = [
    "I am a failure", "i am failure", "i am a failure", "im a failure",
    "i'm failure", "i'm a failure", "I'm a failure", "I am a disgrace",
    "I am useless", "I am stupid", "I am an idiot", "I am dumb",
    "I am disappointing", "I am useless", "I am not smart", "I'm dumb",
    "I'm stupid", "i am disgrace", "i am a disgrace", "im a disgrace",
    "i'm disgrace", "i'm a disgrace", "i am idiot", "i am an idiot",
    "im an idiot", "i'm idiot", "i'm an idiot", "i am unsmart", "im unsmart",
    "i'm unsmart", "i am stupid", "i am a stupid", "im a stupid", "i'm stupid",
    "i'm a stupid", "i am dumb", "i am a dumb", "im a dumb", "i'm dumb",
    "i'm a dumb", "i am disappointing", "i am a dissappointing",
    "im a dissappointing", "i'm dissappointing", "i'm a dissappointing",
    "i am useless", "i am a useless", "im a useless", "i'm useless",
    "i'm a useless", "i am unintelligent", "i am a unintelligent",
    "im a unintelligent", "i'm unintelligent", "i'm a unintelligent",
    "i am not smart", "i am a not smart", "im a not smart", "i'm not smart",
    "i'm a not smart", "i am Failure", "i am a Failure", "im a Failure",
    "i'm Failure", "i'm a Failure", "i am Idiot", "i am a Idiot", "im a Idiot",
    "i'm Idiot", "i'm a Idiot", "i am Stupid", "i am a Stupid", "im a Stupid",
    "i'm Stupid", "i'm a Stupid", "i am Dumb", "i am a Dumb", "im a Dumb",
    "i'm Dumb", "i'm a Dumb", "i am Disappointing", "i am a Disappointing",
    "im a Disappointing", "i'm Disappointing", "i'm a Disappointing",
    "i am Useless", "i am a Useless", "im a Useless", "i'm Useless",
    "i'm a Useless", "i am Disgrace", "i am a Disgrace", "im a Disgrace",
    "i'm Disgrace", "i'm a Disgrace", "i am Unsmart", "i am a Unsmart",
    "im a Unsmart", "i'm Unsmart", "i'm a Unsmart", "I'm stupid",
    "i am Unintelligent", "i am a Unintelligent", "im a Unintelligent",
    "i'm Unintelligent", "i'm a Unintelligent", "i am Not smart",
    "I am Not smart", "i am a Not smart", "im a Not smart", "i'm Not smart",
    "i'm a Not smart", "I am trash", "i'm trash", "I'm trash", "i am trash",
    "I???m garbage", "i'm garbage", "I am garbage", "i am garbage"
]
encouraging_words = [
    "Aww! That is not true :(", "No, you are an amazing person :)",
    "Hopefully it gets better <(^-^<)",
    "You are a capable individual with great potential!",
    "Believe in yourself, you got this!",
    "Keep your head high! Eventually you will get there :)",
    "Don't give up! You got this!",
    "There is light at the end of the tunnel :)",
    "Sending good vibes and happy thoughts your way  <(^-^<)",
    "Believe in yourself! Because I for sure do :)",
    "Believe in yourself, you are amazing!", "Stay strong! You are powerful and you are a fighter! You got this!", "I am rooting for you!", "You are a wonderful person!"
]

hug_gif = [
    "https://c.tenor.com/nUrfyD_VmM8AAAAC/hug-cute.gif",
    "https://c.tenor.com/4XQiR1rkwIAAAAAC/ghost-hug-ghost-hugs.gif",
    "https://c.tenor.com/UKsNkAqj7YcAAAAC/hug.gif",
    "https://c.tenor.com/NGFif4dxa-EAAAAC/hug-hugs.gif",
    "https://c.tenor.com/GdJRGf60YN4AAAAC/hugs-sending-virtual-hugs.gif",
    "https://c.tenor.com/XQh-aF1wTUIAAAAC/ghosthug.gif",
    "https://c.tenor.com/Vx-Fmk3G7McAAAAM/cute.gif",
    "https://media2.giphy.com/media/9Y1LEFKsbbP4hrLgV3/giphy.gif?cid=790b76119eb6ba36ddfbe56bf3ca28b4c38ddc7f8c1cacef&rid=giphy.gif&ct=g",
    "https://c.tenor.com/8Jk1ueYnyYUAAAAC/hug.gif",
    "https://c.tenor.com/1T1B8HcWalQAAAAC/anime-hug.gif",
    "https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif",
    "https://c.tenor.com/ia_mkwn2dwYAAAAC/love.gif",
    "https://c.tenor.com/endJ8_rbXUYAAAAC/be-happy-love.gif",
    "https://c.tenor.com/XyMvYx1xcJAAAAAC/super-excited.gif",
    "https://c.tenor.com/3mr1aHrTXSsAAAAC/hug-anime.gif",
    "https://c.tenor.com/EqzscTWbbXEAAAAC/kanna-dragon-maid.gif",
    "https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif"
]
coin_outcomes = [
    "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**",
    "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**",
    "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**",
    "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**"
]

dice_roll = [
    "You rolled a **1** :game_die:", "You rolled a **2** :game_die:",
    "You rolled a **3** :game_die:", "You rolled a **4** :game_die:",
    "You rolled a **5** :game_die:", "You rolled a **6** :game_die:"
]

cat_images = [
    "https://upload.wikimedia.org/wikipedia/commons/3/38/Adorable-animal-cat-20787.jpg",
    "https://images.rawpixel.com/image_1000/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L2ZyYW5pbWFsX2NhdF9raXR0ZW5fYnJpdGlzaC1pbWFnZS1reWJlYXlrNC5qcGc.jpg",
    "https://cc0.photo/wp-content/uploads/2016/10/Striped-cat-on-a-meadow-2048x1365.jpg",
    "https://c.pxhere.com/images/8d/1e/604c6eb3dca5d46f3854ae974ccf-1603569.jpg!d",
    "https://pixnio.com/free-images/2021/09/14/2021-09-14-08-25-52-1049x1350.jpg",
    "https://c.tenor.com/bK1qpWGyQKkAAAAd/kitty.gif",
    "https://c.tenor.com/1iAVPVejxSkAAAAd/cat-cats.gif",
    "https://cdn.pixabay.com/photo/2020/06/02/06/18/kitten-5249587_1280.jpg",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-09-57-33-1100x733.jpg",
    "https://i0.wp.com/pixahive.com/wp-content/uploads/2020/10/A-cute-cat-124534-pixahive.jpg?fit=1560%2C1040&ssl=1",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-09-59-07-1100x733.jpg",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-07-39-47-1100x733.jpg",
    "https://live.staticflickr.com/5698/23119711630_c3ffe739a0_b.jpg",
    "https://cdn.stocksnap.io/img-thumbs/960w/cat-kitten_BY1YIGNS0Y.jpg",
    "https://images.rawpixel.com/image_1300/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3B4NzU1MDcwLWltYWdlLWt3dnhnbzBsLmpwZw.jpg",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-07-23-15-1100x818.jpg",
    "https://c.pxhere.com/photos/5e/7b/cat_feline_staring_kitty_pet_cute_cat-640016.jpg!d",

]

wyr_questions = [
    "Give up junk food for a month **OR** Give up all forms of social media for a week?",
    "Be reborn as a cat **OR** A dog?",
    "Be invisible **OR** Be able to fly?",
    "Be rich but lonely **OR** Be poor but have friends?",
    "Know how you die **OR** Know when you die?",
    "Have a lot of distant friends **OR** One really good and close friend?",
    "Cry each time something funny happens **OR** Laugh each time something tragic /  sad happens?",
    "Be caught cheating in a relationship **OR** Be caught cheating on a test?",
    "Have as much wealth as you wish but always remain sad **OR** Live paycheck to paycheck but be happy?",
    "Never be able to speak again **OR** Never be able to hear again?",
    "Be able to sleep 8 hours but only during day-time **OR** Only be able to sleep for 1 hour during the night?",
    "Be able to go back in the past and fix a mistake **OR** Be able to go back in the past and revive one dead person?",
    "Find the love of your life **OR** Win a million dollars?",
    "Give up showering for a month **OR** Give up all forms of social media for a month?",
    "Be a famous serial-killer **OR** Be poor?",
    "Get a private island **OR** A private jet?",
    "Be the fastest runner in the world **OR** Have the highest vertical jump in the world?",
    "Be a famous athlete **OR** A famous singer?",
    "Never be able to lie **OR** Always be lied to?",
    "Give up being able to eat meat **OR** Give up being able to eat vegetables?",
    "Live in the middle of the ocean or an year **OR** Live in the middle of a dense forest for an year?",
    "Live in 45??C for one year **OR** Live in -45??C for one year?",
    "Be chased by a clown **OR** Be chased by a lion?",
    "Be fluent in every language **OR** Be a master of every single musical instrument?",
    "Be stuck in an elevator with the power supply gone **OR** Be stuck in a train in the middle of nowhere?",
    "Be 4 feet tall **OR** Be 8 feet tall?",
    "Be a famous singer **OR** A famous Author?",
    "Be an Olympic gold medalist **OR** Win a Nobel Prize?",
    "Never be able to make a phone call ever again **OR** Never be able to send a text ever again?",
    "Give up social media for the rest of your life **OR** Eat the same dinner for the rest of your life?",
    "Give up YouTube **OR** Give up Netflix?",
    "Have the ability to freeze time for 10 minutes but it be only a one time thing **OR** Be able to time travel 10 minutes into the future but have it be only a one time thing (i.e. you only have 1 chance to use the ability)?",
    "Give up ramen **OR** Give up sushi?",
    "Give up tea **OR** Give up coffee?",
    "End world hunger **OR** Be able to eat the most expensive food's for free, whenever and wherever?",
    "Get $1 million handed to your right now **OR** be paid $10,000 every month for the next 12 months?",
    "Have front row tickets to a musician you???ve never heard of **OR** Listen to your favorite band perform from the parking lot?",
    "Only eat burger for the rest of your life **OR** Only eat pizza for the rest of your life?"
    
  
    
]

random_facts = [
    "Sudan has more pyramids than any country in the world. :flag_sd:",
    "The bumblebee bat is the world???s smallest mammal. :bat:",
    "There are parts of Africa in all four hemispheres. :earth_africa:",
    "The Philippines consists of 7,641 islands. :flag_ph:",
    "Japan has one vending machine for every 40 people. :flag_jp:",
    "There???s only one letter that doesn???t appear in any U.S. state name, it is Q. :regional_indicator_q:",
    "A cow-bison hybrid is called a beefalo. :cow: :bison:",
    "Armadillo shells are bulletproof. :muscle:",
    "Some octopus species lay around 56,000 eggs at a time. :octopus:",
    "Blue whales eat up to half a million calories in one mouthful. :whale:",
    "The current American flag was designed by a high school student. :flag_us:",
    "No number before 1,000 contains the letter A. :1234:",
    "Giraffe tongues can be 20 inches long. :giraffe:",
    "Cats are believed to be the only mammals who don???t taste sweetness. :cat:",
    "Humans aren???t the only animals that dream, rats dream too. :rat:",
    "If the sun exploded right now, you wouldn't know about it for another eight minutes. :boom:",
    "Over 80 million bacteria can be exchanged in one kiss. :microbe:",
    "Australia is wider than the moon, while the moon as a diameter of 3400 km, Australia has a diameter of 4000 km. :flag_au:",
    "*face with tears of joy* is the most used emoji worldwide. :joy:",
    "A shrimp's heart is located in its head. :shrimp:",
    "Odontophobia is the fear of teeth (or the fear of anything related to dentistry in general). :tooth:",
    "Elephants are the only animal to have four forward-facing knees. :elephant:"
]

trivia_questions = [
    ":thinking: Who was the 28th U.S. president? (Answer: || Woodrow Wilson ||)",
    ":thinking: How many countries does the continent Africa comprise of? (Answer: || 54 ||)",
    ":thinking: Which is the largest country in the world by land area? (Answer: || Russia ||)",
    ":thinking: How many states does the United States of America comprise of? (Answer: || 50 ||) ",
    ":thinking: Which were the last two states to join the Union? (Answer: || Alaska and Hawaii ||)",
    ":thinking: Which country won the Men's Fifa World Cup 2018, and against whom? (Answer: || France won against Croatia ||) ",
    ":thinking: Which team (either one is fine) has won the most Men's NBA Championships? (Answer: || Boston Celtics and Los Angeles Lakers have both won 17 NBA Championships ||)",
    ":thinking: Who was the first person to step foot on the Moon? (Answer: || Neil Armstrong ||)",
    ":thinking: What is the area on the Moon known as where the first person stepped foot on? (Answer: || Sea of Tranquility ||)",
    ":thinking: In the state of Georgia, it???s illegal to eat what with a fork? (Answer: || Fried Chicken ||)",
    ":thinking: The name of which African animal means *river horse*? (Answer: || Hippopotamus ||)",
    ":thinking: Which country has won the most Men's ICC Cricket World Cup titles? (Answer: || Australia ||)",
    ":thinking: In which year did World War II start? Which year did it end in? (Answer: || Start: 1939, End: 1945 ||)",
    ":thinking: What is the capital of Norway? (Answer: || Oslo ||)",
    ":thinking: Which continent, based on land area, is the largest in the world? (Answer: || Asia ||)",
    ":thinking: Which state in the United States of America has the most electoral college votes? (Answer: || California, it has 55 electroal votes ||)",
    ":thinking: Which country is also known as the *land of the rising sun*? (Answer: || Japan ||)",
    ":thinking: How many points is a touchdown? (Answer: || 6 points ||)",
    ":thinking: How many terms did Benjamin Franklin serve as president? (Answer: || He was never a president ||)",
    ":thinking: Which team won the first ever NBA championship? (Answer: || Philadelphia Warriors in 1946 ||)",
    ":thinking: Which is the largest state in the United States of America based on land area? (Answer: || Alaska ||)",
    ":thinking: Which is the largest state in the United States of America based on land area? (Answer: || Rhode Island ||)",
    ":thinking: Who is on the 100 U.S. Dollar bill? (Answer: || Benjamin Franklin ||)",
    ":thinking: Who was the 1st President of the United States of America? (Answer: || George Washington ||)",
    ":thinking: Who was the 16th U.S. president and is on the $5 bill? (Answer: || Abraham Lincoln ||)",
    ":thinking: What is the more popular name for the portrait officially titled ???La Gioconda,??? painted in 1503? (Answer: || Mona Lisa ||)",
    ":thinking: What is the capital of India? (Answer: || New Dehli ||)",
    ":thinking: What is the capital of the United States of America? (Answer: || Washington, D.C. ||)",
    ":thinking: Which two countries have the longest shared international border? (Answer: || Canada and the U.S.A. ||)",
    ":thinking: What is the human body???s largest organ? (Answer: || Skin ||)",
    ":thinking: How many bones do sharks have? (Answer: || 0 bones ||)",
    ":thinking: What was the first country to give women the right to vote? (Answer: || New Zealand ||)",
    ":thinking: What river runs through Paris? (Answer: || The Seine ||)",
    ":thinking: Which is the longest river in the world? (Answer: || The Nile ||)",
    ":thinking: Mount Everest is the tallest mountain in the world, what is the second tallest mountain in the world? (Answer: || Mount K2 ||)",
    ":thinking: How many stars and stripes are in the U.S.A. flag? (Answer: || 50 stars & 13 stripes  ||)"
    ":thinking: ",
    ":thinking: What is the rarest blood type? (Answer: || AB Negative ||)",
    ":thinking: How many countries are in the European Union? (Answer: || 27 ||)",
    ":thinking: What does DNA stand for? (Answer: || Deoxyribonucleic Acid ||)",
    ":thinking: How many phases does the moon have? (Answer: || Eight ||)",
    ":thinking: How many hearts does an octopus have? (Answer: || Three ||)",
    ":thinking: Which two planets in our Solar System have no moons? (Answer: || Mercury and Venus ||)",
    ":thinking: What U.S. city has the nickname ???Motown,??? derived from ???motor town???? (Answer: || Detroit ||)",
    ":thinking: Uranus and which other planet are nicknamed the ???ice giants???? (Answer: || Neptune ||) ",
    ":thinking: How many centimeters are in 1 inch (Answer: || 2.54, however any value between 2.5 and 2.54 is acceptable ||)"
]


