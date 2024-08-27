print("       Let's Play Kaun banaga Crorepati        ")
Questions=[["Who is the current railway minister of India?","Mamta Banerjee","Ram Vilash","Ashwini Vaishnav", "Ram nath Kovind",3],
           ["Which God is also known as 'Gauri Nandan'?","Ganesha","Hanuman","Agni","Indra",1],
           ["What does not grow on tree according to a popular Hindi saying?","Money","Flowers","Fruits", "Leaves",1],
           ["Which city is known as the Pink City of India?","Udaipur","Gandhinagar","Rajkot","Jaipur",4],
           ["How many major religions are there in India?","4","6","7", "8",2],
           ["Which one of the following places is famous for the Great Vishnu Temple?","Bordubar, Indonesia","Bamiyan, Afghanistan","Punjab Sahib, Pakistan", "Ankorvat, Cambodia",4],
           ["Where is the largest Buddhist Monastery in India located?","Sarnath, UP","Tawang, AP","Dharmshala, HP","Gangtok, Sikkim",2],
           ["Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?","Qutubminar","India Gate","Charminar", "Vijay Stambha",4],
           ["Which female player led the Indian contingent at Asian Games opening ceremony 2023?","Lovlina Borgohain","Mirabai Chanu","Dutee Chand", "Koneru Humpy",1],
           ["Who is the first woman to successfully climb K2, the world’s second highest mountain peak?","Wanda Rutkiewicz","Junko Tabei","Tamae Watanabe", "Chantal Mauduit",1],
           ["Aman Sehrawat, who recently won bronze medal at Paris Olympics 2024, is associated with which sports?","Table Tennis","Boxing","Wrestling", "Badminton",3],
           ["According to the Padma Purana, which king had to live as a tiger for a hundred years due to a deer's curse?","Kshemadhurti","Dharmadatta","Mitadhvaja", "Prabhanjana",4],
           ["What was the title of the thesis that Dr. B. R. Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923?","The Want and Means of India","The Problem of the Rupee","National Dividend of India", "The Law and Lawyers",3]]

Levels=[5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,50000000]
Money=0

for i in range(0,len(Questions)):
  Question=Questions[i]
  print(f"Question for Rs.{Levels[i]} is: ")
  print(f"{Question[0]}")
  print(f"1.{Question[1]}          2.{Question[2]}")
  print(f"3.{Question[3]}          4.{Question[4]}")
  reply=int(input("Enter your answer(1-4) or 0 to quit: "))
  if(reply==0):
    Money=Levels[i-1]
    print(f"you quit the game and won Rs.{Money}")
    break
  if(reply==Question[-1]):
    print(f"Correct answer, you have won Rs.{Levels[i]}")
    if(i==4):
      Money=10000
    elif(i==9):
      Money=320000
    elif(i==14):
      Money=10000000
  else:
    print("Wrong answer!")
    break

