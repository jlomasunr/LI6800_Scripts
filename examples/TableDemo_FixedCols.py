from bpdefs import GROUP, ASSIGN, EXEC, WAIT, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox, DataDict

steps=[
    EXEC(0,file="/home/licor/resources/lib/bpoutput.py"),
    # Create an instance of BPTable()
    EXEC(0,source="table=BPTable()"),
    # Set the top label
    EXEC(0,source="table.setTopLabel(\"Fixed Columns, adding rows\")"),
    # Define 4 columns, with labels and units
    EXEC(0,source="table.define(cols=['abc','def','ghi','jkl'], units=['m/s','','','miles'])"),
    # Fill in 4 rows, each with a label and values (numbers or strings)
	EXEC(0,source="table.add('Case 1', [15.6, 20.2, 33.9, 123.4])"),
	EXEC(0,source="table.add('Case 2', [25.6, 21.2, 34.9, 'missing'])"),
	EXEC(0,source="table.add('Case 3', [35.6, 22.2, 35.9, 'unknown'])"),
	EXEC(0,source="table.add('Case 4', [45.6, 23.2, 36.9, 77.7])"),
    # Dramatic pause....
	WAIT(dur="10",units="Seconds"),
	# Replace the replace 3rd row (index=2), with new label and values
	EXEC(0,source="table.replace(2, 'New!', [1,2,3,4])"),
]
