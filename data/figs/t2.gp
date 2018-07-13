load 'layout12_side.gp'

set output 'gw100hist_hor_12.tex'

xtit=0.1
ytit=0.9

#ev(x) = 27.2114*x

#################################
@LEFT

#set key top right at graph 0.92, graph ytit horizontal Left reverse width -2.5 samplen 1.8
unset key

#set xtics font ",8"
set ylabel 'Error (eV)' offset 1.5,0
set yrange [-1.3:1.3]
set ytics -1.5,0.5
set mytics 5
set format y '%0.1f'
#set grid xtics noytics back

set xlabel '$\Delta$EOM-CCSD IP (eV)'
set xrange [0:25]
set xtics 5
set mxtics 5
set format x '%0.0f'

#set style line 9 lw 2.0 lc 'grey'
#set style fill solid 0.25 border

#set label 1 'EOM-CCSD' at graph xtit, graph ytit left font "6"
#set label 2 'ME = 0.017 eV' at graph xtit, graph ytit-0.08 left font "6"
#set label 3 'MAE = 0.066 eV' at graph xtit, graph ytit-0.16 left font "6"

#set label 1 'SO$_2$' at 14.08,-1.13
#set label 2 'C$_4$H$_5$N$_3$O' at 10.21, -0.77
#set label 3 'C$_4$H$_3$N$_2$O$_2$' at 10.72, -0.56
#set label 4 'MgO' at 8.08, 0.66

plot \
'../ccsd_none/ccsd_none_scatter.dat' u 1:2 w points pointtype 7 pointsize 0.5
#u ($1+0.05):2 ls 3 w boxes

#################################
@RIGHT

#set key top right at graph 0.92, graph ytit horizontal Left reverse width -2.5 samplen 1.8
unset key

#set xtics font ",8"
#set xlabel 'Error (eV)'
unset ylabel
set yrange [-1.3:1.3]
set ytics -1.5,0.5
set mytics 5
set format y ""
#set grid xtics noytics back

#set ylabel 'Number of molecules'
#unset ylabel
set xlabel "Number of molecules"
set xrange [0.1:60]
set format x '%0.0f'
set xtics 10
set mxtics 5
set grid xtics noytics back

#set style line 9 lw 2.0 lc 'grey'
set style fill solid 0.25 border

set object 1 rect from graph 0.5*xtit, ytit+0.06 to graph 1-0.5*xtit, graph 1.02*(ytit-0.24)
set label 1 'TITLE' at graph xtit, graph ytit left front
set label 2 'ME = -0.010 eV' at graph xtit, graph ytit-0.08 left front
set label 3 'MAE = 0.091 eV' at graph xtit, graph ytit-0.16 left front

# Check this +0.05
plot \
'../ccsd_none/ccsd_none_ip_errors.dat' u 2:1:(0.0):2:($1):($1+0.1) w boxxyerrorbars


