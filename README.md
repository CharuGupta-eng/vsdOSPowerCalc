# OS-power-analysis-tool
Power analysis has materialized as a principal theme in today’s world of semiconductor industries. Very Large Scaled Integrated Circuits (VLSI) are far beyond human ability because of complexity. So to analyse power in these circuits we use open source computer aided tools, plenty of tools are available but most of them are costly. I designed open source power analysis tool for the academic use which analyse power dissipation (average switching and leakage power) efficiently.

## Power analysis
Power analysis of design can be reconnoitred at several levels such as system level, architectural level, logic level, circuit level and device level. Power analyser is a tool which determines how much power is utilize by a system or circuit. In this process we give circuits as input along with few operating conditions to power analyser to get report about the power. 

For power analysis I simulate D flip flop using pass transistor, transmission gate, pass transistor with stacking of transistor. Simulate 2-4 line decoder using CMOS logic and TG, DVL alternatively. Simulate 2-1 MUX using pass transistor, transmission gate, MTCMOS logic. Generate netlist and input output and power(V * I) waveform for all schematic circuit.

# Inputs for Python Power Tool
 First input is spice netlist. While executing script some more inputs are taken such as
    Name of Supply Voltage
    Node name of Supply Voltage
    For synchronous circuit time perod of clock and for asynchronous minimum time period among all input pulse
# Python Power tool with example
   First download or clone this repository.
   To see circuit diagrams of scheamtic, go to images and there are images of circuit by their names.
# Python Power Tool Outputs interpretation
  Both leakage and average switching power are displayed in Watts.
  After running POW.py for average power clculation poweranalysis.cir and Leakage.py for leakage power calculation powerleakage.cir file are added   in your system. These are modified netlist for power calculation.
  To view average power curve and power values you can run these netlist in ngspice.
###  Average Switching Power netlist can be run by following command.
     $ ngspice poweranalysis.cir
     
### Following power plot you get (Depending on your cicuit)
                                               
                                               INVETRER
                                              
     
