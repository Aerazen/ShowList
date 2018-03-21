#!/usr/bin/env python
import json
import os

""" You can see that"""
path = os.getenv('APPDATA')
if "Pheonix_Save_File" in os.listdir(path):
    if "PheonixList.json" in os.listdir(path + "/Pheonix_Save_File"):
        Dict_file = open(path + "/Pheonix_Save_File/PheonixList.json", "r")
        Dict_List = json.load(Dict_file)
    else:
        Dict_List = {}
else:
    Dict_List = {}
Help_TF = False
Changed = False


def Action_Choice(action):
    """
    This function is the central board, it takes the information from the user
    and set him on correct path to what he wish to do in the program"""
    global Help
    if action == "Add":
        return Add_Info_Show()
    elif action == "Remove":
        return remove()
    elif action == "View":
        return view_Show()
    elif action == "Quit":
        return Quit(action)
    elif action == "Save":
        return Save_file()
    elif action == "Help":
        return Help()
    elif action == "Info":
        return Info()


def view_Show():

    """
    Here is the View Show. This function contain everything to see name of the
    shows saved inside a type and a genre."""
    if Help_TF is True:
        print("Here you have to write in type f.eks: Movie")
        print("")
    for t in Dict_List:
        print(t)
    view_t = input("Write in Type")
    if view_t not in Dict_List.keys():
        print("The type you wrote in dosn't exist.")
    else:
        for a in Dict_List:
            for g in Dict_List[view_t]:
                print(g)
        view_g = input("write in the genre:")
        if view_g not in Dict_List[view_t].keys():
            print("No Genre with that name exsist")
        else:
            view_desc = ""
            while view_desc != "Back":
                for a in Dict_List[view_t]:
                    for b in Dict_List[view_t][view_g]:
                        print(b)
                view_input = "To view desc, write the name of a show, "
                view_desc = input(view_input + "or type Back ")
                if view_desc == "Back":
                    return "Back"
                else:
                    if view_desc in Dict_List[view_t][view_g].keys():
                        print(Dict_List[view_t][view_g][view_desc])
                    else:
                        print("Write the name correctly")


def Add_Info_Show():
    """ Add info show is a function that was added pretty late in the
    development. It purpose is to take all the info from user like type, genre
    , show name and description then send it to the Add_show function.
    """
    if Help_TF is True:
        print("")
        print("Example: Movie, Action, Avengers")
        print("The Type and Genre will automaticly be added")
        print("Be careful to write them all correctly")
        print("You can change description of a show by adding the show again")
        print("")
    T_G = input("Write in (Type, Genre, Show): ").split(", ")
    if len(T_G) != 3:
        print("You need to write it correctly like the example")
        return False
    if Help_TF is True:
        print("")
        print("Write in info or what you think about the show")
        print("")
    Desc = input("Write in a description? ")
    if T_G[0] not in Dict_List.keys():
        return Add_Show(T_G, Desc, Overwrite=False)
    elif T_G[1] not in Dict_List[T_G[0]].keys():
        return Add_Show(T_G, Desc, Overwrite=False)
    elif T_G[2] in Dict_List[T_G[0]][T_G[1]].keys():
        Overwrite_input = "Show allready exist. Do You wanna overwrite?Y or N "
        Overwrite = input(Overwrite_input)
        if Overwrite == "Y":
            return Add_Show(T_G, Desc, Overwrite=True)
        if Overwrite == "N":
            return False
    else:
        return Add_Show(T_G, Desc, Overwrite=False)


def Add_Show(T_G, Desc, Overwrite=False):
    """ Add_Show the function that put together all the information it got from
    Add_Info_show and creates the show. But if the type or genre dosn't exist
    it will automaticly create them aswell."""
    global Dict_List, Changed
    Dict_List.setdefault(T_G[0], {})
    Dict_List[T_G[0]].setdefault(T_G[1], {})
    if Overwrite is True:
        Dict_List[T_G[0]][T_G[1]].update({T_G[2]: Desc})
        Changed = True
        print("Overwrite Successful")
        return Dict_List
    if Overwrite is False:
        Changed = True
        Dict_List[T_G[0]][T_G[1]].setdefault(T_G[2], Desc)
        return Dict_List


def remove():
    if Help_TF is True:
        print("")
        print("Here you can choice what you want to remove.")
        print("If you remove type you will also remove genre and show auto")
        print("That exsist within that type.")
        print("If you remove Genre you remove all show in that type genre")
        print("")
    remove_What = input("Type, Genre or Show: ")
    if remove_What == "Show":
        return remove_Show()
    elif remove_What == "Genre":
        return remove_Genre()
    elif remove_What == "Type":
        return remove_Type()


