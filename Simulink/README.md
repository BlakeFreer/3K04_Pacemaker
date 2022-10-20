# Simulink

## Parameter Buses
Most parameters are stored on the General Bus. The Atrial and Ventricular Buses are structured identically so that they can be used interchangably.

These parameters and their units were obtained from the PACEMAKER document, table 6 and 7.

Format:<br>
```SIMULINK_VARIABLE_NAME``` - Full Description - ```[units]```

1. ```BusGEN.```
    - ```MODE``` - Operating Mode - ```[ENUM]```
    - ```LRL``` - Lower Rate Limit - ```[BPM]```
    - ```URL``` - Upper Rate Limit - ```[BPM]```
    - ```MAX_SENSOR_RATE``` - Maximum Sensor Rate - ```[BPM]```
    - ```FIXED_AV_DELAY``` - Fixed AV Delay - ```[ms]```
    - ```DYNAMIC_AV_DELAY``` - Dynamic AV Delay - ```[OFF/ON]```
    - ```SENSED_AV_DELAY_OFFSET``` - Sensed AV Delay Offset - ```[ms]```
    - ```PVARP``` - Post Ventricular Atrial Refractory Period - ```[ms]```
    - ```PVARP_EXT``` - PVARP Extension - ```[ms]```
    - ```HYSTERESIS``` - Hysteresis - ```[BPM]```
    - ```RATE_SMOOTHING``` - Rate Smoothing - ```[double]```
    - ```ATR_DURATION``` - Atrial Tachycardia Response Duration - ```[Cardiac Cycles]```
    - ```ATR_FALLBACK_MODE``` - ATR Fallback Mode - ```[OFF/ON]```
    - ```ATR_FALLBACK_TIME``` - ATR Fallback Time - ```[min]```
    - ```ACTIVITY_THRESH``` - Activity Threshold - ```[ENUM]```
    - ```REACTION_TIME``` - Reaction Time - ```[sec]```
    - ```RESPONSE_FACTOR``` - Response Factor - ```[int]```
    - ```RECOVERY_TIME``` - Recovery Time - ```[min]```
2. ```BusSPECIFIC.```
    - ```AMP``` - A/V Amplitude - ```[V]```
    - ```PULSE_WIDTH``` - A/V Pulse Width - ```[ms]```
    - ```SENSITIVITY``` - A/V Sensitivity - ```[V]```
    - ```RP``` - A/V Refactory Period - ```[ms]```
3. ```BusMEASURED```
    - ```R_WAVE``` - R Wave Measurements - ```[mV]```
    - ```P_WAVE``` - P Wave Measurements - ```[mV]```
    - ```LEAD_IMPEDANCE``` - Lead Impedance - ```[Ohm]```
    - ```BATTERY_VOLTAGE``` - Battery Voltage - ```[V]```
## Enumerations
### MODE
| Name | Value |
|:-----|:-----:|
|Off|0|
|DDD|1|
|VDD|2|
|DDI|3|
|DOO|4|
|AOO|5|
|AAI|6|
|VOO|7|
|VVI|8|
|AAT|9|
|VVT|10|
|DDDR|11|
|VDDR|12|
|DDIR|13|
|DOOR|14|
|AOOR|15|
|AAIR|16|
|VOOR|17|
|VVIR|18|
### ACT_THRESH
| Name | Value |
|:-----|:-----:|
|VLOW|0|
|LOW|1|
|MEDLOW|2|
|MED|3|
|MEDHIGH|4|
|HIGH|5|
|VHIGH|6|
