# This script creates Table II from the paper
# To run this, you will first need to use eomccsd_analysis.py on all methods of interest

def main():

		# Create the necessary lists for ordering and correct stylization
		# Change this to change which methods are(n't) included in the final table
		form_dict = {"lin_none": "EOM-linCCSD", "cc2_none": "EOM-CC2", "mbpt2_none": "EOM-MBPT2", "cc2_mp": "P-EOM-CC2", "mbpt2_mp": "P-EOM-MBPT2"}

		# Actual printing routine

		# Start with the necessary headers
		print "\\begin{table}[t]"
		print "\\begin{tabular}{l r r r r}"
		print "\\hline\hline"
		print "Method & IP ME (eV) & IP MAE (eV) & EA ME (eV) & EA MAE (eV) \\\\"
		print "\\hline"

		# Grab the IPs and EAs from the data file and stylize them correctly
		with open('IP-EA-data.dat', 'r') as f:
			for lin in f:
				form, me_ip, mae_ip, form2, me_ea, mae_ea = lin.strip().split()
				if form in form_dict:
						print "%s & %.2f & %.2f & %.2f & %.2f \\\\"%(form_dict[form], float(me_ip), float(mae_ip), float(me_ea), float(mae_ea))

		# Write out the footers
		print "\\hline\\hline"
		print "\\label{tab:approxips}"
		print "\\end{tabular}"
		print "\\caption{Mean error (ME) and mean absolute error (MAE) in eV of ionization potentals (IPs) and electron affinities (EAs) for molecules contained in the GW100 test set.  Error metrics are calculated with respect  to  IP/EA-EOM-CCSD  without  approximation,  except  for the GW results from Ref. 34,  which are calculated with respect to $\Delta$CCSD(T) results from Ref. 33.}" 
		print "\\end{table}"



if "__main__": 
	main()
