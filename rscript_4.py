from ROOT import *
import math
import sys, os

#N = 5
#N = 10
N  = int(sys.argv[1])
M  = float(sys.argv[2])
I1 = int(sys.argv[3])
I2 = int(sys.argv[4])
J1 = int(sys.argv[5])
J2 = int(sys.argv[6])
OUT = sys.argv[7]
#step = 1.0/N
#step = 0.2/N
#step = 0.5/N
#step = 1.0/N
step = M/N

#hutXsec = 50.82
#hctXsec = 38.88

fs1 = []
fs2 = []
FS = []

for c in ['b2j3', 'b3j3', 'b2j4', 'b3j4', 'b4j4']:
    fs1.append(TFile.Open('input/input_MVAHutComb_'+c+'_hut_Mergedbackgrounds.root'))
    fs2.append(TFile.Open('input/input_MVAHctComb_'+c+'_hct_Mergedbackgrounds.root'))
    hs1 = {}
    hs2 = {}
    for p in ['data_obs', 'sig_stop', 'sig_ttbar', 'sig', 'ttbb', 'ttcc', 'ttlf', 'other']:
        if p is not 'data_obs':
            S = None
            if p in ['ttbb', 'ttcc', 'ttlf']:
                #S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_MEPS', '_UE', '_scaleEnvelope']
                S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_hdamp', '_scaleEnvelope', '_UE', '_PDFEnvelope']
            else:
                S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer']
            for s in S:
                if s is not '':
                    for v in ['Up', 'Down']:
                        hn = 'combSTandTT_'+p+s+v
                        htemp1 = fs1[-1].Get(hn)
                        if not htemp1: continue
                        hs1[hn] = htemp1.Clone()
                        hs1[hn].SetDirectory(0)
                        htemp2 = fs2[-1].Get(hn)
                        if not htemp2: continue
                        hs2[hn] = htemp2.Clone()
                        hs2[hn].SetDirectory(0)
                else:
                    hn = 'combSTandTT_'+p
                    htemp1 = fs1[-1].Get(hn)
                    if not htemp1: continue
                    hs1[hn] = htemp1.Clone()
                    hs1[hn].SetDirectory(0)
                    htemp2 = fs2[-1].Get(hn)
                    if not htemp2: continue
                    hs2[hn] = htemp2.Clone()
                    hs2[hn].SetDirectory(0)
        else:
            hn = 'combSTandTT_'+p
            htemp1 = fs1[-1].Get(hn)
            if not htemp1: continue
            hs1[hn] = htemp1.Clone()
            hs1[hn].SetDirectory(0)
            htemp2 = fs2[-1].Get(hn)
            if not htemp2: continue
            hs2[hn] = htemp2.Clone()
            hs2[hn].SetDirectory(0)

    fs1[-1].Close()
    fs2[-1].Close()

    #for hcti in xrange(0, N+1):
    for hcti in xrange(I1, I2):
        khct = step*hcti
        #brhct = step*hcti
        #for huti in range(0, N+1):
        for huti in range(J1, J2):
            khut = step*huti
            #brhut = step*huti
            hsn = {}
            #os.system('mkdir output/'+str(hcti)+'_'+str(huti))
            #FS.append(TFile.Open('output/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D_100/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D_100_1/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D_20/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D_20_11-04-2017/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D_20_12-04-2017/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D_50_13-04-2017/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            #FS.append(TFile.Open('root://eoscms.cern.ch//eos/cms/store/caf/user/mdjordje/Cirkovic/rescaling2D_50/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            FS.append(TFile.Open(OUT+'/'+str(hcti)+'_'+str(huti)+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
            for p in ['data_obs', 'sig_stop', 'sig_ttbar', 'sig', 'ttbb', 'ttcc', 'ttlf', 'other']:
                if p is not 'data_obs':
                    S = None
                    if p in ['ttbb', 'ttcc', 'ttlf']:
                        #S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_MEPS', '_UE', '_scaleEnvelope']
                        S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_hdamp', '_scaleEnvelope', '_UE', '_PDFEnvelope']
                    else:
                        S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer']
                    for s in S:
                        if s is not '':
                            for v in ['Up', 'Down']:
                                hn = 'combSTandTT_'+p+s+v
                                if p in ['sig', 'sig_stop', 'sig_ttbar']:
