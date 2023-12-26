'''****************************************************************
This module is a wrapper around gappa_swig, which is created
directly by wrapping the C++ code of Gamera with Swig. The goal
is to allow the usage of astropy quantities as input to gappa.
If astropy is not installed, gappa will still work in the old
way without any units.
****************************************************************'''


import gappa_swig as gappa_swig

# First, we add all constants TODO: Maybe there is a better, automatic way
TeV_to_erg = gappa_swig.TeV_to_erg
GeV_to_erg = gappa_swig.GeV_to_erg
eV_to_erg = gappa_swig.eV_to_erg
erg_to_TeV = gappa_swig.erg_to_TeV
sigma_T = gappa_swig.sigma_T
e_radius = gappa_swig.e_radius
pc_to_cm = gappa_swig.pc_to_cm
kpc_to_cm = gappa_swig.kpc_to_cm
AU_to_cm = gappa_swig.AU_to_cm
m_p_g = gappa_swig.m_p_g
yr_to_sec = gappa_swig.yr_to_sec
mSol = gappa_swig.mSol
m_e = gappa_swig.m_e
kb = gappa_swig.kb
m_p = gappa_swig.m_p
m_pi = gappa_swig.m_pi
pi = gappa_swig.pi
c_speed = gappa_swig.c_speed
el_charge = gappa_swig.el_charge
eRadius = gappa_swig.eRadius
hp = gappa_swig.hp
fineStructConst = gappa_swig.fineStructConst
h_to_sec = gappa_swig.h_to_sec
pc_to_lyr = gappa_swig.pc_to_lyr
ln10 = gappa_swig.ln10




try:
    import astropy as ap
    import astropy.units as u

except ImportError:
    print('In gappa.py: Astropy units could not be imported. Gappa now only works with standard numbers.')
    class Radiation(gappa_swig.Radiation):
        pass
    class Particles(gappa_swig.Particles):
        pass
    class Astro(gappa_swig.Astro):
        pass
    class Utils(gappa_swig.Utils):
        pass
    
    
else:
    
    def convert_to_value(a, unit):
        if isinstance(a,ap.units.quantity.Quantity):
            a = a.to(unit); a = a.value
        return a
    
    
    class Radiation(gappa_swig.Radiation):
        
        def SetBField(self, B):
            B = convert_to_value(B,'G')
            super().SetBField(B)
            return
        
    class Particles(gappa_swig.Particles):
        pass
    class Astro(gappa_swig.Astro):
        pass
    class Utils(gappa_swig.Utils):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
