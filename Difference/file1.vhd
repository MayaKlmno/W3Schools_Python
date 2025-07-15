library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.Numeric_Std.all;

--library Moku;
--use Moku.Support.sum_no_overflow;
ENTITY CustomWrapper IS
PORT(
    clk: IN STD_LOGIC;
    reset: IN STD_LOGIC;
    InputA: IN signed(15 downto 0);
    Control0: IN signed(15 downto 0);
    Control1: IN signed(15 downto 0);
    Control2: IN signed(15 downto 0);
    OutputA: OUT signed(15 downto 0)
    );
END CustomWrapper;

architecture Behavioural of CustomWrapper is
type state_type is (state_Idle, state_vBottom, state_vTop, state_vBottom2);
    signal state: state_type;
    signal nextState: state_type;

    signal trigger_flag: std_logic ;

    constant delay : integer := 5; --cannot be zero!
    constant pulse : integer := 10;

    signal index : integer := 0;

    signal vtop : signed(15 downto 0); -- voltage at top/ Max voltage
    signal vbottom : signed(15 downto 0); -- floor voltage
    signal threshold : signed(15 downto 0); --threshold to detect a
trigger pulse on InputA
     -- ex: vtop = 512 (~16mV) , vl1=vl2=256 (~8mV), offset = 0,
threshold = 2048 (~65mV)
begin

     vtop <= signed(Control0(15 downto 0));
     vbottom <= signed(Control1(15 downto 0));
     threshold <= signed(Control2(15 downto 0));
     -- end of read input parameters

     process(clk, state)
     begin
         case state is
           when state_Idle =>
             OutputA <= (others => '0');
             index <= 0;
             if trigger_flag = '1' then
                nextState <= state_vBottom;
             else
                nextState <= state_Idle;
             end if;
           when state_vBottom =>
             OutputA <= vbottom;
             if index < delay then
                nextState <= state_vBottom;
                index <= index + 1;
             else
                nextState <= state_vTop;
                index <= 0;
             end if;
           when state_vTop =>
             OutputA <= vtop;
             if index < pulse then
                nextState <= state_vTop;
                index <= index + 1;
             else
                nextState <= state_vBottom2;
                index <= 0;
             end if;
            when state_vBottom2 =>
              OutputA <= vbottom;
              if index < delay then
                nextState <= state_vBottom2;
                index <= index + 1;
              else
                nextState <= state_Idle;
                index <= 0;
              end if;
           when others =>
              OutputA <= (others => '0');
              nextState <= state_Idle;

        end case;
     end process;

     process(clk, reset, InputA)
     begin
       if reset = '1' then
       	 state <= state_Idle;
         trigger_flag <= '0';
         index <= '0';
       elsif rising_edge(clk) then
       	 state <= nextState;
         -- Update index
         if index < (delay + pulse + delay -1) then
            index <= index + 1;
         else
            index <= 0;
         end if;
         
         if InputA > threshold then
           trigger_flag <= '1';
         else trigger_flag <= '0';
         end if;
       end if;
     end process;

end Behavioural;