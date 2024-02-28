import math

# Geometry Quizziz Practice
# Angles of Elevation and Depression 
# Feb 26, 2024


# Question 1
print("Question 1")
print("I am cleaning the windows on my house. I place a 4.5 m ladder against the side of my house to reach a window that is 4m above the ground. What is the angle that the ladder makes with the ground? Hint: think about how a ladder leans to draw your picture.")

# Given values for the ladder problem
ladder_length = 4.5  # length of the ladder in meters
height_reached = 4  # height the ladder reaches in meters

# Using Pythagoras' theorem to find the base of the triangle formed by the ladder, ground, and wall
# ladder_length^2 = height_reached^2 + base^2
# We need to calculate the angle the ladder makes with the ground using sine, cosine, or tangent.
# Since we know the opposite side (height_reached) and the hypotenuse (ladder_length), we use sine.
# sin(angle) = opposite/hypotenuse = height_reached/ladder_length

# Calculating the angle using arcsin
angle_with_ground_radians = math.asin(height_reached / ladder_length)

# Converting the angle from radians to degrees
angle_with_ground_degrees = math.degrees(angle_with_ground_radians)

# Rounding the answer
angle_with_ground_degrees_rounded = round(angle_with_ground_degrees, 1)

angle_with_ground_degrees_rounded


print("\nangle_with_ground_degrees_rounded: " + str(angle_with_ground_degrees_rounded))

print("\n*********************************\n")


# Question 2
print("Question 2")
print("From a point on the ground 12 ft from the base of a flagpole, the angle of elevation of the top of the pole measures 53°. How tall is the flagpole? Round your answer to the nearest tenth.")

# Given values
distance_from_base = 12  # distance from the base of the flagpole in feet
angle_of_elevation_degrees = 53  # angle of elevation in degrees

# Converting angle of elevation from degrees to radians for calculation
angle_of_elevation_radians = math.radians(angle_of_elevation_degrees)

# Calculating the height of the flagpole using tangent
# tan(angle) = opposite/adjacent
# Height = tan(angle) * distance_from_base
height_of_flagpole = math.tan(angle_of_elevation_radians) * distance_from_base

# Rounding the answer to the nearest tenth
height_of_flagpole_rounded = round(height_of_flagpole, 1)

height_of_flagpole_rounded

print("\nheight_of_flagpole_rounded: " + str(height_of_flagpole_rounded))

print("\n*********************************\n")

# Question 3
print("Question 3")
print("An airplane takes off 200 feet in front of a 60 foot building. At what angle of elevation must the plane take off in order to avoid crashing into the building? Assume that the airplane flies in a straight line and the angle of elevation remains constant until the airplane flies over the building.")

# Given values
distance_from_building = 200  # distance from the building in feet
building_height = 60  # height of the building in feet

# Calculating the angle of elevation using tangent
# tan(angle) = opposite/adjacent
# Here, opposite is the building height and adjacent is the distance from the building
angle_of_elevation_radians = math.atan(building_height / distance_from_building)

# Converting the angle from radians to degrees
angle_of_elevation_degrees = math.degrees(angle_of_elevation_radians)

angle_of_elevation_degrees

print("\nangle_of_elevation_degrees: " + str(angle_of_elevation_degrees))

print("\n*********************************\n")

# Question 4
print("Question 4")
print("Brian's kite is flying above a field at the end of 65 m of string. If the angle of elevation to the kite measures 70°, about how high is the kite above Brian's head?")

# Given values for the kite problem
string_length = 65  # length of the kite string in meters
angle_of_elevation = 70  # angle of elevation in degrees

# Calculating the height of the kite above Brian's head using sine
# sin(angle) = opposite/hypotenuse
# Height = sin(angle) * string_length
height_of_kite = math.sin(math.radians(angle_of_elevation)) * string_length

# Rounding the answer to the nearest whole number
height_of_kite_rounded = round(height_of_kite)

height_of_kite_rounded

print("\nheight_of_kite_rounded: " + str(height_of_kite_rounded))

print("\n*********************************\n")

# Question 5
print("Question 5")
print(" a diver is to retrieve an object that is 14m away from the wall of a swimming pool. It is given that the angle of depression of the object from the pool platform is 30°. Find the vertical distance the diver has to swim in order to retrieve the object, correct to 3 significant figures.")

