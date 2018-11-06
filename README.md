# python-programimport random
import time
proposed_answers=['certain','decidely so','without a doubt','yes,definitely','you may rely on it','as i see it,yes']
print('hey there you want enjoy this game,this is Magic Ball,please enter your name?')
enteredname=input()
print('hello'+enteredname)

def balls():
    print('Ask me any Question.')
    input()
    print(proposed_answers[random.randint(0, len(proposed_answers)-1)])
    print('i hope you are stasified')
    replay()
    print('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        balls()
    elif reply == 'N':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        replay()
        balls()
def replay():
    return 4;
