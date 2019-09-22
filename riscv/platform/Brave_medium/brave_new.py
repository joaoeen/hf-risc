import os
import sys
import NX1H35_EK_V2

from os import path
from nanoxmap import *
from NX1H35_EK_V2 import *

dir = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir)

project = createProject(dir)

project.setVariantName('NG-MEDIUM')

project.setTopCellName('hfrisc_soc')

project.addFile('brave.vhd')

project.addFiles([


'../rams/boot_ram_brave.vhd',
'../rams/ram_2k8_brave.vhd',
'../rams/RAM_DATA.vhd',
'../rams/ram.vhd',
'../../../devices/controllers/uart/uart.vhd',
'../../../devices/peripherals/basic_soc.vhd',
'../../core_rv32i/alu.vhd',
'../../core_rv32i/bshifter.vhd',
'../../core_rv32i/int_control.vhd',
'../../core_rv32i/reg_bank.vhd',
'../../core_rv32i/control.vhd',
'../../core_rv32i/cpu.vhd',
'../../core_rv32i/datapath.vhd'


])

project.setOptions({
    'DefaultFSMEncoding':           'Binary', # *'OneHot' 'OneHotSafe' 'OneHotSafeExtra' 'Binary'
    'DefaultRAMMapping':            'RAM', # *'RF' 'RAM'
    'DefaultROMMapping':            'LUT', # *'LUT' 'RF' 'RAM'
    'DisableAdderBasicMerge':       'No', # Disable carry optimization around adders and subtractors.
    'DisableAdderTreeOptimization': 'No', # Disable adder mux reordering and adder tree balancing.
    'DisableAdderTrivialRemoval':   'No', # Disable simplification of adder that could fit in 1 or 2 LUTs.
    'DisableDSPAluOperator':        'No', # Disable merge of ALU within inferred DSP.
    'DisableDSPFullRecognition':    'No', # Disable inference of DSP.
    'DisableDSPPreOperator':        'No', # Disable merge of pre-operator within inferred DSP.
    'DisableDSPRegisters':          'No', # Disable merge of registers within inferred DSP.
    'DisableLoadAndResetBypass':    'No', # Disable load and reset signal bypass on DFF.
    'DisableRAMAlternateForm':      'No', # Disable recognition of registered address read port.
    'DisableRAMRegisters':          'No', # Disable merge of registers within inferred RAM.
    'ExhaustiveBitstream':          'No', # Can be used to force generation of all configurations and contexts in bitstream (can be 'No', 'Config', 'Context' or 'ConfigContext').
    'GenerateIntermediateArchives': 'Never', # If set to 'Always', .nxi archives are generated for each intermediate step of the flow (for debug purpose).
    'GenerateBitstreamCMIC':        'Always', # Enable/Disable CMIC in bitstream.
    'IgnoreRAMFlashClear':          'No', # Do not output error when recognizing a RAM with flash clear.
    'ManageAsynchronousReadPort':   'No', # If 'Yes', detect asynchronous read port in memories and repair it in synchronous read port. The read port receive the reversed write clock. It can slow down the design and sometimes may cause invalid behavior.
    'ManageUnconnectedOutputs':     'Error', # Undriven outputs of HDL modules are treated as 'Error', 'Ground' or 'Power'.
    'ManageUnconnectedSignals':     'Ground', # Undriven internal signals of HDL modules are treated as 'Error', 'Ground' or 'Power'.
    'ManageUninitializedLoops':     'Never', # Remove reset-less looped DFF causing extra-mapping and `X' values in simulation (can be 'Never', 'Ground', 'Always').
    'MappingEffort':                'Low', # Effort for an optimized mapping (can be 'Low', 'Medium' or 'High').
    'MaxRegisterCount':             '2500', # Maximum number of registers handled per HDL module (not the whole design) by the synthesizer.
    'MergeRegisterToPad':           'Never', # Automatically merge registers into IO buffers (can be 'Always', 'Never', 'Input' or 'Output').
    'Rollback':                     'Yes', # Allow the application to roll-back to a previous state when an error is encountered during Routing, and resume the process with new parameters.
    'TimingDriven':                 'Yes', # If set to 'Yes', algorithms are timing driven (can be 'Yes' or 'No').
    'UnusedPads':                   'Floating', # State in which the pads must be set when not used. Values can be 'Floating','WeakPullUp', 'WeakPullDown'.
    'UseNxLibrary':                 'Yes', # If set to 'Yes', physical elements from nxLibrary.vhdp can be directly instantiate in the source file.
    'UseSynthesisRetiming':         'No', # If set to 'Yes', retiming algorithms will be enabled during synthesis.
    'UseXLUT':                      'Yes', # If set to 'Yes', Place stage will use XLUTs to reduce interconnexion timing between LUTs (in some cases, using XLUTs can degrade final frequency).
    'VariantAwareSynthesis':        'Yes' # If set to 'Yes' synthesis will automatically map to equivalent resource when specific resource is depleted.
    })

kit = NX1H35_EK_V2.Kit()

project.createClock('getPort(clk_in)', 'clk_in', 40000)

project.save('native.nxm')

if not project.synthesize():
	sys.exit(1)

project.save('_synthese.vhd')

project.save('synthesized.nxm')

if not project.place():
	sys.exit(1)

project.save('placed.nxm')

##if not project.route():
##	sys.exit(1)

##project.save('routed.nxm')

#reports
project.reportInstances()

#STA
analyzer = project.createAnalyzer()

analyzer.launch()

analyzer.destroy()

#bitstream
##project.generateBitstream('payload_x.nxb')

#power consuption
project.reportPowerConsumption()

project.destroy()

print 'Errors: ', getErrorCount()
print 'Warnings: ', getWarningCount()
