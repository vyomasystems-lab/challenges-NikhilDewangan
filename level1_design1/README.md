# Level1 - Design1 - Mux verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image_2022-08-01_20-16-37](https://user-images.githubusercontent.com/72139504/182176408-d5690493-521a-45b5-a84c-e0e5c02149e4.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes total of 32 inputs of which 31-inputs(inp0,inp1...inp30) are 2-bit and remaining 1-input(sel) is of 5-bit, upon selecting
a particular input using "sel" an output is generated in "out" port which is of 2-bit size.

The values are assigned to the input port using 
dut.inp0.value = random.randint(1,3)<br />
dut.inp1.value = random.randint(1,3)<br />
.<br />
.<br />
.<br />
dut.inp30.value = random.randint(1,3)

The assert statement is used for comparing the mux's output to the expected value.

The following error is seen:
assert (dut.sel.value==i)and(dut.out.value == inp[i]),"Randomised test failed, For select = {sel} [input != output => {inp} != {output}] ".format(sel = dut.sel.value,inp = inp[i], output = dut.out.value)
                     AssertionError: Randomised test failed, For select = 01100 [input != output => 2 != 00]
                     
## Test Scenario (Important)
- Test Inputs: inp0,inp1.....inp30 were randomized between 1 to 3
- Expected Output: out = randmized value of input with respect to the value of "sel" port. 
- Observed Output in the DUT, For sel = 5'b01100 (indicating inp12) - out = 0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

      5'b01101: out = inp12;            <=== Here is the bug 
                 
For the mux design, for the above pointed bug the bit value of sel should be "5'b01100" instead of "5'b01101" as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image_2022-08-01_20-12-21](https://user-images.githubusercontent.com/72139504/182175579-daff68ce-649c-41ef-b3c0-3df159a7703b.png)

The updated design is checked in as mux_fix.v

## Verification strategy
> Driving random inputs of range 1 to 3 in order to avoid getting value '0' in the inputs which may result in bug escape because the default is set to value '0'.
