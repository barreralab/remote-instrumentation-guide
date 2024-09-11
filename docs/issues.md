# Issues 
1. **Serial port initialization**
When Arduino connects to computer, it resets. It then takes time for the arduino to setup serial communication (has to run the bootloader, gets to Serial.begin() in 2 seconds or so). Currently, in pyvisa the instrument is available for use after opening a resource. If no wait time is applied between opening arduino-based instrument, then pyvisa can throw error as it tries to read/write to uninitialized serial buffer. 
See 
    - [Disable Arduino's Auto-Reset on Connection](https://www.astroscopic.com/blog/disable-arduinos-auto-reset-connection#:~:text=Permanent%20Method,permanently%20installed%20into%20a%20project)
    - [Serial Input Basics](https://forum.arduino.cc/t/serial-input-basics-updated/382007)
    
***RESOLVED*** ~~override the `get_idn()` method and sleep for 3 seconds before continuing. That way, when `self.connect_message` is called after initialization, the serial port will be up and running. Hardware corrections will make reprogramming the arduino more difficult.~~
Add 3 second sleep to init function in driver before `self.connect_message()` is called. You may still have to override `get_idn()` if your instrument doesn't return a standard identification string. See one of the sections above **TODO** which section?  

2. **Synchronization**
Related to above issue. How to ensure synchronization of commands? Develop some implementation of  `*OPC` and/or `*WAI` commands.

3. **IPython Compatibility**
QCoDeS designed to run in ipython environments (jupyter notebooks). Interactive widgets, in line plotting, and logging are only available in ipython. 

4. **Driver attributes/methods not recognized by intellisense**
The QCoDeS documentation recommends assigning parameters defined via `self.add_parameter(...)` to similarly named attributes for compatibility with code editor's auto-completion systems. The problem is 2-fold 
    1. If assigned as `self.param = self.add_parameter(...)`, then for some reason, qcodes throws an error when you try to set/get self.param as you would a regular parameter. i.e, if in some driver method, you want to set param, `self.param(x)` throws an error. In fact, digging into the source code for the InstrumentBase class reveals that the `add_parameter()` method returns Nonetype! If no assignment is made to a class attribute, then this problem disappears. 
    2. To resolve the above issue, I directly instantiated parameters from the Parameter class and assigned to a class attribute as recommended. `self.param = Parameter(self.inst, ...)` (note that a reference to the instrument itself has to be passed here). This enabled the usual syntax for setting/getting the param, but vscode still didn't recognize any of the attributes/methods of the driver class. This was observed in the [YokogawaGS820](/QCoDeS/src/LabDrivers/Yokogawa_GS820.py) driver, which is likely a consequence of relegating parameter constructions to the InstrumentChannel class. 
    

***RESOLVED***: ~~A number of their instruments have been modified to conform to method 2. To see this discrepancy firsthand, take a look at the Weinschel8320 driver in [QC-Docs/CreatingInstrumentDrivers](http://microsoft.github.io/Qcodes/examples/writing_drivers/Creating-Instrument-Drivers.html). Notice that they use method 1 here. But, if you look at the source code for the driver [here](http://microsoft.github.io/Qcodes/_modules/qcodes/instrument_drivers/weinschel/Weinschel_8320.html#Weinschel8320), you'll notice that method 2 was snuck in.~~
I was using qcodes version 0.45.0 which had `self.add_parameter` return NoneType. In version 0.46.0 and above, the method returns the parameter allowing approach 1 above to work. 

5. **Unifying Lab Codebase**
The current sweep scripts need to modify the system PATH variable to gain access to the LabDrivers folders containing the custom yoko and keithley modules. 
Would be nice to `import YokogawaGS820 from BarreraLabDrivers.Yokogawa`
Can be achieved by creating python package for lab drivers on private github repo. Pip can import modules defined in private git repositories. 
Leads to question of how code for lab should be organized
    - Dedicated Lab Driver package
    - Individual Repos for each experiment? Containing standard scripts and utilities
    - One global backup database? Database for each experiment?
GitHub organization is an approach I've seen. 

6. **QCODES DOCS UPDATE**
QCoDeS updated their documentation page on August 14th, 2024. Will have to update some of the links above. 


--- 
