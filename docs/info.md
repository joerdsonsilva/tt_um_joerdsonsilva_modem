<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

The multimode modem uses a clock signal to generate digitized signals over time, in sinusoidal format (carrier wave).
From this digitized sinusoid, the modulation process is applied using different methods for each scheme, implemented 
through specific internal blocks to perform modulations ASK (switching the amplitude of the sine wave), FSK (switching 
the frequency of the sine wave through a digital signal modulator) and PSK (phase coding). In the demodulation stage, 
these three modulation schemes are analyzed to recover the original information, manifesting as '0' or '1' values that 
reflect the data signal already restored after the process.

## How to test

 The multimode modem has the following inputs and outputs:
     
  - Input  - clock (1 bit)
  - Input  - reset (1 bit)
  - Input  - sel (2 bits)
  - Output - mod_out (7 bits)
  - Output - demod_out (1 bit)
       
Apply a “clock” of 40~50 MHz. Then, apply a “reset” signal of logic level “1” to synchronize the modem system and then make the 
“reset” signal a logic level “0”. After that, select the type of modulation to be used, as per the sequence below:

  - Sel = "01" <= ASK modulation and demodulation
    
  - Sel = "10" <= FSK modulation and demodulation

  - Sel = "11" <= PSK modulation and demodulation

After selecting the modulation type, the modulated signal is expressed at the “mod_out” output, and the demodulated signal at the 
“demod_out” output.

## External hardware

Analog Discovery 2
