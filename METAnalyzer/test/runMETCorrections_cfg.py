import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'root://cmseos.fnal.gov//store/user/vhegde/MET_HATS2017/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_PUMoriond17_80X_1C34F84E-A8BE-E611-BE97-441EA1733CCC.root'#WJetsToLNu MC
       #'root://cmseos.fnal.gov//store/user/vhegde/MET_HATS2017/Run2016G_MET_MINIAOD_03Feb2017-v1_2E1DF27E-37EC-E611-A696-00259073E4E2.root'#Run 2016G MET dataset
      # MC file
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/006F1B9A-81D0-E611-B9CE-0025905AA9CC.root'
    )
)

#from MetTools.MetPhiCorrections.tools.multPhiCorr_Summer16_MC_DY_80X_sumPt_cfi import multPhiCorr_MC_DY_sumPT_80X as phiCorrBins
#process.load('MetTools.MetPhiCorrections.phiCorr_PHYS14_cff')
##Replacements for mAOD
#process.metPhiCorrInfoWriter.vertexCollection = cms.untracked.InputTag("offlineSlimmedPrimaryVertices")
#process.metPhiCorrInfoWriter.srcPFlow = cms.untracked.InputTag("packedPFCandidates")

process.demo = cms.EDAnalyzer('METCorrections',
                              metSrc = cms.untracked.InputTag("slimmedMETs"),
                              ifPrint = cms.untracked.bool(False)
)

process.TFileService = cms.Service("TFileService",
   fileName = cms.string("metCorrections.root")
)

#process.p = cms.Path(process.metPhiCorrInfoWriterSequence * process.demo)

process.p = cms.Path(process.demo)
