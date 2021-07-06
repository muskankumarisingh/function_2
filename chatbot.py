print("Welcome to navgurukul information centre")
Name=input("enter a name:")
print("hii",Name,"how can i help you")
print("What you want know about: \n 1.About navgurukul press 1 \n 2.campuses of Navgurukul press 2  \n 3.Admission process press 3\n 4.Payback process 4\n 5.To know about study") 
Help=int(input("please ask what you want to know?"))
if Help==1:
    print("Navgurukul is a NGO.Navgurukul offers a fully-funded skilling program in software engineering with guaranteed job to youth from low-income families.\n The program is for one year and is a residential course.")
    know_more=input("to know more about  enter yes:")
    if know_more=="yes":
        print("Mr.Abhishek Gupta is a founder of Navgurukul")     
        facility=input("to know about facility enter yes")
        if facility=="yes":
            print("Facilites are good!,Here students have to study and do there work themselves apart form this NG provides whatevere things are needed")
        else:    
            print("thanks for connecting")    
    else:
        print("thank you")    
elif Help==2:
    print("there are four campus in Navgurukul")
    To_know=input("to know enter yes")
    if To_know=="yes":
        print("bangalore,pune,dharamshala,sarjapur")
        more_to_know=input("more to know enter yes")
        if more_to_know=="yes":
            print("bangalore,pune,and sarjapur is for girls and dharamshala for boys")
        else:
            print("thanks for connecting")
    else:
        print("thank you")            
elif Help==3:        
    print("To join NG their are 3 steps you have to clear that.")
    steps=input("steps to know enter yes or no ")
    if steps=="yes":
        print("first one online test,algebra interview,english interview,and culture fit interview\n if you clear these setps you will be selected and you will get joing letter") 
    else:
        print("thanks for connecting")
elif Help==4:
    print("after getting job you have to payback Rs.120000 in installement")    
elif Help==5:
    print("Here they are doing study in themselves")
    know_about=input("enter to know about press yes or no:")
    if know_about=="yes":
        print("Here every student have one mentor they guide them \n navgurukul have main object to provide each and every student a garuteened job in one year ") 
    else:
        print("thank you")           
if(True):
    print("thanks for connecting us")      
    print("if you want to know more about navgurukul visit this website.http://admissions.navgurukul.org/")mus