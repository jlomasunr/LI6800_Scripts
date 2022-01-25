from bpdefs import PROPERTIES, ASSIGN, WHILE, LOG, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox

steps=[
# Set program properties: PROPERTIES([verbose=False] [,pause=False])
PROPERTIES(verbose="False",pause="False"),
# Assign a variable to a Data Dictionary entry: ASSIGN('varname', dd=DataDict('group', 'name' [,bool_logged]) [,track=False] [,optvar='varname'] [dlg=Nothing()))])
ASSIGN("f",
	dd=DataDict('PPFD_out','Meas'),
	track=True),
# Loop while something is True: WHILE("bool_expression", [,var='elapsed_seconds'] [,mininc="secs"])
WHILE("f>5",
	mininc="10*60",
	steps=(
		# Log a data record: LOG([avg='Default'] [,match='Default] [,flr='Default'] [flash='Default'])
		LOG(),
	)
),
]
