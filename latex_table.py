import sys
from molecule import MOLECULE

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print 'usage: (number of IPs) (number of EAs)' 
        sys.exit(1)
    nip = int(args[0])
    nea = int(args[1])
    ips = {}
    qps = {}
    eas = {}
    eaqps = {}
    ipconv = {}
    eaconv = {}

    with open('ip_data/ccsd_none/ccsd_none_all_ips.dat', 'r') as fil:
        for line in fil:
            lin = line.strip().split()
            ips[lin[0]] = [-float(i)*27.21139 for i in lin[1::3]]
            qps[lin[0]] = [float(i) for i in lin[2::3]]
            ipconv[lin[0]] = [i for i in lin[3::3]]
    
    with open('ea_data/ccsd_none/ccsd_none_all_eas.dat', 'r') as fil:
        for line in fil:
            lin = line.strip().split()
            eas[lin[0]] = [float(i)*27.21139 for i in lin[1::3]]
            eaqps[lin[0]] = [float(i) for i in lin[2::3]]
            eaconv[lin[0]] = [i for i in lin[3::3]]


    with open('ip_data/paper_names.txt', 'r') as fil:
        print '\\begin{longtable*}{@{\\extracolsep{\\fill}} l l '+'r '*nip+'r '*nea+'}'
        print '\\hline\\hline'
        print 'Formula & Name ',
        for n in range(nip-1):
            print '& HOMO-%d '%(nip-n-1),
        print '& HOMO ',
        print '& LUMO ',
        for n in range(1,nea):
            print '& LUMO+%d '%(n),
        print ' \\\\'
        print '\\hline'
        for line in fil:
            form, latex, name = line.strip().split('\t')
            mo = MOLECULE(form, name, latex, ips[form], qps[form], ipconv[form], eas[form], eaqps[form], eaconv[form])
            cols = mo.print_mol()
            cols_ip, cols_ea = cols[0].split('&'), cols[1].split('&')
            str = '%s & %s '%(cols_ip[0], cols_ip[1])
            for n in range(nip):
                try:
                    str += "& " + cols_ip[2+nip-n-1]
                except:
                    str += " & "
            for n in range(nea):
                try:
                    str += "& " + cols_ea[2+n]
                except:
                    str += " & "
            print str,
            n_amp = str.count('&')
            for n in range(2+nip+nea-n_amp-1):
                print "& ",
            print '\\\\'
        print '\\hline\\hline'
        #print '\\end{tabular}'
        print '\\caption{Quasiparticle energies (negative of the ionization potentials and electron affinities) of molecules in the $GW$100 calculated with IP/EA-EOM-CCSD in the def2-TZVPP basis set.}'
        print '\\label{tab:eomccsd}'
        print '\\end{longtable*}'
        #print '\\end{table*}'


if __name__ == '__main__':
    main()
