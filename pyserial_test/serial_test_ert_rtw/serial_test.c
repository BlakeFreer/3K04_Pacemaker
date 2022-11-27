/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: serial_test.c
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

#include "serial_test.h"
#include "serial_test_types.h"
#include "rtwtypes.h"
#include <string.h>
#include <stddef.h>

/* Named constants for Chart: '<Root>/Chart' */
#define serial_test_IN_Init            ((uint8_T)1U)
#define serial_test_IN_SET_Params      ((uint8_T)2U)
#define serial_test_IN_STANDBY         ((uint8_T)3U)

/* Block signals (default storage) */
B_serial_test_T serial_test_B;

/* Block states (default storage) */
DW_serial_test_T serial_test_DW;

/* Real-time model */
static RT_MODEL_serial_test_T serial_test_M_;
RT_MODEL_serial_test_T *const serial_test_M = &serial_test_M_;

/* Forward declaration for local functions */
static void serial_test_SystemCore_setup(freedomk64f_SCIRead_serial_te_T *obj);
static void serial_test_SystemCore_setup(freedomk64f_SCIRead_serial_te_T *obj)
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
void serial_test_step(void)
{
  int8_T RxData[3];
  uint8_T RxDataLocChar[3];
  uint8_T status;

  /* MATLABSystem: '<Root>/Serial Receive' */
  if (serial_test_DW.obj.SampleTime != serial_test_P.SerialReceive_SampleTime) {
    serial_test_DW.obj.SampleTime = serial_test_P.SerialReceive_SampleTime;
  }

  status = MW_SCI_Receive(serial_test_DW.obj.MW_SCIHANDLE, &RxDataLocChar[0], 3U);
  memcpy((void *)&RxData[0], (void *)&RxDataLocChar[0], (uint32_T)((size_t)3 *
          sizeof(int8_T)));

  /* Chart: '<Root>/Chart' incorporates:
   *  MATLABSystem: '<Root>/Serial Receive'
   */
  if (serial_test_DW.is_active_c3_serial_test == 0U) {
    serial_test_DW.is_active_c3_serial_test = 1U;
    serial_test_DW.is_c3_serial_test = serial_test_IN_Init;
  } else {
    switch (serial_test_DW.is_c3_serial_test) {
     case serial_test_IN_Init:
      serial_test_DW.is_c3_serial_test = serial_test_IN_STANDBY;
      break;

     case serial_test_IN_SET_Params:
      serial_test_DW.is_c3_serial_test = serial_test_IN_STANDBY;
      break;

     default:
      /* case IN_STANDBY: */
      if (status == 0) {
        if (RxData[0] == 6) {
          serial_test_DW.is_c3_serial_test = serial_test_IN_SET_Params;
          serial_test_B.red_out = RxData[1];
        } else {
          serial_test_DW.is_c3_serial_test = serial_test_IN_STANDBY;
        }
      }
      break;
    }
  }

  /* End of Chart: '<Root>/Chart' */

  /* MATLABSystem: '<Root>/Digital Write' */
  MW_digitalIO_write(serial_test_DW.obj_b.MW_DIGITALIO_HANDLE,
                     serial_test_B.red_out != 0);
}

/* Model initialize function */
void serial_test_initialize(void)
{
  {
    freedomk64f_DigitalWrite_seri_T *obj;

    /* Start for MATLABSystem: '<Root>/Serial Receive' */
    serial_test_DW.obj.isInitialized = 0;
    serial_test_DW.obj.matlabCodegenIsDeleted = false;
    serial_test_DW.obj.SampleTime = serial_test_P.SerialReceive_SampleTime;
    serial_test_SystemCore_setup(&serial_test_DW.obj);

    /* Start for MATLABSystem: '<Root>/Digital Write' */
    serial_test_DW.obj_b.matlabCodegenIsDeleted = true;
    serial_test_DW.obj_b.isInitialized = 0;
    serial_test_DW.obj_b.matlabCodegenIsDeleted = false;
    obj = &serial_test_DW.obj_b;
    serial_test_DW.obj_b.isSetupComplete = false;
    serial_test_DW.obj_b.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(42U, 1);
    serial_test_DW.obj_b.isSetupComplete = true;
  }
}

/* Model terminate function */
void serial_test_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/Serial Receive' */
  if (!serial_test_DW.obj.matlabCodegenIsDeleted) {
    serial_test_DW.obj.matlabCodegenIsDeleted = true;
    if ((serial_test_DW.obj.isInitialized == 1) &&
        serial_test_DW.obj.isSetupComplete) {
      MW_SCI_Close(serial_test_DW.obj.MW_SCIHANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Serial Receive' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write' */
  if (!serial_test_DW.obj_b.matlabCodegenIsDeleted) {
    serial_test_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((serial_test_DW.obj_b.isInitialized == 1) &&
        serial_test_DW.obj_b.isSetupComplete) {
      MW_digitalIO_close(serial_test_DW.obj_b.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
