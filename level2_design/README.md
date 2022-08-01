# Bitmanupulation coprocessor Design Verification

Bug1 is in the model file : 
mav_putvalue=mav_putvalue_src1 & (~mav_putvalue_src2)      
![image_2022-08-01_23-43-59](https://user-images.githubusercontent.com/72139504/182214612-87068630-559e-4c82-a6a2-c7fe29304212.png)


Bug2 is in the design, mav_putvalue_instr is defind with other than the combination of func7,func3 and opcode it generates some random value which does not match with the model<br />
![image_2022-08-01_23-48-48](https://user-images.githubusercontent.com/72139504/182216767-b1d5340d-e80a-479b-89c7-6653da29eb39.png)

fix for bug1 :
mav_putvalue=mav_putvalue_src1 & (mav_putvalue_src2)

