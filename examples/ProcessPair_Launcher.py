from bpdefs import ASSIGN, EXEC, WAIT, LOOP, SHOW, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("worker_file",
	exp="'/home/licor/apps/examples/ProcessPair.py'"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="BP.launch(worker_file, args={'x':8.2,'y':24.3})"),
# Wait for an event: WAIT(event="bool expression"
WAIT(event="BP.isChildDone(worker_file)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("results",
	exp="BP.childResult(worker_file)"),
# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
LOOP(list="list(results.keys())",
	var="x",
	steps=(
		# Print to run log: SHOW([items=(list of items)] or [string='string_to_print'])
		SHOW(string="'{0} = {1}'.format(x, results[x])"),
	)
),
]
