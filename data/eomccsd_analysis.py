# This script compares obtained IP/EA values to reference values (CCSD()T or other)
# Will print out first part with format: FORMULA IP-VAL REF-VAL ERROR for scatter plot
# And a second part with format: BIN COUNT for histogram


import sys

def main():
    args = sys.argv[1:]
    if len(args) != 1 and len(args) != 2:
        print 'usage: ip.dat [ref.dat]' 
        sys.exit(1)

    ip_file = args[0]
    if len(args) == 1:
        ref = './reference/ccsdt.dat'					# Default reference
    else:    
        ref = args[1]									# User chosen reference

	# This section creates the reference dictionary 
    ref_dict = {}
    f = open(ref)
    for line in f:
        form, name, ip = line.strip().split(',')
        if ip == None or ip == 'None':
            ref_dict[form] = 99
        else:
            ref_dict[form] = float(ip)

	# This section compares the obtained value to the reference value and prints out the result
	# Format is FORMULA IP-VAL REF-VAL ERROR
    ccsd_error = list()
    f = open(ip_file)
    for line in f:
        form, ip = line.strip().split()
        ip_ccsd = float(ip)*27.21139
        ip_ref = ref_dict[form]
        if abs(ip_ccsd - ip_ref) < 5.0:
            ccsd_error.append(ip_ccsd - ip_ref)
        print "# %10s %8.4f %8.4f %6.4f"%(form, ip_ccsd, ip_ref, ip_ccsd - ip_ref)

	# Here the ME and MAE values are printed
    import numpy as np
    ccsd_error = np.array(ccsd_error)
    print "# mean error =", np.mean(ccsd_error)
    print "# mean abs error =", np.mean(np.abs(ccsd_error))

	# This section creates the histogram data and prints out
	# Format is BIN COUNT
    hist, bin_edges = np.histogram(ccsd_error, bins=24, range=(-1.25,1.15))
    for bin, ct in zip(bin_edges, hist):
        print "%.2f %s"%(bin, ct)

if __name__ == '__main__':
    main()
