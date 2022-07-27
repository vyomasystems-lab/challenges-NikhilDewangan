# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path
from collections import deque

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    inputs = [0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,1]
    stimulus_queue = deque( maxlen = 5 )
    seq = 0

    def stimulus(i):
        #inp = dut.inp_bit.value = random.randint(0,1)
        inp = dut.inp_bit.value = i 
        return inp

    for i in inputs:
        # in_ = stimulus()
        in_ = stimulus(i)
        stimulus_queue.append(in_)
        await RisingEdge(dut.clk)

        #dut._log.info(f'Output : {int(dut.seq_seen.value)}')
        print("input_value: ",int(in_)," Output: ",dut.seq_seen.value)

        if(len(stimulus_queue)>=4):
            s = [str(i) for i in stimulus_queue]
            seq = str("".join(s))
            print(seq)
            if(seq=='1011'):
                await RisingEdge(dut.clk)
                assert (dut.seq_seen.value==1),"error assertion" 
    print(seq)        
    print(stimulus_queue)
    