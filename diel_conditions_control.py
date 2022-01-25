from bpdefs import ASSIGN, LOOP, SETCONTROL, LOG, Nothing, CheckBox,Text, Button, DropDown, RadioBtns, EditBox
steps=[
SETCONTROL("VDP_leaf","1.8","float"),
SETCONTROL("t_leaf", "23", "float"),

LOOP(dur="1441",
    units="Minutes",
    mininc="300"
    steps=(
        LOG(),
        IF("Qin<10", SETCONTROL("VDP_leaf","1.2","float"),
        ELSE( SETCONTROL("VDP_leaf","1.8","float"),
        IF("Qin<10", SETCONTROL("t_leaf","21","float"),
        ELSE("Qin<10", SETCONTROL("t_leaf","23","float")
    ))]
