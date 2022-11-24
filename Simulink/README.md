# Simulink
Created by
- Blake Freer
- Liam Luimes
- Aldraech Liac 

## Troubleshooting
### Buses Not Found
Go to the Pacemaker.slx model, then `MODELLING -> DESIGN -> BUS EDITOR -> Import -> MAT File` and select `Simulink/src/Buses.mat`
### Enums / Subsystems not found
Ensure that all subfolders withing 3K04_Pacemaker/Simulink are included in the Matlab path.

Within Matlab, go to `Environment -> Set Path` and add all paths

---

## Requirements Table
See `Simulink/RequirementsTable.slx`

---

## Parameter Buses
Most parameters are stored on the General Bus. The Atrial and Ventricular Buses are structured identically so that they can be used interchangably.

These parameters and their units were obtained from the PACEMAKER document, table 6 and 7.

Format:\
`SIMULINK_VARIABLE_NAME` - Full Description - `[units]`

1. `BusGEN.`
    - `MODE` - Operating Mode - `[ENUM]`
    - `RATE_ADAPTIVE` - Rate Adaptive - `[OFF/ON]`
    - `LRL` - Lower Rate Limit - `[BPM]`
    - `URL` - Upper Rate Limit - `[BPM]`
    - `MAX_SENSOR_RATE` - Maximum Sensor Rate - `[BPM]`
    - `FIXED_AV_DELAY` - Fixed AV Delay - `[ms]`
    - `DYNAMIC_AV_DELAY` - Dynamic AV Delay - `[OFF/ON]`
    - `MINIMUM_DYNAMIC_AV_DELAY` - Minimum Dynamic AV Delay - `[ms]` 
    - `SENSED_AV_DELAY_OFFSET` - Sensed AV Delay Offset - `[ms]`
    - `PVARP` - Post Ventricular Atrial Refractory Period - `[ms]`
    - `PVARP_EXT` - PVARP Extension - `[ms]`
    - `HYSTERESIS` - Hysteresis - `[BPM]`
    - `RATE_SMOOTHING` - Rate Smoothing - `[double]`
    - `ATR_MODE` - Atrial Tachycardia Response - `[OFF/ON]`
    - `ATR_DURATION` - Atrial Tachycardia Response Duration - `[Cardiac Cycles]`
    - `ATR_FALLBACK_MODE` - ATR Fallback Mode - `[OFF/ON]`
    - `ATR_FALLBACK_TIME` - ATR Fallback Time - `[min]`
    - `VENTRICULAR_BLANKING` - Ventricular Blanking - `[ms]`
    - `ACTIVITY_THRESH` - Activity Threshold - `[ENUM]`
    - `REACTION_TIME` - Reaction Time - `[sec]`
    - `RESPONSE_FACTOR` - Response Factor - `[int]`
    - `RECOVERY_TIME` - Recovery Time - `[min]`
2. `BusSPECIFIC.`
    - `AMP` - A/V Amplitude - `[V]`
    - `AMP_UNREGULATED` - A/V Amplitude Unregulated - `[V]`
    - `PULSE_WIDTH` - A/V Pulse Width - `[ms]`
    - `SENSITIVITY` - A/V Sensitivity - `[V]`
    - `RP` - A/V Refactory Period - `[ms]`
3. `BusMEASURED`
    - `R_WAVE` - R Wave Measurements - `[mV]`
    - `P_WAVE` - P Wave Measurements - `[mV]`
    - `LEAD_IMPEDANCE` - Lead Impedance - `[Ohm]`
    - `BATTERY_VOLTAGE` - Battery Voltage - `[V]`
---
## Enumerations
### **MODE**
| RATE_MOD = OFF | MODE | RATE_MOD = ON |
|-----:|:----:|:--------|
| OFF | 0 | OFF |
| DDD | 1 | DDDR |
| VDD | 2 | VDDR |
| DDI | 3 | DDIR |
| DOO | 4 | DOOR |
| AOO | 5 | AOOR |
| AAI | 6 | AAIR |
| VOO | 7 | VOOR |
| VVI | 8 | VVIR |
| AAT | 9 | AAT |
| VVT | 10 | VVT |

### Example
`VVI` is stored as `(MODE=8` and `RATE_MOD=FALSE)`

`VVIR` is stored as `(MODE=8` and `RATE_MOD=TRUE)`

### **ACT_THRESH**
| Name | Value |
|:-----|:-----:|
|VLOW|0|
|LOW|1|
|MEDLOW|2|
|MED|3|
|MEDHIGH|4|
|HIGH|5|
|VHIGH|6|
