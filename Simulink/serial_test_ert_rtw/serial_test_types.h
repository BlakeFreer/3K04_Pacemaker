/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: serial_test_types.h
 *
 * Code generated for Simulink model 'serial_test'.
 *
 * Model version                  : 1.18
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Thu Nov 24 12:19:30 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_serial_test_types_h_
#define RTW_HEADER_serial_test_types_h_
#include "rtwtypes.h"
#include "MW_SVD.h"

/* Model Code Variants */

/* Custom Type definition for MATLABSystem: '<Root>/Serial Transmit' */
#include "MW_SVD.h"
#ifndef struct_tag_0QIIqIWUIOhUbf1p9QN9pB
#define struct_tag_0QIIqIWUIOhUbf1p9QN9pB

struct tag_0QIIqIWUIOhUbf1p9QN9pB
{
  int32_T __dummy;
};

#endif                                 /* struct_tag_0QIIqIWUIOhUbf1p9QN9pB */

#ifndef typedef_b_freedomk64f_Hardware_serial_T
#define typedef_b_freedomk64f_Hardware_serial_T

typedef struct tag_0QIIqIWUIOhUbf1p9QN9pB b_freedomk64f_Hardware_serial_T;

#endif                             /* typedef_b_freedomk64f_Hardware_serial_T */

#ifndef struct_tag_EkIWEs70Gs0LyfeXELZ2TC
#define struct_tag_EkIWEs70Gs0LyfeXELZ2TC

struct tag_EkIWEs70Gs0LyfeXELZ2TC
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_serial_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
};

#endif                                 /* struct_tag_EkIWEs70Gs0LyfeXELZ2TC */

#ifndef typedef_freedomk64f_DigitalWrite_seri_T
#define typedef_freedomk64f_DigitalWrite_seri_T

typedef struct tag_EkIWEs70Gs0LyfeXELZ2TC freedomk64f_DigitalWrite_seri_T;

#endif                             /* typedef_freedomk64f_DigitalWrite_seri_T */

#ifndef struct_tag_214cR1nKZWaoqoq0FTtOUH
#define struct_tag_214cR1nKZWaoqoq0FTtOUH

struct tag_214cR1nKZWaoqoq0FTtOUH
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_serial_T Hw;
  MW_Handle_Type MW_SCIHANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_214cR1nKZWaoqoq0FTtOUH */

#ifndef typedef_freedomk64f_SCIRead_serial_te_T
#define typedef_freedomk64f_SCIRead_serial_te_T

typedef struct tag_214cR1nKZWaoqoq0FTtOUH freedomk64f_SCIRead_serial_te_T;

#endif                             /* typedef_freedomk64f_SCIRead_serial_te_T */

#ifndef struct_tag_GV9UedAE1zOVNNbkXknChB
#define struct_tag_GV9UedAE1zOVNNbkXknChB

struct tag_GV9UedAE1zOVNNbkXknChB
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_serial_T Hw;
  MW_Handle_Type MW_SCIHANDLE;
};

#endif                                 /* struct_tag_GV9UedAE1zOVNNbkXknChB */

#ifndef typedef_freedomk64f_SCIWrite_serial_t_T
#define typedef_freedomk64f_SCIWrite_serial_t_T

typedef struct tag_GV9UedAE1zOVNNbkXknChB freedomk64f_SCIWrite_serial_t_T;

#endif                             /* typedef_freedomk64f_SCIWrite_serial_t_T */

/* Parameters (default storage) */
typedef struct P_serial_test_T_ P_serial_test_T;

/* Forward declaration for rtModel */
typedef struct tag_RTM_serial_test_T RT_MODEL_serial_test_T;

#endif                                 /* RTW_HEADER_serial_test_types_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
