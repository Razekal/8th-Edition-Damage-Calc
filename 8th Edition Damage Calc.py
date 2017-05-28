__Author__ = "William Schuy"
__Date__ = "May 2017"


##Program Purpose: To calculate how many shots will be required to kill a target in 8th Edition
##                 Warhammer 40,000, while allowing the user to customize the level of calculation
##                  and repeat steps in case unit abilities confer re-rolls.


# Function Boolean is_integer(String string)
#     Declare Real real_val
#     Try
#         real_val = stringToReal(string)
#     Except
#         Return False
#     End Try
#     Return True
# End Function

def is_integer(string):
    integer_val = 0
    try:
        integer_val = int(string)
    except:
        return False
    return True

#Function Boolean is_real(String string)
#    Declare Real real_val
#    Try
#        real_val = stringToReal(string)
#    Except
#        Return False
#    End Try
#    Return True
#End Function

def is_real(string):
    real_val = 0.0
    try:
        real_val = float(string)
    except:
        return False
    return True

#Function integer integer_input(promp)
#   Declare string number_in
#   Declare integer number
#   Display(prompt)
#   Input number_in
#   While not(is_integer(number_in))
#       Display
#       Display("Integer required (no decimals or letters)")
#       Display(prompt)
#       Input number_in
#   number = stringToInteger(number)
#   return number


def integer_input(prompt):
    number_in = ""
    number = 0
    print(prompt)
    number_in = input()
    while not(is_integer(number_in)):
        print("Integer required (no decimals or letters)")
        print(prompt)
        number_in = input()
    number = int(number_in)
    return number

#Function integer integer_input(promp)
#   Declare string number_in
#   Declare integer number
#   Display(prompt)
#   Input number_in
#   While not(is_real(number_in))
#       Display
#       Display("Floating number required (no letters)")
#       Display(prompt)
#       Input number_in
#   number = stringToReal(number)
#   return number


def float_input(prompt):
    number_float = ""
    number = 0
    print(prompt)
    number_float = input()
    while (not(is_integer(number_float))):
        print("Floating number required (no letters)")
        print(prompt)
        number_float = input()
    number = float(number_float)
    return number


#Function validate_roll(prompt):
#    Declare integer roll
#    input roll = integer_input("Please enter number between 1 to 6 (7 in case of armor save calculations")
#    while (roll < 1) and (roll <=7)
#        roll = integer_input("Please enter number between 1 to 6 (7 in case of armor save calculations")
#End Function

def validate_roll(prompt):
    roll = 0
    roll = integer_input(prompt)
    while ((roll < 1) and (roll <= 7)):
        roll = integer_input(prompt)
    return roll

#Function validate_roll(prompt):
#    Declare integer roll
#    Set roll = float_input(prompt)
#    While (roll < 1)
#        Display "Must be at least 1
#        roll = float_input(prompt)
#    End While
#End Function

def validate_stat(prompt):
    roll = 0
    roll = float_input(prompt)
    while (roll < 1):
        print("Must be greater than 1")
        roll = float_input(prompt)
    return roll

#Function damage_to_kill()
#   Declare integer wounds
#   Declare integer damage
#   set wounds = validate_stat("How many wounds does the target have?"
#   set damage = float_input((validate_stat("How much damage does the weapon deal? Use averages (1d6 = 3.5, 1d3 = 2): "))
#   total_hits = wounds / damage
#   total_hits = round(total_hits, 1)
#   Display (total_hits, + " total shots currently.")
#End Function

def damage_to_kill():
    wounds = 0
    damage = 0.0
    wounds = validate_stat("How many wounds does the target have? ")
    damage = float_input(validate_stat("How much damage does the weapon deal? Use averages (1d6 = 3.5, 1d3 = 2): "))
    total_hits = wounds / damage
    total_hits = round(total_hits, 1)
    print(total_hits, " total shots currently.")
    return total_hits

#Function damaging_hits(total_hits):
#   Declare integer strength
#   Declare integer toughness
#   Declare integer penetration
#   set strength = integer_input("What is the strength of the weapon (shooting) or attacks (close combat)"
#   set toughness = integer_input("What is the toughness statistic of the target?" )
#   if strength >= toughness * 2:
#       penetration = 83.3
#   elif strength > toughness:
#       penetration = 66
#   elif strength == toughness:
#       penetration = 50
#   elif strength * 2 <= toughness:
#       penetration = 16.6
#   elif toughness > strength:
#       penetration = 33.3
#   End if
#   total_hits = float(total_hits / (float(penetration) / 100))
#   total_hits = round(total_hits, 1)
#   print(total_hits)
#   return total_hits
#End Function

def damaging_hits(total_hits):
    strength = 0
    toughness = 0
    penetration = 0
    strength = integer_input("What is the strength of the weapon (shooting) or attacks (close combat)")
    toughness = integer_input("What is the toughness statistic of the target?" )
    if strength >= toughness * 2:
        penetration = 83.3
    elif strength > toughness:
        penetration = 66
    elif strength == toughness:
        penetration = 50
    elif strength * 2 <= toughness:
        penetration = 16.6
    elif toughness > strength:
        penetration = 33.3
    total_hits = float(total_hits / (float(penetration) / 100))
    total_hits = round(total_hits, 1)
    print(total_hits)
    return total_hits