# Given values for the diver problem
distance_from_wall = 14  # distance from the wall to the object in meters
angle_of_depression = 30  # angle of depression in degrees

# Calculating the vertical distance using tangent
# In this scenario, tan(angle) = opposite/adjacent
# Vertical distance = tan(angle) * distance_from_wall
vertical_distance = math.tan(math.radians(angle_of_depression)) * distance_from_wall

# Rounding the answer to three significant figures
vertical_distance_rounded = round(vertical_distance, 3)

vertical_distance_rounded

print("\nvertical_distance_rounded: " + str(vertical_distance_rounded))

print("\n*********************************\n")

# Question 6
print("Question 6")
print("Standing on a cliff 380 meters above the sea, Pat sees an approaching ship and measures its angle of depression, obtaining 9 degrees. Now Pat sights a second ship beyond the first. The angle of depression of the second ship is 5 degrees. How far apart are the ships?")

# Given values
height_of_cliff = 380  # height of the cliff in meters
angle_of_depression_first_ship = 9  # angle of depression to the first ship in degrees
angle_of_depression_second_ship = 5  # angle of depression to the second ship in degrees

# Calculating distances to each ship
distance_to_first_ship = height_of_cliff / math.tan(math.radians(angle_of_depression_first_ship))
distance_to_second_ship = height_of_cliff / math.tan(math.radians(angle_of_depression_second_ship))

# Calculating the difference in distances to find out how far apart the ships are
distance_apart = distance_to_second_ship - distance_to_first_ship

distance_apart

print("\ndistance_apart: " + str(distance_apart))

print("\n*********************************\n")

# Question 7
print("Question 7")
print("A man flies a kite and lets out 100 feet of string. The angle of elevation of the string is 52°. How far away is the man from the spot directly under the kite?")

# Given values for the kite problem
string_length_kite = 100  # length of the kite string in feet
angle_of_elevation_kite = 52  # angle of elevation in degrees

# Calculating the horizontal distance from the man to the spot directly under the kite using cosine
# cos(angle) = adjacent/hypotenuse
# Distance = cos(angle) * string_length
horizontal_distance = math.cos(math.radians(angle_of_elevation_kite)) * string_length_kite

# Rounding the answer to the nearest whole number
horizontal_distance_rounded = round(horizontal_distance)

horizontal_distance_rounded

print("\nhorizontal_distance_rounded: " + str(horizontal_distance_rounded))

print("\n*********************************\n")

# Question 8
print("Question 8")
print("Cade's kite is flying above a field at the end of 50ft of string. If the angle of elevation to the kite measures 70° and Cade is 6 ft tall exactly, about how high is the kite above the ground?")

# Given values for Cade's kite problem
string_length_cade = 50  # length of the kite string in feet
angle_of_elevation_cade = 70  # angle of elevation in degrees
cade_height = 6  # Cade's height in feet

# Calculating the height of the kite above Cade's head using sine
# sin(angle) = opposite/hypotenuse
# Height above Cade's head = sin(angle) * string_length
height_above_cade_head = math.sin(math.radians(angle_of_elevation_cade)) * string_length_cade

# Total height above the ground = height above Cade's head + Cade's height
total_height_above_ground = height_above_cade_head + cade_height

# Rounding the answer to the nearest whole number
total_height_above_ground_rounded = round(total_height_above_ground)

total_height_above_ground_rounded

print("\ntotal_height_above_ground_rounded: " + str(total_height_above_ground_rounded))

print("\n*********************************\n")

# Question 9
print("Question 9")
print("A 14 foot ladder is used to scale a 13 foot wall. At what angle of elevation must the ladder be situated in order to reach the top of the wall?")

# Given values for the ladder problem
ladder_length_wall = 14  # length of the ladder in feet
wall_height = 13  # height of the wall in feet

# Calculating the angle of elevation using sine
# sin(angle) = opposite/hypotenuse
# angle = arcsin(opposite/hypotenuse)
angle_of_elevation_wall_radians = math.asin(wall_height / ladder_length_wall)

# Converting the angle from radians to degrees
angle_of_elevation_wall_degrees = math.degrees(angle_of_elevation_wall_radians)

angle_of_elevation_wall_degrees


print("\nangle_of_elevation_wall_degrees: " + str(angle_of_elevation_wall_degrees))

print("\n*********************************\n")

