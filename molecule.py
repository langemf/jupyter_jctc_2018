import numpy as np

def format_ip(energy, weight, conv):
    if weight > 0.3:
        if conv == "True":
            return '$%0.2f$'%(energy)
        else:
            return '\\boldsymbol{$%0.2f$}'%(energy)
    else:
        if conv == "True":
            return '$\\red{%0.2f}$'%(energy)
        else:
            return '\\boldsymbol{$\\red{%0.2f}}$'%(energy)
        #return '$$'

class MOLECULE(object):
    
    def __init__(self, form='', name='', latex='', ips=[], qps=[], ipconv=[], eas=[], eaqps=[], eaconv=[]):
        self.formula = form
        self.name = name
        self.latex = latex
        self.ips = ips
        self.qps = qps
        self.ipconv = ipconv
        self.eas = eas
        self.eaqps = eaqps
        self.eaconv = eaconv

        idx = (-np.array(ips)).argsort()
        self.ips = np.array(ips)[idx]
        self.qps = np.array(qps)[idx]
        self.ipconv = np.array(ipconv)[idx]
    
    def print_mol(self):
        return [self.latex + ' & ' + self.name + ' & ' + self.print_ips(),
                self.latex + ' & ' + self.name + ' & ' + self.print_eas()]

    def print_ips(self):
        out = format_ip(self.ips[0], self.qps[0], self.ipconv[0])
        mult = 1
        if 0 == len(self.ips)-1:
            out = out + ' $(\\times %d)$'%(1)
        #print "self.ips[i] =", self.ips[0], "mult =", mult
        for i in range(1,len(self.ips)):
            if abs(self.ips[i]-self.ips[i-1]) < 0.0005:
                mult += 1
                if i == len(self.ips)-1:
                    out = out + ' $(\\times %d)$'%(mult)
            else:
                out = out + ' $(\\times %d)$ & '%(mult) + format_ip(self.ips[i], self.qps[i], self.ipconv[i])
                mult = 1
                if i == len(self.ips)-1:
                    out = out + ' $(\\times %d)$'%(1)
            #print "self.ips[i] =", self.ips[i], "mult =", mult
        return out
    
    def print_eas(self):
        out = format_ip(self.eas[0], self.eaqps[0], self.eaconv[0])
        mult = 1
        if 0 == len(self.eas)-1:
            out = out + ' $(\\times %d)$'%(1)
        #print "self.ips[i] =", self.ips[0], "mult =", mult
        for i in range(1,len(self.eas)):
            if abs(self.eas[i]-self.eas[i-1]) < 0.0005:
                mult += 1
                if i == len(self.eas)-1:
                    out = out + ' $(\\times %d)$'%(mult)
            else:
                out = out + ' $(\\times %d)$ & '%(mult) + format_ip(self.eas[i], self.eaqps[i], self.eaconv[i])
                mult = 1
                if i == len(self.eas)-1:
                    out = out + ' $(\\times %d)$'%(1)
            #print "self.ips[i] =", self.ips[i], "mult =", mult
        return out
