
score=0
while True:
    start=int(input('Do you want to play the game? press 1 to start, 0 to exit'))
    if start==1:
        print('Great!')

    elif start==0:
        break
    else:
        print("invalid input")
        
    q1=int(input('What is 2 + 2?'))
    if q1 == 4:
        print('correct!')
        score+=1
    else:
        print('incorrect')
    break


print('Thank you')
print(f'your score was {score}')

