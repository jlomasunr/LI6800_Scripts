from bpdefs import PROPERTIES, EXEC, ASSIGN, LOOP, SETCONTROL, WAIT, LOG, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="False",pause="False"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,file="/home/licor/resources/lib/list_utility.py"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("q",
	exp="linearList(1500,10,8)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("redpct",
	exp="lambda x: int(100-(x/1500.)*20)"),
# Loop n times: LOOP(count="int_exp" [,var=''] [,mininc=''])
LOOP(count="len(q)",
	var="i",
	steps=(
		# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
		SETCONTROL("Qin","q[i]","float"),
		# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
		SETCONTROL("Color_Qin","'r'+str(redpct(q[i]))","string"),
		# Wait for statility: WAIT(min="float_seconds", max="float_seconds" [,early=False])]
		WAIT(min="60",max="120",early="False"),
		# Log a data record: LOG([avg='Default'] [,match='Default] [,flr='Default'] [flash='Default'])
		LOG(),
	)
),
]
