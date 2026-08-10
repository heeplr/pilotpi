
# KiCAD files for PilotPi -
a RaspberryPi HAT for vehicle control using ardupilot

Based on https://github.com/SalimTerryLi/PilotPi_PCB


## Changes

### rc5
* optimize for low cost
* add (optional) piezo speaker
* more efficient TPS56A37 10A synchronous DCDC buck converter
* add CAN interface
* add RS485 transceiver
* move Vref to Power board
* use jumpers for config, not switches
* jumper for V_batt -> ADC to optionally free input for other analog stuff


## TODO
* use modern synchronous DCDC converter
* use KiCAD design variants? (CMx, beagleboard, etc.)
