library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_misc.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
use std.textio.all;
use work.ram_data.all


entity ram is
   generic(memory_type : string := "DEFAULT");
   port(clk               : in std_logic;
        enable            : in std_logic;
        write_byte_enable : in std_logic_vector(3 downto 0);
        address           : in std_logic_vector(31 downto 2);
        data_write        : in std_logic_vector(31 downto 0);
        data_read         : out std_logic_vector(31 downto 0));
end; --entity ram

architecture logic of ram is
   constant ZERO          : std_logic_vector(31 downto 0) := "00000000000000000000000000000000"; 

begin



   RAMB_inst0 : work.ram_2k8
   generic map (
		mem_ctxt	=> RAM0_DATA
	)
   port map (
		CLK	=> clk,
		DI	=> data_write(31 downto 24),
		DO	=> data_read(31 downto 24),
		AD	=> address(12 downto 2),
		WE	=> write_byte_enable(3));

   RAMB_inst1 : work.ram_2k8
   generic map (
		mem_ctxt	=> RAM1_DATA
	)
   port map (
	CLK	=> clk,
	DI	=> data_write(23 downto 16),
	DO	=> data_read(23 downto 16),
	AD	=> address(12 downto 2),
	WE	=> write_byte_enable(2));

   RAMB_inst2 : work.ram_2k8
  generic map (
		mem_ctxt	=> RAM2_DATA
	)
   port map (
     CLK	=> clk,
	DI	=> data_write(15 downto 8),
	DO	=> data_read(15 downto 8),
	AD	=> address(12 downto 2),
	WE	=> write_byte_enable(1));

   RAMB_inst3 : work.ram_2k8
  generic map (
		mem_ctxt	=> RAM3_DATA
	)
   port map (
	CLK	=> clk,
	DI	=> data_write(7 downto 0),
	DO	=> data_read(7 downto 0),
	AD	=> address(12 downto 2),
	WE	=> write_byte_enable(0));


end; --architecture logic
