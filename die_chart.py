import pygal

from die import Die

# Create as many die and enter the ones you want to use into die_list

#Argument here can be changed to a different numbered die
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)
die_list = [die_1, die_2, die_3]

#sets rolls equal to an x amount of rolls (list)

#change 10000 to desired amount of rolls
rolls = die_1.record_rolls(die_list, 10000)

# total sides = total amount of sides possble 
total_sides =die_1.sum_side(die_list)

#counted rolls = number of times all numbers have rolled
counted_rolls = die_1.count_rolls(len(die_list), total_sides, rolls)
#Creates a list for x-axis
x_list = die_1.x_list(total_sides, len(die_list))

title = die_1.title_generator(die_list)

hist = pygal.Bar()

hist.title = title
hist.x_labels = x_list
hist.y_title = "Frequency Results"
#
hist.add(die_1.dice_title, counted_rolls)
hist.render_to_file('die_visual.svg')

