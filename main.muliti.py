import random
tools=["srp","dice","coin","exit"]
print("--------------------multi--tool--------------------")
print("------->type srp for sicssor paper rock ")
print("-------->type coin to toss a coin")
print("---------->type dice to roll a dice")
#functions for each coomand

def play_srp():#sicssor paper rock game 
    
       user=0
       bot_sc=0
       choices=["sicssor","paper","rock"]
       choice=["sicssor","paper","rock","exit"]
       print("------------A sicssor paper rovk game------")
       print("bot--> it will be fun to play with you")
       
       #error handling for invlaid rounds
       
       while True:
           try:
              rounds=int(input("how many rounds"))
              break
              
           except ValueError:
                  print("--->invalid input number") 
                  
                        #real game logic
       for i in range(rounds):
           bot_choice=random.choice(choices)
           user_c=input("'------------>")
           print(f"bor--> i choosed {bot_choice}")
           
           
           if user_c=="paper" and bot_choice=="rock":
               print("bot--> nooi! i lost you won")
               user+=1
               
           elif user_c=="rock" and bot_choice=="sicssor":
               print("bot--> its hard to beat you")
               user+=1
               
           elif user_c=="sicssor" and bot_choice=="paper":
               print("bot----> it will be fun to play with you")
               print("bot--->you won")
               user+=1
               
           elif user_c not in choice:
               print ("in valid bot will get a point")
               bot_sc+=1
               continue
               
           elif user_c==bot_choice:
               print("its a tie")
           
           else:
                print("bot---> i won hahaha")
                bot_sc+=1
       print(f"your score is{user}")
       print(f"bot score is {bot_sc}")
       
       #result system
       
       if bot_sc>user:
          print("bot--> yeah i won in total")
       elif bot_sc<user:
          print("bot---> noooo i lost")
       elif bot_sc==user:
           print("its a tie")
       else:
          print("its a tie you are houmerable oppomemt")
     
#function for dice rolling

def roll_dice():
    while True:
       numbers=["1","2","3","4","5","6"]
       ph=(input("roll the dice?(Y/N")).lower()
       
       if ph=="y":
           n=random.choice(numbers)
           print(f"you got {n}")
       elif ph!="y" and ph!="n":#error handeling
           print("----->>>>invalid")
       elif ph=="n":
           print("------------>thanks for using<--------")
           break

def coin_toss():
  while True:
      conditions=["head","tail"]
      user=(input("toss the coin (y/n)")).lower()
      if user=="y":
          result=random.choice(conditions)
          print(f"-------->you got {result}")
      elif user=="n":
          print("---->thanks for playing<-----")
          break
      elif user!="y" and user!="n":
          print("--------->invalid try y and n <-------")
          
      
      
  


#main pannel
while True:
    value=(input("----------------------------->>"))
    if value=="srp":
        play_srp()    
        
    elif value=="dice":
        roll_dice()
    elif value not in tools:
        print ("------------>in valid try srl,coin ,dice")
    elif value=="exit":
        break
    elif  value=="coin":
         coin_toss()


  
  
  
