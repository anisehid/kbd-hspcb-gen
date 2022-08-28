from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

lfk17_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(name='MX_LED',dest=TEMPLATE,tool=SKIDL,rgb=1,col=1,d_ref='D1',d_pin=4,row=1,ref_prefix='M',num_units=2,fplist=['cherry'],do_erc=True,footprint='Keyboard:MXHS-1U-RGB-ALI-3528-HOLE-NOPAD',pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='VCC',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='GND',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='CP',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='CN',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='DI',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='DO',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='MX',dest=TEMPLATE,tool=SKIDL,col=1,row=1,ref_prefix='M',num_units=1,fplist=['cherry'],do_erc=True,footprint='Keyboard:MXHS-1U',pins=[
            Pin(num='MX1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='MX2',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='D',dest=TEMPLATE,tool=SKIDL,description='1N4148 Switch Diode',keywords='diode',x=1.0,y=1.0,row=1,ref_prefix='D',num_units=1,fplist=['D_*'],do_erc=True,footprint='Keyboard:0805D',pins=[
            Pin(num='1',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='BTB',dest=TEMPLATE,tool=SKIDL,description='DF40C-30DS-0.4V Male',keywords='b2b-conn',row=1,ref_prefix='CN',num_units=1,fplist=['CN_*'],do_erc=True,footprint='Keyboard:30PIN_0.4MM_BTB_MALE',pins=[
            Pin(num= '1',name= '1',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '2',name= '2',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '3',name= '3',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '4',name= '4',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '5',name= '5',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '6',name= '6',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '7',name= '7',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '8',name= '8',func=Pin.PASSIVE,do_erc=True),
            Pin(num= '9',name= '9',func=Pin.PASSIVE,do_erc=True),
            Pin(num='10',name='10',func=Pin.PASSIVE,do_erc=True),
            Pin(num='11',name='11',func=Pin.PASSIVE,do_erc=True),
            Pin(num='12',name='12',func=Pin.PASSIVE,do_erc=True),
            Pin(num='13',name='13',func=Pin.PASSIVE,do_erc=True),
            Pin(num='14',name='14',func=Pin.PASSIVE,do_erc=True),
            Pin(num='15',name='15',func=Pin.PASSIVE,do_erc=True),
            Pin(num='16',name='16',func=Pin.PASSIVE,do_erc=True),
            Pin(num='17',name='17',func=Pin.PASSIVE,do_erc=True),
            Pin(num='18',name='18',func=Pin.PASSIVE,do_erc=True),
            Pin(num='19',name='19',func=Pin.PASSIVE,do_erc=True),
            Pin(num='20',name='20',func=Pin.PASSIVE,do_erc=True),
            Pin(num='21',name='21',func=Pin.PASSIVE,do_erc=True),
            Pin(num='22',name='22',func=Pin.PASSIVE,do_erc=True),
            Pin(num='23',name='23',func=Pin.PASSIVE,do_erc=True),
            Pin(num='24',name='24',func=Pin.PASSIVE,do_erc=True),
            Pin(num='25',name='25',func=Pin.PASSIVE,do_erc=True),
            Pin(num='26',name='26',func=Pin.PASSIVE,do_erc=True),
            Pin(num='27',name='27',func=Pin.PASSIVE,do_erc=True),
            Pin(num='28',name='28',func=Pin.PASSIVE,do_erc=True),
            Pin(num='29',name='29',func=Pin.PASSIVE,do_erc=True),
            Pin(num='30',name='30',func=Pin.PASSIVE,do_erc=True),
            ]),
        Part(name='C',dest=TEMPLATE,tool=SKIDL,description='Unpolarized capacitor',keywords='cap capacitor',ref_prefix='C',num_units=1,fplist=['C_*'],do_erc=True,footprint='Capacitors_SMD:C_0603',pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='R',dest=TEMPLATE,tool=SKIDL,description='Resistor',keywords='r res resistor',ref_prefix='R',num_units=1,fplist=['R_*', 'R_*'],do_erc=True,footprint='Resistors_SMD:R_0603',pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='SW_PUSH',dest=TEMPLATE,tool=SKIDL,description='Button',keywords='Switch',ref_prefix='SW',num_units=1,do_erc=True,footprint='Buttons_Switches_SMD:SW_SPST_EVPBF',pins=[
            Pin(num='1',name='1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.PASSIVE,do_erc=True)]),
        ])
