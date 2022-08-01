# 4-bit UpDown Counter Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image_2022-08-01_20-16-37](https://user-images.githubusercontent.com/72139504/182199370-4409b66f-2a24-41c5-b678-fc5fd6f9163d.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (updown_counter module here) which takes 5 inputs of 1-bit size named "clk","rst","load","updown", a 4-bit input "data" and provides a 4-bit output "data_out". Depending upon the the value of "updown" the counter starts counting at every clockedge provided reset to be transited from high to low. The data can be loaded to the counter be enabling "load" input for one clock cycle and loading data through "data" port, the counter will take the inputs from "data" port as reference point from where it continous counting.

Here we are verifying 5 scenarios:
> Reset <br />
> Up count <br />
> Down count <br />
> Up count with data loading <br />
> Down count with data loading <br />

For Reset verification, we check whether the "data_out" is properly made clear(all bits to 0) or not.<br />
For Up count verification, we check whether the values are getting incremented after every clockedge and if it reaches the limit it should restart the count.<br />
For Down count verification, we check whether the values are getting decremented after every clockedge and if it reaches the limit it should restart the count.<br />
For Up count with data loading, here the data which has been loaded after enabling load signal is verified (the counter continous counting up taking data loaded as reference).<br />
For Down count with data loading, here the data which has been loaded after enabling load signal is verified (the counter continous counting down taking data loaded as refernce)<br />

The assert statement is used for comparing the counter's output to the expected value.

The following errors are seen:<br />

assert(dut.data_out.value == 0000),"rst error, Reset not working properly"
                     AssertionError: rst error, Reset not working properly
                     
assert (output == present_count),"Error while counting down"
                     AssertionError: Error while counting down


## Test Scenario (Important)
- Reset -> data_out == 4'b0000
- Up count -> count increments from 0 to 15 then rolls back to 0.
- Down count -> count decrements from 15 to 0 then rolls back to 15.
- Up count with data input -> data = 'd12
- down count with data input -> data = 'd12

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following<br />
Bug1:<br />
always@(posedge clk)<br />
  begin<br />
    if(rst)<br />
      data_out <= 1'b1;<br />         ==== bug1 ( data_out <= 4'b0000 )
      
Bug2:<br />
  else<br />
      data_out <= ((updown)?(data_out + 1'b1):0);<br />      === bug2 (data_out <= ((updown)?(data_out + 1'b1):(data_out - 1'b1); 
  <br />end<br />
      

## Design Fix
Updating the design and re-running the test makes the test pass.

![image_2022-08-01_23-07-18](https://user-images.githubusercontent.com/72139504/182209095-4be2adaf-6e0c-4b7f-9a64-2c59f940e2e9.png)

The updated design is checked in as up_down_counter_fix.v

## Verification Strategy
> The count has been verified by taking the previous value of the count in a variable and comparing it with the count value after the clockedge.

## Is the verification complete ?
Yes

i.imgur.com/miWGA1o.png
