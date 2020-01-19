def doEvent(event_type,action = None):
    if event_type == None:
        print("I don't think I can put anything there.",sep="")
        return False,False

    elif event_type == False:
        print("I don't think ",action," belongs there.",sep="")
        return False,False

    else:
        if event_type == "move":
            print("> Moved to area ",action,sep="")
            return "move",action

        elif event_type == "talk":
            action.play()
            
            return False,False

        elif event_type == "use":
            return "use",action
        
        elif event_type == "grab":
            return "grab",action
        else:
            print("This thing does something undescribable.")
            return False,False