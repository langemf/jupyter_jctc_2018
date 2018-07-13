# This file serves as a driver for using PySCF for the calculation of IPs and EAs of a molecule
# The file can be changed as needed depending on whatever the users needs may be

import sys
from pyscf import gto, scf, cc 

def main():
	# Here we check for the correct number of arguments. In the paper, this allowed rapid generation and organization of different methods
    args = sys.argv[1:]
    if len(args) != 4:
        print 'usage: formula basis ccsd/mbpt2/lin/cc2 none/full/mp/brutal' 
        sys.exit(1)
	# Save the user input
    formula = args[0]
    basis = args[1]
    cctype = args[2]
    approx = cctype.lower()
	# Use the approximation as desired by user
    if approx == 'ccsd':
        approx = None
    partition = args[3]
	# Use the partitioning scheme as desired by user (usually none or mp)
    if partition.lower() == 'none':
        partition = None
    
	# Please see gw100 file for further information
	# Here we simply load the molecule information from the gw100 object
    from gw100 import GW100 
    gw100_set = GW100()
    mol = gw100_set.molecules[formula].mol
	# Here we change the default basis to the basis of interest
    mol.basis = basis
	# And rebuild the molecule object
    mol.build()
	# This instantiates the SCF object as RHF
    mf = scf.RHF(mol)
	# Verbosity can be important, but can also be minimized
    mf.verbose = 3
	# This line runs the actual SCF calculation
    ehf = mf.scf()

	# Load the frozen orbital count (taken from Krause paper)
    frozen = gw100_set.molecules[formula].frozen
	# Identify the correct number of roots to find 
    nocc = mol.nelectron//2
    nvir = mol.nao_nr()-nocc
    nip = min(nocc-len(frozen), 4)
    nea = min(nvir, 12)
	# Instantiate the cc object as RCCSD
    mcc = cc.RCCSD(mf, frozen=frozen)
#    mcc = cc.RCCSD(mf, approx=approx, frozen=frozen) # If you'd like to include run an
#    approximate calculation - use this variant
	# Again, verbosity can be changed as needed
    mcc.verbose = 4
	# Run the actual cc calculation (this is for the GROUND state)
    mcc.ccsd()
	# This runs the IP calculation, asking for koopman-like roots, with nip IP values, and partitioning of choice
    e,c = mcc.ipccsd(nip, koopmans=True, partition=partition)
	# This runs the EA calculation, asking for koopman-like roots, with nea EA values, and partitioning of choice
    e,c = mcc.eaccsd(nea, koopmans=True, partition=partition)

if __name__ == '__main__':
    main()
