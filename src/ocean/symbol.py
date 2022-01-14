from enum import Enum
from skillbridge import Symbol, Key


class SymbolEnum(Enum):
    def __repr_skill__(self):
        return self.value.__repr_skill__()


class AnalysisType(SymbolEnum):
    """Analysis Type"""
    pz = Symbol('pz')
    lf = Symbol('lf')
    acmatch = Symbol('acmatch')
    dcmatch = Symbol('dcmatch')
    stb = Symbol('stb')
    tran = Symbol('tran')
    envlp = Symbol('envlp')
    ac = Symbol('ac')
    dc = Symbol('dc')
    dc_op = Symbol('dcOp')
    dc_op_info = Symbol('dcOpInfo')
    noise = Symbol('noise')
    xf = Symbol('xf')
    sp = Symbol('sp')
    pss = Symbol('pss')
    pac = Symbol('pac')
    pstb = Symbol('pstb')
    pnoise = Symbol('pnoise')
    pxf = Symbol('pxf')
    psp = Symbol('psp')
    qpss = Symbol('qpss')
    qpac = Symbol('qpac')
    qpnoise = Symbol('qpnoise')
    qpxf = Symbol('qpxf')
    qpsp = Symbol('qpsp')
    hb = Symbol('hb')
    hbac = Symbol('hbac')
    hbstb = Symbol('hbstb')
    hbnoise = Symbol('hbnoise')
    hbxf = Symbol('hbxf')
    hbsp = Symbol('hbsp')
    sens = Symbol('sens')


class Categ(SymbolEnum):
    """Category"""
    analog = Symbol('analog')
    digital = Symbol('digital')


class Mode(SymbolEnum):
    """Mode"""
    read = Symbol('r')
    write = Symbol('w')
    append = Symbol('a')


class SaveType(SymbolEnum):
    """Save Type"""
    #: Specifies that a list of subsequent net names be saved.
    v = Symbol('v')
    #: Specifies that a list of subsequent currents be saved.
    i = Symbol('i')
    #: Specifies that all nets and all currents are to be saved.
    all = Symbol('all')
    #: Specifies that all voltages are to be saved.
    allv = Symbol('allv')
    #: Specifies that all currents are to be saved.
    alli = Symbol('alli')


class Simulator(SymbolEnum):
    """Simulator"""
    ADSsim = Symbol('ADSsim')
    ams = Symbol('ams')
    hspiceD = Symbol('hspiceD')
    spectre = Symbol('spectre')
    UltraSim = Symbol('UltraSim')


class HostMode(SymbolEnum):
    """Host mode"""
    #: Sets the simulation to run locally on the user's machine.
    local = Symbol('local')
    #: Sets the simulation to run on a remote host queue.
    #  For this release, the remote host is specified in the cdsenv file.
    remote = Symbol('remote')
    #: Sets the simulation to run using the distributed processing software.
    distributed = Symbol('distributed')
