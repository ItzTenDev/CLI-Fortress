from math import *
from random import *
from src.modules.formated_terminal import *
from src.modules.terminal import *

from time import *

# Must be in every single command files.
def export() -> dict:
    name = "game-jdl"
    description = "Start a game of the Jeu de l'oie"
    args = ["players", "dice(s)", "dice_faces"]
    usage = name + "".join([" <" + arg + ">" for arg in args])
    permission = 0 
    
    return { "name" : name, "description" : description, "args" : args, "usage" : usage, "permission" : permission }


# Must be in every single command files.
def execute(user, args, database) -> None:
    # So it will have the part allowing the user to start the game with x players
    player_count = int(args[0])
    dice_count = int(args[1])
    dice_faces = int(args[2])
    
    # Data for the game
    win_condition = False
    dices = [0 for i in range(dice_count)]
    cases_count = 63
    player_positions = [0 for i in range(player_count)]
    goose_cases = [5, 9, 14, 18, 23, 27, 33, 36, 41, 45, 50, 54, 59]
    
    winner = 0
    
    messages = {
        "6" : "§7Wow §6Player %p%§7 crossed the bridge, they instantly jump to case 12 !",
        "19": "§7Oh, looks like §6Player %p%§7 will spend their turn at a hotel !",
        "32": "§7Apparently §6Player %p%§7 can reroll the dice a second time !",
        "42": "§7Meh, §6Player %p%§7 seem to have lost their path in the labyrinth, they went back on case 30...",
        "52": "§7Oh, looks like §6Player %p%§7 is spending a turn in jail...",
        "58": "§7Oh... §6Player %p%§7 is very unlucky, they fell off the roof and go back to square one !",
    }
    
    # If you get case : 
    # Bridge    : 6 -> goto case 12
    # Hotel     : 19 -> skip turn
    # Well      : 32 -> reroll dice
    # Labyrinth : 42 -> goto 30
    # Prison    : 52 -> skip turn
    # Fall roof : 58 -> goto 1, lol.

    # Goose     : Double steps
    # Dices adds up
    # Goose positions : 5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59
    
    # Turn :
    # - Player rolls dice
    # - Player moves
    # - Player earn the spec of its case
    # - Next player
    
    def get_dices_sum():
        return sum(dices)
    
    def roll_dices():
        for i in range(len(dices)):
            dices[i] = randint(1, dice_faces)
    
    def display_pos():
        print("\n\n-----------------------------")
        
        for i in range(player_count):
            player = i + 1
            pos = player_positions[i]
            
            printf("§ePlayer " + str(player) + " §r| §7case §f" + str(pos), False)
        
        print("-----------------------------\n")
    
    while win_condition == False:
        sleep(2)
        run_command("cls")
        
        for player in range(player_count):
            sleep(0.5)

            display_pos()
            
            match player_positions[player]:
                case 19:
                    printf(messages["19"].replace("%p%", str(player + 1)), False)
                    player_positions[player] = 20
                    continue
                case 52:
                    printf(messages["52"].replace("%p%", str(player + 1)), False)
                    player_positions[player] = 53
                    continue
            
            printf("§6Player " + str(player + 1) + " : §7 ", False)
            player_action = input(">>> ")
            
            match player_action:
                case "roll":
                    printf("\n§e> §fPlayer " + str(player + 1) + " §7rolled the dice...", False)
                    sleep(0.7)
                    roll_dices()
                    
                    printf("§e> §fPlayer " + str(player + 1) + " §7obtained §2" + " + ".join([str(i) for i in dices]) + " §7= §f§l" + str(get_dices_sum()), False)
                    sleep(0.5)
                    printf("§e> §fPlayer " + str(player + 1) + " §7advances §f" + str(get_dices_sum()) + " cases", False)
                    
                    player_positions[player] += get_dices_sum()
                    
                    printf("\n§e> §fPlayer " + str(player + 1) + " §7reaches their square: §f" + str(player_positions[player] - get_dices_sum()) + " §r-> §2" + str(player_positions[player]), False)
            
            sleep(0.5)
            if str(player_positions[player]) in messages: printf("\n" + messages[str(player_positions[player])].replace("%p%", str(player + 1)), False)
            elif player_positions[player] in goose_cases: printf(("\n§7Oh... §6Player %p%§7 fell on a goose square, they double their case jumps ! + " + str(get_dices_sum())).replace("%p%", str(player + 1)), False)
            
            sleep(0.7)
            if player_positions[player] in goose_cases: player_positions[player] += get_dices_sum()
            
            match player_positions[player]:
                case 6: 
                    player_positions[player] = 12
                case 32:
                    printf("\n§e> §fPlayer " + str(player + 1) + " §7rolled the dice... again !", False)
                    sleep(0.7)
                    roll_dices()
                    
                    printf("§e> §fPlayer " + str(player + 1) + " §7obtained §2" + " + ".join([str(i) for i in dices]) + " §7= §f§l" + str(get_dices_sum()), False)
                    sleep(0.5)
                    printf("§e> §fPlayer " + str(player + 1) + " §7advances §f" + str(get_dices_sum()) + " cases", False)
                    
                    player_positions[player] += get_dices_sum()
                    
                    printf("\n§e> §fPlayer " + str(player + 1) + " §7reaches their square: §f" + str(player_positions[player] - get_dices_sum()) + " §r-> §2" + str(player_positions[player]), False)
            
                case 42:
                    player_positions[player] = 30
                case 58:
                    player_positions[player] = 1
            
            if player_positions[player] >= 63: 
                win_condition = True
                winner = player + 1
                break
        
    display_pos()   
    printf("🎉 " + "§6Player " + str(winner) + " §fWON !! Because they are so smart !" + "🎉", False)
                    