# OS-power-analysis-tool
Power analysis has materialized as a principal theme in today’s world of semiconductor industries. Very Large Scaled Integrated Circuits (VLSI) are far beyond human ability because of complexity. So to analyse power in these circuits we use open source computer aided tools, plenty of tools are available but most of them are costly. I designed open source power analysis tool for the academic use which analyse power dissipation (average switching and leakage power) efficiently.

# Power analysis
Power analysis of design can be reconnoitred at several levels such as system level, architectural level, logic level, circuit level and device level. Power analyser is a tool which determines how much power is utilize by a system or circuit. In this process we give circuits as input along with few operating conditions to power analyser to get report about the power. 

For power analysis I simulate D flip flop using pass transistor, transmission gate, pass transistor with stacking of transistor. Simulate 2-4 line decoder using CMOS logic and TG, DVL alternatively. Simulate 2-1 MUX using pass transistor, transmission gate, MTCMOS logic. Generate netlist and input output and power(V * I) waveform for all schematic circuit.

# Average or Switching Power Dissipation
The significant cause of it is switching activities that occur in circuits. Or we can say that it occur during charging and discharging of capacitance as shown in figure. 
                       
  ![image](https://user-images.githubusercontent.com/66687579/87031520-de161880-c200-11ea-9d5c-8a4f068904a4.png)

Where CL is loading capacitor, VDD is power supply, α is activity factor and f is clock frequency. To evaluate average switching power in charging and discharging of capacitor we integrate power energy needed to charge to VDD and discharge to ground level while applying input waveform which have zero rise and fall time with time period T
                                                 
                                            CMOS inverter 
            
  ![image](https://user-images.githubusercontent.com/66687579/87031719-28979500-c201-11ea-8944-cfce77c11f65.png)

# Leakage or Static Power Dissipation: 
It occur when circuit is not active or in OFF state. It is a function of the supply voltage (VDD), threshold Voltage (Vth), and transistor dimensions. The main components of leakage current in the scaled devices which also caused power dissipation are shown in figure.
                                                  
                                 Major leakage current component in NMOS
        
  ![image](https://user-images.githubusercontent.com/66687579/87031815-3d742880-c201-11ea-9721-0bf197a5cb5e.png)
 
 # Power Tool Strategy
 
 ## For calculating Average power
I placed a power meter between power supply and  device as shown in figure below and calculate the product of average current and Voltage. For calculating average current i placed one extra power source of 0V in netlist. 
              
                         
                  The power meter circuit used for the simulation of average dynamic power
   ![image](https://user-images.githubusercontent.com/66687579/87151569-b93da600-c2d1-11ea-99c8-284ff100406c.png)


                                               
  
  ## For calculating leakage power
I remove all non constant power supply voltages and calculate the product of leakage current and Voltage. For calculating leakage current i      placed one extra power source of 0V in netlist. 


# Inputs for Python Power Tool
 First input is spice netlist. While executing script some more inputs are taken such as
   1. Name of Supply Voltage
   
   2. For synchronous circuit time perod of clock and for asynchronous minimum time period among all input pulse.
   
   
# Python Power tool with example
  1.First download or clone this repository.
                 
                 git clone https://github.com/CharuGupta-eng/vsdOSPowerCalc
   
  2. To see circuit diagrams input output waveform of scheamtic, go to images and there are images of input output waveform by their names.
   
  3. Save the netlist of the cicuit, model parameters file, ngspice and python code in the same folder.
  
  4. To see how we download ngspice, python3 and other useful things like PANDAS module which have to download please see below in Python Power          Tool Usage(Dependencies) section.
  ### NOTE: This tool work properly in PYTHON3. It sometime create problem in exexution in PYTHON2 so i recommend to use it in PYTHON3 only.

# USE PYTHON SCRIPT TO FIND Average POWER

1. To run code

       $ python3 AVPOWER.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage> -t <Time period in seconds(clock or minimum time period among all inputs>
       OR
       chmod 777 AVPOWER.py
       ./AVPOWER.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage> -t <Time period in seconds(clock or minimum time period among all inputs>
      
      Example:
      
        $ python3 AVPOWER.py -i DFF_TG.cir -v V_V20 -t 0.000002   

### NOTE : .tran 1e-0  20e-6(end value according to you)  line must be present that means transition analysis. 

                                               Python scipt 
![image](https://user-images.githubusercontent.com/66687579/86670466-494dc800-c012-11ea-8e05-cf1d5ecee6d1.png)

                                              

                                               DFFTG.cir file 
                                               
 ![image](https://user-images.githubusercontent.com/66687579/86670547-62ef0f80-c012-11ea-97f8-2b481e59f6d5.png)                                              
                                         
    
                                         Showing Time Period In Schematic                                         
                                  

 4.Finally you get average power value.
 
# PYTHON SCRIPT TO FIND LEAKAGE POWER
1. Run script by writing
            
           $ python3 Leakage.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage>
                or 
           
           chmod 777 Leakage.py
           ./leakage.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage>
           
      Example:
       
             
                                                    Python script
                                                    
 ![image](https://user-images.githubusercontent.com/66687579/88431652-68bd6100-ce18-11ea-93f1-7d989441756e.png)
 

                                                   
                                                    
                                               

3.You get leakage power.
   
   
# Python Power Tool Outputs interpretation
  Both leakage and average switching power are displayed in Watts and MicroWatts.
  After running AVPOWER.py for average power clculation poweranalysis.cir and Leakage.py for leakage power calculation powerleakage.cir file are     added in your system. These are modified netlist for power calculation.
  To view average power curve and power values you can run these netlist in ngspice after removing quit from the last of netlist file.
###  Average Switching Power netlist can be run by following command.
     $ ngspice poweranalysis.cir
     
### Following power plot you get (Depending on your cicuit)
                                               
                                  Average Power Calculation on NGSPICE(DFFusing TG)
                                              
     
![image](https://user-images.githubusercontent.com/66687579/86125148-cf8d7a00-baf9-11ea-859d-649e08bdcd3b.png)

###  Leakage Power netlist can be run by following command.
     $ ngspice powerleakage.cir
     
# Future Work
For proper working of this tool cicuit must have single power supply source.Hence it can be modified so that it works for multipile supply voltages. I tested this tool for osu 180 and TSMC 180 technologoy parameter file only.

# Python Power Tool Usage

## Dependencies
This tool works in NGSPICE and PYTHON only.
Prerequisite things to run power analysis tool.
### About Ngspice
Ngspice is an open source mixed signal circuit simulator.

#### Installing Ngspice

 Open your terminal and type the following to install Ngspice
 
    $ sudo apt-get install  ngspice
 
#### Installing Python
 
  ### NOTE: This tool work properly in PYTHON3. It sometime create problem in exexution in PYTHON2 so i recommend to use it in PYTHON3 only.

 Open your terminal and type the following to install Python3
 
    $ sudo apt-get install  python 
 NOTE: ngspice shell and python code are in same folder.
 
 # To run Python Script to find average power

NOTE: I used panda module so firstly  you have to download  panda
 ### window user
 In command prompt write
    
    pip install pandas

### linux or ubuntu users
 step 1 : Open your terminal (ctrl + Alt + T), then type these command
    
    sudo apt-get install python3-pip
   
Step 2: Write this command also 
        
     sudo python3 -m pip install pandas

step 3: When pip installed, type the command to insatll pandas
    
    pip install pandas
 
NOTE: ngspice shell and python code are in same folder. 
 
# Steps to run PYTHON POWER TOOL

Following steps to be followed to run tool to get average power and leakage power of any circuit:

1. To clone respository or download files, Open terminal first and type
         
         $ sudo apt install -y git
         $ git clone https://github.com/CharuGupta-eng/vsdOSPowerCalc 

 2. Save the netlist of your cicuit, model parameters file, ngspice and python code in the same folder.
 
 3. .tran line must be in your netlist.
 
 4. To run code for calculating average power
     
        $ python3 AVPOWER.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage> -t <Time period in seconds(clock or minimum time period among all inputs>
        
        OR
        
        chmod 777 AVPOWER.py
        ./AVPOWER.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage> -t <Time period in seconds(clock or minimum time period among all inputs>
      
      Example:
      
        $ python3 AVPOWER.py -i DFF_TG.cir -v V_V20 -t 0.000002   
  
  5. Ener the name of file, Supply voltage name, Time period.
  
  6. Average power value is displayed.
  
  7. To run code for calculating leakage power
      

           $ python3 Leakage.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage>
               
               or 
           
           chmod 777 Leakage.py
           ./leakage.py -i <enter .txt file name Or .cir file> -v <Name of supply Voltage>  
   8. Ener the name of file after removing all non constant voltage source from netlist, Supply voltage name, node name of supply voltage and value       of value of supply voltage.
   
   9. Leakage power value is displayed.
   


## Unit of output displayed by power analysis tool
Both leakage and average switching power are displayed in Watts and MicroWatts.

### If there is an issue running tool, please contact administrator for support or report in “issues” section of GitHub

# Contact information.
1. Charu Gupta M.tech VLSI Design and Embedded Systems DTU,Delhi charugupta2511@gmail.com
2. Kunal Ghosh Director, VSD Corp.Pvt. Ltd. kunalpghosh@gmail.com
3. Philipp Guhring Software Architect at LibreSilicon Association pg@futureware.at
4. Dr. Gaurav Trivedi Co Principle Investigator, EICT Academy, and Associative Professor IEEE department IIT Guwahati trivedi@iitg.ac.in



