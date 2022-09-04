class MMA_Fighters:
  def __init__(self, name, nickname, age, record, weight, height, reach, recent_fight, rank):
    self.name = name
    self.nickname = nickname
    self.age = age
    self.record = record
    self.weight = weight
    self.height = height
    self.reach = reach
    self.recent_fight = recent_fight
    self.rank = rank

  def recent_fight_result(self):
    if self.recent_fight == 'W':
      return self.name + " " + "Won The Last Fight!"
    elif self.recent_fight == 'L':
      return self.name + " " + "Lost The Last Fight!"
    elif self.recent_fight == 'D':
      return "His Last Fight Was A Draw!"
    else:
      return "His Last Fight Was No Contest!"

  def weight_division(self):
    if self.weight == 125:
      return "Flyweight Division"
    elif self.weight == 135:
      return "Bantamweight Division"
    elif self.weight == 145:
      return "Featherweight Division"
    elif self.weight == 155:
      return "Lightweight Division"
    elif self.weight == 170:
      return "Welterweight Division"
    elif self.weight == 185:
      return "Middleweight Division"
    elif self.weight == 205:
      return "Light Heavyweight Division"
    else:
      return "Heavyweight Division"

  def is_the_champion(self):
    if self.rank == 'C':
      return "UFC Champion"
    elif self.rank == "IC":
      return "Interim UFC Champion #1"
    else:
      return "#" + str(self.rank)