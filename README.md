# OS-power-analysis-tool
Power analysis has materialized as a principal theme in today’s world of semiconductor industries. Very Large Scaled Integrated Circuits (VLSI) are far beyond human ability because of complexity. So to analyse power in these circuits we use open source computer aided tools, plenty of tools are available but most of them are costly. I designed open source power analysis tool for the academic use which analyse power dissipation (average switching and leakage power) efficiently.

## Power analysis
Power analysis of design can be reconnoitred at several levels such as system level, architectural level, logic level, circuit level and device level. Power analyser is a tool which determines how much power is utilize by a system or circuit. In this process we give circuits as input along with few operating conditions to power analyser to get report about the power. 

For power analysis I simulate D flip flop using pass transistor, transmission gate, pass transistor with stacking of transistor. Simulate 2-4 line decoder using CMOS logic and TG, DVL alternatively. Simulate 2-1 MUX using pass transistor, transmission gate, MTCMOS logic. Generate netlist and input output and power(V * I) waveform for all schematic circuit.

Simulations done on PSPICE which runs under windows, so no need of linux commands.
For schematic cicuit we use either TSMC 180nm or OSU018 model parameter file for NMOS and PMOS transistors.In this project i used TSMC 180nm need to change to OSU018.

### About Ngspice
Ngspice is an open source mixed signal circuit simulator.

#### Installing Ngspice

##### For Ubuntu
 Open your terminal and type the following to install Ngspice
 
 $ sudo apt-get install -y ngspice
 
 ###### Running the Simulation
 Download all files from Ngspice Simulator folder.
 
 To enter the Ngspice Shell, open the terminal and type:
 
 $ ngspice
 
 To simulate a netlist, type:
 
 ngspice 1-> source <filename>.cir
 
 You can exit from ngspice Shell by typing:
 
 ngspice 1-> exit
        or
 ngspice 1 -> quit

## Steps for Simulation on Window

First install PSPICE from any available site. After installation of PSPICE follow following instructions:
1. Open PSPICE, Click on file -> new -> project -> enter name of your project -> select Analog or mixed A/D -> ok