#Function armor_cover_save(total_hits):
#   Declare integer save
#   Set save = validate_roll("What is the die roll required to successfully save? Treat not having a save as 7+")
#   If save >= 7:
#      save = 100
#   elif save == 2:
#      save = 16.66
#   elif save == 3:
#      save = 33.33
#   elif save == 4:
#      save = 50
#   elif save == 5:
#      save = 66.66
#   elif save == 6:
#      save = 83.33
#   End If
#   Set total_hits = total_hits / (save / 100)
#   Set total_hits = round(total_hits, 0)
#   Display(total_hits, + "total hits")
#   return total_hits
#End Function


def armor_cover_save(total_hits):
    save = 0
    save = validate_roll("What is the die roll required to successfully save? Treat not having a save as 7+")
    if save >= 7:
        save = 100
    elif save == 2:
        save = 16.66
    elif save == 3:
        save = 33.33
    elif save == 4:
        save = 50
    elif save == 5:
        save = 66.66
    elif save == 6:
        save = 83.33
    total_hits = total_hits / (save / 100)
    total_hits = round(total_hits, 0)
    print(total_hits, " total hits")
    return total_hits

#Function chance_to_hit(total_hits):
#    Declare integer hit_chance
#    Set hit_chance = validate_roll("dice roll to hit? ")
#    If hit_chance == 1:
#        hit_chance = 100
#    elif hit_chance == 2:
#        hit_chance = 83.33
#    elif hit_chance == 3:
#        hit_chance = 66.66
#    elif hit_chance == 4:
#        hit_chance = 50
#    elif hit_chance == 5:
#        hit_chance = 33.33
#    elif hit_chance == 6:
#        hit_chance = 16.666
#    End If
#    Set total_hits = total_hits / (hit_chance / 100)
#    Set total_hits = round(total_hits, 0)
#    Display(total_hits, " hits")
#    return total_hits
#End Function

def chance_to_hit(total_hits):
    hit_chance = 0
    hit_chance = validate_roll("dice roll to hit? ")
    if hit_chance == 1:
        hit_chance = 100
    elif hit_chance == 2:
        hit_chance = 83.33
    elif hit_chance == 3:
        hit_chance = 66.66
    elif hit_chance == 4:
        hit_chance = 50
    elif hit_chance == 5:
        hit_chance = 33.33
    elif hit_chance == 6:
        hit_chance = 16.666
    total_hits = total_hits / (hit_chance / 100)
    total_hits = round(total_hits, 0)
    print(total_hits, " hits")
    return total_hits

#Function outtro(total_hits):
#    Display "All calculations resulted in: ", total_hits, " hits. Good luck!"

def outtro(total_hits):
    print("All calculations resulted in: ", total_hits, " hits. Good luck!")

#Function menu_input(prompt):
#    Declare String menu_select
#    Set menu_select = input(prompt)
#    While (not("Damaging Hits") or not("Armor Saves") or not("Chance to Hit") or not("Finalize")):
#        Display("Must select ""Damaging Hits"", ""Armor Saves"", ""Chance to hit"", or ""Finalize""")
#        Set menu_select = input(prompt)
#    End While
#    return menu_select

def menu_input(prompt):
    menu_select = ""
    menu_select = input(prompt)
    while (not("Damaging Hits") or not("Armor Saves") or not("Chance to Hit") or not("Finalize")):
        print("Must select ""Damaging Hits"", ""Armor Saves"", ""Chance to hit"", or ""Finalize""")
        menu_select = input(prompt)
    return menu_select

#Function hits_to_terminate():
#    Declare float total_hits
#    Declare string menu_select
#    Declare Boolean more_check
#    Set more_checks = True
#    Set total_hits = damage_to_kill()
#    While(more_checks == True):
#        menu_select = menu_input("Select between ""Damaging Hits"", ""Armor Saves"", ""Chance to Hit"","
#                                """or Finalize: """)
#        if menu_select == "Damaging Hits":
#            total_hits = damaging_hits(total_hits)
#        elif menu_select == "Armor Saves":
#            total_hits = armor_cover_save(total_hits)
#        elif menu_select == "Chance to Hit":
#            total_hits = chance_to_hit(total_hits)
#        elif menu_select == "Finalize":
#             more_checks = False
#   End While
#    outtro(total_hits)
#End Function

def hits_to_terminate():
    total_hits = 0.0
    menu_select = ""
    more_checks = False
    more_checks = True
    total_hits = damage_to_kill()
    while(more_checks == True):
        menu_select = menu_input("Select between ""Damaging Hits"", ""Armor Saves"", ""Chance to Hit"","
                                 """or Finalize: """)
        if menu_select == "Damaging Hits":
            total_hits = damaging_hits(total_hits)
        elif menu_select == "Armor Saves":
            total_hits = armor_cover_save(total_hits)
        elif menu_select == "Chance to Hit":
            total_hits = chance_to_hit(total_hits)
        elif menu_select == "Finalize":
             more_checks = False
    outtro(total_hits)

hits_to_terminate()