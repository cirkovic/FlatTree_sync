from ROOT import *
import sys

outdir = '/afs/cern.ch/user/c/cirkovic/www/24-10-2016/FCNC_sync/'
Nevt = -1

if sys.argv[1] == 'mu':
    open(outdir+'/'+'EventInfo_mu.txt', 'w').close()
elif sys.argv[1] == 'el':
    open(outdir+'/'+'EventInfo_el.txt', 'w').close()

fs = []
ts = []

fs.append(TFile.Open("output.root"))
ts.append(fs[-1].Get("FlatTree/tree"))
#ts[-1].Print()
#sys.exit()
'''
fprintf(_fevc,"%6d %6d %10d  %+2d  %6.2f %+4.2f %+4.2f    %6.1f  %+4.2f    %d %d \n",
           run, lumi, id,
           lepId, lepPt, lepEta, lepPhi,
           metpt, metphi,
           njets, nbjets)
'''

if sys.argv[1] == 'mu':

    with open(outdir+'/'+'EventInfo_mu.txt', 'a') as ofile:
        for ie, e in enumerate(ts[-1]):
            if Nevt == -1 or ie < Nevt:
                for imu in xrange(0, e.mu_n):
                    ofile.write("%6d %6d %10d  %+2d  %6.2f %+4.2f %+4.2f   %6.1f  %+4.2f    %d %d \n" % (
                           e.ev_run, e.ev_lumi, e.ev_id,
                           e.mu_id[imu], e.mu_pt[imu], e.mu_eta[imu], e.mu_phi[imu],
                           e.met_pt, e.met_phi,
                           e.jet_n, 0
                        )
                    )

elif sys.argv[1] == 'el':

    with open(outdir+'/'+'EventInfo_el.txt', 'a') as ofile:
        for ie, e in enumerate(ts[-1]):
            if Nevt == -1 or ie < Nevt:
                for iel in xrange(0, e.el_n):
                    ofile.write("%6d %6d %10d  %+2d  %6.2f %+4.2f %+4.2f   %6.1f  %+4.2f    %d %d \n" % (
                           e.ev_run, e.ev_lumi, e.ev_id,
                           e.el_id[iel], e.el_pt[iel], e.el_eta[iel], e.el_phi[iel],
                           e.met_pt, e.met_phi,
                           e.jet_n, 0
                        )
                    )

