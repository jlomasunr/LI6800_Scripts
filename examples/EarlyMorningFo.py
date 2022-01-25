from bpdefs import PROPERTIES, WAIT, SETCONTROL, LOG, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="True",pause="False"),
# Wait until time of day: WAIT(until="spec" [,format="tdfstring"])
WAIT(until="5"),
# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
SETCONTROL("PowerState","On",""),
# Wait for a time duration: WAIT(dur="float" [,units='Seconds' (Seconds|Minutes|Hours)])
WAIT(dur="10",units="Minutes"),
# Open a log file: LOG(file=name [,app=False])
LOG(open="\"/home/licor/logs/early\"",app=False),
# Log a data record: LOG([avg='Default'] [,match='Default] [,flr='Default'] [flash='Default'])
LOG(flr="1: FoFm (dark) or FsFm' (light)",
	flash="Rectangular"),
# Close a log file: LOG(close='')
LOG(close=0),
# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
SETCONTROL("PowerState","Sleep",""),
]
