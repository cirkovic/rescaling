from ROOT import *
import math
import sys, os

#N = 5
#N = 10
#N  = int(sys.argv[1])
#M  = float(sys.argv[2])
#I1 = int(sys.argv[3])
#I2 = int(sys.argv[4])
#J1 = int(sys.argv[5])
#J2 = int(sys.argv[6])
OUT = 'output_10'
#step = 1.0/N
#step = 0.2/N
#step = 0.5/N
#step = 1.0/N
#step = M/N

#hutXsec = 50.82
#hctXsec = 38.88

ps = ['data_obs', 'sig_stop', 'sig_ttbar', 'sig', 'ttbb', 'ttcc', 'ttlf', 'other']
Ps = ['data_obs', 'SigStop', 'SigTTbar', 'Sig', 'ttbb', 'ttcc', 'ttlf', 'other']

for pm in ['u', 'c']:
    fs = []
    fs1 = []
    FS = []

    for c in ['b2j3', 'b3j3', 'b2j4', 'b3j4', 'b4j4']:
        fs.append(TFile.Open('input_10/input_MVAHutComb_'+c+'_hut_Mergedbackgrounds.root'))
        fs1.append(TFile.Open('input_10/input_MVAHutComb_'+c+'_hut_Mergedbackgrounds.root'))
        hs = {}
        for pi, p in enumerate(ps):
            if p is not 'data_obs':
                S = None
                if p in ['ttbb', 'ttcc', 'ttlf']:
                    #S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_MEPS', '_UE', '_scaleEnvelope']
                    S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_hdamp', '_scaleEnvelope', '_UE', '_PDFEnvelope']
                else:
                    S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer']
                for ibin in xrange(0, 20):
                    #print "TOADD: "+'combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up', fs1[-1].Get('combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up')
                    if fs1[-1].Get('combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up'):
                    #if fs[-1].Get('combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up'):
                        S.append('_'+c+'StatBin'+Ps[pi]+str(ibin))
                for s in S:
                    if s is not '':
                        for v in ['Up', 'Down']:
                            hn = 'combSTandTT_'+p+s+v
                            htemp = fs[-1].Get(hn)
                            if not htemp: continue
                            hs[hn] = htemp.Clone()
                            hs[hn].SetDirectory(0)
                    else:
                        hn = 'combSTandTT_'+p
                        htemp = fs[-1].Get(hn)
                        if not htemp: continue
                        hs[hn] = htemp.Clone()
                        hs[hn].SetDirectory(0)
            else:
                hn = 'combSTandTT_'+p
                htemp = fs[-1].Get(hn)
                if not htemp: continue
                hs[hn] = htemp.Clone()
                hs[hn].SetDirectory(0)

        fs[-1].Close()

        #for hcti in xrange(0, N+1):
        #for hcti in xrange(I1, I2):
        for hcti in xrange(0, 1):
            #khct = step*hcti
            #brhct = step*hcti
            #for huti in range(0, N+1):
            #for huti in range(J1, J2):
            for huti in range(0, 1):
                #khut = step*huti
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
                #FS.append(TFile.Open(OUT+'/input_MVAHuctComb_'+c+'_huct_Mergedbackgrounds.root', 'RECREATE'))
                FS.append(TFile.Open(OUT+'/input_MVAH'+pm+'tComb_'+c+'_h'+pm+'t_Mergedbackgrounds.root', 'RECREATE'))
                for pi, p in enumerate(ps):
                    if p is not 'data_obs':
                        S = None
                        if p in ['ttbb', 'ttcc', 'ttlf']:
                            #S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_MEPS', '_UE', '_scaleEnvelope']
                            S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer', '_hdamp', '_scaleEnvelope', '_UE', '_PDFEnvelope']
                        else:
                            S = ['', '_SfIteraviveFitLf', '_SfIteraviveFitHf', '_SfIteraviveFitLfstats1', '_SfIteraviveFitLfstats2', '_SfIteraviveFitHfstats1', '_SfIteraviveFitHfstats2', '_SfIteraviveFitCferr1', '_SfIteraviveFitCferr2', '_SfPileup', '_SfLepton', '_SfTopPt', '_Jes', '_Jer']
                        for ibin in xrange(0, 20):
                            #print "TOADD: "+'combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up', fs1[-1].Get('combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up')
                            if fs1[-1].Get('combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up'):
                            #if fs[-1].Get('combSTandTT_'+p+'_'+c+'StatBin'+Ps[pi]+str(ibin)+'Up'):
                                S.append('_'+c+'StatBin'+Ps[pi]+str(ibin))
                        for s in S:
                            if s is not '':
                                for v in ['Up', 'Down']:
                                    hn = 'combSTandTT_'+p+s+v
                                    if p in ['sig', 'sig_stop', 'sig_ttbar']:
                                        kx = 1.0/0.1#/hutXsec
                                    else:
                                        kx = 1.0#*khut**2
                                    print hn, kx
                                    hsn[hn] = hs[hn].Clone()
                                    hsn[hn].Scale(kx)
                                    hsn[hn].Write()
                            else:
                                hn = 'combSTandTT_'+p
                                if p in ['sig', 'sig_stop', 'sig_ttbar']:
                                    kx = 1.0/0.1#/hutXsec
                                else:
                                    kx = 1.0#*khut**2
                                print hn, kx
                                hsn[hn] = hs[hn].Clone()
                                hsn[hn].Scale(kx)
                                hsn[hn].Write()
                    else:
                        hn = 'combSTandTT_'+p
                        kx = 1.0
                        print hn, kx
                        hsn[hn] = hs[hn].Clone()
                        hsn[hn].Scale(kx)
                        hsn[hn].Write()
                FS[-1].Close()
