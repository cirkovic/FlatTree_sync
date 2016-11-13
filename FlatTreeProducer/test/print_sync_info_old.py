from ROOT import *
import sys

outdir = '/afs/cern.ch/user/c/cirkovic/www/24-10-2016/FCNC_sync/'
ofile = None
if sys.argv[1] == 'el':
    ofile = open(outdir+'/'+'EventInfo_el.txt', 'w')
elif sys.argv[1] == 'mu':
    ofile = open(outdir+'/'+'EventInfo_mu.txt', 'w')
ofile.close()

if sys.argv[1] == 'el':
    ofile = open(outdir+'/'+'EventInfo_el.txt', 'a')
elif sys.argv[1] == 'mu':
    ofile = open(outdir+'/'+'EventInfo_mu.txt', 'a')

fs = []
ts = []

fs.append(TFile.Open("output.root"))
ts.append(fs[-1].Get("FlatTree/tree"))
#ts[-1].Print()
#sys.exit()
'''
#for ie, e in enumerate(ts[-1]):
    print "%6d %6d %10d  %+2d  %6.2f %+4.2f %+4.2f    %6.1f  %+4.2f    %d [%s]" % (
           e.ev_run, e.ev_lumi, e.ev_id,
           e.el_id, e.el_pt, e.el_eta, e.el_phi,
           e.met_pt, e.met_phi,
           e.jet_n, '0.0') #', '.join(['%5.3f' % v for v in e.jet_CSVv2]))
'''
for ie, e in enumerate(ts[-1]):
    if sys.argv[1] == 'el':
        for iel in xrange(0, e.el_n):
            ofile.write("%6d %6d %10d  %+2d  %6.2f %+4.2f %+4.2f    %6.1f  %+4.2f    %d %s\n" % (
                   e.ev_run, e.ev_lumi, e.ev_id,
                   e.el_id[iel], e.el_pt[iel], e.el_eta[iel], e.el_phi[iel],
                   e.met_pt, e.met_phi,
                   e.jet_n, '0.0'
                )
            )
    elif sys.argv[1] == 'mu':
        for imu in xrange(0, e.mu_n):
            ofile.write("%6d %6d %10d  %+2d  %6.2f %+4.2f %+4.2f    %6.1f  %+4.2f    %d %s\n" % (
                   e.ev_run, e.ev_lumi, e.ev_id,
                   e.mu_id[imu], e.mu_pt[imu], e.mu_eta[imu], e.mu_phi[imu],
                   e.met_pt, e.met_phi,
                   e.jet_n, '0.0'
                )
            )

    if ie > 1000: break

ofile.close()
