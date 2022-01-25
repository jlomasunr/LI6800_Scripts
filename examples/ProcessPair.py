from bpdefs import ASSIGN, EXEC, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("arg_x",
	exp="BP.getArgs().get('x', 1)"),
# Assign a variable to an expression: ASSIGN('varname', exp="expression" [,dlg=Nothing()])
ASSIGN("arg_y",
	exp="BP.getArgs().get('y', 2)"),
# Compile and run python: EXEC(scope, [source=code] or [file=filename])
EXEC(0,source="BP.setResult({'product':arg_x*arg_y,  'ratio':arg_x/arg_y})"),
]
