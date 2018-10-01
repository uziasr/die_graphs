from random import randint

class Die():
    """ A class representing a single die"""
    
    def __init__(self, num_sides=6):
        """ Assume a siz-sided die """
        self.num_sides = num_sides
        self.total_sides = 0
        self.rolls = 0
        self.die_count = 0
        self.dice_title = ""
      
    
    def roll(self):
        """ resturn a random value between 1 and number of sides"""
        return randint(1, self.num_sides)
    
    
    def sum_side(self, die_list):
        """ counts the number of possibilites"""
        sum_sides = 0
        for die in die_list:
            sum_sides +=die.num_sides
        if len(die_list)>1:
            sum_sides +=1 -len(die_list)
        elif len(die_list) == 1:
            sum_sides += 0
        return sum_sides
    
    
    def record_rolls(self, die_list, rolls):
        """ rolls dice and add results to a list """ 
        die_roll = []
        self.rolls = rolls
        for roll in range(rolls):
            #dies_rolled = len(die_list)
            die_total = 0
            for die in die_list:
                die_total += die.roll()
            die_roll.append(die_total)
        return die_roll
    
    
    def count_rolls(self, die_count ,die_roll, result_list):
        """ counts every number rolled and records the number into a list """ 
        frequencies = []
        self.die_count = die_count
        frequency = 0
        for value in range(die_count, die_roll+die_count):
            frequency = result_list.count(value) 
            frequencies.append(frequency)
        return frequencies
      
         
    def x_list(self, sum_sides, die_count):
        """ Creates the labels for x-axis on chart """
        a_count = die_count
        x_label = []
        while (a_count <=sum_sides+die_count-1):
            x_label.append(a_count)
            a_count +=1
        return x_label

    def title_generator(self, die_list):
        """ creates title for chart"""
        dice=""
        for die in die_list[:-1]:
            dice +="D"+str(die.num_sides) + ", "
        dice += "D"+str(die_list[-1].num_sides) 
        title = "The Results of Rolling " + dice + ", "  + str(self.rolls) + " times."
        self.dice_title = dice 
        return title
