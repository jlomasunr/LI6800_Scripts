from bpdefs import PROPERTIES, EXEC, ASSIGN, LOOP, SETCONTROL, LOG, WAIT, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="True",pause="False"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,file="/home/licor/resources/lib/list_utility.py"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("q",
	exp="linearList(1500,50,8)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("minWait",
	exp="60"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("firstWait",
	exp="300"),
# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
LOOP(list="400,300,200,100",
	var="co2",
	steps=(
		# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
		SETCONTROL("CO2_s","co2","float"),
		# Open a log file: LOG(file=name [,app=False])
		LOG(open="\"/home/licor/logs/co2_\"+str(co2)",app=False),
		# Log a remark: LOG(rem=string)
		LOG(rem="'automatic file'"),
		# Loop n times: LOOP(count="int_exp" [,var=''] [,mininc=''])
		LOOP(count="len(q)",
			var="i",
			steps=(
				# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
				SETCONTROL("Qin","q[i]","float"),
				# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
				ASSIGN("w",
					exp="firstWait if i==0 else minWait"),
				# Wait for statility: WAIT(min="float_seconds", max="float_seconds" [,early=False])]
				WAIT(min="w",max="2*w",early="False"),
				# Log a data record: LOG([avg='Default'] [,match='Default] [,flr='Default'] [flash='Default'])
				LOG(avg="On"),
			)
		),
		# Close a log file: LOG(close='')
		LOG(close=0),
	)
),
]
