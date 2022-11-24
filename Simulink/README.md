# Simulink
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
2. `BusSPECIFIC.` - Prefix each parameter with `ATR_` or `VENT_` within DCM as necessary
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
| Value | Mode |
|-----:|:----:|
| OFF | 0 |
| DDD | 1 |
| VDD | 2 |
| DDI | 3 |
| DOO | 4 |
| AOO | 5 |
| AAI | 6 |
| VOO | 7 |
| VVI | 8 |
| AAT | 9 |
| VVT | 10 |
| DDDR | 11 |
| VDDR | 12 |
| DDIR | 13 |
| DOOR | 14 |
| AOOR | 15 |
| AAIR | 16 |
| VOOR | 17 |
| VVIR | 18 |

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

## Serial
A 32 byte package is sent from the DCM to Pacemaker. Each byte corresponds to a single parameter. Since some parameters have values that are not in the range 0-255, they are encoded as an 8 bit UNSIGNED integer and decoded on the pacemaker.
> For example, `ATR_RP` has a range of 10-500 ms, which is too large for one byte. However, values are incremented by 10 ms, so no information is lost by dividing the RP by 10, and the range is decreased to 1-50, which fits in a byte.

> Similarly, the `ATR_PULSE_WIDTH` is a decimal value between 0.05-1.9 ms. These values are multiplied by 100 to fit within an 8 bit integer.

The values are appropriately re-scaled on the pacemaker.

In addition, the strings `OFF` and `ON` are converted to the values `0` and `1` respectively

### Parameter Serial Package
If no method is specified, the the Parameter value is already an appropriate 8 bit unsigned integer.
| Byte Index | Parameter | Encoding Method | Decoding Method |
|:-:|:-|:-:|:-:|
| 0 | MODE | Enum |  |
| 1 | LRL |  |  |
| 2 | URL |  |  |
| 3 | MAX_SENSOR_RATE |  |  |
| 4 | FIXED_AV_DELAY | $\div10$ | $\times10$ |
| 5 | DYNAMIC_AV_DELAY |  |  |
| 6 | MINIMUM_DYNAMIC_AV_DELAY | | |
| 7 | SENSED_AV_DELAY_OFFSET |  $\times (-1)$ | $\times(-1)$  |
| 8 | PVARP | $\div10$ | $\times10$ |
| 9 | PVARP_EXT | $\div10$ | $\times10$ |
| 10 | HYSTERESIS |  |  |
| 11 | RATE_SMOOTHING |  |  |
| 12 | ATR_MODE |  |  |
| 13 | ATR_DURATION | $\div10$ | $\times10$ |
| 14 | ATR_FALLBACK_MODE |  |  |
| 15 | ATR_FALLBACK_TIME |  |  |
| 16 | VENTRICULAR_BLANKING |  |  |
| 17 | ACTIVITY_THRESH | Enum |  |
| 18 | REACTION_TIME |  |  |
| 19 | RESPONSE_FACTOR |  |  |
| 20 | RECOVERY_TIME |  |  |
| 21 | ATR_AMP | $\times10$ | $\div10$ |
| 22 | ATR_AMP_UNREGULATED | $\times4$ | $\div4$ |
| 23 | ATR_PULSE_WIDTH | $\times100$ | $\div100$ |
| 24 | ATR_SENSITIVITY | $\times4$ | $\times4$ |
| 25 | ATR_RP | $\div10$ | $\times10$ |
| 26 | VENT_AMP | $\times10$ | $\div10$ |
| 27 | VENT_AMP_UNREGULATED | $\times4$ | $\div4$ |
| 28 | VENT_PULSE_WIDTH | $\times100$ | $\div100$ |
| 29 | VENT_SENSITIVITY | $\times4$ | $\times4$ |
| 30 | VENT_RP | $\div10$ | $\times10$ |
| 31 | (BLANK) |  |  |