
Bug is in the model file : 
mav_putvalue=mav_putvalue_src1 & (~mav_putvalue_src2)    <=====  "~" is a bug here,which should be removed

fix for the bug :
mav_putvalue=mav_putvalue_src1 & (mav_putvalue_src2)    
