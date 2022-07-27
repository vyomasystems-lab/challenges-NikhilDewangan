# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    inp = []
    i0 = dut.inp0.value  = random.randint(0,3)
    inp.append(i0)
    i1 = dut.inp1.value  = random.randint(0,3) 
    inp.append(i1)
    i2 = dut.inp2.value  = random.randint(0,3)
    inp.append(i2)    
    i3 = dut.inp3.value  = random.randint(0,3) 
    inp.append(i3)   
    i4 = dut.inp4.value  = random.randint(0,3)
    inp.append(i4)      
    i5 = dut.inp5.value  = random.randint(0,3) 
    inp.append(i5)   
    i6 = dut.inp6.value  = random.randint(0,3) 
    inp.append(i6)   
    i7 = dut.inp7.value  = random.randint(0,3) 
    inp.append(i7)   
    i8 = dut.inp8.value  = random.randint(0,3) 
    inp.append(i8)   
    i9 = dut.inp9.value  = random.randint(0,3) 
    inp.append(i9)   
    i10 = dut.inp10.value= random.randint(0,3) 
    inp.append(i10)   
    i11 = dut.inp11.value= random.randint(0,3) 
    inp.append(i11)   
    i12 = dut.inp12.value= random.randint(0,3) 
    inp.append(i12)   
    i13 = dut.inp13.value= random.randint(0,3) 
    inp.append(i13)   
    i14 = dut.inp14.value= random.randint(0,3) 
    inp.append(i14)   
    i15 = dut.inp15.value= random.randint(0,3) 
    inp.append(i15)   
    i16 = dut.inp16.value= random.randint(0,3) 
    inp.append(i16)   
    i17 = dut.inp17.value= random.randint(0,3) 
    inp.append(i17)   
    i18 = dut.inp18.value= random.randint(0,3) 
    inp.append(i18)   
    i19 = dut.inp19.value= random.randint(0,3) 
    inp.append(i19)   
    i20 = dut.inp20.value= random.randint(0,3) 
    inp.append(i20)   
    i21 = dut.inp21.value= random.randint(0,3) 
    inp.append(i21)   
    i22 = dut.inp22.value= random.randint(0,3) 
    inp.append(i22)   
    i23 = dut.inp23.value= random.randint(0,3) 
    inp.append(i23)   
    i24 = dut.inp24.value= random.randint(0,3) 
    inp.append(i24)   
    i25 = dut.inp25.value= random.randint(0,3) 
    inp.append(i25)   
    i26 = dut.inp26.value= random.randint(0,3) 
    inp.append(i26)      
    i27 = dut.inp27.value= random.randint(0,3) 
    inp.append(i27)   
    i28 = dut.inp28.value= random.randint(0,3) 
    inp.append(i28)   
    i29 = dut.inp29.value= random.randint(0,3) 
    inp.append(i29)   
    i30 = dut.inp30.value= random.randint(0,3) 
    inp.append(i30)   

    for i in range(0,30):
        dut.sel.value = i
        await Timer(2, units='ns')
        dut._log.info(f'inp{i}={inp[i]} sel={int(dut.sel.value)} expected_output={inp[i]} DUT={int(dut.out.value)}')

        assert (dut.sel.value==i)and(dut.out.value == inp[i]),"Randomised test failed"
        # assert dut.out.value == inp[i], "Randomised test failed with: {A} + {B} = {SUM}".format(
        #     A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)

    cocotb.log.info('##### CTB: Develop your test here ########')