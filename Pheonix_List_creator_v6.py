#!/usr/bin/env python
import json
import os
""" You can see that"""
if "Pheonix_Save_File" in os.listdir():
    Dict_file = open("Pheonix_Save_File/PheonixList.txt", "r")
    Dict_List = json.load(Dict_file)
else:
    Dict_List = {}

Changed = False


def Action_Choice(action):
    """
    This function is the central board, it takes the information from the user
    and set him on correct path to what he wish to do in the program"""
    if action == "Add":
        return Add_Info_Show()
    elif action == "Remove":
        return remove_show()
    elif action == "View Show":
        return view_Shows()
    elif action == "View Genre":
        return view_Genre()
    elif action == "Quit":
        return Quit(action)
    elif action == "Save":
        return Save_file()


def view_Shows():
    """
    Here is the View Show. This function contain everything to see name of the
    shows saved inside a type and a genre."""

    view = input("Where do you wanna view? (Type, Genre)").split(", ")
    if len(view) != 2:
        print("Write in correctly")
        return False
    elif view[0] not in Dict_List.keys():
        print("You writed the Type wrong.")
    elif view[1] not in Dict_List[view[0]].keys():
        print("You writed the Genre wrong.")
    else:
        while view != "Back":
            for a in Dict_List[view[0]]:
                for b in Dict_List[view[0]][view[1]]:
                    print(b)
            view_desc = input(
                "To view desc write the show name else type back:")
            if view_desc == "Back":
                return "Back"
            else:
                if view_desc in Dict_List[view[0]][view[1]].keys():
                    print(Dict_List[view[0]][view[1]][view_desc])
                else:
                    print("Write the name correctly")


def view_Genre():
    """
    View Genre is a function made to let you see all the genre you have made
    in certain types
    """
    print(Dict_List.keys())
    view_g = input("Write in the type you want to see the Genre of: ")
    if view_g not in Dict_List.keys():
        print("No Type with that name.")
    else:
        print(sorted(Dict_List[view_g].keys()))


def Add_Info_Show():
    """ Add info show is a function that was added pretty late in the
    development. It purpose is to take all the info from user like type, genre
    , show name and description then send it to the Add_show function.
    """
    T_G = input("Write in (Type, Genre, Show): ").split(", ")
    if len(T_G) != 3:
        print("You need to write it correctly like the exampel")
        return False
    Desc = input("Write in a description? ")
    if T_G[0] not in Dict_List.keys():
        return Add_Show(T_G, Desc, Overwrite=False)
    elif T_G[1] not in Dict_List[T_G[0]].keys():
        return Add_Show(T_G, Desc, Overwrite=False)
    elif T_G[2] in Dict_List[T_G[0]][T_G[1]].keys():
        Overwrite = input(
            "Show allready exist. Do You wanna overwrite? Y or N"
        )
        if Overwrite == "Y":
            return Add_Show(T_G, Desc, Overwrite=True)
        if Overwrite == "N":
            return False
    else:
        return Add_Show(T_G, Desc, Overwrite=False)


def Add_Show(T_G, Desc, Overwrite=False):
    """ Add_Show the function that put together all the information it got from
    Add_Info_show and creates the show. But if the type or genre dosn't exsist
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


def remove_show():
    """This function purpose is to remove show.
    This function made incase the user don't want a show on
     the list anymore or if he typed the name wrong."""
    global Dict_List, Changed
    delete_Show = input("write it like this (Type, Genre, name)").split(", ")
    if len(delete_Show) != 3:
        print("Write in correctly")
        return False
    Changed = True
    Dict_List[delete_Show[0]][delete_Show[1]].pop(delete_Show[2])
    return Dict_List


def Save_file():
    """Save_File function purpose is to save everything done into the txt Dict_file
     inside of
     a map. Normaly it would get error if the file or map dosn't exsist
     But coded it so it will automaticly create the map and the file if they
     don't exsist in the same map as the program file"""
    global Changed
    extra_safety = input(
        "You sure you wanna overwrite old data? Y or N: "
    )
    if extra_safety == "Y":
        if "Pheonix_Save_File" not in os.listdir():
            os.mkdir("Pheonix_Save_File")
        Saving_file = open("Pheonix_Save_File/PheonixList.txt", "w")
        json.dump(Dict_List, Saving_file)
        Saving_file.close()
        Changed = False
    elif extra_safety == "N":
        return False


def Quit(action):
    """The function end the program turning it of.
    But made a safety measure incase somebody forgot to save that it will give
    them a warning before it quit letting them save it if they want to."""
    if Changed is False:
        return action
    if Changed is True:
        print("You havn't saved recent List.")
        You_sure = input("You sure you wanna Quit?: Y or N ")
        if You_sure == "Y":
            return action
        if You_sure == "N":
            return Save_file()


Argument_AC = ""
while Argument_AC != "Quit":
    print(Dict_List.keys())
    Action = input(
        "Option: View Show, View Genre, Add, Remove, Save, or Quit:")
    Argument_AC = Action_Choice(Action)
