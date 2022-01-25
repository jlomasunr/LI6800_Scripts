from bpdefs import ASSIGN, SHOW, WHILE, COMMENT, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Assign a variable to a Data Dictionary entry: ASSIGN('varname', dd=DataDict('group', 'name' [,bool_logged]) [,track=False] [,optvar='varname'] [dlg=Nothing()))])
ASSIGN("f",
	dd=DataDict('Flow_s','Status'),
	track=True),
# Print to run log: SHOW([items=(list of items)] or [string='string_to_print'])
SHOW(string="'Waiting for chamber to close\\n(for Flow_s to be > 20)'"),
# Loop while something is True: WHILE("bool_expression", [,var='elapsed_seconds'] [,mininc="secs"])
WHILE("f < 20 and t < 60",
	var="t",
	mininc="0",
	steps=(
		# Comment for ui: COMMENT(text)
		COMMENT("<Insert steps here>"),
	)
),
]
