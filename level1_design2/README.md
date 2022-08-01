# Level-1 Design-2 1011_Sequence_Detector Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image_2022-08-01_20-16-37](https://user-images.githubusercontent.com/72139504/182178778-2d4819d2-02c0-4b99-88fa-2646c8588f0b.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (sequence_detector module here) which takes in 1-bit input at every clockedge and generates the output value "1" in the next clocedge whenever the required sequenece of bits ("1011") is detected. *sum*

The values are assigned to the input port using a list

inputs = [0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1]
which will be sent sequentially at every clockedge starting from left to right.

The assert statement is used for comparing the sequence_detectors's output to expected value of output.

The following error is seen:
assert (dut.seq_seen.value==1),"Error,Unable to detect sequence"
                     AssertionError: Error,Unable to detect sequence
## Test Scenario (Important)
- Test Inputs: A sequence of bits were provided which are as follows   010110110110010111111010111
- Expected Output: The result of the sequence detector should generate 000001001001000001000000001
- Observed Output in the DUT is able to detect the sequence for the first time but misses the overlapping condition completely.

Output mismatches for the above inputs proving that there is a design bug

## Design Bugs
Based on the above test input and analysing the design, we see the following
Bug-1<br />
SEQ_1:<br />
      begin<br />
        if(inp_bit == 1)<br />
          next_state = IDLE;<br />                     // bug1:"IDLE" should be changed to "SEQ1" or "current_state"
        else<br />
          next_state = SEQ_10;<br />
      end<br />
Bug-2<br />
SEQ_101:<br />
      begin<br />
        if(inp_bit == 1)<br />
          next_state = SEQ_1011;<br />
        else<br />
          next_state = IDLE;<br />                      // bug2:"IDLE" should be changed to "SEQ_10"
      end<br />
Bug-3<br />
SEQ_1011:<br />
      begin<br /> 
        next_state = IDLE; <br />                       // bug3: missing condional statement for overlapping sequence
   <br />end<br />
      
For bug3 the following statement needs to be added by replacing "next_state = IDLE;" :<br />
        if(inp_bit==0)<br />
         next_state = SEQ_10;<br />
         else <br />
         next_state = SEQ_1; <br />

## Design Fix
Updating the design and re-running the test makes the test pass.

![image_2022-08-01_21-48-53](https://user-images.githubusercontent.com/72139504/182196150-131c37fc-20c9-4f4d-b9ce-87f4ba6c6e7a.png)

The updated design is checked in as seq_detect_1011_fix.v

## Verification Strategy
> For detecting the output on the next clockedge after the sequence detection has been using a "deque" of size limit 1 more than the size of the sequence which is to be detected (in our case "1011").