# Question 10
print("Question 10")
print("An air balloon is 250 m directly above Emily and Emily is 500 m away from Sophia. What is the angle of depression of the balloon to Sophia? ")

# Given values for the balloon problem
height_of_balloon = 250  # height of the balloon above Emily in meters
distance_emily_to_sophia = 500  # horizontal distance between Emily and Sophia in meters

# Calculating the distance from the balloon to Sophia (hypotenuse) using Pythagoras' theorem
# Since the balloon is directly above Emily, the distance from the balloon to Sophia is the same as the distance from Emily to Sophia.
distance_balloon_to_sophia = distance_emily_to_sophia  # this is the adjacent side in the right-angled triangle formed

# Calculating the angle of depression using tangent
# tan(angle) = opposite/adjacent
angle_of_depression_radians = math.atan(height_of_balloon / distance_balloon_to_sophia)

# Converting the angle from radians to degrees
angle_of_depression_degrees = math.degrees(angle_of_depression_radians)

# Rounding the answer to the nearest whole number
angle_of_depression_degrees_rounded = round(angle_of_depression_degrees)

angle_of_depression_degrees_rounded

print("\nangle_of_depression_degrees_rounded: " + str(angle_of_depression_degrees_rounded))

print("\n*********************************\n")

# Question 11
print("Question 11")
print("The angle of elevation of air balloon from point A, which is 200 m away from the point directly below the balloon on the ground, is 28 degrees. If the balloon moves upwards, it is now at an angle of elevation of 38 degrees. How far does the balloon moves upward?")

# Given values for the air balloon problem
distance_from_A_to_balloon_base = 200  # distance from point A to the point directly below the balloon in meters
angle_of_elevation_initial = 28  # initial angle of elevation in degrees
angle_of_elevation_final = 38  # final angle of elevation in degrees

# Calculating the initial height of the balloon using tan(angle) = opposite/adjacent
initial_height = math.tan(math.radians(angle_of_elevation_initial)) * distance_from_A_to_balloon_base

# Calculating the final height of the balloon using tan(angle) = opposite/adjacent
final_height = math.tan(math.radians(angle_of_elevation_final)) * distance_from_A_to_balloon_base

# Calculating the difference in height to find how far the balloon moves upward
height_difference = final_height - initial_height

# Rounding the answer to the nearest whole number
height_difference_rounded = round(height_difference)

height_difference_rounded

print("\nheight_difference_rounded: " + str(height_difference_rounded))

print("\n*********************************\n")

# Question 12
print("Question 12")
print("A man of 175 cm height casts a shadow 190 cm long. Calculate, correct to the nearest degree, the angle of elevation of the sun at this time of day.")

# Given values for the shadow problem
man_height = 175  # man's height in cm
shadow_length = 190  # length of the shadow in cm

# Calculating the angle of elevation using tangent
# tan(angle) = opposite/adjacent = man_height/shadow_length
angle_of_elevation_radians = math.atan(man_height / shadow_length)

# Converting the angle from radians to degrees
angle_of_elevation_degrees = math.degrees(angle_of_elevation_radians)

# Rounding the answer to the nearest tenth (1st decimal place)
angle_of_elevation_degrees_rounded = round(angle_of_elevation_degrees, 1)

angle_of_elevation_degrees_rounded

print("\nangle_of_elevation_degrees_rounded: " + str(angle_of_elevation_degrees_rounded))

print("\n*********************************\n")

# Question 13
print("Question 13")
print("From the top of a vertical cliff 40 m high, the angle of depression of an object that is level with the base of the cliff is 34º. How far is the object from the base of the cliff? Round your answer to the nearest tenth.")

# Given values for the cliff problem
height_of_cliff = 40  # height of the cliff in meters
angle_of_depression = 34  # angle of depression in degrees

# Calculating the distance from the base of the cliff to the object using tangent
# tan(angle) = opposite/adjacent
# distance = opposite/tan(angle)
distance_from_base_to_object = height_of_cliff / math.tan(math.radians(angle_of_depression))

# Rounding the answer to the nearest tenth
distance_from_base_to_object_rounded = round(distance_from_base_to_object, 1)

distance_from_base_to_object_rounded

print("\ndistance_from_base_to_object_rounded: " + str(distance_from_base_to_object_rounded))

print("\n*********************************\n")




