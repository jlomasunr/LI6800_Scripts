from bpdefs import PROPERTIES, EXEC, ASSIGN, DIALOG, IF, RETURN, LOOP, SETCONTROL, WAIT, LOG, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="True",pause="False"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(1,file="/home/licor/resources/lib/list_utility.py"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("start",
	exp="2000",
	dlg=EditBox("'Starting value'", units="'µmol m⁻² s⁻¹'", desc="'Qin set point'")),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("stop",
	exp="10",
	dlg=EditBox("'Final value'", units="'µmol m⁻² s⁻¹'", desc="'Qin set point'")),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("count",
	exp="10",
	dlg=EditBox("'Number of set points'", desc="'Recommended: 8 to 12'")),
# Open a dialog: DIALOG(title=string [,sub=string] [,text=string] [,items=list_of_edit_items] [,buttons=list_of_buttons] [var=pressed_btn_name])
DIALOG(title="'Light Response Curve'",
	sub="'Automatically generates linearly spaced setpoints'",
	items="start,stop,count",
	buttons="'Cancel','Continue'",
	var="button"),
IF("button == 'Cancel'",
	steps=(
		RETURN(),
	)
),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("setpoints",
	exp="linearList(start,stop,count)"),
# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
LOOP(list="setpoints",
	var="x",
	steps=(
		# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
		SETCONTROL("Qin","x","float"),
		# Wait for statility: WAIT(min="float_seconds", max="float_seconds" [,early=False])]
		WAIT(min="60",max="120",early="False"),
		# Log a data record: LOG([avg='Default'] [,match='Default] [,flr='Default'] [flash='Default'])
		LOG(),
	)
),
]
