
# KiCAD files for PilotPi -
a RaspberryPi HAT for vehicle control using ardupilot

Based on https://github.com/SalimTerryLi/PilotPi_PCB


## Changes

### rc5
* optimize for cost
* add piezo speaker
* add CAN interface
* move Vref to Power board
* use jumpers for config, not switches
* jumper for Vref -> ADC to optionally free input for other stuff


## TODO
* use modern synchronous DCDC converter
* use KiCAD design variants? (CMx, beagleboard, etc.)
