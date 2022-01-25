from bpdefs import SETCONTROL, ASSIGN, LOOP, LOG, IF, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox, DataDict

steps=[
# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
SETCONTROL("VPD_leaf","1.8","float"),
# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
SETCONTROL("Tleaf","23","float"),
# Assign a variable to a Data Dictionary entry: ASSIGN('varname', dd=DataDict('group', 'name' [,bool_logged]) [,track=False] [,optvar='varname'] [dlg=Nothing()))])
ASSIGN("Q",
	dd=DataDict('PPFD_out','Meas'),
	track=True),
# Loop for a duration: LOOP(dur="float" [,units='Seconds' Second|Minutes|Hours ] [,var=''] [,mininc=''])
LOOP(dur="1441",
	units="Minutes",
	mininc="300",
	steps=(
		# Log a data record: LOG([avg='Default'] [,match='Default'] [,matchH2O='Default'] [,flr='Default'] [flash='Default'])
		LOG(),
		IF("Q<10",
			steps=(
				# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
				SETCONTROL("VPD_leaf","1.2","float"),
				# Log a remark: LOG(rem=string)
				LOG(rem="VPD_leaf updated to 1.2 based on Q"),
			)
		),
		IF("Q<10",
			steps=(
				# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
				SETCONTROL("Tleaf","21","float"),
				# Log a remark: LOG(rem=string)
				LOG(rem="Tleaf updated to 21C based on Q"),
			)
		),
		IF("Q>=10",
			steps=(
				# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
				SETCONTROL("VPD_leaf","1.8","float"),
				# Log a remark: LOG(rem=string)
				LOG(rem="VPD_leaf updated to 1.8 based on Q"),
			)
		),
		IF("Q>=10",
			steps=(
				# Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
				SETCONTROL("Tleaf","23","float"),
				# Log a remark: LOG(rem=string)
				LOG(rem="Tleaf updated to 23C based on Q"),
			)
		),
	)
),
]
