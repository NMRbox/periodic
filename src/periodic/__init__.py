
import logging
_logger = logging.getLogger(__name__)

__version__ = 1.0

from dataclasses import dataclass
from enum import Enum

from dataclasses_json import dataclass_json
from typing import Union,Optional


class ElementField(Enum):
    ATOMIC = 'atomic'
    NAME = 'name'
    SYMBOL = 'symbol'


@dataclass_json
@dataclass
class Element:
    atomic: int
    name: str
    symbol: str
    mass: float
    british: str = ''

    def __post_init__(self):
        if self.british == '':
            self.british = self.name
            self._lower_names =(self.name.lower(),)
        else:
            self._lower_names =(self.name.lower(),self.british.lower())

    def is_named(self,value:str):
        """Case-insensitive British / American search for element name"""
        return  value.lower() in self._lower_names



class PeriodicTable:

    def __init__(self):
        self.elements =  (
            Element(1, 'Hydrogen', 'H', 1.00794),
            Element(2, 'Helium', 'He', 4.002602),
            Element(3, 'Lithium', 'Li', 6.941),
            Element(4, 'Beryllium', 'Be', 9.012182),
            Element(5, 'Boron', 'B', 10.811),
            Element(6, 'Carbon', 'C', 12.0107),
            Element(7, 'Nitrogen', 'N', 14.0067),
            Element(8, 'Oxygen', 'O', 15.9994),
            Element(9, 'Fluorine', 'F', 18.9994),
            Element(10, 'Neon', 'Ne', 20.1797),
            Element(11, 'Sodium', 'Na', 22.98976928),
            Element(12, 'Magnesium', 'Mg', 24.305),
            Element(13, 'Aluminum', 'Al', 26.9815386,'Aluminium'),
            Element(14, 'Silicon', 'Si', 28.0855),
            Element(15, 'Phosphorus', 'P', 30.973762),
            Element(16, 'Sulfur', 'S', 32.065,'Sulphur'),
            Element(17, 'Chlorine', 'Cl', 35.453),
            Element(18, 'Argon', 'Ar', 39.948),
            Element(19, 'Potassium', 'K', 39.0983),
            Element(20, 'Calcium', 'Ca', 40.078),
            Element(21, 'Scandium', 'Sc', 44.955912),
            Element(22, 'Titanium', 'Ti', 47.867),
            Element(23, 'Vanadium', 'V', 50.9415),
            Element(24, 'Chromium', 'Cr', 51.9961),
            Element(25, 'Manganese', 'Mn', 54.938045),
            Element(26, 'Iron', 'Fe', 55.845),
            Element(27, 'Cobalt', 'Co', 58.933195),
            Element(28, 'Nickel', 'Ni', 58.6934),
            Element(29, 'Copper', 'Cu', 63.546),
            Element(30, 'Zinc', 'Zn', 65.38),
            Element(31, 'Gallium', 'Ga', 69.723),
            Element(32, 'Germanium', 'Ge', 72.64),
            Element(33, 'Arsenic', 'As', 74.9216),
            Element(34, 'Selenium', 'Se', 78.96),
            Element(35, 'Bromine', 'Br', 79.904),
            Element(36, 'Krypton', 'Kr', 83.798),
            Element(37, 'Rubidium', 'Rb', 85.4678),
            Element(38, 'Strontium', 'Sr', 87.62),
            Element(39, 'Yttrium', 'Y', 88.90585),
            Element(40, 'Zirconium', 'Zr', 91.224),
            Element(41, 'Niobium', 'Nb', 92.90638),
            Element(42, 'Molybdenum', 'Mo', 95.96),
            Element(43, 'Technetium', 'Tc', 98.0),
            Element(44, 'Ruthenium', 'Ru', 101.07),
            Element(45, 'Rhodium', 'Rh', 102.9055),
            Element(46, 'Palladium', 'Pd', 106.42),
            Element(47, 'Silver', 'Ag', 107.8682),
            Element(48, 'Cadmium', 'Cd', 112.411),
            Element(49, 'Indium', 'In', 114.818),
            Element(50, 'Tin', 'Sn', 118.71),
            Element(51, 'Antimony', 'Sb', 121.76),
            Element(52, 'Tellurium', 'Te', 127.6),
            Element(53, 'Iodine', 'I', 126.90447),
            Element(54, 'Xenon', 'Xe', 131.293),
            Element(55, 'Cesium', 'Cs', 132.9054519),
            Element(56, 'Barium', 'Ba', 137.327),
            Element(57, 'Lanthanum', 'La', 138.90547),
            Element(58, 'Cesium', 'Ce', 140.116),
            Element(59, 'Praseodymium', 'Pr', 140.90765),
            Element(60, 'Neodymium', 'Nd', 144.242),
            Element(61, 'Promethium', 'Pm', 145.0),
            Element(62, 'Samarium', 'Sm', 150.36),
            Element(63, 'Europium', 'Eu', 151.964),
            Element(64, 'Gadolinium', 'Gd', 157.25),
            Element(65, 'Terbium', 'Tb', 158.92535),
            Element(66, 'Dysprosium', 'Dy', 162.5001),
            Element(67, 'Holmium', 'Ho', 164.93032),
            Element(68, 'Erbium', 'Er', 167.259),
            Element(69, 'Thulium', 'Tm', 168.93421),
            Element(70, 'Ytterbium', 'Yb', 173.054),
            Element(71, 'Lutetium', 'Lu', 174.9668),
            Element(72, 'Hafnium', 'Hf', 178.49),
            Element(73, 'Tantalum', 'Ta', 180.94788),
            Element(74, 'Tungsten', 'W', 183.84),
            Element(75, 'Rhenium', 'Re', 186.207),
            Element(76, 'Osmium', 'Os', 190.23),
            Element(77, 'Iridium', 'Ir', 192.217),
            Element(78, 'Platinum', 'Pt', 192.084),
            Element(79, 'Gold', 'Au', 196.966569),
            Element(80, 'Hydrargyrum', 'Hg', 200.59),
            Element(81, 'Thallium', 'Tl', 204.3833),
            Element(82, 'Lead', 'Pb', 207.2),
            Element(83, 'Bismuth', 'Bi', 208.980401),
            Element(84, 'Polonium', 'Po', 210.0),
            Element(85, 'Astatine', 'At', 210.0),
            Element(86, 'Radon', 'Rn', 220.0),
            Element(87, 'Francium', 'Fr', 223.0),
            Element(88, 'Radium', 'Ra', 226.0),
            Element(89, 'Actinium', 'Ac', 227.0),
            Element(90, 'Thorium', 'Th', 232.03806),
            Element(91, 'Protactinium', 'Pa', 231.03588),
            Element(92, 'Uranium', 'U', 238.02891),
            Element(93, 'Neptunium', 'Np', 237.0),
            Element(94, 'Plutonium', 'Pu', 244.0),
            Element(95, 'Americium', 'Am', 243.0),
            Element(96, 'Curium', 'Cm', 247.0),
            Element(97, 'Berkelium', 'Bk', 247.0),
            Element(98, 'Californium', 'Cf', 251.0),
            Element(99, 'Einsteinium', 'Es', 252.0),
            Element(100, 'Fermium', 'Fm', 257.0),
            Element(101, 'Mendelevium', 'Md', 258.0),
            Element(102, 'Nobelium', 'No', 259.0),
            Element(103, 'Lawrencium', 'Lr', 262.0),
            Element(104, 'Rutherfordium', 'Rf', 261.0),
            Element(105, 'Dubnium', 'Db', 262.0),
            Element(106, 'Seaborgium', 'Sg', 266.0),
            Element(107, 'Bohrium', 'Bh', 264.0),
            Element(108, 'Hassium', 'Hs', 277.0),
            Element(109, 'Meitnerium', 'Mt', 268.0),
            Element(110, 'Ununnilium', 'Ds', 271.0),
            Element(111, 'Unununium', 'Rg', 272.0),
            Element(112, 'Ununbium', 'Uub', 285.0),
            Element(113, 'Ununtrium', 'Uut', 284.0),
            Element(114, 'Ununquadium', 'Uuq', 289.0),
            Element(115, 'Ununpentium', 'Uup', 288.0),
            Element(116, 'Ununhexium', 'Uuh', 292.0),
            Element(118, 'Ununoctium', 'Uuo', 294.0),
        )

    def search_name(self,name:str)-> Optional[Element]:
        """Case-insensitive British / American search for element name"""
        for e in self.elements:
            if e.is_named(name):
                return e
        return None

    def search_symbol(self,symbol:str)-> Optional[Element]:
        """Case-insensitive search for element symbol"""
        lsymbol = symbol.lower()
        for e in self.elements:
            if lsymbol == e.symbol.lower():
                return e
        return None

    def search_number(self,number:int)-> Optional[Element]:
        """Search by atomic number"""
        for e in self.elements:
            if e.atomic == number:
                return e
        return None


if __name__ == "__main__":
    pt = PeriodicTable()
    print(pt.search_number(1))
    print(pt.search_symbol('fe'))
    print(pt.search_symbol('Fe'))
    s = pt.search_number(16)
    names = ('sulfur','Sulfur','Sulphur')
    for n in names:
        if not s.is_named(n):
            print(n)
