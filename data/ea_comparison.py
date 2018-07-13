# This screat will create a Latex-stylized longtable containing the first Ionization Potential for a given method. This needs to be run in the parent folder for all of the ionization potential data (usually .../ea_data)
# This screat creates a Pandas DataFrame to organize the data and make writing it to a file much simpler.

import pandas as pd
import numpy as np
import os

# Creating DataFrames for all of the different methods
df1 = pd.read_csv('ccsd_mp/ccsd_mp_ea.dat', delim_whitespace=True, header=None, index_col=0, names = ['Molecule', 'ccsd_mp'])
df2 = pd.read_csv('lin_none/lin_none_ea.dat', delim_whitespace=True, header=None, index_col=0, names = ['Molecule', 'lin_none'])
df3 = pd.read_csv('lin_mp/lin_mp_ea.dat', delim_whitespace=True, header=None, index_col=0, names = ['Molecule', 'lin_mp'])
df4 = pd.read_csv('cc2_none/cc2_none_ea.dat', delim_whitespace=True, header=None, index_col=0, names = ['Molecule', 'cc2_none'])
df5 = pd.read_csv('cc2_mp/cc2_mp_ea.dat', delim_whitespace=True, header=None, index_col=0, names = ['Molecule', 'cc2_mp'])
df6 = pd.read_csv('mbpt2_none/mbpt2_none_ea.dat', delim_whitespace=True, header=None, index_col=0, names = ['Molecule', 'mbpt2_none'])
df7 = pd.read_csv('mbpt2_mp/mbpt2_mp_ea.dat', delim_whitespace=True, header=None, index_col=0, names = ['Molecule', 'mbpt2_mp'])

# Joining the DataFrames by row into a single DataFrame containing all methods
df1 = df1.join([df2, df3, df4, df5, df6, df7])

# Converting Hartree units to eV units
df1 *= 27.21139

# The streaping procedure streas alphabetically, which doesn't match the ordering in the original GW paper ()
# Here we do a workaround, which re-orders the DataFrame in a way which matches that of the paper and also includes the Latex stylized formulas
df1.to_csv('ea_comparison_table.txt', sep='\t', na_rep='NaN', float_format='%.6f')

with open('out.txt', 'w') as o:
    with open('paper_names.txt', 'r') as f:		# paper_names.txt contains the Latex-stylized formulas and the correct ordering
            for lin in f:
                    with open('ea_comparison_table.txt', 'r') as g:		# This is the DataFrame to be re-ordered
                        for l in g:
                                if lin.strip().split()[0] == l.strip().split()[0]:
                                    o.write((lin.strip().split()[1] + '\t' +  l))			# Actual re-ordering and inclusion of Latex formula

# Read in the correct DataFrame
df = pd.read_csv('out.txt', delim_whitespace=True, header=None, index_col=1, names = ['Molecule', 'mol-index', 'ccsd_mp', 'lin_none', 'lin_mp', 'cc2_none', 'cc2_mp', 'mbpt2_none', 'mbpt2_mp'])

# Write the DatFrame to ea_table.txt with the necessary header as a longtable
# The primary customization options are the centering of the columns - replace 'l' or 'r' with 'c', 'l', or 'r' as needed
# The columns included in the final table - add or delete from 'columns=[]' below
# Change the Float formatting, currently at 2 decimal places
with open('ea_table.txt', 'w') as f:
    f.write('\\begin{longtable*}{@{\\extracolsep{\\fill}}l r r r r r }\n')							#Header
    f.write('\hline\hline\n')																		#Header
    f.write('Formula  & EOM-linCCSD  & EOM-CC2  & EOM-MBPT2  & P-EOM-CC2  & P-EOM-MBPT2  \\\\\n')	#Header
    f.write('\hline\n')																				#Header
    df.to_csv(f, header=False, sep='&', na_rep='*', index=False, line_terminator='\\\\\n', columns=['Molecule', 'lin_none', 'cc2_none', 'mbpt2_none', 'cc2_mp', 'mbpt2_mp'], float_format='%.2f') 
    f.write('\hline\hline\n')																		#Footer
    f.write('\\caption{Full data set of first electron affinities predicted by approximations to EOM-CCSD, as summarized in the text. Asterisks indicate molecules for which ground state CC2 did not converge.}\n')
    f.write('\\label{tab:eomccsd}\n')																#Footer
    f.write('\\end{longtable*}\n')																	#Footer

# Finally, delete all intermediate files
os.remove('out.txt')
os.remove('ea_comparison_table.txt')






