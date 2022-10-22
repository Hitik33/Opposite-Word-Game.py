print()

print('Wellcome To English Opposite Word Game! ')

print()

playing = input(' Dou You Want To Play? :- ')

print()

if playing.lower() != 'yes':
    quit()
else:
    print(" Okay! Let's Play :-")

print()

score = 0

answer = input(" 1. Bad .\n Answer:- ")
if answer.lower()=="good":
    print(" Correct!")   
    score += 1
else:
    print(" Wrong Answer")

print()    
    
answer = input(" 2. Beautiful .\n Answer:- ")
if answer.lower()=="ugly":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")    

print()

answer = input(" 3. Boy.\n answer:- ")
if answer.lower()=="girl":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")

print()    
    
answer = input(" 4. Happy .\n Answer:- ")
if answer.lower()=="sad":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")

print()
    
answer = input(" 5. Hot.\n Answer:- ")
if answer.lower()=="cold":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")

print()
    
answer = input(" 6. Larg.\n Answer:- ")
if answer.lower()=="small":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")

print()
   
answer = input(" 7. Light.\n Answer:- ")
if answer.lower()=="dark":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")

print()
    
answer = input(" 8. Love.\n Answer:- ")
if answer.lower()=="hate":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")

print()
    
answer = input(" 9. Top.\n Answer:- ")
if answer.lower()=="bottom":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")

print()
    
    
answer = input(" 10. Truth.\n Answer:- ")
if answer.lower()=="lie":
    print(" Correct!")
    score += 1
else:
    print(" Wrong Answer")                                

print()    



print('You Got '+str(score)+' Question Answer')
print('You Have '+str((score / 10) * 100)+' %' ' Of Score.')

print()