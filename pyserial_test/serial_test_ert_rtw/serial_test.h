/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: serial_test.h
 *
 * Code generated for Simulink model 'serial_test'.
 *
 * Model version                  : 1.22
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Fri Nov 25 15:49:09 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_serial_test_h_
#define RTW_HEADER_serial_test_h_
#ifndef serial_test_COMMON_INCLUDES_
#define serial_test_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_SCI.h"
#endif                                 /* serial_test_COMMON_INCLUDES_ */

#include "serial_test_types.h"
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
  int8_T red_out;                      /* '<Root>/Chart' */
} B_serial_test_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_SCIRead_serial_te_T obj; /* '<Root>/Serial Receive' */
  freedomk64f_DigitalWrite_seri_T obj_b;/* '<Root>/Digital Write' */
  uint8_T is_active_c3_serial_test;    /* '<Root>/Chart' */
  uint8_T is_c3_serial_test;           /* '<Root>/Chart' */
} DW_serial_test_T;

/* Parameters (default storage) */
struct P_serial_test_T_ {
  real_T SerialReceive_SampleTime;     /* Expression: -1
                                        * Referenced by: '<Root>/Serial Receive'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_serial_test_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_serial_test_T serial_test_P;

/* Block signals (default storage) */
extern B_serial_test_T serial_test_B;

/* Block states (default storage) */
extern DW_serial_test_T serial_test_DW;

/* Model entry point functions */
extern void serial_test_initialize(void);
extern void serial_test_step(void);
extern void serial_test_terminate(void);

/* Real-time Model object */
extern RT_MODEL_serial_test_T *const serial_test_M;

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
 * '<Root>' : 'serial_test'
 * '<S1>'   : 'serial_test/Chart'
 */
#endif                                 /* RTW_HEADER_serial_test_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
