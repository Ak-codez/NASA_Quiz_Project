import time
import random


def decor(count):
    """Print a line of '=' characters based on the integer 'count'"""
    print("="*count)


def wait(sec):
    """Pause the code for 'sec' seconds"""
    time.sleep(sec)


def main():


    CORRECT_RESPONSES = ("Bravo!",
                         "Well done!",
                         "Good job!",
                         "You're right!",
                         "Indeed!"
                         #Add or remove to your liking
                         )

    INCORRECT_RESPONSES = ("Incorrect!",
                           "Good try!",
                           "Almost there!",
                           "Oops!",
                           "Not quite!"
                           #Add or remove to your liking
                           )

    VALID_CHOICES = ["A", "B", "C", "D"]

    questions = ("Who was the commander of the Apollo 11 mission?",
                 "What is the full form of NASA?",
                 "Where is NASA's headquarters?",
                 "What is the most recent NASA mission underway?",
                 "What year did the first humans land on the moon in the Apollo 11 mission?",
                 "Which telescope was launched in 2021 to replace Hubble?",
                 "Which famous space station, worth over 100 billion dollars, did NASA collaborate on?"
                 #Add or remove to your liking
                 )

    options= (('A. Edwin Aldrin',                     'B. Neil Armstrong',                 'C. Michael Collins',                                'D. Jim Lovell'),
              ('A. National Aerospace Space Agency',  'B. New Aliens Space Association',   'C. National Aeronautics and Space Administration',  'D. National Administration of Space Affairs'),
              ('A. Washington D.C',                   'B. Seattle',                        'C. New York',                                       'D. Manhattan'),
              ('A. Gemini 5',                         'B. Apollo 21',                      'C. Voyager 3',                                      'D. Artemis III'),
              ('A. 1990',                             'B. 1969',                           'C. 1959',                                           'D. 1970'),
              ('A. James Webb',                       'B. Lunar Alpha',                    'C. Cosmic Eye',                                     'D. Nebula 2'),
              ('A. Sputnik 1',                        'B. Apollo 15',                      'C. International Space Station (ISS)',              'D. Cassini')
              )

    answers = ('B','C','A','D','B','A','C')
    guesses = []
    score = 0
    question_number = 0

    decor(25)
    print("       NASA QUIZ         ")

    for question in questions:
        decor(25)
        print(f"Q) {question}")
        for option in options[question_number]:
            print(option, end=" ")
            print()

        guess = input("Your answer is: ").upper()

        while guess not in VALID_CHOICES:
            guess = input("Please enter A, B, C, or D: ").upper()

        guesses.append(guess)
        if guess == answers[question_number]:
            print("🎉", random.choice(CORRECT_RESPONSES), f"{guess} was the correct answer!")
            score += 1
        else:
            print("❌", random.choice(INCORRECT_RESPONSES), f"{answers[question_number]} was the correct answer.")

        wait(2)
        question_number += 1

    decor(25)
    print("Your guesses:")
    print(" ".join(guesses))

    print("Correct answers:")
    print(" ".join(answers))

    print("\nCalculating results...")
    wait(4)

    decor(25)
    print("         RESULTS         ")
    decor(25)

    percent= (score/len(questions))*100
    if 80 <= percent <= 100:
        print("Awesome job!")
    elif 40 <= percent < 80:
        print("Well done!")
    else:
        print("Good try!")

    print(f"Your final score is {score}/{len(questions)} or {percent:.1f}%")
    decor(31)
    print("Thanks for playing!")

if __name__ == '__main__':
    main()