#                                    kx = 2*khut**2#/hutXsec
#                                    ky = 2*khct**2#/hctXsec
#                                    kx = khut**2#/hutXsec
#                                    ky = khct**2#/hctXsec
#                                    kx = math.sqrt(brhut*1.4/100/0.1836)**2#/hutXsec
#                                    ky = math.sqrt(brhct*1.4/100/0.1836)**2#/hctXsec
#                                    kx = math.sqrt(brhut*1.4/0.1836)**2#/hutXsec
#                                    ky = math.sqrt(brhct*1.4/0.1836)**2#/hctXsec
#                                    kx = khut**2/0.01#/hutXsec
#                                    ky = khct**2/0.01#/hctXsec
                                    #kx = khut**2/0.1#/hutXsec
                                    #ky = khct**2/0.1#/hctXsec
                                    kx = (1/50.82)*(khut**2)/0.1#/hutXsec
                                    ky = (1/38.88)*(khct**2)/0.1#/hctXsec
                                    #kx = (khut**2)/0.1#/hutXsec
                                    #ky = (khct**2)/0.1#/hctXsec
                                else:
                                    kx = 0.5#1.0#*khut**2
                                    ky = 0.5#1.0#*khct**2
                                print hn, kx, ky
                                hsn[hn] = hs1[hn].Clone()
                                #if c != "b4j4":
                                if True:
                                    hsn[hn].Scale(kx)
                                else:
                                    hsn[hn].Scale(0)
                                hsn[hn].Add(hs2[hn], ky)
                                hsn[hn].Write()
                        else:
                            hn = 'combSTandTT_'+p
                            if p in ['sig', 'sig_stop', 'sig_ttbar']:
#                                kx = 2*khut**2#/hutXsec
#                                ky = 2*khct**2#/hctXsec
#                                kx = khut**2#/hutXsec
#                                ky = khct**2#/hctXsec
#                                kx = math.sqrt(brhut*1.4/100/0.1836)**2#/hutXsec
#                                ky = math.sqrt(brhct*1.4/100/0.1836)**2#/hctXsec
#                                kx = math.sqrt(brhut*1.4/0.1836)**2#/hutXsec
#                                ky = math.sqrt(brhct*1.4/0.1836)**2#/hctXsec
#                                kx = khut**2/0.01#/hutXsec
#                                ky = khct**2/0.01#/hctXsec
                                #kx = khut**2/0.1#/hutXsec
                                #ky = khct**2/0.1#/hctXsec
                                kx = (1/50.82)*(khut**2)/0.1#/hutXsec
                                ky = (1/38.88)*(khct**2)/0.1#/hctXsec
                                #kx = (khut**2)/0.1#/hutXsec
                                #ky = (khct**2)/0.1#/hctXsec
                            else:
                                kx = 0.5#1.0#*khut**2
                                ky = 0.5#1.0#*khct**2
                            print hn, kx, ky
                            hsn[hn] = hs1[hn].Clone()
                            #if c != "b4j4":
                            if True:
                                hsn[hn].Scale(kx)
                            else:
                                hsn[hn].Scale(0)
                            hsn[hn].Add(hs2[hn], ky)
                            hsn[hn].Write()
                else:
                    hn = 'combSTandTT_'+p
                    kx = 1.0
                    ky = 1.0
                    print hn, kx, ky
                    hsn[hn] = hs1[hn].Clone()
                    hsn[hn].Scale(kx)
                    hsn[hn].Add(hs2[hn], ky)
                    hsn[hn].Write()
            FS[-1].Close()
