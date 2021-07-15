print("Welcome to navgurukul information centre")
Name=input("enter a name:---\n")
print("Hello",Name,"How Can I Help You")
print("What you want To know about: \n 1.About Navgurukul press 1 \n 2.campuses of Navgurukul press 2  \n 3.Admission process press 3\n 4.Payback process 4\n 5.To know about study") 
Help=int(input("please ask what you want to know?"))
if Help==1:
    print("Navgurukul is a NGO.Navgurukul offers a fully-funded skilling program in software engineering with guaranteed job to youth from low-income families.\n The program is for one year and is a residential course.")
    know_more=input("To know more about  enter yes:")
    if know_more=="yes":
        print("Mr.Abhishek Gupta is a founder of Navgurukul")     
        facility=input("to know about facility enter yes")
        if facility=="yes":
            print("Facilites are good!,Here students have to study and do there work themselves apart form this NG provides whatevere things are needed")
        else:    
            print("Thanks for connecting")    
    else:
        print("Thank you")    
elif Help==2:
    print("There are four campus in Navgurukul")
    To_know=input("To know enter yes")
    if To_know=="yes":
        print("Bangalore,Pune,Dharamshala,Sarjapur")
        more_to_know=input("more to know enter yes")
        if more_to_know=="yes":
            print("Bangalore,Pune, Sarjapur is for girls and Dharamshala for boys")
        else:
            print("Thanks for connecting")
    else:
        print("Thank you")            
elif Help==3:        
    print("To join NG their are 3 steps you have to clear that.")
    steps=input("Steps to know enter yes or no ")
    if steps=="yes":
        print("First one online test,algebra interview,english interview,and culture fit interview\n if you clear these setps you will be selected and you will get joing letter") 
    else:
        print("Thanks for connecting")
elif Help==4:
    print("After getting job you have to payback Rs.120000 in installement")    
elif Help==5:
    print("Here they are doing study in themselves")
    know_about=input("enter to know about press yes or no:")
    if know_about=="yes":
        print("Here every student have one mentor they guide them \n Navgurukul have main object to provide each and every student a garuteened job in one year ") 
    else:
        print("Thank you")           
if(True):
    print("Thanks for connecting us")      
    print("If you want to know more about Navgurukul visit this website.http://admissions.navgurukul.org/")