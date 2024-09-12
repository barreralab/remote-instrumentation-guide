import pyvisa
from instruments import Keithley8600, YokoGS820

START = 0
STOP = 1
STEP = 0.1

rm = pyvisa.ResourceManager('')

# These are classes I created to make interfacing easier 
yoko_addr = 'GPIB0::1::INSTR'
keith_addr = 'TCPIP0::169.254.214.60::inst0::INSTR'

yoko = YokoGS820(rm.open_resource(yoko_addr))
keithley = Keithley8600(rm.open_resource(keith_addr))


def setup_sweep(chnl):
    keithley.write(":SENS:AZERO:ONCE")

    yoko.write(f"CHAN{chnl}:SOUR:TRIG EXT")         # set yoko chnl to have external trigger
    yoko.linear_sweep(chnl, START, STOP, STEP)      # setup linear voltage sweep on channel 1

    keithley.measure_DC_volt()                      # Configure for single high-acc DC V measure
    keithley.opc()


def sweep():
    voltages = []
    incs = round((STOP - START)/STEP)

    yoko.start()                                    # Start Sweep on Yoko
    for _ in range(incs + 1):
        yoko.write("TRIG")                          # Trigger Yoko to make voltage step
        voltage = float(keithley.query("READ?"))    # Read voltage off Keithley
        voltages.append(voltage)

    return voltages

def clean(msg):
    keithley.display(msg)
    yoko.display(msg)

    keithley.beep()
    yoko.beep()

    keithley.close()
    yoko.close()


if __name__ == "__main__":
    yoko.reset()
    keithley.reset()

    setup_sweep(1)                                  # Configure instruments for sweep on yoko channel 1
    voltages = sweep()                              # Perform sweep experiment
    print(f"Voltages = {voltages}")
    clean('LANdid')


