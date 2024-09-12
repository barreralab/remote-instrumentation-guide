from abc import ABC, abstractmethod

class Instrument(ABC):
    """
    Base class for instruments

    Instance Variables
    inst: visa instrument resource
    """
    def __init__(self, resource):
        """
        Initialize instrument with Visa resource
        """
        self.inst = resource

    def ID(self):
        """
        Get instrument identification
        """
        return self.inst.query("*IDN?")
    
    def reset(self):
        """
        Reset instrument
        """
        self.inst.write("*RST")
        # self.inst.write("*OPC?")

    def opc(self):
        return self.inst.query("*OPC?")
    
    def wait(self):
        self.inst.write("*WAI")
    
    def query(self, command):
        """
        Query instrument with command and return response
        """
        return self.inst.query(command)
    
    def read(self, command):
        """
        Read instrument with command and return response
        """
        return self.inst.read(command)
    
    def write(self, command):
        """
        Write command to instrument
        """
        self.inst.write(command)
        self.wait()

    @abstractmethod
    def display(self, text):
        raise NotImplementedError

    @abstractmethod
    def beep(self):
        raise NotImplementedError
    
    def close(self):
        """
        Close instrument connection
        """
        self.inst.close()




class Keithley8600(Instrument):
    def measure_DC_volt(self):
        """
        Sets up Keithley for single DC voltage measurement using the instrument

        Returns:
            None
        """
        self.inst.write(":SENS:FUNC \"VOLT:DC\"")
        self.inst.write(":SENS:VOLT:RANG 10")
        self.inst.write(":SENS:VOLT:INP AUTO")
        self.inst.write("SENS:VOLT:NPLC 1")
        self.inst.write(":SENS:VOLT:AZER ON")
        self.inst.write(":SENS:VOLT:AVER ON")
    
    def display(self, text):
        self.inst.write(f"DISP:USER1:TEXT \"{text}\"")
        self.inst.write("DISP:SCR SWIPE_USER")

    def beep(self, hz=750, time=0.5):
        self.inst.write(f"SYST:BEEP {hz}, {time}")



class YokoGS820(Instrument):
    def linear_sweep(self, chnl, start, stop, step):
        """
        Perform a linear sweep on the specified channel of the instrument.

        Parameters:
            chnl (int): The channel number to perform the sweep on.
            start (float): The starting voltage for the sweep.
            stop (float): The ending voltage for the sweep.
            step (float): The step size for the sweep.

        Returns:
            None
        """
        self.inst.write(f"CHAN{chnl}:OUTP 1")
        # self.inst.write(f"CHAN{chnl}:SWEep:TRIGger:AUXiliary:POLarity NORMal")
        self.inst.write(f"CHAN{chnl}:SOURce:MODE SWEep")
        self.inst.write(f"CHAN{chnl}:SOURce:VOLTage:SWEep:SPACing LINear")
        self.inst.write(f"CHAN{chnl}:SOURce:VOLTage:SWEep:STARt {start}V")
        self.inst.write(f"CHAN{chnl}:SOURce:VOLTage:SWEep:STOP {stop}V")
        self.inst.write(f"CHAN{chnl}:SOURce:VOLTage:SWEep:STEP {step}V")

    def start(self):
        self.inst.write(":STARt")

    def display(self, text):
        self.inst.write(f"SYST:DISP:TEXT \"{text}\"")

    def beep(self):
        pass

