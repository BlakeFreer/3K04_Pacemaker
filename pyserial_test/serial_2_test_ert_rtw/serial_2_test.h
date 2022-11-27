/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: serial_2_test.h
 *
 * Code generated for Simulink model 'serial_2_test'.
 *
 * Model version                  : 1.8
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Sat Nov 26 00:19:47 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_serial_2_test_h_
#define RTW_HEADER_serial_2_test_h_
#ifndef serial_2_test_COMMON_INCLUDES_
#define serial_2_test_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_SCI.h"
#endif                                 /* serial_2_test_COMMON_INCLUDES_ */

#include "serial_2_test_types.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  int8_T RxData[37];
  real_T rand_h;                       /* '<Root>/Chart2' */
  int8_T LRL;                          /* '<Root>/Chart2' */
  int8_T URL;                          /* '<Root>/Chart2' */
  int8_T MAX_SENSOR_RATE;              /* '<Root>/Chart2' */
  int8_T FIXED_AV_DELAY;               /* '<Root>/Chart2' */
  int8_T DYNAMIC_AV_DELAY;             /* '<Root>/Chart2' */
  int8_T SENSED_AV_DELAY_OFFSET;       /* '<Root>/Chart2' */
  int8_T PVARP;                        /* '<Root>/Chart2' */
  int8_T PVARP_EXT;                    /* '<Root>/Chart2' */
  int8_T HYSTERESIS;                   /* '<Root>/Chart2' */
  int8_T RATE_SMOOTHING;               /* '<Root>/Chart2' */
  int8_T ATR_DURATION;                 /* '<Root>/Chart2' */
  int8_T ATR_FALLBACK_MODE;            /* '<Root>/Chart2' */
  int8_T ATR_FALLBACK_TIME;            /* '<Root>/Chart2' */
  int8_T ACTIVITY_TRESH;               /* '<Root>/Chart2' */
  int8_T REACTION_TIME;                /* '<Root>/Chart2' */
  int8_T RESPONSE_FACTOR;              /* '<Root>/Chart2' */
  int8_T RECOVERY_TIME;                /* '<Root>/Chart2' */
  int8_T AMP_ATR;                      /* '<Root>/Chart2' */
  int8_T PULSE_WIDTH_ATR;              /* '<Root>/Chart2' */
  int8_T SENSITIVITY_ATR;              /* '<Root>/Chart2' */
  int8_T RP_ATR;                       /* '<Root>/Chart2' */
  int8_T AMP_VENT;                     /* '<Root>/Chart2' */
  int8_T PULSE_WIDTH_VENT;             /* '<Root>/Chart2' */
  int8_T SENSITIVITY_VENT;             /* '<Root>/Chart2' */
  int8_T RP_VENT;                      /* '<Root>/Chart2' */
  int8_T ATR_MODE;                     /* '<Root>/Chart2' */
  int8_T min_dynam_av_delay;           /* '<Root>/Chart2' */
  int8_T VENTRICULAR_BLANKING;         /* '<Root>/Chart2' */
  int8_T AMP_UNREGULATED_ATR;          /* '<Root>/Chart2' */
  int8_T AMP_UNREGULATED_VENT;         /* '<Root>/Chart2' */
  int8_T mode;                         /* '<Root>/Chart2' */
  boolean_T green_out;                 /* '<Root>/Chart1' */
} B_serial_2_test_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_SCIRead_serial_2__T obj; /* '<Root>/Serial Receive1' */
  freedomk64f_DigitalWrite_seri_T obj_o;/* '<Root>/Digital Write1' */
  freedomk64f_DigitalWrite_seri_T obj_b;/* '<Root>/Digital Write' */
  uint8_T is_active_c10_serial_2_test; /* '<Root>/Chart2' */
  uint8_T is_c10_serial_2_test;        /* '<Root>/Chart2' */
  uint8_T is_active_c1_serial_2_test;  /* '<Root>/Chart1' */
  uint8_T is_c1_serial_2_test;         /* '<Root>/Chart1' */
  uint8_T is_active_c3_serial_2_test;  /* '<Root>/Chart' */
  uint8_T is_c3_serial_2_test;         /* '<Root>/Chart' */
} DW_serial_2_test_T;

/* Parameters (default storage) */
struct P_serial_2_test_T_ {
  real_T SerialReceive1_SampleTime;    /* Expression: -1
                                        * Referenced by: '<Root>/Serial Receive1'
                                        */
  real_T Constant_Value;               /* Expression: 1/10
                                        * Referenced by: '<Root>/Constant'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_serial_2_test_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_serial_2_test_T serial_2_test_P;

/* Block signals (default storage) */
extern B_serial_2_test_T serial_2_test_B;

/* Block states (default storage) */
extern DW_serial_2_test_T serial_2_test_DW;

/* Model entry point functions */
extern void serial_2_test_initialize(void);
extern void serial_2_test_step(void);
extern void serial_2_test_terminate(void);

/* Real-time Model object */
extern RT_MODEL_serial_2_test_T *const serial_2_test_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'serial_2_test'
 * '<S1>'   : 'serial_2_test/Chart'
 * '<S2>'   : 'serial_2_test/Chart1'
 * '<S3>'   : 'serial_2_test/Chart2'
 */
#endif                                 /* RTW_HEADER_serial_2_test_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