![image](https://user-images.githubusercontent.com/66687579/86346683-ea3b2c80-bc7a-11ea-916a-84e0f54febc4.png)

###  Leakage Power netlist can be run by following command.
     $ ngspice powerleakage.cir
     
# Future Work
For proper working of this tool cicuit must have single power supply source.Hence it can be modified so that it works for multipile supply voltages. I tested this tool for osu 180 and TSMC 180 technologoy parameter file only.

# Python Power Tool Usage

## Dependencies
This tool works in NGSPICE and PYTHON only.
### About Ngspice
Ngspice is an open source mixed signal circuit simulator.

#### Installing Ngspice

 Open your terminal and type the following to install Ngspice
 
    $ sudo apt-get install  ngspice
 
#### Installing Python

 Open your terminal and type the following to install Ngspice
 
    $ sudo apt-get install  python 
 NOTE: ngspice shell and python code are in same folder.
 
 # To run Python Script to find average power

NOTE: I used panda module so firstly  you have to download  panda
 ### window user
 In command prompt write
    
    pip install pandas

### linux or ubuntu users
 step 1 : Open your terminal (ctrl + Alt + T), then type these command 
   
   
   FOR PYTHON 2
    
    sudo apt-get install python-pip
   FOR PYTHON 3
    
    sudo apt-get install python3-pip
   
Step 2: Write this command also 
        
     sudo python3 -m pip install pandas

step 3: When pip installed, type the command to insatll pandas
    
    pip install pandas
 
 
 

### Following are cicuit schematic,input output waveforms and power calculation for each schematic cicuit.

I. D FF using PT




                                              Circuit Schematic
![](https://user-images.githubusercontent.com/66687579/84521097-2ae5fc80-acf2-11ea-9c34-c959429fc6d2.png)

                                                






                                            Input Output Waveform
![image](https://user-images.githubusercontent.com/66687579/85319276-e96a0400-b4de-11ea-8e50-52cf62fff3a6.png)





                                            Power Calculation
![](https://user-images.githubusercontent.com/66687579/84529828-c03bbd80-acff-11ea-90a4-7f3b1884de1d.png)




                                       Average Power Calculation from NGSPICE



![image](https://user-images.githubusercontent.com/66687579/86125395-34e16b00-bafa-11ea-91cf-b1e0367a5f8f.png)
                                       
                                       




                            




II. D FF using TG

                                             Circuit Schematic




![](https://user-images.githubusercontent.com/66687579/84522947-2242f580-acf5-11ea-8c3f-53da93747b8f.png)
                                           
                                           
                                           
                                           
                                           
                                           
                                           Input Output Waveform




![image](https://user-images.githubusercontent.com/66687579/85319522-44036000-b4df-11ea-9431-de8df45f2ee0.png)
                                           
                                           
                                           
                                           Power Calculation




![](https://user-images.githubusercontent.com/66687579/84530960-689e5180-ad01-11ea-99bd-3fc8b6396c54.png)




                                         Average Power Calculation from NGSPICE 
                                         
                                          
![image](https://user-images.githubusercontent.com/66687579/86125148-cf8d7a00-baf9-11ea-859d-649e08bdcd3b.png)                                          
                                         







III. D FF using stack transistor

                                                Circuit Schematic



![](https://user-images.githubusercontent.com/66687579/84524727-0b51d280-acf8-11ea-920b-c28f19492a05.png)



                                                Input Output Waveform




![image](https://user-images.githubusercontent.com/66687579/85320016-14a12300-b4e0-11ea-86bc-96da5e7eb8c6.png)




                                               Power Calculation





![](https://user-images.githubusercontent.com/66687579/84524791-2886a100-acf8-11ea-8627-e424517d5bd1.png)





IV. Line decoder using CMOS LOGIC 


                                             Circuit Schematic


![](https://user-images.githubusercontent.com/66687579/84528701-c9c42600-acfd-11ea-8c86-99fce7130868.png)
                                          
                                          
                                          Input Output Waveform



![image](https://user-images.githubusercontent.com/66687579/85320349-8f6a3e00-b4e0-11ea-85b9-ddd5747aa46a.png)






V. Line decoder using alternate DVL and TG

                                             Circuit Schematic




![](https://user-images.githubusercontent.com/66687579/84528816-fb3cf180-acfd-11ea-8911-e188f1ce04d6.png)
                                          
                                          
                                          
                                          Input Output Waveform



![image](https://user-images.githubusercontent.com/66687579/85320623-fa1b7980-b4e0-11ea-8339-2cab5a689901.png)












VI. MUX using PT


                                           Circuit Schematic



![](https://user-images.githubusercontent.com/66687579/84526325-bebbc680-acfa-11ea-8248-b40b62921c6a.png)
                                          
                                          
                                          
                                          
                                          Input Output Waveform






![image](https://user-images.githubusercontent.com/66687579/85321127-d147b400-b4e1-11ea-8d2f-a4d0cfc32a0b.png)


                                         
                                         
                                         
                                         
                                         Power Calculation




![](https://user-images.githubusercontent.com/66687579/84526461-f4f94600-acfa-11ea-93f1-c0ab4db6021a.png)





VIi. MUX using TG 
                                       
                                       
                                       
                                       Circuit Schematic



![](https://user-images.githubusercontent.com/66687579/84527660-e7908b80-acfb-11ea-87e9-5e1346a2c117.png)
                                      
                                      
                                      
                                      
                                      Input Output Waveform




![image](https://user-images.githubusercontent.com/66687579/85321568-7b274080-b4e2-11ea-82a7-4c9e2595f4d7.png)
                                       
                                       
                                       
                                       
                                       Power Calculation





![](https://user-images.githubusercontent.com/66687579/84527711-02630000-acfc-11ea-9166-546ba8a8f74b.png)


 Some average power curve which i got on ngspice steps

                                              INVETRER
                                              
     
![image](https://user-images.githubusercontent.com/66687579/86346683-ea3b2c80-bc7a-11ea-916a-84e0f54febc4.png)
                                              
                                              MUX using PT
![image](https://user-images.githubusercontent.com/66687579/86570741-05b17a80-bf8e-11ea-92a6-a984b6cb7d0a.png)

                                         
                                              1BIT ADDER
![image](https://user-images.githubusercontent.com/66687579/86346734-f9ba7580-bc7a-11ea-974b-9e68d0136e87.png)
                                            
                                              
                                              DFF using PT
                                              
 ![image](https://user-images.githubusercontent.com/66687579/86125395-34e16b00-bafa-11ea-91cf-b1e0367a5f8f.png)
 
                                        Inverter design By my friend
 ![image](https://user-images.githubusercontent.com/66687579/86346814-148cea00-bc7b-11ea-9fbb-1b5f965d1c4e.png) 

# USE OF PYTHON SCRIPT TO FIND AVERAGE POWER
NOTE: ngspice shell and python code are in same folder.
NOTE: I am usind panda module so firstly  you have to download  panda
 ### window user
 In command prompt write
    
    pip install pandas

### linux or ubuntu users
 step 1 : Open your terminal (ctrl + Alt + T), then type these command 
   
   
   FOR PYTHON 2
    
    sudo apt-get install python-pip
   FOR PYTHON 3
    
    sudo apt-get install python3-pip
   
Step 2: Write this command also 
        
     sudo python3 -m pip install pandas

step 3: When pip installed, type the command to insatll pandas
    
    pip install pandas

1. Run POW.py by writing 
           
           python POW.py 
                or 
           
           chmod 777 POW.py
           ./POW.py
              or
          
          python3 POW.py
 Depending on your system.          
2. Following window open in which you have to enter .txt file nameN Or .cir file name as I enter DFF_TG.cir file of DFF using transmission gate.
### NOTE : .tran 1e-0  20e-6(end value according to you)  line must be present that means transition analysis. 

                                               Python scipt 
![image](https://user-images.githubusercontent.com/66687579/86670466-494dc800-c012-11ea-8e05-cf1d5ecee6d1.png)

                                              

                                               DFFTG.cir file 
                                               
 ![image](https://user-images.githubusercontent.com/66687579/86670547-62ef0f80-c012-11ea-97f8-2b481e59f6d5.png)                                              
                                         
                                   Showing supply voltage value and node name on schematic
                                  
![image](https://user-images.githubusercontent.com/66687579/86589705-c6922200-bfab-11ea-9d0f-fc9b6aaa3360.png)
                                 
                                   

                                         Showing Time Period In Schematic                                         
![image](https://user-images.githubusercontent.com/66687579/86511730-81d68180-be19-11ea-8c9f-a80b9fd7058c.png)
                                  

 4.Finally you get average power value.

   

                            
 

# USE PYTHON SCRIPT TO FIND LEAKAGE POWER
1. Run script by writing
            
            python leakage.py 
                or 
           
           chmod 777 leakage.py
           ./leakage.py
              or
          
          python3 leakage.py
2.Following window open in which you have to enter .txt file name or .cir file name as I enter TT.cir file of DFF using transmission gate after removing non constant voltage sources (pulse) and no needs to remove any other line.  

                                                    Python script
                                                    
 ![image](https://user-images.githubusercontent.com/66687579/86589743-d9a4f200-bfab-11ea-960f-3b3d55ee9adc.png) 

                                                   
                                                    
                                               

3.You get leakage power on ngspice



## Contact information.
1. Charu Gupta M.tech VLSI Design and Embedded Systems DTU,Delhi charugupta2511@gmail.com
2. Kunal Ghosh Director, VSD Corp.Pvt. Ltd. kunalpghosh@gmail.com
3. Philipp Guhring Software Architect at LibreSilicon Association pg@futureware.at
4. Dr. Gaurav Trivedi Co Principle Investigator, EICT Academy, and Associative Professor IEEE department IIT Guwahati trivedi@iitg.ac.in



