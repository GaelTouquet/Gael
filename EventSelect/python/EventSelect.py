import FWCore.ParameterSet.Config as cms
import os
import Gael.EventSelect.SelectEventTools as tools # import getStringFromFile, convertStringToScheme
import Gael.EventSelect.select_configs as configs

config = 'config1'

config = getattr(configs, config)

##____________________________________________________________________________||
process = cms.Process("SELECT")

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

dataset_name = config['dataset']

component = creator.makeMCComponent('Dataset', '/SUSYGluGluToBBHToTauTau_M-1000_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 'CMS', '.*root', 1.0)

print 'test'
##____________________________________________________________________________||

txtfile = config['txtfile']
rawdata = tools.getStringFromFile(txtfile)
data = tools.convertStringToScheme(rawdata)
# data = ['1:505:88822', '1:81:14196']

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePoolInputSources#Example_6_Selecting_Input_Lumi_B
# see edmDumpEventContent, edmFileUtil
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        component.files
        ),
    eventsToProcess = cms.untracked.VEventRange(data) 
    )

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('select.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
        )
    )
# process.outtaus = cms.OutputModule(
#     "PoolOutputModule",
#     fileName = cms.untracked.string('select_taus.root'),
#     SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
#     outputCommands = cms.untracked.vstring(
#         'drop *',
#         'keep patTaus_*_*_*'
#         )
#     )


##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 100


##____________________________________________________________________________||
process.p = cms.Path()

process.e1 = cms.EndPath(
    process.out 
    # + process.outtaus
    )

print process.source

##____________________________________________________________________________||

