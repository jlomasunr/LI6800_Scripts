from bpdefs import EXEC, GROUP, ASSIGN, Nothing, CheckBox, Text, Button, DropDown, RadioBtns, EditBox, DataDict

steps=[
EXEC(0,file="/home/licor/resources/lib/bpoutput.py"),
GROUP("True","Graph",
	steps=(
		ASSIGN("xyg",
			exp="BPGraph()"),
		ASSIGN("x", exp="[1,2,3,4,5,6]"),
		ASSIGN("z", exp="[i*i*i for i in x]"),
		ASSIGN("y", exp="[i*i for i in x]"),
		ASSIGN("y1", exp="[i*i/2 for i in x]"),
		EXEC(0,source="xyg.clear()"),
		EXEC(0,source="xyg.labelAxes(xbottom='X value',yleft='Y value',yright='Z value')"),
		EXEC(0,source="xyg.plotLeft(x,y,legend='squared')"),
		EXEC(0,source="xyg.plotLeft(x,y1,legend='squared', line='--')"),
		EXEC(0,source="xyg.plotRight(x,z,legend='cubed',symbol='o', size=10, color='aqua', line='-')"),
		EXEC(0,source="xyg.setTitle('BP Demo Graph')"),
		# Define some labels for the x vs y plot
		ASSIGN("y_data_labels",
			exp="['Lab '+chr(65+i) for i in range(len(x))]"),
		# Put markers above the x,y points, include them in the 'squared' legen
		EXEC(0,source="xyg.markPtLeft(x, y, y_data_labels, align='|^', legend='squared')"),
		# Place a marker with a solid diamond with text to the right of it
		EXEC(0,source="xyg.markPtRight(2, 200, '(2, 200)', align='>-', color='red', fill=True, symbol='Diamond')"),
		# Show the value of pi on the bottom axis, with a dotted dark green vertical line, label to the right of the line
		EXEC(0,source="xyg.markLineBot(math.pi, line='.', size=14, color='#007700',text=\"\u03c0\", align='>v')  "),
		# Show the value of e**pi on the left axis, label to the right, dotted line
		EXEC(0,source="xyg.markLineLeft(math.e**math.pi, line='-.', width=2, size=14, color='orange',text=\"e<sup>\u03c0</sup> value\", align='<^')  "),
		# Use a dashed line to the boiling point of water in degress F on the right axis
		EXEC(0,source="xyg.markLineRight(212, line='--', size=12, color='grey',text=\"Water boils (F)\", align='>^')  "),
		# Display the result
		EXEC(0,source="xyg.show()"),
	)
),
]