![](https://user-images.githubusercontent.com/66687579/84684588-7ac4fd80-af56-11ea-8086-9f3bd5d6c547.png)




![](https://user-images.githubusercontent.com/66687579/84686322-5b7b9f80-af59-11ea-9a54-36eb751522b8.png)



2. Draw schematic.
3. Right click on nmos -> Edit properties -> enter required value of W and L.


![](https://user-images.githubusercontent.com/66687579/84685743-6550d300-af58-11ea-85d0-416e162b62d3.png)



4. Right click on nmos -> Edit Pspice Model -> enter required model parameter file of either TSMC 180nm or OSU018.



![](https://user-images.githubusercontent.com/66687579/84686035-da240d00-af58-11ea-9dd7-9cd12adba68e.png)

5. Repeat 3 and 4 steps for pmos.
6. Save schematic.
7. PSpice -> edit simulation profile -> select required analysis -> Apply -> Ok.


![](https://user-images.githubusercontent.com/66687579/84687216-fb85f880-af5a-11ea-9798-486f39fca773.png)



8. TO run, PSpice -> Run.

![](https://user-images.githubusercontent.com/66687579/84687023-9f22d900-af5a-11ea-98a3-9b22a2b221e4.png)



9. Simulation window open, Trace -> Add trace -> select required current or voltage -> ok.



![image](https://user-images.githubusercontent.com/66687579/84695058-dd72c500-af67-11ea-9a65-0fd91d1812c0.png)




![image](https://user-images.githubusercontent.com/66687579/84695125-fa0efd00-af67-11ea-9aa5-6952cae39cb3.png)




10. You get output on simulation window.




![image](https://user-images.githubusercontent.com/66687579/84695148-02ffce80-af68-11ea-822c-019f9e4010ea.png)





### Calculation of power in PSPICE:
1. In simulation window, Tool -> Measurement -> Select powerDissipation -> Eval -> Enter required voltage and current of load along with time duration -> Ok.
2. Power dissipation in uW is obtained.


#### Installation and simulation on LINUX

Note: use ** for comment

** uninstall and clean up wine completely:

sudo apt-get remove --purge wine winetricks    # not enough, needs also:
sudo apt-get remove --purge wine1.2            
sudo apt-get autoremove --purge             # for wine1.2-gecko etc
ls -d /home/administrator/.wine*  # shows: .wine/ .winetrickscache/
rm -rf ~/.wine*

** install wine 
sudo apt-get install wine # installs winetricks, wine1.2-gecko

** run wineconfig, and set win 98 mode
winecfg 

** run winetricks and install dependencies
** note: mfc42=vcrun6
winetricks corefonts dcom98 mfc42


** run wineconfig again, and under 
** 'Libraries', set rpcrt4 to "built-in" - NOT 'native';
** else installer will crash @ 'Call from 0x7b836852 to unimplemented function rpcrt4.dll.I_RpcExceptionFilter, aborting'
winecfg 

** now run the Pspice installer
** install Pspice in a dir without spaces; 
** for example /home/user/Orcad_Demo
** that will be Z:\\home\\user\\Orcad_Demo for wine
cd ps9_1/
wine Setup.exe

** Install should be done now, 
** programs start

** check whether dll's have been registered in wine registry:
grep 'ipspice' ~/.wine/*.reg
grep 'sim' ~/.wine/*.reg
grep 'pspi' ~/.wine/*.reg

** check if PSPICEEV.INI is installed
$ ls ~/.wine/drive_c/windows/

** run wineconfig YET again, and under 
** 'Libraries', set ole32, oleaut32, rpcrt4 to "built-in" - NOT 'native';
winecfg 

** check if by any chance multiple copies of SIMSRVR.EXE have been started;
** if so kill them
ps axf | grep -i 'sim'
sudo killall SIMSRVR.EXE

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




## USE OF PYTHON SCRIPT TO FIND AVERAGE POWER
NOTE: ngspice shell and python code are in same folder.
1. Run POW.py by writing 
           
           python POW.py 
                or 
           
           chmod 777 POW.py
           ./POW.py
              or
          
          python3 POW.py
 Depending on your system.          
2. Following window open in which you have to enter .txt file name as I enter DFFtg.cir file of DFF using transmission gate after removing lines instructed by python script as shown in 2nd figure.  
## no need to convert .cir to .txt you can also write file name with extension .cir  

                                               Python scipt First Step
![image](https://user-images.githubusercontent.com/66687579/86589532-787d1e80-bfab-11ea-983d-7a7dc98ade68.png)                                               

                                        DFFtg.cir file enter by user for changing
                                              
![image](https://user-images.githubusercontent.com/66687579/86589625-9fd3eb80-bfab-11ea-98e2-05f2cdd603ee.png)
                                         
                                   Showing supply voltage value and node name on schematic
                                  
![image](https://user-images.githubusercontent.com/66687579/86589705-c6922200-bfab-11ea-9d0f-fc9b6aaa3360.png)
                                 
                                   

                                         Showing Time Period In Schematic                                         
![image](https://user-images.githubusercontent.com/66687579/86511730-81d68180-be19-11ea-8c9f-a80b9fd7058c.png)
                                  

 4.Finally you got output waveform and values on ngspice please copy these values and make .csv file with column name as INDEX TIME POWER.

   (I am trying to generate itsself from script)                                  
                                                                               
                                         Average power plot on ngspice
![image](https://user-images.githubusercontent.com/66687579/86263299-ab579900-bbde-11ea-8da3-2397479ae1e4.png)

5. Similarly you got for your cicuit I am showing you some average power curve which i got following these steps

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
 
# Steps to find one value of average power by runing avg.py python file
NOTE: I am usind panda module so firstly  you have to download  panda
 ## window user
 In command prompt write
    
    pip install pandas

## linux or ubuntu users
 step 1 : open your terminal (ctrl + Alt + T), then type these command 
    
    sudo apt-get install python-pip
 step 2: Wheb pip installed, type the command to insatll pandas
    
    pip install pandas
 
1. Run by writing 
           
           python avg.py 
                or 
           
           chmod 777 avg.py
           ./avg.py
              or
          
          python3 avg.py
2. Follow steps instructed by script you will get.

                                    Python scipt
                                    
![image](https://user-images.githubusercontent.com/66687579/86591534-67361100-bfaf-11ea-98d7-59f5ba17d7bf.png)                                   
                                    
                                    tg.csv file
![image](https://user-images.githubusercontent.com/66687579/86530450-65e4e580-bed6-11ea-9725-173a9b517ad7.png)                                    

### USE PYTHON SCRIPT TO FIND LEAKAGE POWER
1. Run script by writing
            
            python leakage.py 
                or 
           
           chmod 777 leakage.py
           ./leakage.py
              or
          
          python3 leakage.py
2.Following window open in which you have to enter .txt file name as I enter tg_leakage.txt file of DFF using transmission gate after removing lines instructed by python script.

## no need to convert .cir to .txt you can also write file name with extension .cir  

                                                    Python script
                                                    
 ![image](https://user-images.githubusercontent.com/66687579/86589743-d9a4f200-bfab-11ea-960f-3b3d55ee9adc.png) 

                                                   
                                                    
                                               

3.You get leakage power on ngspice



## Contact information.
1. Charu Gupta M.tech VLSI Design and Embedded Systems DTU,Delhi charugupta2511@gmail.com
2. Kunal Ghosh Director, VSD Corp.Pvt. Ltd. kunalpghosh@gmail.com
3. Philipp Guhring Software Architect at LibreSilicon Association pg@futureware.at
4. Dr. Gaurav Trivedi Co Principle Investigator, EICT Academy, and Associative Professor IEEE department IIT Guwahati trivedi@iitg.ac.in



