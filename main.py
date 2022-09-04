from MMAFighters import MMA_Fighters

print("UFC Fighters' Profiles")

# P4P
fighter1 = MMA_Fighters("Alexander Volkanovski", "The Great", 33, "25-1-0", 145, 168, 180, 'W', 'C')
fighter2 = MMA_Fighters("Israel Adesanya", "The Last Stylebender", 33, "23-1-0", 185, 193, 203, 'W', 'C')
fighter3 = MMA_Fighters("Charles Oliveria", "Do Bronx", 32, "33-8-0", 155, 178, 188, 'W', 1)
fighter4 = MMA_Fighters("Kamaru Usman", "The Nigerian Nightmare", 35, "20-2-0", 170, 183, 193, 'L', 1)
fighter5 = MMA_Fighters("Francis Ngannou", "The Predator", 35, "17-3-0", 257, 193, 211, 'W', 'C')
fighter6 = MMA_Fighters("Leon Edwards", "Rocky", 31, "20-3-1", 170, 183, 188, 'W', 'C')
fighter7 = MMA_Fighters("Aljamain Sterling", "Funk Master", 33, "21-3-0", 135, 170, 180, 'W', 'C')
fighter8 = MMA_Fighters("Dustin Poirier", "The Diamond", 33, "28-7-0", 155, 175, 183, 'L', 2)
fighter9 = MMA_Fighters("Deiveson Figueiredo", "Deus Da Guerra", 34, "21-2-1", 125, 165, 173, 'W', 'C')
fighter10 = MMA_Fighters("Jiri Procházka", "Denisa", 29, "29-3-1", 205, 193, 203, 'W', 'C')
fighter11 = MMA_Fighters("Max Holloway", "Blessed", 30, "23-7-0", 145, 180, 175, 'L', 1)
fighter12 = MMA_Fighters("Jon Jones", "Bones", 35, "26-1-0", 205, 193, 215, 'W', 'Unknown')
fighter13 = MMA_Fighters("Stipe Miocic", "", 40, "20-4-0", 234, 193, 203, 'L', 2)
fighter14 = MMA_Fighters("Petr Yan", "No Mercy", 29, "16-3-0", 135, 170, 170, 'L', 1)
fighter15 = MMA_Fighters("Brandon Moreno", "The Assassin Baby", 28, "20-6-2", 125, 170, 178, 'W', "IC")

fighters = [fighter1, fighter2, fighter3, fighter4, fighter5, fighter6, fighter7, fighter8, fighter9, fighter10, fighter11, fighter12, fighter13, fighter14, fighter15]
count = 1;

while True:
  choice = input("Choose: P4P/p4p (Pound For Pound), FLW/flw (Flyweight), BW/bw (Bantamweight), FEW/few (Featherweight), LW/lw(Lightweight), WW/ww(Welterweight), MW/mw(Middleweight), LHW/lhw(Light Heavyweight), HW/hw(Heavyweight): ")
  print()
  
  if choice == "P4P" or choice == "p4p":
    print("Pound For Pound:")
    for fighter in fighters:
      print("  #" + str(count) + ": " + fighter.name)
      count += 1
    print()
    pick = int(input("Choose a fighter: "))
    print()
    for fighter in fighters:
      if pick-1 == fighters.index(fighter):
        print("Profile: ")
        print("  Name: " + fighter.name)
        print("  Nickname: " + fighter.nickname)
        print("  Age: " + str(fighter.age))
        print("  Record: " + fighter.record)
        print("  Weight: " + str(fighter.weight) + " lbs, " + fighter.weight_division())
        print("  Height: " + str(fighter.height) + " cm")
        print("  Reach: " + str(fighter.reach) + " cm")
        print("  Rank: " + fighter.is_the_champion() + " " + fighter.weight_division() + ", #" + str(pick) + " Pound For Pound")
        print()
        print("  Did the fighter win the last fight? " + fighter.recent_fight_result())
    print()
    choose = input("Do you want to continue: (Y/y (Yes)) or (N/n (No)): ")
    print()
    if choose == "Y" or choose == 'y':
      count = 1
      print()
      continue
    else:
      print()
      break

print("Thank you!")
