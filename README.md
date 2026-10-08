# UNTESTED YET! (preliminary release only)

<p align="center">
  <img src="https://raw.githubusercontent.com/heeplr/pilotpi/refs/heads/master/assets/logo.svg" alt="PilotPi" width="50%">
</p>

## KiCAD files for PilotPi - &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [![KiCAD ERC/DRC](https://github.com/heeplr/pilotpi/actions/workflows/kicad-erc-drc.yml/badge.svg)](https://github.com/heeplr/pilotpi/actions/workflows/kicad-erc-drc.yml)
a RaspberryPi HAT for vehicle control using ardupilot based on [@SalimTerryLi/PilotPi_PCB](https://github.com/SalimTerryLi/PilotPi_PCB)

<br>

### [Power PCB & Schematics](/power)
### [Sensors PCB & Schematics](/sensors)

<br><br><br>

## Features

* **Power:**
    * 3~6S battery with built-in voltage sensing.
    * Power the Pi through USB cable

* **Accelerometer / Gyro:**
    * ICM42605

* **Magnetometer:**
    * MMC5983MA

* **Barometer:**
    * SPA06-003

* **PWM:**
    * PCA9685

* **ADC:**
    * ADS1115

* **CAN:**
    * MCP2515 + MCP2562

* **RS485:**
    * SP3485EN


* **Connectivity:**
    - 16x PWM outputting channels
    - CAN
    - RS485
    - GPS connector (UART)
    - Telemetry connector (UART)
    - External I2C bus connector (Note: conflicts with CSI camera)
    - RC input port (SBUS/i-BUS UART)
    - 3x ADC channels range 0~5V
    - 2*8 2.54mm unused GPIO connector

    - Direct accessible from RPi:

      - 4x USB connector
      - CSI connector(Note: conflict with external I2C bus)
      - ...

<br><br><br>

## Changes

### rc5
* add (optional) piezo speaker
* add RGB LED
* more efficient TPS56A37 10A synchronous DCDC buck converter
* use ICM-42605 IMU
* use 
* add CAN interface
* add RS485 transceiver
* add I2C expander to Power board
* move Vref to Power board
* use jumpers for config, not switches
* jumper for V_batt -> ADC to optionally free input for other analog stuff
* add shift register to SPI0


## TODO
* use KiCAD design variants? (one for CMx, one for beagleboard, etc.)
