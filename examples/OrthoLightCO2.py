from bpdefs import PROPERTIES, EXEC, ASSIGN, SHOW, LOOP, SETCONTROL, WAIT, LOG, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="True",pause="False"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(1,file="/home/licor/resources/lib/list_utility.py"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("q",
	exp="linearList(50,1500,12,rounded=0)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("c",
	exp="linearList(50,1000,12,rounded=0)"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="(q,c)=makeOrtho((q,c))"),
# Print to run log: SHOW([items=(list of items)] or [string='string_to_print'])
SHOW(items="q,c"),
# Loop n times: LOOP(count="int_exp" [,var=''] [,mininc=''])
LOOP(count="len(q)",
	var="i",
	steps=(
		# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
		SETCONTROL("Qin","q[i]","float"),
		# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
		SETCONTROL("CO2_s","c[i]","float"),
		# Wait for statility: WAIT(min="float_seconds", max="float_seconds" [,early=False])]
		WAIT(min="120",max="300",early="False"),
		# Log a data record: LOG([avg='Default'] [,match='Default] [,flr='Default'] [flash='Default'])
		LOG(),
	)
),
]
