library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library NX;
use NX.nxPackage.all;

entity ram_2k8 is
	generic(
		mem_ctxt : string
	);
    port(
	CLK	:   in std_logic;
	DI	:   in std_logic_vector(7 downto 0);
	DO	:   out std_logic_vector(7 downto 0);
	AD	:   in std_logic_vector(10 downto 0);
	WE	:   in std_logic
    );
end entity;

architecture rtl of ram_2k8 is

begin

RAM_0 : NX_RAM
generic map (
     std_mode => "NOECC_6kx8",
	  mem_ctxt => mem_ctxt
)
port map (
     ACK  => CLK
   , ACKC => CLK
   , ACKD => OPEN
   , ACKR => OPEN
   , AI1  => DI(0)
   , AI2  => DI(1)
   , AI3  => DI(2)
   , AI4  => DI(3)
   , AI5  => DI(4)
   , AI6  => DI(5)
   , AI7  => DI(6)
   , AI8  => DI(7)
   , AI9  => OPEN
   , AI10 => OPEN
   , AI11 => OPEN
   , AI12 => OPEN
   , AI13 => OPEN
   , AI14 => OPEN
   , AI15 => OPEN
   , AI16 => OPEN
   , AI17 => OPEN
   , AI18 => OPEN
   , AI19 => OPEN
   , AI20 => OPEN
   , AI21 => OPEN
   , AI22 => OPEN
   , AI23 => OPEN
   , AI24 => OPEN
   , ACOR => OPEN
   , AERR => OPEN
   , AO1  => DO(0)
   , AO2  => DO(1)
   , AO3  => DO(2)
   , AO4  => DO(3)
   , AO5  => DO(4)
   , AO6  => DO(5)
   , AO7  => DO(6)
   , AO8  => DO(7)
   , AO9  => OPEN
   , AO10 => OPEN
   , AO11 => OPEN
   , AO12 => OPEN
   , AO13 => OPEN
   , AO14 => OPEN
   , AO15 => OPEN
   , AO16 => OPEN
   , AO17 => OPEN
   , AO18 => OPEN
   , AO19 => OPEN
   , AO20 => OPEN
   , AO21 => OPEN
   , AO22 => OPEN
   , AO23 => OPEN
   , AO24 => OPEN
   , AA1  => AD(0)
   , AA2  => AD(1)
   , AA3  => AD(2)
   , AA4  => AD(3)
   , AA5  => AD(4)
   , AA6  => AD(5)
   , AA7  => AD(6)
   , AA8  => AD(7)
   , AA9  => AD(8)
   , AA10 => AD(9)
   , AA11 => AD(10)
   , AA12 => OPEN
   , AA13 => OPEN
   , AA14 => OPEN
   , AA15 => OPEN
   , AA16 => OPEN
   , ACS  => '1'
   , AWE  => WE
   , AR   => OPEN
   , BCK  => OPEN
   , BCKC => OPEN
   , BCKD => OPEN
   , BCKR => OPEN
   , BI1  => OPEN
   , BI2  => OPEN
   , BI3  => OPEN
   , BI4  => OPEN
   , BI5  => OPEN
   , BI6  => OPEN
   , BI7  => OPEN
   , BI8  => OPEN
   , BI9  => OPEN
   , BI10 => OPEN
   , BI11 => OPEN
   , BI12 => OPEN
   , BI13 => OPEN
   , BI14 => OPEN
   , BI15 => OPEN
   , BI16 => OPEN
   , BI17 => OPEN
   , BI18 => OPEN
   , BI19 => OPEN
   , BI20 => OPEN
   , BI21 => OPEN
   , BI22 => OPEN
   , BI23 => OPEN
   , BI24 => OPEN
   , BCOR => OPEN
   , BERR => OPEN
   , BO1  => OPEN
   , BO2  => OPEN
   , BO3  => OPEN
   , BO4  => OPEN
   , BO5  => OPEN
   , BO6  => OPEN
   , BO7  => OPEN
   , BO8  => OPEN
   , BO9  => OPEN
   , BO10 => OPEN
   , BO11 => OPEN
   , BO12 => OPEN
   , BO13 => OPEN
   , BO14 => OPEN
   , BO15 => OPEN
   , BO16 => OPEN
   , BO17 => OPEN
   , BO18 => OPEN
   , BO19 => OPEN
   , BO20 => OPEN
   , BO21 => OPEN
   , BO22 => OPEN
   , BO23 => OPEN
   , BO24 => OPEN
   , BA1  => OPEN
   , BA2  => OPEN
   , BA3  => OPEN
   , BA4  => OPEN
   , BA5  => OPEN
   , BA6  => OPEN
   , BA7  => OPEN
   , BA8  => OPEN
   , BA9  => OPEN
   , BA10 => OPEN
   , BA11 => OPEN
   , BA12 => OPEN
   , BA13 => OPEN
   , BA14 => OPEN
   , BA15 => OPEN
   , BA16 => OPEN
   , BCS  => OPEN
   , BWE  => OPEN
   , BR   => OPEN
);

end architecture;
