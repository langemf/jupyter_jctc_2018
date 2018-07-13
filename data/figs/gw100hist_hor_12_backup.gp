load 'layout12_side.gp'

set output 'gw100hist_hor_12.tex'

xtit=0.1
ytit=0.9

#ev(x) = 27.2114*x

#################################
@LEFT

# This section creates the scatter plot on the left

unset key

# Set the y-axis labels and parameters
set ylabel 'Error (eV)' offset 1.5,0
set yrange [-1.3:1.3]
set ytics -1.5,0.5
set mytics 5
set format y '%0.1f'

# Set the x-axis labels and parameters
set xlabel '$\Delta$EOM-CCSD IP (eV)'
set xrange [0:25]
set xtics 5
set mxtics 5
set format x '%0.0f'

# Plot the data
plot \
'SCATTER_FILE' u 1:2 w points pointtype 7 pointsize 0.5

#################################
@RIGHT

# This section creates the sideways bar graph on the right

unset key

# Set all of the y-axis labels and parameters
unset ylabel
set yrange [-1.3:1.3]
set ytics -1.5,0.5
set mytics 5
set format y ""

# Set all of the x-axis labels and parameters
set xlabel "Number of molecules"
set xrange [0.1:60]
set format x '%0.0f'
set xtics 10
set mxtics 5
set grid xtics noytics back

set style fill solid 0.25 border

# The following creates the label and summary of ME and MAE values.
set object 1 rect from graph 0.5*xtit, ytit+0.06 to graph 1-0.5*xtit, graph 1.02*(ytit-0.24)
set label 1 'TITLE' at graph xtit, graph ytit left front
set label 2 'ME = MEVAL eV' at graph xtit, graph ytit-0.08 left front
set label 3 'MAE = MAEVAL eV' at graph xtit, graph ytit-0.16 left front

# Plot the data
plot \
'HIST_FILE' u 2:1:(0.0):2:($1):($1+0.1) w boxxyerrorbars