def remove_Show():
    """This function purpose is to remove show."""
    global Dict_List, Changed
    if Help_TF is True:
        print("")
        print("Example: Movie, Comedy, Hangover")
        print("")
    D_S_Text = "Write it like this (Type, Genre, Name) "
    d_Show = input(D_S_Text).split(", ")
    if len(d_Show) != 3:
        print("Write in correctly")
    elif d_Show[0] in Dict_List.keys():
        if d_Show[0][1] in Dict_List[d_Show[0]].keys():
            if d_Show[0][1][2] in Dict_List[d_Show[0]][d_Show[1]].keys():
                Changed = True
                Dict_List[d_Show[0]][d_Show[1]].pop(d_Show[2])
                print("Show removed")
                return Dict_List
            else:
                print("Show dosn't exist")
        else:
            print("The Genre dosn't exist")
    else:
        print("The type dosn't exist")


def remove_Genre():
    """This function purpose is to remove Genre."""
    global Dict_List, Changed
    if Help_TF is True:
        print("")
        print("Example: Anime, Drama")
        print("")
    d_Genre = input("write it like this (Type, Genre) ").split(", ")
    if len(d_Genre) != 2:
        print("The Genre dosn't exist")
    elif d_Genre[0] in Dict_List.keys():
        if d_Genre[0][1] in Dict_List[d_Genre[0]].keys():
            Changed = True
            Dict_List[d_Genre[0]].pop(d_Genre[1])
            return Dict_List
        else:
            print("The Genre dosn't exist")
    else:
        print("The Type dosn't exist")


def remove_Type():
    """This function purpose is to remove Type."""
    global Dict_List, Changed
    if Help_TF is True:
        print("")
        print("Example: Movie")
        print("")
    for a in Dict_List:
        print(a)
    d_Type = input("write in the type you wanna delete ")
    if d_Type in Dict_List.keys():
        Changed = True
        Dict_List.pop(d_Type)
        return Dict_List
    else:
        print("Write in correctly")


def Save_file():
    """Save_File function purpose is to save everything done
     into the txt Dict_file, inside of
     a map. Normaly it would get error if the file or map dosn't exist
     But coded it so it will automaticly create the map and the file if they
     don't exist in the same map as the program file"""
    global Changed
    the_info = "You overwriting old data, wanna continue? Y or N: "
    extra_safety = input(the_info)
    if extra_safety == "Y":
        if "Pheonix_Save_File" not in os.listdir(path):
            os.mkdir(path + "/Pheonix_Save_File")
        Saving_file = open(path + "/Pheonix_Save_File/PheonixList.json", "w")
        json.dump(Dict_List, Saving_file)
        Saving_file.close()
        Changed = False
        print("Save Completed")
    elif extra_safety == "N":
        print("Save aborted")
        return False


def Quit(action):
    """The function end the program turning it of.
    But made a safety measure incase somebody forgot to save that it will give
    them a warning before it quit letting them save it if they want to."""
    if Changed is False:
        return action
    if Changed is True:
        print("You havn't saved recent List.")
        You_sure = input("Wanna contiune to quit?: Y or N ")
        if You_sure == "Y":
            return action
        if You_sure == "N":
            return Save_file()


def Info():
    print("")
    print("")
    print("Program name: Pheonix List Creator")
    print("Author: Kai-Andreas Ruud Pettersen (Github name : Aerazen)")
    print("Version: 1.4 CMD Version")
    print("")
    print("")


def Help():
    global Help_TF
    if Help_TF is False:
        print("Help Activated, write Help to deactivate")
        Help_TF = True
        return Help_TF
    if Help_TF is True:
        print("Help deactivated, write Help to activate")
        Help_TF = False
        return Help_TF


print("Welcome to List creator")
Argument_AC = ""
while Argument_AC != "Quit":
    for a in Dict_List:
        print(a)
    if Help_TF is True:
        print("Write in one of the option exactly as it's shown.")
        if Dict_List == {}:
            print("")
            print("To start your list you have to Add first")
            print("After you added something, you will get the option view,")
            print("and remove.")
            print("")
    if Dict_List == {}:
        Action_input = ""
    else:
        Action_input = "View, Remove, "
    if Help_TF is False:
        Help_status = "(OFF)"
    elif Help_TF is True:
        Help_status = "(ON)"
    Action_input2 = "Add, Save, Quit, Info or Help " + Help_status
    Action = input("Option: " + Action_input + Action_input2)
    Argument_AC = Action_Choice(Action)
