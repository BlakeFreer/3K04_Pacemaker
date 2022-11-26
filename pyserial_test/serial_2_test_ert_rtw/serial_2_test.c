/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: serial_2_test.c
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

#include "serial_2_test.h"
#include "serial_2_test_types.h"
#include "rtwtypes.h"
#include <string.h>
#include <stddef.h>

/* Named constants for Chart: '<Root>/Chart' */
#define serial_2_test_IN_Init          ((uint8_T)1U)
#define serial_2_test_IN_RED_ON        ((uint8_T)2U)

/* Named constants for Chart: '<Root>/Chart1' */
#define serial_2_test_IN_green_on      ((uint8_T)1U)
#define serial_2_test_IN_init          ((uint8_T)2U)

/* Named constants for Chart: '<Root>/Chart2' */
#define serial_2_test_IN_SET_PRAMS     ((uint8_T)2U)
#define serial_2_test_IN_STANDBY       ((uint8_T)3U)

/* Block signals (default storage) */
B_serial_2_test_T serial_2_test_B;

/* Block states (default storage) */
DW_serial_2_test_T serial_2_test_DW;

/* Real-time model */
static RT_MODEL_serial_2_test_T serial_2_test_M_;
RT_MODEL_serial_2_test_T *const serial_2_test_M = &serial_2_test_M_;

/* Forward declaration for local functions */
static void serial_2_test_SystemCore_setup(freedomk64f_SCIRead_serial_2__T *obj);
static void serial_2_test_SystemCore_setup(freedomk64f_SCIRead_serial_2__T *obj)
{
  MW_SCI_Parity_Type ParityValue;
  MW_SCI_StopBits_Type StopBitsValue;
  uint32_T SCIModuleLoc;
  uint32_T TxPinLoc;
  obj->isSetupComplete = false;
  obj->isInitialized = 1;
  TxPinLoc = MW_UNDEFINED_VALUE;
  SCIModuleLoc = 0;
  obj->MW_SCIHANDLE = MW_SCI_Open(&SCIModuleLoc, false, 10U, TxPinLoc);
  MW_SCI_SetBaudrate(obj->MW_SCIHANDLE, 115200U);
  StopBitsValue = MW_SCI_STOPBITS_1;
  ParityValue = MW_SCI_PARITY_NONE;
  MW_SCI_SetFrameFormat(obj->MW_SCIHANDLE, 8, ParityValue, StopBitsValue);
  obj->isSetupComplete = true;
}

