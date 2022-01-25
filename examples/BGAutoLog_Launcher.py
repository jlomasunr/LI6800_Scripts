from bpdefs import ASSIGN, EXEC, GROUP, WAIT, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("f",
	exp="'/home/licor/apps/examples/BGAutoLog.py'"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="BP.launch(f, args={'duration':10,'interval':15})"),
# Collection: GROUP(enabled, label)
GROUP("True","Do stuff while the child BP logs",
	steps=(
		# Wait for a time duration: WAIT(dur="float" [,units='Seconds' (Seconds|Minutes|Hours)])
		WAIT(dur="10",units="Minutes"),
	)
),
# Collection: GROUP(enabled, label)
GROUP("True","Stop the child BP",
	steps=(
		# Compile and run python: EXEC(scope, [source=code] or [file=filename])
		EXEC(0,source="BP.cancelChild(f)"),
		# Wait for a time duration: WAIT(dur="float" [,units='Seconds' (Seconds|Minutes|Hours)])
		WAIT(dur="10",units="Seconds"),
	)
),
]
