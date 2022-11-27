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

### BusGEN
| Parameter | Full Name | Units | Datatype |
|:-|:-|:-|:-|
| LRL | Lower Rate Limit | BPM | double |
| URL | Upper Rate Limit | BPM | double |
| MAX_SENSOR_RATE | Maximum Sensor Rate | BPM | double |
| FIXED_AV_DELAY | Fixed AV Delay | ms | double |
| DYNAMIC_AV_DELAY | Dynamic AV Delay | OFF/ON | boolean |
| MINIMUM_DYNAMIC_AV_DELAY | Minimum Dynamic AV Delay | ms | double |
| SENSED_AV_DELAY_OFFSET | Sensed AV Delay Offset | ms | double |
| PVARP | Post Ventricular Atrial Refractory Period | ms | double |
| PVARP_EXT | PVARP Extension | ms | double |
| HYSTERESIS | Hysteresis | BPM | double |
| RATE_SMOOTHING | Rate Smoothing | double | double |
| ATR_MODE | Atrial Tachycardia Response | OFF/ON | boolean |
| ATR_DURATION | Atrial Tachycardia Response Duration | Cardiac Cycles | int64 |
| ATR_FALLBACK_MODE | ATR Fallback Mode | OFF/ON | boolean |
| ATR_FALLBACK_TIME | ATR Fallback Time | min | double |
| VENTRICULAR_BLANKING | Ventricular Blanking | ms | double |
| ACTIVITY_THRESH | Activity Threshold | ENUM | Enum: ACT_THRESH |
| REACTION_TIME | Reaction Time | sec | double |
| RESPONSE_FACTOR | Response Factor | ul | double|
| RECOVERY_TIME | Recovery Time | min | double |
### BusSPECIFIC
| Parameter | Full Name | Units | Datatype |
|:-|:-|:-|:-|
| AMP | A/V Amplitude | V | double |
| AMP_UNREGULATED | A/V Amplitude Unregulated | V | double |
| PULSE_WIDTH | A/V Pulse Width | ms | double |
| SENSITIVITY | A/V Sensitivity | V | double |
| RP | A/V Refactory Period | ms | double |
### BusMEASURED
| Parameter | Full Name | Units | Datatype |
|:-|:-|:-|:-|
| R_WAVE | R Wave Measurements | mV | boolean |
| P_WAVE | P Wave Measurements | mV | boolean |
| LEAD_IMPEDANCE | Lead Impedance | Ohm | double |
| BATTERY_VOLTAGE | Battery Voltage | V | double |
| HEART_RATE | Current Pacing Heart Rate | BPM | double |
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
See DCM/README Serial Section