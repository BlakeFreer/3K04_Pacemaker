# Simulink

## Parameter Buses
The Atrial and Ventricular Buses are structured identically so that they can be used interchangably.

These parameters and their units were obtained from the PACEMAKER document, table 6 and 7.

Format:<br>
```SIMULINK_VARIABLE_NAME``` - Full Description - ```[units]```

1. ```BusGEN.```
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
2. ```BusATR.```
    - ```AMP``` - Atrial Amplitude - ```[V]```
    - ```PULSE_WIDTH``` - Atrial Pulse Width - ```[ms]```
    - ```SENSITIVITY``` - Atrial Sensitivity - ```[V]```
    - ```RP``` - Atrial Refactory Period - ```[ms]```
3. ```BusVENT.```
    - ```AMP``` - Ventricular Sensitivity - ```[V]```
    - ```PULSE_WIDTH``` - Ventricular Pulse Width - ```[ms]```
    - ```SENSITIVITY``` - Ventricular Sensitivity - ```[V]```
    - ```RP``` - Ventricular Refractory Period - ```[ms]```