/* Model step function */
void serial_2_test_step(void)
{
  uint8_T RxDataLocChar[37];
  boolean_T rtb_red_out;

  /* MATLABSystem: '<Root>/Serial Receive1' */
  if (serial_2_test_DW.obj.SampleTime !=
      serial_2_test_P.SerialReceive1_SampleTime) {
    serial_2_test_DW.obj.SampleTime = serial_2_test_P.SerialReceive1_SampleTime;
  }

  MW_SCI_Receive(serial_2_test_DW.obj.MW_SCIHANDLE, &RxDataLocChar[0], 37U);
  memcpy((void *)&serial_2_test_B.RxData[0], (void *)&RxDataLocChar[0],
         (uint32_T)((size_t)37 * sizeof(int8_T)));

  /* Chart: '<Root>/Chart2' incorporates:
   *  MATLABSystem: '<Root>/Serial Receive1'
   */
  if (serial_2_test_DW.is_active_c10_serial_2_test == 0U) {
    serial_2_test_DW.is_active_c10_serial_2_test = 1U;
    serial_2_test_DW.is_c10_serial_2_test = serial_2_test_IN_Init;
  } else {
    switch (serial_2_test_DW.is_c10_serial_2_test) {
     case serial_2_test_IN_Init:
      serial_2_test_DW.is_c10_serial_2_test = serial_2_test_IN_STANDBY;
      break;

     case serial_2_test_IN_SET_PRAMS:
      serial_2_test_B.rand_h = 0.0;
      serial_2_test_DW.is_c10_serial_2_test = serial_2_test_IN_STANDBY;
      break;

     default:
      /* case IN_STANDBY: */
      if (serial_2_test_B.RxData[36] == 33) {
        serial_2_test_DW.is_c10_serial_2_test = serial_2_test_IN_SET_PRAMS;
        serial_2_test_B.rand_h = 0.0;
        memcpy((void *)&serial_2_test_B.mode, (void *)&serial_2_test_B.RxData[0],
               (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.LRL, (void *)&serial_2_test_B.RxData[1],
               (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.URL, (void *)&serial_2_test_B.RxData[2],
               (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.MAX_SENSOR_RATE, (void *)
               &serial_2_test_B.RxData[3], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.FIXED_AV_DELAY, (void *)
               &serial_2_test_B.RxData[4], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.DYNAMIC_AV_DELAY, (void *)
               &serial_2_test_B.RxData[5], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.min_dynam_av_delay, (void *)
               &serial_2_test_B.RxData[6], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.SENSED_AV_DELAY_OFFSET, (void *)
               &serial_2_test_B.RxData[7], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.PVARP, (void *)&serial_2_test_B.RxData[8],
               (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.PVARP_EXT, (void *)
               &serial_2_test_B.RxData[9], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.HYSTERESIS, (void *)
               &serial_2_test_B.RxData[10], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.RATE_SMOOTHING, (void *)
               &serial_2_test_B.RxData[11], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.ATR_MODE, (void *)
               &serial_2_test_B.RxData[12], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.ATR_DURATION, (void *)
               &serial_2_test_B.RxData[13], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.ATR_FALLBACK_MODE, (void *)
               &serial_2_test_B.RxData[14], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.ATR_FALLBACK_TIME, (void *)
               &serial_2_test_B.RxData[15], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.VENTRICULAR_BLANKING, (void *)
               &serial_2_test_B.RxData[16], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.ACTIVITY_TRESH, (void *)
               &serial_2_test_B.RxData[17], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.REACTION_TIME, (void *)
               &serial_2_test_B.RxData[18], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.RESPONSE_FACTOR, (void *)
               &serial_2_test_B.RxData[19], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.RECOVERY_TIME, (void *)
               &serial_2_test_B.RxData[20], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.AMP_ATR, (void *)
               &serial_2_test_B.RxData[21], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.AMP_UNREGULATED_ATR, (void *)
               &serial_2_test_B.RxData[22], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.PULSE_WIDTH_ATR, (void *)
               &serial_2_test_B.RxData[23], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.SENSITIVITY_ATR, (void *)
               &serial_2_test_B.RxData[24], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.RP_ATR, (void *)&serial_2_test_B.RxData
               [25], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.AMP_ATR, (void *)
               &serial_2_test_B.RxData[26], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.AMP_UNREGULATED_ATR, (void *)
               &serial_2_test_B.RxData[27], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.PULSE_WIDTH_ATR, (void *)
               &serial_2_test_B.RxData[28], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.SENSITIVITY_ATR, (void *)
               &serial_2_test_B.RxData[29], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.RP_ATR, (void *)&serial_2_test_B.RxData
               [30], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.AMP_VENT, (void *)
               &serial_2_test_B.RxData[31], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.AMP_UNREGULATED_VENT, (void *)
               &serial_2_test_B.RxData[32], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.PULSE_WIDTH_VENT, (void *)
               &serial_2_test_B.RxData[33], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.SENSITIVITY_VENT, (void *)
               &serial_2_test_B.RxData[34], (uint32_T)((size_t)1 * sizeof(int8_T)));
        memcpy((void *)&serial_2_test_B.RP_VENT, (void *)
               &serial_2_test_B.RxData[35], (uint32_T)((size_t)1 * sizeof(int8_T)));
      }
      break;
    }
  }

  /* End of Chart: '<Root>/Chart2' */

  /* Chart: '<Root>/Chart' incorporates:
   *  Sum: '<Root>/Add'
   */
  if (serial_2_test_DW.is_active_c3_serial_2_test == 0U) {
    serial_2_test_DW.is_active_c3_serial_2_test = 1U;
    serial_2_test_DW.is_c3_serial_2_test = serial_2_test_IN_Init;
    rtb_red_out = false;
  } else if (serial_2_test_DW.is_c3_serial_2_test == serial_2_test_IN_Init) {
    rtb_red_out = false;
    if ((real_T)(((((((((((((((((((((((((((((serial_2_test_B.LRL +
        serial_2_test_B.URL) + serial_2_test_B.MAX_SENSOR_RATE) +
        serial_2_test_B.FIXED_AV_DELAY) + serial_2_test_B.DYNAMIC_AV_DELAY) +
        serial_2_test_B.SENSED_AV_DELAY_OFFSET) + serial_2_test_B.PVARP) +
        serial_2_test_B.PVARP_EXT) + serial_2_test_B.HYSTERESIS) +
        serial_2_test_B.RATE_SMOOTHING) + serial_2_test_B.ATR_DURATION) +
        serial_2_test_B.ATR_FALLBACK_MODE) + serial_2_test_B.ATR_FALLBACK_TIME)
        + serial_2_test_B.ACTIVITY_TRESH) + serial_2_test_B.REACTION_TIME) +
        serial_2_test_B.RESPONSE_FACTOR) + serial_2_test_B.RECOVERY_TIME) +
        serial_2_test_B.AMP_ATR) + serial_2_test_B.PULSE_WIDTH_ATR) +
                           serial_2_test_B.SENSITIVITY_ATR) +
                          serial_2_test_B.RP_ATR) + serial_2_test_B.AMP_VENT) +
                        serial_2_test_B.PULSE_WIDTH_VENT) +
                       serial_2_test_B.SENSITIVITY_VENT) +
                      serial_2_test_B.RP_VENT) + serial_2_test_B.ATR_MODE) +
                    serial_2_test_B.min_dynam_av_delay) +
                   serial_2_test_B.VENTRICULAR_BLANKING) +
                  serial_2_test_B.AMP_UNREGULATED_ATR) +
                 serial_2_test_B.AMP_UNREGULATED_VENT) + serial_2_test_B.rand_h ==
        31.0) {
      serial_2_test_DW.is_c3_serial_2_test = serial_2_test_IN_RED_ON;
      rtb_red_out = true;
    }
  } else {
    /* case IN_RED_ON: */
    rtb_red_out = true;
  }

  /* End of Chart: '<Root>/Chart' */

  /* MATLABSystem: '<Root>/Digital Write' */
  MW_digitalIO_write(serial_2_test_DW.obj_b.MW_DIGITALIO_HANDLE, rtb_red_out);

  /* Chart: '<Root>/Chart1' incorporates:
   *  Constant: '<Root>/Constant'
   *  Product: '<Root>/Product'
   */
  if (serial_2_test_DW.is_active_c1_serial_2_test == 0U) {
    serial_2_test_DW.is_active_c1_serial_2_test = 1U;
    serial_2_test_DW.is_c1_serial_2_test = serial_2_test_IN_init;
  } else if (serial_2_test_DW.is_c1_serial_2_test == serial_2_test_IN_green_on)
  {
    serial_2_test_B.green_out = true;

    /* case IN_init: */
  } else if ((real_T)serial_2_test_B.mode * serial_2_test_P.Constant_Value ==
             10.0) {
    serial_2_test_DW.is_c1_serial_2_test = serial_2_test_IN_green_on;
    serial_2_test_B.green_out = true;
  }

  /* End of Chart: '<Root>/Chart1' */

  /* MATLABSystem: '<Root>/Digital Write1' */
  MW_digitalIO_write(serial_2_test_DW.obj_o.MW_DIGITALIO_HANDLE,
                     serial_2_test_B.green_out);
}

/* Model initialize function */
void serial_2_test_initialize(void)
{
  {
    freedomk64f_DigitalWrite_seri_T *obj;

    /* Start for MATLABSystem: '<Root>/Serial Receive1' */
    serial_2_test_DW.obj.isInitialized = 0;
    serial_2_test_DW.obj.matlabCodegenIsDeleted = false;
    serial_2_test_DW.obj.SampleTime = serial_2_test_P.SerialReceive1_SampleTime;
    serial_2_test_SystemCore_setup(&serial_2_test_DW.obj);

    /* Start for MATLABSystem: '<Root>/Digital Write' */
    serial_2_test_DW.obj_b.matlabCodegenIsDeleted = true;
    serial_2_test_DW.obj_b.isInitialized = 0;
    serial_2_test_DW.obj_b.matlabCodegenIsDeleted = false;
    obj = &serial_2_test_DW.obj_b;
    serial_2_test_DW.obj_b.isSetupComplete = false;
    serial_2_test_DW.obj_b.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(42U, 1);
    serial_2_test_DW.obj_b.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write1' */
    serial_2_test_DW.obj_o.matlabCodegenIsDeleted = true;
    serial_2_test_DW.obj_o.isInitialized = 0;
    serial_2_test_DW.obj_o.matlabCodegenIsDeleted = false;
    obj = &serial_2_test_DW.obj_o;
    serial_2_test_DW.obj_o.isSetupComplete = false;
    serial_2_test_DW.obj_o.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(43U, 1);
    serial_2_test_DW.obj_o.isSetupComplete = true;
  }
}

/* Model terminate function */
void serial_2_test_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/Serial Receive1' */
  if (!serial_2_test_DW.obj.matlabCodegenIsDeleted) {
    serial_2_test_DW.obj.matlabCodegenIsDeleted = true;
    if ((serial_2_test_DW.obj.isInitialized == 1) &&
        serial_2_test_DW.obj.isSetupComplete) {
      MW_SCI_Close(serial_2_test_DW.obj.MW_SCIHANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Serial Receive1' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write' */
  if (!serial_2_test_DW.obj_b.matlabCodegenIsDeleted) {
    serial_2_test_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((serial_2_test_DW.obj_b.isInitialized == 1) &&
        serial_2_test_DW.obj_b.isSetupComplete) {
      MW_digitalIO_close(serial_2_test_DW.obj_b.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write1' */
  if (!serial_2_test_DW.obj_o.matlabCodegenIsDeleted) {
    serial_2_test_DW.obj_o.matlabCodegenIsDeleted = true;
    if ((serial_2_test_DW.obj_o.isInitialized == 1) &&
        serial_2_test_DW.obj_o.isSetupComplete) {
      MW_digitalIO_close(serial_2_test_DW.obj_o.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write1' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
