from bpdefs import ASSIGN, LOOP, SETCONTROL, LOG, Nothing, CheckBox,Text, Button, DropDown, RadioBtns, EditBox
steps=[
# Assign a variable to an expression: ASSIGN('varname',exp="expression" [,dlg=Nothing()])
ASSIGN("logint",exp="lambda x: 30/(1+50*math.exp(-0.03*x))+0"),

# Assign a variable to an expression: ASSIGN('varname',exp="expression" [,dlg=Nothing()])
ASSIGN("test",exp="lambda x: x if x >= 1 else 0"),
#comment
# Loop through a list: LOOP(list=itemList [,var=varname][,mininc=''])
LOOP(list="1500,50,1500",
    var="x",
    steps=(
        # Set a control: SETCONTROL('target', 'value', 'eval' [,opt_target=''])
        SETCONTROL("Qin","x","float"),
        # Loop for a duration: LOOP(dur="float"[,units='Seconds' Second|Minutes|Hours ] [,var=''] [,mininc=''])
        LOOP(dur="15",
            units="Minutes"
            var="t",
            mininc="test(logint(t))",
            steps=(
                # Log a data record:LOG([avg='Default'] [,match='Default] [,flr='Default'][flash='Default'])
                LOG(avg="Off",
                    match="Off",
                    flr="0: Nothing"),)),)),]
