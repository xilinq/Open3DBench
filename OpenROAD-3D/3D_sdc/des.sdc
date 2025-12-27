###################################################################

# Created by write_sdc on Tue Nov 25 13:23:37 2025

###################################################################
set sdc_version 2.1

set_units -time ps -resistance kOhm -capacitance fF -voltage V -current mA
set_wire_load_mode top
set_max_transition 40 [current_design]
create_clock [get_ports clk]  -period 1000  -waveform {0 500}
set_clock_uncertainty 30  [get_clocks clk]
set_clock_transition -max -rise 30 [get_clocks clk]
set_clock_transition -min -rise 10 [get_clocks clk]
set_clock_transition -max -fall 30 [get_clocks clk]
set_clock_transition -min -fall 10 [get_clocks clk]
group_path -name DFF  -from [list [get_cells data_o_reg_0_] [get_cells data_o_reg_1_] [get_cells    \
data_o_reg_2_] [get_cells data_o_reg_3_] [get_cells data_o_reg_4_] [get_cells  \
data_o_reg_5_] [get_cells data_o_reg_6_] [get_cells data_o_reg_7_] [get_cells  \
data_o_reg_8_] [get_cells data_o_reg_9_] [get_cells data_o_reg_10_] [get_cells \
data_o_reg_11_] [get_cells data_o_reg_12_] [get_cells data_o_reg_13_]          \
[get_cells data_o_reg_14_] [get_cells data_o_reg_15_] [get_cells               \
data_o_reg_16_] [get_cells data_o_reg_17_] [get_cells data_o_reg_18_]          \
[get_cells data_o_reg_19_] [get_cells data_o_reg_20_] [get_cells               \
data_o_reg_21_] [get_cells data_o_reg_22_] [get_cells data_o_reg_23_]          \
[get_cells data_o_reg_24_] [get_cells data_o_reg_25_] [get_cells               \
data_o_reg_26_] [get_cells data_o_reg_27_] [get_cells data_o_reg_28_]          \
[get_cells data_o_reg_29_] [get_cells data_o_reg_30_] [get_cells               \
data_o_reg_31_] [get_cells data_o_reg_32_] [get_cells data_o_reg_33_]          \
[get_cells data_o_reg_34_] [get_cells data_o_reg_35_] [get_cells               \
data_o_reg_36_] [get_cells data_o_reg_37_] [get_cells data_o_reg_38_]          \
[get_cells data_o_reg_39_] [get_cells data_o_reg_40_] [get_cells               \
data_o_reg_41_] [get_cells data_o_reg_42_] [get_cells data_o_reg_43_]          \
[get_cells data_o_reg_44_] [get_cells data_o_reg_45_] [get_cells               \
data_o_reg_46_] [get_cells data_o_reg_47_] [get_cells data_o_reg_48_]          \
[get_cells data_o_reg_49_] [get_cells data_o_reg_50_] [get_cells               \
data_o_reg_51_] [get_cells data_o_reg_52_] [get_cells data_o_reg_53_]          \
[get_cells data_o_reg_54_] [get_cells data_o_reg_55_] [get_cells               \
data_o_reg_56_] [get_cells data_o_reg_57_] [get_cells data_o_reg_58_]          \
[get_cells data_o_reg_59_] [get_cells data_o_reg_60_] [get_cells               \
data_o_reg_61_] [get_cells data_o_reg_62_] [get_cells data_o_reg_63_]          \
[get_cells ready_o_reg] [get_cells data_ready_reg] [get_cells                  \
stage1_iter_reg_0_] [get_cells stage1_iter_reg_1_] [get_cells                  \
stage1_iter_reg_2_] [get_cells stage1_iter_reg_3_] [get_cells rd1/L_o_reg_0_]  \
[get_cells rd1/L_o_reg_1_] [get_cells rd1/L_o_reg_2_] [get_cells               \
rd1/L_o_reg_3_] [get_cells rd1/L_o_reg_4_] [get_cells rd1/L_o_reg_5_]          \
[get_cells rd1/L_o_reg_6_] [get_cells rd1/L_o_reg_7_] [get_cells               \
rd1/L_o_reg_8_] [get_cells rd1/L_o_reg_9_] [get_cells rd1/L_o_reg_10_]         \
[get_cells rd1/L_o_reg_11_] [get_cells rd1/L_o_reg_12_] [get_cells             \
rd1/L_o_reg_13_] [get_cells rd1/L_o_reg_14_] [get_cells rd1/L_o_reg_15_]       \
[get_cells rd1/L_o_reg_16_] [get_cells rd1/L_o_reg_17_] [get_cells             \
rd1/L_o_reg_18_] [get_cells rd1/L_o_reg_19_] [get_cells rd1/L_o_reg_20_]       \
[get_cells rd1/L_o_reg_21_] [get_cells rd1/L_o_reg_22_] [get_cells             \
rd1/L_o_reg_23_] [get_cells rd1/L_o_reg_24_] [get_cells rd1/L_o_reg_25_]       \
[get_cells rd1/L_o_reg_26_] [get_cells rd1/L_o_reg_27_] [get_cells             \
rd1/L_o_reg_28_] [get_cells rd1/L_o_reg_29_] [get_cells rd1/L_o_reg_30_]       \
[get_cells rd1/L_o_reg_31_] [get_cells rd1/Key_o_reg_0_] [get_cells            \
rd1/Key_o_reg_1_] [get_cells rd1/Key_o_reg_2_] [get_cells rd1/Key_o_reg_3_]    \
[get_cells rd1/Key_o_reg_4_] [get_cells rd1/Key_o_reg_5_] [get_cells           \
rd1/Key_o_reg_6_] [get_cells rd1/Key_o_reg_7_] [get_cells rd1/Key_o_reg_8_]    \
[get_cells rd1/Key_o_reg_9_] [get_cells rd1/Key_o_reg_10_] [get_cells          \
rd1/Key_o_reg_11_] [get_cells rd1/Key_o_reg_12_] [get_cells rd1/Key_o_reg_13_] \
[get_cells rd1/Key_o_reg_14_] [get_cells rd1/Key_o_reg_15_] [get_cells         \
rd1/Key_o_reg_16_] [get_cells rd1/Key_o_reg_17_] [get_cells rd1/Key_o_reg_18_] \
[get_cells rd1/Key_o_reg_19_] [get_cells rd1/Key_o_reg_20_] [get_cells         \
rd1/Key_o_reg_21_] [get_cells rd1/Key_o_reg_22_] [get_cells rd1/Key_o_reg_23_] \
[get_cells rd1/Key_o_reg_24_] [get_cells rd1/Key_o_reg_25_] [get_cells         \
rd1/Key_o_reg_26_] [get_cells rd1/Key_o_reg_27_] [get_cells rd1/Key_o_reg_28_] \
[get_cells rd1/Key_o_reg_29_] [get_cells rd1/Key_o_reg_30_] [get_cells         \
rd1/Key_o_reg_31_] [get_cells rd1/Key_o_reg_32_] [get_cells rd1/Key_o_reg_33_] \
[get_cells rd1/Key_o_reg_34_] [get_cells rd1/Key_o_reg_35_] [get_cells         \
rd1/Key_o_reg_36_] [get_cells rd1/Key_o_reg_37_] [get_cells rd1/Key_o_reg_38_] \
[get_cells rd1/Key_o_reg_39_] [get_cells rd1/Key_o_reg_40_] [get_cells         \
rd1/Key_o_reg_41_] [get_cells rd1/Key_o_reg_42_] [get_cells rd1/Key_o_reg_43_] \
[get_cells rd1/Key_o_reg_44_] [get_cells rd1/Key_o_reg_45_] [get_cells         \
rd1/Key_o_reg_46_] [get_cells rd1/Key_o_reg_47_] [get_cells rd1/Key_o_reg_48_] \
[get_cells rd1/Key_o_reg_49_] [get_cells rd1/Key_o_reg_50_] [get_cells         \
rd1/Key_o_reg_51_] [get_cells rd1/Key_o_reg_52_] [get_cells rd1/Key_o_reg_53_] \
[get_cells rd1/Key_o_reg_54_] [get_cells rd1/Key_o_reg_55_] [get_cells         \
rd1/R_o_reg_0_] [get_cells rd1/R_o_reg_1_] [get_cells rd1/R_o_reg_2_]          \
[get_cells rd1/R_o_reg_3_] [get_cells rd1/R_o_reg_4_] [get_cells               \
rd1/R_o_reg_5_] [get_cells rd1/R_o_reg_6_] [get_cells rd1/R_o_reg_7_]          \
[get_cells rd1/R_o_reg_8_] [get_cells rd1/R_o_reg_9_] [get_cells               \
rd1/R_o_reg_10_] [get_cells rd1/R_o_reg_11_] [get_cells rd1/R_o_reg_12_]       \
[get_cells rd1/R_o_reg_13_] [get_cells rd1/R_o_reg_14_] [get_cells             \
rd1/R_o_reg_15_] [get_cells rd1/R_o_reg_16_] [get_cells rd1/R_o_reg_17_]       \
[get_cells rd1/R_o_reg_18_] [get_cells rd1/R_o_reg_19_] [get_cells             \
rd1/R_o_reg_20_] [get_cells rd1/R_o_reg_21_] [get_cells rd1/R_o_reg_22_]       \
[get_cells rd1/R_o_reg_23_] [get_cells rd1/R_o_reg_24_] [get_cells             \
rd1/R_o_reg_25_] [get_cells rd1/R_o_reg_26_] [get_cells rd1/R_o_reg_27_]       \
[get_cells rd1/R_o_reg_28_] [get_cells rd1/R_o_reg_29_] [get_cells             \
rd1/R_o_reg_30_] [get_cells rd1/R_o_reg_31_]]  -to [list [get_cells data_o_reg_0_] [get_cells data_o_reg_1_] [get_cells      \
data_o_reg_2_] [get_cells data_o_reg_3_] [get_cells data_o_reg_4_] [get_cells  \
data_o_reg_5_] [get_cells data_o_reg_6_] [get_cells data_o_reg_7_] [get_cells  \
data_o_reg_8_] [get_cells data_o_reg_9_] [get_cells data_o_reg_10_] [get_cells \
data_o_reg_11_] [get_cells data_o_reg_12_] [get_cells data_o_reg_13_]          \
[get_cells data_o_reg_14_] [get_cells data_o_reg_15_] [get_cells               \
data_o_reg_16_] [get_cells data_o_reg_17_] [get_cells data_o_reg_18_]          \
[get_cells data_o_reg_19_] [get_cells data_o_reg_20_] [get_cells               \
data_o_reg_21_] [get_cells data_o_reg_22_] [get_cells data_o_reg_23_]          \
[get_cells data_o_reg_24_] [get_cells data_o_reg_25_] [get_cells               \
data_o_reg_26_] [get_cells data_o_reg_27_] [get_cells data_o_reg_28_]          \
[get_cells data_o_reg_29_] [get_cells data_o_reg_30_] [get_cells               \
data_o_reg_31_] [get_cells data_o_reg_32_] [get_cells data_o_reg_33_]          \
[get_cells data_o_reg_34_] [get_cells data_o_reg_35_] [get_cells               \
data_o_reg_36_] [get_cells data_o_reg_37_] [get_cells data_o_reg_38_]          \
[get_cells data_o_reg_39_] [get_cells data_o_reg_40_] [get_cells               \
data_o_reg_41_] [get_cells data_o_reg_42_] [get_cells data_o_reg_43_]          \
[get_cells data_o_reg_44_] [get_cells data_o_reg_45_] [get_cells               \
data_o_reg_46_] [get_cells data_o_reg_47_] [get_cells data_o_reg_48_]          \
[get_cells data_o_reg_49_] [get_cells data_o_reg_50_] [get_cells               \
data_o_reg_51_] [get_cells data_o_reg_52_] [get_cells data_o_reg_53_]          \
[get_cells data_o_reg_54_] [get_cells data_o_reg_55_] [get_cells               \
data_o_reg_56_] [get_cells data_o_reg_57_] [get_cells data_o_reg_58_]          \
[get_cells data_o_reg_59_] [get_cells data_o_reg_60_] [get_cells               \
data_o_reg_61_] [get_cells data_o_reg_62_] [get_cells data_o_reg_63_]          \
[get_cells ready_o_reg] [get_cells data_ready_reg] [get_cells                  \
stage1_iter_reg_0_] [get_cells stage1_iter_reg_1_] [get_cells                  \
stage1_iter_reg_2_] [get_cells stage1_iter_reg_3_] [get_cells rd1/L_o_reg_0_]  \
[get_cells rd1/L_o_reg_1_] [get_cells rd1/L_o_reg_2_] [get_cells               \
rd1/L_o_reg_3_] [get_cells rd1/L_o_reg_4_] [get_cells rd1/L_o_reg_5_]          \
[get_cells rd1/L_o_reg_6_] [get_cells rd1/L_o_reg_7_] [get_cells               \
rd1/L_o_reg_8_] [get_cells rd1/L_o_reg_9_] [get_cells rd1/L_o_reg_10_]         \
[get_cells rd1/L_o_reg_11_] [get_cells rd1/L_o_reg_12_] [get_cells             \
rd1/L_o_reg_13_] [get_cells rd1/L_o_reg_14_] [get_cells rd1/L_o_reg_15_]       \
[get_cells rd1/L_o_reg_16_] [get_cells rd1/L_o_reg_17_] [get_cells             \
rd1/L_o_reg_18_] [get_cells rd1/L_o_reg_19_] [get_cells rd1/L_o_reg_20_]       \
[get_cells rd1/L_o_reg_21_] [get_cells rd1/L_o_reg_22_] [get_cells             \
rd1/L_o_reg_23_] [get_cells rd1/L_o_reg_24_] [get_cells rd1/L_o_reg_25_]       \
[get_cells rd1/L_o_reg_26_] [get_cells rd1/L_o_reg_27_] [get_cells             \
rd1/L_o_reg_28_] [get_cells rd1/L_o_reg_29_] [get_cells rd1/L_o_reg_30_]       \
[get_cells rd1/L_o_reg_31_] [get_cells rd1/Key_o_reg_0_] [get_cells            \
rd1/Key_o_reg_1_] [get_cells rd1/Key_o_reg_2_] [get_cells rd1/Key_o_reg_3_]    \
[get_cells rd1/Key_o_reg_4_] [get_cells rd1/Key_o_reg_5_] [get_cells           \
rd1/Key_o_reg_6_] [get_cells rd1/Key_o_reg_7_] [get_cells rd1/Key_o_reg_8_]    \
[get_cells rd1/Key_o_reg_9_] [get_cells rd1/Key_o_reg_10_] [get_cells          \
rd1/Key_o_reg_11_] [get_cells rd1/Key_o_reg_12_] [get_cells rd1/Key_o_reg_13_] \
[get_cells rd1/Key_o_reg_14_] [get_cells rd1/Key_o_reg_15_] [get_cells         \
rd1/Key_o_reg_16_] [get_cells rd1/Key_o_reg_17_] [get_cells rd1/Key_o_reg_18_] \
[get_cells rd1/Key_o_reg_19_] [get_cells rd1/Key_o_reg_20_] [get_cells         \
rd1/Key_o_reg_21_] [get_cells rd1/Key_o_reg_22_] [get_cells rd1/Key_o_reg_23_] \
[get_cells rd1/Key_o_reg_24_] [get_cells rd1/Key_o_reg_25_] [get_cells         \
rd1/Key_o_reg_26_] [get_cells rd1/Key_o_reg_27_] [get_cells rd1/Key_o_reg_28_] \
[get_cells rd1/Key_o_reg_29_] [get_cells rd1/Key_o_reg_30_] [get_cells         \
rd1/Key_o_reg_31_] [get_cells rd1/Key_o_reg_32_] [get_cells rd1/Key_o_reg_33_] \
[get_cells rd1/Key_o_reg_34_] [get_cells rd1/Key_o_reg_35_] [get_cells         \
rd1/Key_o_reg_36_] [get_cells rd1/Key_o_reg_37_] [get_cells rd1/Key_o_reg_38_] \
[get_cells rd1/Key_o_reg_39_] [get_cells rd1/Key_o_reg_40_] [get_cells         \
rd1/Key_o_reg_41_] [get_cells rd1/Key_o_reg_42_] [get_cells rd1/Key_o_reg_43_] \
[get_cells rd1/Key_o_reg_44_] [get_cells rd1/Key_o_reg_45_] [get_cells         \
rd1/Key_o_reg_46_] [get_cells rd1/Key_o_reg_47_] [get_cells rd1/Key_o_reg_48_] \
[get_cells rd1/Key_o_reg_49_] [get_cells rd1/Key_o_reg_50_] [get_cells         \
rd1/Key_o_reg_51_] [get_cells rd1/Key_o_reg_52_] [get_cells rd1/Key_o_reg_53_] \
[get_cells rd1/Key_o_reg_54_] [get_cells rd1/Key_o_reg_55_] [get_cells         \
rd1/R_o_reg_0_] [get_cells rd1/R_o_reg_1_] [get_cells rd1/R_o_reg_2_]          \
[get_cells rd1/R_o_reg_3_] [get_cells rd1/R_o_reg_4_] [get_cells               \
rd1/R_o_reg_5_] [get_cells rd1/R_o_reg_6_] [get_cells rd1/R_o_reg_7_]          \
[get_cells rd1/R_o_reg_8_] [get_cells rd1/R_o_reg_9_] [get_cells               \
rd1/R_o_reg_10_] [get_cells rd1/R_o_reg_11_] [get_cells rd1/R_o_reg_12_]       \
[get_cells rd1/R_o_reg_13_] [get_cells rd1/R_o_reg_14_] [get_cells             \
rd1/R_o_reg_15_] [get_cells rd1/R_o_reg_16_] [get_cells rd1/R_o_reg_17_]       \
[get_cells rd1/R_o_reg_18_] [get_cells rd1/R_o_reg_19_] [get_cells             \
rd1/R_o_reg_20_] [get_cells rd1/R_o_reg_21_] [get_cells rd1/R_o_reg_22_]       \
[get_cells rd1/R_o_reg_23_] [get_cells rd1/R_o_reg_24_] [get_cells             \
rd1/R_o_reg_25_] [get_cells rd1/R_o_reg_26_] [get_cells rd1/R_o_reg_27_]       \
[get_cells rd1/R_o_reg_28_] [get_cells rd1/R_o_reg_29_] [get_cells             \
rd1/R_o_reg_30_] [get_cells rd1/R_o_reg_31_]]
group_path -name INPUT_GROUP  -from [list [get_ports clk] [get_ports reset] [get_ports load_i] [get_ports   \
decrypt_i] [get_ports {data_i[63]}] [get_ports {data_i[62]}] [get_ports        \
{data_i[61]}] [get_ports {data_i[60]}] [get_ports {data_i[59]}] [get_ports     \
{data_i[58]}] [get_ports {data_i[57]}] [get_ports {data_i[56]}] [get_ports     \
{data_i[55]}] [get_ports {data_i[54]}] [get_ports {data_i[53]}] [get_ports     \
{data_i[52]}] [get_ports {data_i[51]}] [get_ports {data_i[50]}] [get_ports     \
{data_i[49]}] [get_ports {data_i[48]}] [get_ports {data_i[47]}] [get_ports     \
{data_i[46]}] [get_ports {data_i[45]}] [get_ports {data_i[44]}] [get_ports     \
{data_i[43]}] [get_ports {data_i[42]}] [get_ports {data_i[41]}] [get_ports     \
{data_i[40]}] [get_ports {data_i[39]}] [get_ports {data_i[38]}] [get_ports     \
{data_i[37]}] [get_ports {data_i[36]}] [get_ports {data_i[35]}] [get_ports     \
{data_i[34]}] [get_ports {data_i[33]}] [get_ports {data_i[32]}] [get_ports     \
{data_i[31]}] [get_ports {data_i[30]}] [get_ports {data_i[29]}] [get_ports     \
{data_i[28]}] [get_ports {data_i[27]}] [get_ports {data_i[26]}] [get_ports     \
{data_i[25]}] [get_ports {data_i[24]}] [get_ports {data_i[23]}] [get_ports     \
{data_i[22]}] [get_ports {data_i[21]}] [get_ports {data_i[20]}] [get_ports     \
{data_i[19]}] [get_ports {data_i[18]}] [get_ports {data_i[17]}] [get_ports     \
{data_i[16]}] [get_ports {data_i[15]}] [get_ports {data_i[14]}] [get_ports     \
{data_i[13]}] [get_ports {data_i[12]}] [get_ports {data_i[11]}] [get_ports     \
{data_i[10]}] [get_ports {data_i[9]}] [get_ports {data_i[8]}] [get_ports       \
{data_i[7]}] [get_ports {data_i[6]}] [get_ports {data_i[5]}] [get_ports        \
{data_i[4]}] [get_ports {data_i[3]}] [get_ports {data_i[2]}] [get_ports        \
{data_i[1]}] [get_ports {data_i[0]}] [get_ports {key_i[63]}] [get_ports        \
{key_i[62]}] [get_ports {key_i[61]}] [get_ports {key_i[60]}] [get_ports        \
{key_i[59]}] [get_ports {key_i[58]}] [get_ports {key_i[57]}] [get_ports        \
{key_i[56]}] [get_ports {key_i[55]}] [get_ports {key_i[54]}] [get_ports        \
{key_i[53]}] [get_ports {key_i[52]}] [get_ports {key_i[51]}] [get_ports        \
{key_i[50]}] [get_ports {key_i[49]}] [get_ports {key_i[48]}] [get_ports        \
{key_i[47]}] [get_ports {key_i[46]}] [get_ports {key_i[45]}] [get_ports        \
{key_i[44]}] [get_ports {key_i[43]}] [get_ports {key_i[42]}] [get_ports        \
{key_i[41]}] [get_ports {key_i[40]}] [get_ports {key_i[39]}] [get_ports        \
{key_i[38]}] [get_ports {key_i[37]}] [get_ports {key_i[36]}] [get_ports        \
{key_i[35]}] [get_ports {key_i[34]}] [get_ports {key_i[33]}] [get_ports        \
{key_i[32]}] [get_ports {key_i[31]}] [get_ports {key_i[30]}] [get_ports        \
{key_i[29]}] [get_ports {key_i[28]}] [get_ports {key_i[27]}] [get_ports        \
{key_i[26]}] [get_ports {key_i[25]}] [get_ports {key_i[24]}] [get_ports        \
{key_i[23]}] [get_ports {key_i[22]}] [get_ports {key_i[21]}] [get_ports        \
{key_i[20]}] [get_ports {key_i[19]}] [get_ports {key_i[18]}] [get_ports        \
{key_i[17]}] [get_ports {key_i[16]}] [get_ports {key_i[15]}] [get_ports        \
{key_i[14]}] [get_ports {key_i[13]}] [get_ports {key_i[12]}] [get_ports        \
{key_i[11]}] [get_ports {key_i[10]}] [get_ports {key_i[9]}] [get_ports         \
{key_i[8]}] [get_ports {key_i[7]}] [get_ports {key_i[6]}] [get_ports           \
{key_i[5]}] [get_ports {key_i[4]}] [get_ports {key_i[3]}] [get_ports           \
{key_i[2]}] [get_ports {key_i[1]}] [get_ports {key_i[0]}]]
group_path -name OUTPUT_GROUP  -to [list [get_ports {data_o[63]}] [get_ports {data_o[62]}] [get_ports        \
{data_o[61]}] [get_ports {data_o[60]}] [get_ports {data_o[59]}] [get_ports     \
{data_o[58]}] [get_ports {data_o[57]}] [get_ports {data_o[56]}] [get_ports     \
{data_o[55]}] [get_ports {data_o[54]}] [get_ports {data_o[53]}] [get_ports     \
{data_o[52]}] [get_ports {data_o[51]}] [get_ports {data_o[50]}] [get_ports     \
{data_o[49]}] [get_ports {data_o[48]}] [get_ports {data_o[47]}] [get_ports     \
{data_o[46]}] [get_ports {data_o[45]}] [get_ports {data_o[44]}] [get_ports     \
{data_o[43]}] [get_ports {data_o[42]}] [get_ports {data_o[41]}] [get_ports     \
{data_o[40]}] [get_ports {data_o[39]}] [get_ports {data_o[38]}] [get_ports     \
{data_o[37]}] [get_ports {data_o[36]}] [get_ports {data_o[35]}] [get_ports     \
{data_o[34]}] [get_ports {data_o[33]}] [get_ports {data_o[32]}] [get_ports     \
{data_o[31]}] [get_ports {data_o[30]}] [get_ports {data_o[29]}] [get_ports     \
{data_o[28]}] [get_ports {data_o[27]}] [get_ports {data_o[26]}] [get_ports     \
{data_o[25]}] [get_ports {data_o[24]}] [get_ports {data_o[23]}] [get_ports     \
{data_o[22]}] [get_ports {data_o[21]}] [get_ports {data_o[20]}] [get_ports     \
{data_o[19]}] [get_ports {data_o[18]}] [get_ports {data_o[17]}] [get_ports     \
{data_o[16]}] [get_ports {data_o[15]}] [get_ports {data_o[14]}] [get_ports     \
{data_o[13]}] [get_ports {data_o[12]}] [get_ports {data_o[11]}] [get_ports     \
{data_o[10]}] [get_ports {data_o[9]}] [get_ports {data_o[8]}] [get_ports       \
{data_o[7]}] [get_ports {data_o[6]}] [get_ports {data_o[5]}] [get_ports        \
{data_o[4]}] [get_ports {data_o[3]}] [get_ports {data_o[2]}] [get_ports        \
{data_o[1]}] [get_ports {data_o[0]}] [get_ports ready_o]]
set_input_delay -clock clk  0  [get_ports reset]
set_input_delay -clock clk  0  [get_ports load_i]
set_input_delay -clock clk  0  [get_ports decrypt_i]
set_input_delay -clock clk  0  [get_ports {data_i[63]}]
set_input_delay -clock clk  0  [get_ports {data_i[62]}]
set_input_delay -clock clk  0  [get_ports {data_i[61]}]
set_input_delay -clock clk  0  [get_ports {data_i[60]}]
set_input_delay -clock clk  0  [get_ports {data_i[59]}]
set_input_delay -clock clk  0  [get_ports {data_i[58]}]
set_input_delay -clock clk  0  [get_ports {data_i[57]}]
set_input_delay -clock clk  0  [get_ports {data_i[56]}]
set_input_delay -clock clk  0  [get_ports {data_i[55]}]
set_input_delay -clock clk  0  [get_ports {data_i[54]}]
set_input_delay -clock clk  0  [get_ports {data_i[53]}]
set_input_delay -clock clk  0  [get_ports {data_i[52]}]
set_input_delay -clock clk  0  [get_ports {data_i[51]}]
set_input_delay -clock clk  0  [get_ports {data_i[50]}]
set_input_delay -clock clk  0  [get_ports {data_i[49]}]
set_input_delay -clock clk  0  [get_ports {data_i[48]}]
set_input_delay -clock clk  0  [get_ports {data_i[47]}]
set_input_delay -clock clk  0  [get_ports {data_i[46]}]
set_input_delay -clock clk  0  [get_ports {data_i[45]}]
set_input_delay -clock clk  0  [get_ports {data_i[44]}]
set_input_delay -clock clk  0  [get_ports {data_i[43]}]
set_input_delay -clock clk  0  [get_ports {data_i[42]}]
set_input_delay -clock clk  0  [get_ports {data_i[41]}]
set_input_delay -clock clk  0  [get_ports {data_i[40]}]
set_input_delay -clock clk  0  [get_ports {data_i[39]}]
set_input_delay -clock clk  0  [get_ports {data_i[38]}]
set_input_delay -clock clk  0  [get_ports {data_i[37]}]
set_input_delay -clock clk  0  [get_ports {data_i[36]}]
set_input_delay -clock clk  0  [get_ports {data_i[35]}]
set_input_delay -clock clk  0  [get_ports {data_i[34]}]
set_input_delay -clock clk  0  [get_ports {data_i[33]}]
set_input_delay -clock clk  0  [get_ports {data_i[32]}]
set_input_delay -clock clk  0  [get_ports {data_i[31]}]
set_input_delay -clock clk  0  [get_ports {data_i[30]}]
set_input_delay -clock clk  0  [get_ports {data_i[29]}]
set_input_delay -clock clk  0  [get_ports {data_i[28]}]
set_input_delay -clock clk  0  [get_ports {data_i[27]}]
set_input_delay -clock clk  0  [get_ports {data_i[26]}]
set_input_delay -clock clk  0  [get_ports {data_i[25]}]
set_input_delay -clock clk  0  [get_ports {data_i[24]}]
set_input_delay -clock clk  0  [get_ports {data_i[23]}]
set_input_delay -clock clk  0  [get_ports {data_i[22]}]
set_input_delay -clock clk  0  [get_ports {data_i[21]}]
set_input_delay -clock clk  0  [get_ports {data_i[20]}]
set_input_delay -clock clk  0  [get_ports {data_i[19]}]
set_input_delay -clock clk  0  [get_ports {data_i[18]}]
set_input_delay -clock clk  0  [get_ports {data_i[17]}]
set_input_delay -clock clk  0  [get_ports {data_i[16]}]
set_input_delay -clock clk  0  [get_ports {data_i[15]}]
set_input_delay -clock clk  0  [get_ports {data_i[14]}]
set_input_delay -clock clk  0  [get_ports {data_i[13]}]
set_input_delay -clock clk  0  [get_ports {data_i[12]}]
set_input_delay -clock clk  0  [get_ports {data_i[11]}]
set_input_delay -clock clk  0  [get_ports {data_i[10]}]
set_input_delay -clock clk  0  [get_ports {data_i[9]}]
set_input_delay -clock clk  0  [get_ports {data_i[8]}]
set_input_delay -clock clk  0  [get_ports {data_i[7]}]
set_input_delay -clock clk  0  [get_ports {data_i[6]}]
set_input_delay -clock clk  0  [get_ports {data_i[5]}]
set_input_delay -clock clk  0  [get_ports {data_i[4]}]
set_input_delay -clock clk  0  [get_ports {data_i[3]}]
set_input_delay -clock clk  0  [get_ports {data_i[2]}]
set_input_delay -clock clk  0  [get_ports {data_i[1]}]
set_input_delay -clock clk  0  [get_ports {data_i[0]}]
set_input_delay -clock clk  0  [get_ports {key_i[63]}]
set_input_delay -clock clk  0  [get_ports {key_i[62]}]
set_input_delay -clock clk  0  [get_ports {key_i[61]}]
set_input_delay -clock clk  0  [get_ports {key_i[60]}]
set_input_delay -clock clk  0  [get_ports {key_i[59]}]
set_input_delay -clock clk  0  [get_ports {key_i[58]}]
set_input_delay -clock clk  0  [get_ports {key_i[57]}]
set_input_delay -clock clk  0  [get_ports {key_i[56]}]
set_input_delay -clock clk  0  [get_ports {key_i[55]}]
set_input_delay -clock clk  0  [get_ports {key_i[54]}]
set_input_delay -clock clk  0  [get_ports {key_i[53]}]
set_input_delay -clock clk  0  [get_ports {key_i[52]}]
set_input_delay -clock clk  0  [get_ports {key_i[51]}]
set_input_delay -clock clk  0  [get_ports {key_i[50]}]
set_input_delay -clock clk  0  [get_ports {key_i[49]}]
set_input_delay -clock clk  0  [get_ports {key_i[48]}]
set_input_delay -clock clk  0  [get_ports {key_i[47]}]
set_input_delay -clock clk  0  [get_ports {key_i[46]}]
set_input_delay -clock clk  0  [get_ports {key_i[45]}]
set_input_delay -clock clk  0  [get_ports {key_i[44]}]
set_input_delay -clock clk  0  [get_ports {key_i[43]}]
set_input_delay -clock clk  0  [get_ports {key_i[42]}]
set_input_delay -clock clk  0  [get_ports {key_i[41]}]
set_input_delay -clock clk  0  [get_ports {key_i[40]}]
set_input_delay -clock clk  0  [get_ports {key_i[39]}]
set_input_delay -clock clk  0  [get_ports {key_i[38]}]
set_input_delay -clock clk  0  [get_ports {key_i[37]}]
set_input_delay -clock clk  0  [get_ports {key_i[36]}]
set_input_delay -clock clk  0  [get_ports {key_i[35]}]
set_input_delay -clock clk  0  [get_ports {key_i[34]}]
set_input_delay -clock clk  0  [get_ports {key_i[33]}]
set_input_delay -clock clk  0  [get_ports {key_i[32]}]
set_input_delay -clock clk  0  [get_ports {key_i[31]}]
set_input_delay -clock clk  0  [get_ports {key_i[30]}]
set_input_delay -clock clk  0  [get_ports {key_i[29]}]
set_input_delay -clock clk  0  [get_ports {key_i[28]}]
set_input_delay -clock clk  0  [get_ports {key_i[27]}]
set_input_delay -clock clk  0  [get_ports {key_i[26]}]
set_input_delay -clock clk  0  [get_ports {key_i[25]}]
set_input_delay -clock clk  0  [get_ports {key_i[24]}]
set_input_delay -clock clk  0  [get_ports {key_i[23]}]
set_input_delay -clock clk  0  [get_ports {key_i[22]}]
set_input_delay -clock clk  0  [get_ports {key_i[21]}]
set_input_delay -clock clk  0  [get_ports {key_i[20]}]
set_input_delay -clock clk  0  [get_ports {key_i[19]}]
set_input_delay -clock clk  0  [get_ports {key_i[18]}]
set_input_delay -clock clk  0  [get_ports {key_i[17]}]
set_input_delay -clock clk  0  [get_ports {key_i[16]}]
set_input_delay -clock clk  0  [get_ports {key_i[15]}]
set_input_delay -clock clk  0  [get_ports {key_i[14]}]
set_input_delay -clock clk  0  [get_ports {key_i[13]}]
set_input_delay -clock clk  0  [get_ports {key_i[12]}]
set_input_delay -clock clk  0  [get_ports {key_i[11]}]
set_input_delay -clock clk  0  [get_ports {key_i[10]}]
set_input_delay -clock clk  0  [get_ports {key_i[9]}]
set_input_delay -clock clk  0  [get_ports {key_i[8]}]
set_input_delay -clock clk  0  [get_ports {key_i[7]}]
set_input_delay -clock clk  0  [get_ports {key_i[6]}]
set_input_delay -clock clk  0  [get_ports {key_i[5]}]
set_input_delay -clock clk  0  [get_ports {key_i[4]}]
set_input_delay -clock clk  0  [get_ports {key_i[3]}]
set_input_delay -clock clk  0  [get_ports {key_i[2]}]
set_input_delay -clock clk  0  [get_ports {key_i[1]}]
set_input_delay -clock clk  0  [get_ports {key_i[0]}]
set_output_delay -clock clk  0  [get_ports {data_o[63]}]
set_output_delay -clock clk  0  [get_ports {data_o[62]}]
set_output_delay -clock clk  0  [get_ports {data_o[61]}]
set_output_delay -clock clk  0  [get_ports {data_o[60]}]
set_output_delay -clock clk  0  [get_ports {data_o[59]}]
set_output_delay -clock clk  0  [get_ports {data_o[58]}]
set_output_delay -clock clk  0  [get_ports {data_o[57]}]
set_output_delay -clock clk  0  [get_ports {data_o[56]}]
set_output_delay -clock clk  0  [get_ports {data_o[55]}]
set_output_delay -clock clk  0  [get_ports {data_o[54]}]
set_output_delay -clock clk  0  [get_ports {data_o[53]}]
set_output_delay -clock clk  0  [get_ports {data_o[52]}]
set_output_delay -clock clk  0  [get_ports {data_o[51]}]
set_output_delay -clock clk  0  [get_ports {data_o[50]}]
set_output_delay -clock clk  0  [get_ports {data_o[49]}]
set_output_delay -clock clk  0  [get_ports {data_o[48]}]
set_output_delay -clock clk  0  [get_ports {data_o[47]}]
set_output_delay -clock clk  0  [get_ports {data_o[46]}]
set_output_delay -clock clk  0  [get_ports {data_o[45]}]
set_output_delay -clock clk  0  [get_ports {data_o[44]}]
set_output_delay -clock clk  0  [get_ports {data_o[43]}]
set_output_delay -clock clk  0  [get_ports {data_o[42]}]
set_output_delay -clock clk  0  [get_ports {data_o[41]}]
set_output_delay -clock clk  0  [get_ports {data_o[40]}]
set_output_delay -clock clk  0  [get_ports {data_o[39]}]
set_output_delay -clock clk  0  [get_ports {data_o[38]}]
set_output_delay -clock clk  0  [get_ports {data_o[37]}]
set_output_delay -clock clk  0  [get_ports {data_o[36]}]
set_output_delay -clock clk  0  [get_ports {data_o[35]}]
set_output_delay -clock clk  0  [get_ports {data_o[34]}]
set_output_delay -clock clk  0  [get_ports {data_o[33]}]
set_output_delay -clock clk  0  [get_ports {data_o[32]}]
set_output_delay -clock clk  0  [get_ports {data_o[31]}]
set_output_delay -clock clk  0  [get_ports {data_o[30]}]
set_output_delay -clock clk  0  [get_ports {data_o[29]}]
set_output_delay -clock clk  0  [get_ports {data_o[28]}]
set_output_delay -clock clk  0  [get_ports {data_o[27]}]
set_output_delay -clock clk  0  [get_ports {data_o[26]}]
set_output_delay -clock clk  0  [get_ports {data_o[25]}]
set_output_delay -clock clk  0  [get_ports {data_o[24]}]
set_output_delay -clock clk  0  [get_ports {data_o[23]}]
set_output_delay -clock clk  0  [get_ports {data_o[22]}]
set_output_delay -clock clk  0  [get_ports {data_o[21]}]
set_output_delay -clock clk  0  [get_ports {data_o[20]}]
set_output_delay -clock clk  0  [get_ports {data_o[19]}]
set_output_delay -clock clk  0  [get_ports {data_o[18]}]
set_output_delay -clock clk  0  [get_ports {data_o[17]}]
set_output_delay -clock clk  0  [get_ports {data_o[16]}]
set_output_delay -clock clk  0  [get_ports {data_o[15]}]
set_output_delay -clock clk  0  [get_ports {data_o[14]}]
set_output_delay -clock clk  0  [get_ports {data_o[13]}]
set_output_delay -clock clk  0  [get_ports {data_o[12]}]
set_output_delay -clock clk  0  [get_ports {data_o[11]}]
set_output_delay -clock clk  0  [get_ports {data_o[10]}]
set_output_delay -clock clk  0  [get_ports {data_o[9]}]
set_output_delay -clock clk  0  [get_ports {data_o[8]}]
set_output_delay -clock clk  0  [get_ports {data_o[7]}]
set_output_delay -clock clk  0  [get_ports {data_o[6]}]
set_output_delay -clock clk  0  [get_ports {data_o[5]}]
set_output_delay -clock clk  0  [get_ports {data_o[4]}]
set_output_delay -clock clk  0  [get_ports {data_o[3]}]
set_output_delay -clock clk  0  [get_ports {data_o[2]}]
set_output_delay -clock clk  0  [get_ports {data_o[1]}]
set_output_delay -clock clk  0  [get_ports {data_o[0]}]
set_output_delay -clock clk  0  [get_ports ready_o]
