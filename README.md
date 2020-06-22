# OS-power-analysis-tool
Power analysis has materialized as a principal theme in today’s world of semiconductor industries. Very Large Scaled Integrated Circuits (VLSI) are far beyond human ability because of complexity. So to analyse power in these circuits we use open source computer aided tools, plenty of tools are available but most of them are costly. I designed open source power analysis tool for the academic use which analyse power dissipation (average switching and leakage power) efficiently.

## Power analysis
Power analysis of design can be reconnoitred at several levels such as system level, architectural level, logic level, circuit level and device level. Power analyser is a tool which determines how much power is utilize by a system or circuit. In this process we give circuits as input along with few operating conditions to power analyser to get report about the power. 

For power analysis I simulate D flip flop using pass transistor, transmission gate, pass transistor with stacking of transistor. Simulate 2-4 line decoder using CMOS logic and TG, DVL alternatively. Simulate 2-1 MUX using pass transistor, transmission gate, MTCMOS logic. Generate netlist and input output and power(V * I) waveform for all schematic circuit.

Simulations done on PSPICE which runs under windows, so no need of linux commands.
For schematic cicuit we use either TSMC 180nm or OSU018 model parameter file for NMOS and PMOS transistors.In this project i used TSMC 180nm need to change to OSU018.

### Steps for Simulation on Window

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





#### Calculation of power in PSPICE:
1. In simulation window, Tool -> Measurement -> Select powerDissipation -> Eval -> Enter required voltage and current of load along with time duration -> Ok.
2. Power dissipation in uW is obtained.


##### Installation and simulation on LINUX

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

###### Following are cicuit schematic,input output waveforms and power calculation for each schematic cicuit.

I. D FF using PT




                                              Circuit Schematic
![](https://user-images.githubusercontent.com/66687579/84521097-2ae5fc80-acf2-11ea-9c34-c959429fc6d2.png)

                                                






                                            Input Output Waveform
![image](https://user-images.githubusercontent.com/66687579/85319276-e96a0400-b4de-11ea-8e50-52cf62fff3a6.png)





                                            Power Calculation
![](https://user-images.githubusercontent.com/66687579/84529828-c03bbd80-acff-11ea-90a4-7f3b1884de1d.png)




                            




II. D FF using TG

                                             Circuit Schematic




![](https://user-images.githubusercontent.com/66687579/84522947-2242f580-acf5-11ea-8c3f-53da93747b8f.png)
                                           
                                           
                                           
                                           
                                           
                                           
                                           Input Output Waveform




![image](https://user-images.githubusercontent.com/66687579/85319522-44036000-b4df-11ea-9431-de8df45f2ee0.png)
                                           
                                           
                                           
                                           Power Calculation




![](https://user-images.githubusercontent.com/66687579/84530960-689e5180-ad01-11ea-99bd-3fc8b6396c54.png)







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






![](https://user-images.githubusercontent.com/66687579/84527761-1eff3800-acfc-11ea-8746-c639000a1c20.png)
                                         
                                         
                                         
                                         
                                         Power Calculation




![](https://user-images.githubusercontent.com/66687579/84526461-f4f94600-acfa-11ea-93f1-c0ab4db6021a.png)





VIi. MUX using TG 
                                       
                                       
                                       
                                       Circuit Schematic



![](https://user-images.githubusercontent.com/66687579/84527660-e7908b80-acfb-11ea-87e9-5e1346a2c117.png)
                                      
                                      
                                      
                                      
                                      Input Output Waveform




![](https://user-images.githubusercontent.com/66687579/84527691-f5dea780-acfb-11ea-82cc-e35407ed5008.png)
                                       
                                       
                                       
                                       
                                       Power Calculation





![](https://user-images.githubusercontent.com/66687579/84527711-02630000-acfc-11ea-9166-546ba8a8f74b.png)







###### Contact information.
1. Charu Gupta M.tech VLSI Design and EMbedded Systems DTU,Delhi charugupta2511@gmail.com
2. Kunal Ghosh Director, VSD Corp.Pvt. Ltd. kunalpghosh@gmail.com
3. Philipp Guhring Software Architect at LibreSilicon Association pg@futureware.at
4. Dr. Gaurav Trivedi Co Principle Investigator, EICT Academy, and Associative Professor IEEE department IIT Guwahati trivedi@iitg.ac.in



