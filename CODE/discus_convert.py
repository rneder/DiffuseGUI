import math as math
from support import *

def convert_event(eff=None, parent=0, event=0):
        # Change of radiation (X-ray, neutron, electron)
        #
        # Handle if no selection was given
        if is_empty(parent.rad.curselection()):
            radiation = 0
        else:
            radiation = int(parent.rad.curselection()[0])
        # calculate wavelength if Radiobutton is in state Energy
        calc_wvle = parent.rad_type.get() == 1
        convert(parent, calc_wvle)
        #
        if radiation == 0:
            # X-rays set kev, leave all other current settings
            parent.label_ener_unit['text']='keV'
        elif radiation == 1:
            # neutrons, set meV, disable elements, 
            # if elements were chosen, choose wavelength
            parent.label_ener_unit['text']='meV'
            parent.ele.configure(state='disabled')
            if parent.rad_type.get() == 2:
                parent.rad_type.set(0)
                parent.entry_wvle.configure(state='normal', foreground=COLORS.en_fore)
                parent.entry_ener.configure(state='disabled', foreground=COLORS.dis_fore)
        elif radiation == 2:
            # electrons, set keV, disable elements, 
            # if elements were chosen, choose wavelength
            parent.label_ener_unit['text']='keV'
            parent.ele.configure(state='disabled')
            if parent.rad_type.get() == 2:
                parent.rad_type.set(1)
                parent.entry_wvle.configure(state='disabled', foreground=COLORS.dis_fore)
                parent.entry_ener.configure(state='normal', foreground=COLORS.en_fore)

def convert_focus(eff=None, parent=0, event=0):
        # calculate wavelength if Radiobutton is in state Energy
        calc_wvle = parent.rad_type.get() == 1
        convert(parent, calc_wvle)
      

def convert_setup(parent, mode):
        if mode == 0:
            # Change of radiation (X-ray, neutron, electron)
            # calculate wavelength if Radiobutton is in state Energy
            calc_wvle = parent.rad_type.get() == 1
        elif mode == 1:
            # Change of energy ==> wavelength Radiobutton
            calc_wvle = True
            parent.ele.configure(state='disabled')
            parent.entry_wvle.configure(state='normal', foreground=COLORS.en_fore)
            parent.entry_ener.configure(state='disabled', foreground=COLORS.dis_fore)
        elif mode ==-1:
            # Change of wavelength ==> energy Radiobutton
            calc_wvle = False
            parent.ele.configure(state='disabled')
            parent.entry_wvle.configure(state='disabled', foreground=COLORS.dis_fore)
            parent.entry_ener.configure(state='normal', foreground=COLORS.en_fore)
        elif mode == 2:
            # wavelength value was entered calc energy
            calc_wvle = False
        elif mode == -2:
            # energy value was entered calc wavelength
            calc_wvle = True
        elif mode == 3:
            # Select an Element 
            #   Set characteriustic radiation, 
            #   Turn element name selection on
            #   Switch to X-rays
            calc_wvle = False
            parent.ele.configure(state='normal')
            parent.entry_wvle.configure(state='disabled', foreground=COLORS.dis_fore)
            parent.entry_ener.configure(state='disabled', foreground=COLORS.dis_fore)
            parent.rad.selection_clear(1,2)
            parent.rad.selection_set(0)
            element = int(parent.ele.curselection()[0])
            parent.wvle.set(parent.wavelengths[element])
        convert(parent, calc_wvle)

def convert_element(eff=None, parent=0, event=0):
        calc_wvle = False
        element = int(parent.ele.curselection()[0])
        parent.wvle.set(parent.wavelengths[element])
        convert(parent, calc_wvle)

def convert(parent, calc_wvle):
        if is_empty(parent.rad.curselection()):
           radiation = 0
        else:
           radiation = int(parent.rad.curselection()[0])
        if calc_wvle:
            # Calculate wavelength from current energy
            energy = float(parent.ener.get())
            if radiation == 0:
                # X-rays
                wvle = (CONSTANTS.planck*CONSTANTS.light/CONSTANTS.charge ) / energy
            elif radiation == 1:
                # neutrons
                wvle = CONSTANTS.planck/math.sqrt(2.*CONSTANTS.mass_n*CONSTANTS.charge*energy/10.)
            elif radiation == 2:
                # electrons
                wvle = CONSTANTS.planck/math.sqrt(2.*CONSTANTS.mass_e*CONSTANTS.charge*energy*10) / \
                       math.sqrt(1.+(CONSTANTS.charge*energy)/ \
                                    (2*CONSTANTS.mass_e*CONSTANTS.light**2*10))
            wvle = float(int(wvle*100000+0.5)/100000.)
            parent.wvle.set(str(wvle))
        else:
            # Calculate energy from current wavelength
            wvle = float(parent.wvle.get())
            if radiation == 0:
                # X-rays
                energy = (CONSTANTS.planck*CONSTANTS.light/CONSTANTS.charge ) / wvle
            elif radiation == 1:
                # neutrons
                energy = CONSTANTS.planck**2/(2.*CONSTANTS.mass_n*CONSTANTS.charge*wvle**2/10.)
            elif radiation == 2:
                # electrons
                energy = -10.*CONSTANTS.mass_e*CONSTANTS.light**2/CONSTANTS.charge +  \
                        math.sqrt( 100.*CONSTANTS.mass_e**2*CONSTANTS.light**4/CONSTANTS.charge**2 + \
                      ((CONSTANTS.planck*CONSTANTS.light)/(CONSTANTS.charge*wvle))**2)
            energy = float(int(energy*100000+0.5)/100000.)
            parent.ener.set(str(energy))
