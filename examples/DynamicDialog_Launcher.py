from bpdefs import ASSIGN, EXEC, WAIT, LOOP, IF, SHOW, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("dd",
	exp="'/home/licor/apps/examples/DynamicDialog.py'"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("actions",
	exp="['stumble', 'walk', 'hike', 'skip', 'jump']"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("args",
	exp="{'title':'Test Dialog', 'subtitle':'List is dynamic', 'items':actions}"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="BP.launch(dd, args=args)"),
# Wait for an event: WAIT(event="bool expression"
WAIT(event="BP.isChildDone(dd)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("results",
	exp="BP.childResult(dd)"),
# Loop through a list: LOOP(list=itemList [,var=varname] [,mininc=''])
LOOP(list="actions",
	var="x",
	steps=(
		IF("results.get(x, False)",
			steps=(
				# Print to run log: SHOW([items=(list of items)] or [string='string_to_print'])
				SHOW(string="'{0} was selected'.format(x)"),
			)
		),
	)
),
]
