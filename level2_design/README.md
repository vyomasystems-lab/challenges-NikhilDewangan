# Bitmanupulation coprocessor Design Verification

Bug is in the model file : 
mav_putvalue=mav_putvalue_src1 & (~mav_putvalue_src2)      

fix for the bug :
mav_putvalue=mav_putvalue_src1 & (mav_putvalue_src2)    
