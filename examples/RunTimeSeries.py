from bpdefs import LOOP, SETCONTROL, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Loop through lines in a file: LOOP(file='filename' parse=bool delim='Tab' [,skip=0] [,var=varname] [,mininc=''])
LOOP(file="\"/home/licor/logs/light_series.txt\"",
	parse=True,
	delim="Comma",
	skip="1",
	var="q",
	mininc="2",
	steps=(
		# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
		SETCONTROL("Qin","q[1]","float"),
	)
),
]
