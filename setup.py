from cx_Freeze import *
base = None

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Pheonix List",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Pheonix_List_creator_v6",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]
Execut = [Executable("Pheonix_List_creator.py")]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_option =  {'data': msi_data}
setup(
	name="Pheonix list cmd version",
	version= "1.01" ,
	options = {"bdist_msi": bdist_msi_option},
	executables = Execut
	)
