# Author: Blake Freer
# Date Created: November 24, 2022
# Description: Converts a dictionary of pacemaker values to a 32-byte array for serial transmission

# Usage: In the DCM python file, call 'import SerialConverter' and call the method 'foo = SerialCoverter.ConvertData(dictionary)' on the dictionary of data
# This returns an integer array. Send it via serial with Serial.write(bytearray(foo))
# Obviously replace 'foo' with a better variable name

# Additionally, this file provides the default values for each parameter. Access this via SerialConverter.DefaultParams()

def ConvertData(data):

    dict = data.copy()    

    # Preprocessing on dict 
    for k in dict:
        # convert all characters to uppercase and remove whitespace
        dict[k] = dict[k].upper().strip()
     
    # Define Enums for converting to integers
    enumMode = {
        "OFF" : "0",
        "DDD" : "1",
        "VDD" : "2",
        "DDI" : "3",
        "DOO" : "4",
        "AOO" : "5",
        "AAI" : "6",
        "VOO" : "7",
        "VVI" : "8",
        "AAT" : "9",
        "VVT" : "10",
        "DDDR" : "11",
        "VDDR" : "12",
        "DDIR" : "13",
        "DOOR" : "14",
        "AOOR" : "15",
        "AAIR" : "16",
        "VOOR" : "17",
        "VVIR" : "18"
    }
    enumActThresh = {
        "VLOW" : "0",
        "LOW" : "1",
        "MEDLOW" : "2",
        "MED" : "3",
        "MEDHIGH" : "4",
        "HIGH" : "5",
        "VHIGH" : "6"
    }


    output = [0] * 32

    # Convert Enums to integers
    dict["MODE"] = enumMode[dict["MODE"]]
    dict["ACTIVITY_THRESH"] = enumActThresh[dict["ACTIVITY_THRESH"]]

    # Convert "OFF" and "ON" to integers
    for k in dict:
        dict[k] = "0" if dict[k] == "OFF" else dict[k]
        dict[k] = "1" if dict[k] == "ON" else dict[k]


    # This array provides the order of the bytes in output[] and which multiplier to use to fit with 8 bits
    keyOrderMult = [
        ("MODE",1),
        ("LRL",1),
        ("URL",1),
        ("MAX_SENSOR_RATE",1),
        ("FIXED_AV_DELAY",0.1),
        ("DYNAMIC_AV_DELAY",1),
        ("MINIMUM_DYNAMIC_AV_DELAY",1),
        ("SENSED_AV_DELAY_OFFSET",-1),
        ("PVARP",0.1),
        ("PVARP_EXT",0.1),
        ("HYSTERESIS",1),
        ("RATE_SMOOTHING",1),
        ("ATR_MODE",1),
        ("ATR_DURATION",0.1),
        ("ATR_FALLBACK_MODE",0),
        ("ATR_FALLBACK_TIME",1),
        ("VENTRICULAR_BLANKING",1),
        ("ACTIVITY_THRESH",1),
        ("REACTION_TIME",1),
        ("RESPONSE_FACTOR",1),
        ("RECOVERY_TIME",1),
        ("ATR_AMP",10),
        ("ATR_AMP_UNREGULATED",4),
        ("ATR_PULSE_WIDTH",100),
        ("ATR_SENSITIVITY",4),
        ("ATR_RP",0.1),
        ("VENT_AMP",10),
        ("VENT_AMP_UNREGULATED",4),
        ("VENT_PULSE_WIDTH",100),
        ("VENT_SENSITIVITY",4),
        ("VENT_RP",0.1)
    ]

    # Convert all dict values to integer values by applying the appropriate multipliers
    for i, val in enumerate(keyOrderMult):
        if val[1] == 1:
            output[i] = int(dict[val[0]])
        else:
            output[i] = int(float(dict[val[0]]) * val[1])

    return output

def DefaultParams():
    # Default parameter values as specific in the PACEMAKER document
    return {
        'MODE':"DDD",
        'LRL':"60",
        'URL':"120",
        'MAX_SENSOR_RATE':"120",
        'FIXED_AV_DELAY':"150",
        'DYNAMIC_AV_DELAY':"ON",
        'MINIMUM_DYNAMIC_AV_DELAY':"50",
        'SENSED_AV_DELAY_OFFSET':"OFF",
        'PVARP':"250",
        'PVARP_EXT':"OFF",
        'HYSTERESIS':"OFF",
        'RATE_SMOOTHING':"OFF",
        'ATR_MODE':"OFF",
        'ATR_DURATION':"20",
        'ATR_FALLBACK_MODE':"OFF",
        'ATR_FALLBACK_TIME':"1",
        'VENTRICULAR_BLANKING':"40",
        'ACTIVITY_THRESH':"MED",
        'REACTION_TIME':"30",
        'RESPONSE_FACTOR':"8",
        'RECOVERY_TIME':"5",
        'ATR_AMP':"3.5",
        'ATR_AMP_UNREGULATED':"3.75",
        'ATR_PULSE_WIDTH':"0.4",
        'ATR_SENSITIVITY':"0.75",
        'ATR_RP':"250",
        'VENT_AMP':"3.5",
        'VENT_AMP_UNREGULATED':"3.75",
        'VENT_PULSE_WIDTH':"0.4",
        'VENT_SENSITIVITY':"2.5",
        'VENT_RP':"320",
    }
