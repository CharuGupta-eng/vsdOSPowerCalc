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
2. Draw schematic.
3. Right click on nmos -> Edit properties -> enter required value of W and L.
4. Right click on nmos -> Edit Pspice Model -> enter required model parameter file of either TSMC 180nm or OSU018.
5. Repeat 3 and 4 steps for pmos.
6. Save schematic.
7. PSpice -> edit simulation profile -> select required analysis -> Apply -> Ok.
8. TO run, PSpice -> Run.
9. Simulation window open, Trace -> Add trace -> select required current or voltage -> ok.
10. You get output on simulation window.

### Calculation of power in PSPICE:
1. In simulation window, Tool -> Measurement -> Select powerDissipation -> Eval -> Enter required voltage and current of load along with time duration -> Ok.
2. Power dissipation in uW is obtained.

Following are cicuits,waveforms,link of netlist and schematic for each schematic cicuit.

I. D FF using PT

![](C:\Users\Charu\Pictures\images of intern project)

![](C:\Users\Charu\Pictures\R D FF)


https://drive.google.com/file/d/1-Qz6o6Wm2RaIxSafMLSX_6v8VHD1Qo2X/view?usp=drivesdk

https://drive.google.com/file/d/1-RG1rZ0E-Y6SEfRdG4SP367r4oQTMnEl/view?usp=drivesdk

II. D FF using TG

https://drive.google.com/file/d/1-lznv8iIqriBJU5C5aUJQyrcWUzIxGBX/view?usp=drivesdk

https://drive.google.com/file/d/1-mQvoLWdumY3pb7ooL5A7g9N2HFj7YFQ/view?usp=drivesdk

III. D FF using stack transistor

https://drive.google.com/file/d/1-W-p8KwofiCTFQ3EGK-6VTnlduYN6bZI/view?usp=drivesdk

https://drive.google.com/file/d/1-ahe3T0Qigpj3NzMgtzMWJ7X8R79Tm2L/view?usp=drivesdk

IV. Line decoder using CMOS LOGIC 

https://drive.google.com/file/d/10Dn1FV497KkFlDOh19ivO5R4SZGn7gFg/view?usp=drivesdk

https://drive.google.com/file/d/10E7k3WRvHW8QXFM2IU9uHhiwSedZV1Cl/view?usp=drivesdk

V. Line decoder using alternate DVL and TG

https://drive.google.com/file/d/1-pyJoCZdphJSDjtA_n_gLpu5T3Gc8uPG/view?usp=drivesdk

https://drive.google.com/file/d/107Y7yn6Itx4Ic8URhk2LtPF9SnEFYk7E/view?usp=drivesdk

VI. MUX using PT

https://drive.google.com/file/d/10BkdhQN01ubxz_Lfkw5lUAK5AMNX-9y4/view?usp=drivesdk

https://drive.google.com/file/d/1093YPUHQkIPShb2HFkMLbze1VHGu1s35/view?usp=drivesdk

VIi. MUX using TG

https://drive.google.com/file/d/10Cd7TSPhKGEJNzAxd6wi0T6_u7PXPAnj/view?usp=drivesdk

https://drive.google.com/file/d/10CEjkhBNovUZkX1Fmw18yxPHbI_eev0z/view?usp=drivesdk

Contact information.
1. Charu Gupta M.tech VLSI Design and EMbedded Systems DTU,Delhi charugupta2511@gmail.com
2. Kunal Ghosh Director, VSD Corp.Pvt. Ltd. kunalpghosh@gmail.com
3. Philipp Guhring Software Architect at LibreSilicon Association pg@futureware.at
4. Dr. Gaurav Trivedi Co Principle Investigator, EICT Academy, and Associative Professor IEEE department IIT Guwahati trivedi@iitg.ac.in



