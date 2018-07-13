# epslatex template for a one-row, three-column figure
load 'epslatexparams.gp'

# Terminal size in inches, width should be unchanged
termwidth=3.5
termheight=2.3

set terminal epslatex standalone color clip colortext size termwidth,termheight font 9

set macros
set tmargin at screen 0.85
set bmargin at screen 0.20
LEFT = "set lmargin at screen 0.15; set rmargin at screen 0.6"
RIGHT = "set lmargin at screen 0.62; set rmargin at screen 0.95"

NOXTICS = "set format x ''; unset xlabel" 
NOYTICS = "set format y ''; unset ylabel" 
