scene= 'starting'
confidence= 0
game_running= True
while game_running:
    if scene== "starting":
        print("You ask your crush out for a science competition flyer, but accidentally pointing at the spring ball poster, she said YES! but you have no idea which event she thinks you meant  ")
        print("To investigate what event she is coming, , enter'A'. To wait for the day of the event, enter'B'")

        answer=input("A-B: ").upper()

        if answer=='A':
            scene="Investigate"
        elif answer=='B':
            scene="Day of Event"
        else:
            print("Invalid Choice")
  


        if scene== "Investigate":
            print("You find a lab coat and a invite letter to the spring ball, You give up and head towards the cafeteria to join your friends")
            scene="friends"
        elif scene== "Day of Event":
            print("You head to lunch in the cafeteria and join your friends")
            scene="friends"
        
        if scene== "friends":
            print(" Your friend say to be brave and You can do this, you either GO BIG OR GO HOME")
            print("To chose to go to the spring ball, enter'A'. To go for the science competition, enter'B'")

        answer=input("A-B :").upper()
        if answer=="A":
            scene="ending_suit"
        elif answer=="B":
            scene="ending_lab"
        else:
            print("Invalid Choice")
        
        if scene=="ending_suit":
            print("You show up to the dance in a suit , but see her in her lab coat but instead of feeling awkward she  pulls off her lab coat to reveal her formal dress underneath, and you walk into the dance together!")
            game_running= False
        elif scene=="ending_lab":
            print("You both show up in a lab coat and win this years science competition")
            game_running= False



        


