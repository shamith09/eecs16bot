from time import sleep
from splinter import Browser
from random import shuffle
import pyautogui

print('\nHello! I am the EECS 16B self-grade bot, made by a lazy CS & Physics major named Shamith Pasula.')
print('I will be doing your self-grade for you, giving you 8/10 on some questions to not be sus.')
print('The comments for the 8/10 questions are in main.py, edit them if you wish.')
print('If you mess up or want to restart, press Ctrl+C and I will restart. \n')

# params
while True:
    try:
        print('I have a few questions for you:\n')

        name = input('What is your full name (First Last)? ').strip()
        sid = int(input('What is your SID? ').strip())
        email = input('What is your @berkeley.edu email?: ').strip()
        while (email[-13:] != '@berkeley.edu'):
            email = input('Please enter a valid @berkeley.edu email address: ')
        print()

        hw_number = int(input('Which homework are you self-grading? ').strip())
        if hw_number < 10:
            hw_number = '0' + str(hw_number)
        else:
            hw_number = str(hw_number)

        resubmission = None
        while (resubmission != 'Y' and resubmission != 'N'):
            resubmission = input('Is this a resubmission (Enter Y or N)? ').strip().upper()
        resubmission = 'yes' if resubmission == 'Y' else 'no'

        difficulty = int(input(f'How difficult was HW {hw_number} (Enter an integer between 1-10)? ').strip())
        hours_spent = int(input(f'How many hours did you spend on HW {hw_number}? ').strip())
        print()
        num_teammates = int(input('How many people did you work with? ').strip())

        went_to_hw_party = None
        while (went_to_hw_party != 'Y' and went_to_hw_party != 'N'):
            went_to_hw_party = input('Did you go to HW party (Enter Y or N)? ').strip().upper()

        break
    except ValueError:
        print('ERROR: Bad input. Restarting.\n')

print()
for i in range(5):
    print(f'A new Google Chrome window will open in a new window in {5 - i} seconds. Navigate back to your terminal once it opens to continue.', end = '\r')
    sleep(1)
print('\nOpening now...')

with Browser('chrome') as browser:
    # code
    difficulty = str(difficulty)

    url = f'http://www.eecs16b.org/self-grade-{hw_number}.html'
    browser.visit(url)
    browser.find_by_id('name').fill(name)
    browser.find_by_id('email').fill(email)
    browser.find_by_id('sid').fill(sid)
    browser.find_by_value(resubmission).click()

    inputs = browser.find_by_value('Comment')
    indices = list(range(len(inputs)))
    shuffle(indices)

    print(f'There are {len(indices)} questions on this HW.')
    print()
    num_incorrects = int(input('How many questions out of these do you want to give an 8/10? ').strip())
    print('I will now do your self-grade for you! I\'ll mark random questions as 8/10 and the rest as 10/10.')
    print('IMPORTANT: Please navigate back to the Chrome window in the next 5 seconds so I can do your self-grade!')
    
    print()
    for i in range(5):
        print(f'Beginning self-grade in {5 - i} seconds.', end='\r')
        sleep(1)
    print('\nSelf-grading now...')

    # EDIT THIS list TO ADD/CHANGE COMMENTS
    #
    # There is no limit to the number of comments you can add,
    # so add as many as you like!
    comments = ['Calculation error', 'Misread question']

    q, r = divmod(num_incorrects, len(comments))
    comments = q * comments + comments[:r]

    for i in indices[:-num_incorrects]:
        browser.find_by_value('10')[i].click()

    sleep(2)
    counter = 0
    for i in indices[-num_incorrects:]:
        browser.find_by_value('8')[i].click()
        pyautogui.keyDown('tab')
        pyautogui.write(comments[counter])
        counter += 1

        
    browser.find_by_id('d' + difficulty).click()
    browser.find_by_id('Hours Spent').fill(hours_spent)
    browser.find_by_id('Teammate Headcount').fill(num_teammates)
    browser.find_by_id(went_to_hw_party).click()
    browser.find_by_xpath('/html/body/section/form/p/button').click()
    browser.find_by_id('json-download').click()

    sleep(10)
