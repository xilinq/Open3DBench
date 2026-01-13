###################################################################

# Created by write_sdc on Mon Dec 29 14:14:27 2025

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
group_path -name DFF  -from [list [get_cells digest_valid_reg_reg] [get_cells digest_reg_reg_0_]    \
[get_cells digest_reg_reg_1_] [get_cells digest_reg_reg_2_] [get_cells         \
digest_reg_reg_3_] [get_cells digest_reg_reg_4_] [get_cells digest_reg_reg_5_] \
[get_cells digest_reg_reg_6_] [get_cells digest_reg_reg_7_] [get_cells         \
digest_reg_reg_8_] [get_cells digest_reg_reg_9_] [get_cells                    \
digest_reg_reg_10_] [get_cells digest_reg_reg_11_] [get_cells                  \
digest_reg_reg_12_] [get_cells digest_reg_reg_13_] [get_cells                  \
digest_reg_reg_14_] [get_cells digest_reg_reg_15_] [get_cells                  \
digest_reg_reg_16_] [get_cells digest_reg_reg_17_] [get_cells                  \
digest_reg_reg_18_] [get_cells digest_reg_reg_19_] [get_cells                  \
digest_reg_reg_20_] [get_cells digest_reg_reg_21_] [get_cells                  \
digest_reg_reg_22_] [get_cells digest_reg_reg_23_] [get_cells                  \
digest_reg_reg_24_] [get_cells digest_reg_reg_25_] [get_cells                  \
digest_reg_reg_26_] [get_cells digest_reg_reg_27_] [get_cells                  \
digest_reg_reg_28_] [get_cells digest_reg_reg_29_] [get_cells                  \
digest_reg_reg_30_] [get_cells digest_reg_reg_31_] [get_cells                  \
digest_reg_reg_32_] [get_cells digest_reg_reg_33_] [get_cells                  \
digest_reg_reg_34_] [get_cells digest_reg_reg_35_] [get_cells                  \
digest_reg_reg_36_] [get_cells digest_reg_reg_37_] [get_cells                  \
digest_reg_reg_38_] [get_cells digest_reg_reg_39_] [get_cells                  \
digest_reg_reg_40_] [get_cells digest_reg_reg_41_] [get_cells                  \
digest_reg_reg_42_] [get_cells digest_reg_reg_43_] [get_cells                  \
digest_reg_reg_44_] [get_cells digest_reg_reg_45_] [get_cells                  \
digest_reg_reg_46_] [get_cells digest_reg_reg_47_] [get_cells                  \
digest_reg_reg_48_] [get_cells digest_reg_reg_49_] [get_cells                  \
digest_reg_reg_50_] [get_cells digest_reg_reg_51_] [get_cells                  \
digest_reg_reg_52_] [get_cells digest_reg_reg_53_] [get_cells                  \
digest_reg_reg_54_] [get_cells digest_reg_reg_55_] [get_cells                  \
digest_reg_reg_56_] [get_cells digest_reg_reg_57_] [get_cells                  \
digest_reg_reg_58_] [get_cells digest_reg_reg_59_] [get_cells                  \
digest_reg_reg_60_] [get_cells digest_reg_reg_61_] [get_cells                  \
digest_reg_reg_62_] [get_cells digest_reg_reg_63_] [get_cells                  \
digest_reg_reg_64_] [get_cells digest_reg_reg_65_] [get_cells                  \
digest_reg_reg_66_] [get_cells digest_reg_reg_67_] [get_cells                  \
digest_reg_reg_68_] [get_cells digest_reg_reg_69_] [get_cells                  \
digest_reg_reg_70_] [get_cells digest_reg_reg_71_] [get_cells                  \
digest_reg_reg_72_] [get_cells digest_reg_reg_73_] [get_cells                  \
digest_reg_reg_74_] [get_cells digest_reg_reg_75_] [get_cells                  \
digest_reg_reg_76_] [get_cells digest_reg_reg_77_] [get_cells                  \
digest_reg_reg_78_] [get_cells digest_reg_reg_79_] [get_cells                  \
digest_reg_reg_80_] [get_cells digest_reg_reg_81_] [get_cells                  \
digest_reg_reg_82_] [get_cells digest_reg_reg_83_] [get_cells                  \
digest_reg_reg_84_] [get_cells digest_reg_reg_85_] [get_cells                  \
digest_reg_reg_86_] [get_cells digest_reg_reg_87_] [get_cells                  \
digest_reg_reg_88_] [get_cells digest_reg_reg_89_] [get_cells                  \
digest_reg_reg_90_] [get_cells digest_reg_reg_91_] [get_cells                  \
digest_reg_reg_92_] [get_cells digest_reg_reg_93_] [get_cells                  \
digest_reg_reg_94_] [get_cells digest_reg_reg_95_] [get_cells                  \
digest_reg_reg_96_] [get_cells digest_reg_reg_97_] [get_cells                  \
digest_reg_reg_98_] [get_cells digest_reg_reg_99_] [get_cells                  \
digest_reg_reg_100_] [get_cells digest_reg_reg_101_] [get_cells                \
digest_reg_reg_102_] [get_cells digest_reg_reg_103_] [get_cells                \
digest_reg_reg_104_] [get_cells digest_reg_reg_105_] [get_cells                \
digest_reg_reg_106_] [get_cells digest_reg_reg_107_] [get_cells                \
digest_reg_reg_108_] [get_cells digest_reg_reg_109_] [get_cells                \
digest_reg_reg_110_] [get_cells digest_reg_reg_111_] [get_cells                \
digest_reg_reg_112_] [get_cells digest_reg_reg_113_] [get_cells                \
digest_reg_reg_114_] [get_cells digest_reg_reg_115_] [get_cells                \
digest_reg_reg_116_] [get_cells digest_reg_reg_117_] [get_cells                \
digest_reg_reg_118_] [get_cells digest_reg_reg_119_] [get_cells                \
digest_reg_reg_120_] [get_cells digest_reg_reg_121_] [get_cells                \
digest_reg_reg_122_] [get_cells digest_reg_reg_123_] [get_cells                \
digest_reg_reg_124_] [get_cells digest_reg_reg_125_] [get_cells                \
digest_reg_reg_126_] [get_cells digest_reg_reg_127_] [get_cells                \
digest_reg_reg_128_] [get_cells digest_reg_reg_129_] [get_cells                \
digest_reg_reg_130_] [get_cells digest_reg_reg_131_] [get_cells                \
digest_reg_reg_132_] [get_cells digest_reg_reg_133_] [get_cells                \
digest_reg_reg_134_] [get_cells digest_reg_reg_135_] [get_cells                \
digest_reg_reg_136_] [get_cells digest_reg_reg_137_] [get_cells                \
digest_reg_reg_138_] [get_cells digest_reg_reg_139_] [get_cells                \
digest_reg_reg_140_] [get_cells digest_reg_reg_141_] [get_cells                \
digest_reg_reg_142_] [get_cells digest_reg_reg_143_] [get_cells                \
digest_reg_reg_144_] [get_cells digest_reg_reg_145_] [get_cells                \
digest_reg_reg_146_] [get_cells digest_reg_reg_147_] [get_cells                \
digest_reg_reg_148_] [get_cells digest_reg_reg_149_] [get_cells                \
digest_reg_reg_150_] [get_cells digest_reg_reg_151_] [get_cells                \
digest_reg_reg_152_] [get_cells digest_reg_reg_153_] [get_cells                \
digest_reg_reg_154_] [get_cells digest_reg_reg_155_] [get_cells                \
digest_reg_reg_156_] [get_cells digest_reg_reg_157_] [get_cells                \
digest_reg_reg_158_] [get_cells digest_reg_reg_159_] [get_cells                \
digest_reg_reg_160_] [get_cells digest_reg_reg_161_] [get_cells                \
digest_reg_reg_162_] [get_cells digest_reg_reg_163_] [get_cells                \
digest_reg_reg_164_] [get_cells digest_reg_reg_165_] [get_cells                \
digest_reg_reg_166_] [get_cells digest_reg_reg_167_] [get_cells                \
digest_reg_reg_168_] [get_cells digest_reg_reg_169_] [get_cells                \
digest_reg_reg_170_] [get_cells digest_reg_reg_171_] [get_cells                \
digest_reg_reg_172_] [get_cells digest_reg_reg_173_] [get_cells                \
digest_reg_reg_174_] [get_cells digest_reg_reg_175_] [get_cells                \
digest_reg_reg_176_] [get_cells digest_reg_reg_177_] [get_cells                \
digest_reg_reg_178_] [get_cells digest_reg_reg_179_] [get_cells                \
digest_reg_reg_180_] [get_cells digest_reg_reg_181_] [get_cells                \
digest_reg_reg_182_] [get_cells digest_reg_reg_183_] [get_cells                \
digest_reg_reg_184_] [get_cells digest_reg_reg_185_] [get_cells                \
digest_reg_reg_186_] [get_cells digest_reg_reg_187_] [get_cells                \
digest_reg_reg_188_] [get_cells digest_reg_reg_189_] [get_cells                \
digest_reg_reg_190_] [get_cells digest_reg_reg_191_] [get_cells                \
digest_reg_reg_192_] [get_cells digest_reg_reg_193_] [get_cells                \
digest_reg_reg_194_] [get_cells digest_reg_reg_195_] [get_cells                \
digest_reg_reg_196_] [get_cells digest_reg_reg_197_] [get_cells                \
digest_reg_reg_198_] [get_cells digest_reg_reg_199_] [get_cells                \
digest_reg_reg_200_] [get_cells digest_reg_reg_201_] [get_cells                \
digest_reg_reg_202_] [get_cells digest_reg_reg_203_] [get_cells                \
digest_reg_reg_204_] [get_cells digest_reg_reg_205_] [get_cells                \
digest_reg_reg_206_] [get_cells digest_reg_reg_207_] [get_cells                \
digest_reg_reg_208_] [get_cells digest_reg_reg_209_] [get_cells                \
digest_reg_reg_210_] [get_cells digest_reg_reg_211_] [get_cells                \
digest_reg_reg_212_] [get_cells digest_reg_reg_213_] [get_cells                \
digest_reg_reg_214_] [get_cells digest_reg_reg_215_] [get_cells                \
digest_reg_reg_216_] [get_cells digest_reg_reg_217_] [get_cells                \
digest_reg_reg_218_] [get_cells digest_reg_reg_219_] [get_cells                \
digest_reg_reg_220_] [get_cells digest_reg_reg_221_] [get_cells                \
digest_reg_reg_222_] [get_cells digest_reg_reg_223_] [get_cells                \
digest_reg_reg_224_] [get_cells digest_reg_reg_225_] [get_cells                \
digest_reg_reg_226_] [get_cells digest_reg_reg_227_] [get_cells                \
digest_reg_reg_228_] [get_cells digest_reg_reg_229_] [get_cells                \
digest_reg_reg_230_] [get_cells digest_reg_reg_231_] [get_cells                \
digest_reg_reg_232_] [get_cells digest_reg_reg_233_] [get_cells                \
digest_reg_reg_234_] [get_cells digest_reg_reg_235_] [get_cells                \
digest_reg_reg_236_] [get_cells digest_reg_reg_237_] [get_cells                \
digest_reg_reg_238_] [get_cells digest_reg_reg_239_] [get_cells                \
digest_reg_reg_240_] [get_cells digest_reg_reg_241_] [get_cells                \
digest_reg_reg_242_] [get_cells digest_reg_reg_243_] [get_cells                \
digest_reg_reg_244_] [get_cells digest_reg_reg_245_] [get_cells                \
digest_reg_reg_246_] [get_cells digest_reg_reg_247_] [get_cells                \
digest_reg_reg_248_] [get_cells digest_reg_reg_249_] [get_cells                \
digest_reg_reg_250_] [get_cells digest_reg_reg_251_] [get_cells                \
digest_reg_reg_252_] [get_cells digest_reg_reg_253_] [get_cells                \
digest_reg_reg_254_] [get_cells digest_reg_reg_255_] [get_cells init_reg_reg]  \
[get_cells next_reg_reg] [get_cells mode_reg_reg] [get_cells ready_reg_reg]    \
[get_cells block_reg_reg_15__0_] [get_cells block_reg_reg_15__1_] [get_cells   \
block_reg_reg_15__2_] [get_cells block_reg_reg_15__3_] [get_cells              \
block_reg_reg_15__4_] [get_cells block_reg_reg_15__5_] [get_cells              \
block_reg_reg_15__6_] [get_cells block_reg_reg_15__7_] [get_cells              \
block_reg_reg_15__8_] [get_cells block_reg_reg_15__9_] [get_cells              \
block_reg_reg_15__10_] [get_cells block_reg_reg_15__11_] [get_cells            \
block_reg_reg_15__12_] [get_cells block_reg_reg_15__13_] [get_cells            \
block_reg_reg_15__14_] [get_cells block_reg_reg_15__15_] [get_cells            \
block_reg_reg_15__16_] [get_cells block_reg_reg_15__17_] [get_cells            \
block_reg_reg_15__18_] [get_cells block_reg_reg_15__19_] [get_cells            \
block_reg_reg_15__20_] [get_cells block_reg_reg_15__21_] [get_cells            \
block_reg_reg_15__22_] [get_cells block_reg_reg_15__23_] [get_cells            \
block_reg_reg_15__24_] [get_cells block_reg_reg_15__25_] [get_cells            \
block_reg_reg_15__26_] [get_cells block_reg_reg_15__27_] [get_cells            \
block_reg_reg_15__28_] [get_cells block_reg_reg_15__29_] [get_cells            \
block_reg_reg_15__30_] [get_cells block_reg_reg_15__31_] [get_cells            \
block_reg_reg_14__0_] [get_cells block_reg_reg_14__1_] [get_cells              \
block_reg_reg_14__2_] [get_cells block_reg_reg_14__3_] [get_cells              \
block_reg_reg_14__4_] [get_cells block_reg_reg_14__5_] [get_cells              \
block_reg_reg_14__6_] [get_cells block_reg_reg_14__7_] [get_cells              \
block_reg_reg_14__8_] [get_cells block_reg_reg_14__9_] [get_cells              \
block_reg_reg_14__10_] [get_cells block_reg_reg_14__11_] [get_cells            \
block_reg_reg_14__12_] [get_cells block_reg_reg_14__13_] [get_cells            \
block_reg_reg_14__14_] [get_cells block_reg_reg_14__15_] [get_cells            \
block_reg_reg_14__16_] [get_cells block_reg_reg_14__17_] [get_cells            \
block_reg_reg_14__18_] [get_cells block_reg_reg_14__19_] [get_cells            \
block_reg_reg_14__20_] [get_cells block_reg_reg_14__21_] [get_cells            \
block_reg_reg_14__22_] [get_cells block_reg_reg_14__23_] [get_cells            \
block_reg_reg_14__24_] [get_cells block_reg_reg_14__25_] [get_cells            \
block_reg_reg_14__26_] [get_cells block_reg_reg_14__27_] [get_cells            \
block_reg_reg_14__28_] [get_cells block_reg_reg_14__29_] [get_cells            \
block_reg_reg_14__30_] [get_cells block_reg_reg_14__31_] [get_cells            \
block_reg_reg_13__0_] [get_cells block_reg_reg_13__1_] [get_cells              \
block_reg_reg_13__2_] [get_cells block_reg_reg_13__3_] [get_cells              \
block_reg_reg_13__4_] [get_cells block_reg_reg_13__5_] [get_cells              \
block_reg_reg_13__6_] [get_cells block_reg_reg_13__7_] [get_cells              \
block_reg_reg_13__8_] [get_cells block_reg_reg_13__9_] [get_cells              \
block_reg_reg_13__10_] [get_cells block_reg_reg_13__11_] [get_cells            \
block_reg_reg_13__12_] [get_cells block_reg_reg_13__13_] [get_cells            \
block_reg_reg_13__14_] [get_cells block_reg_reg_13__15_] [get_cells            \
block_reg_reg_13__16_] [get_cells block_reg_reg_13__17_] [get_cells            \
block_reg_reg_13__18_] [get_cells block_reg_reg_13__19_] [get_cells            \
block_reg_reg_13__20_] [get_cells block_reg_reg_13__21_] [get_cells            \
block_reg_reg_13__22_] [get_cells block_reg_reg_13__23_] [get_cells            \
block_reg_reg_13__24_] [get_cells block_reg_reg_13__25_] [get_cells            \
block_reg_reg_13__26_] [get_cells block_reg_reg_13__27_] [get_cells            \
block_reg_reg_13__28_] [get_cells block_reg_reg_13__29_] [get_cells            \
block_reg_reg_13__30_] [get_cells block_reg_reg_13__31_] [get_cells            \
block_reg_reg_12__0_] [get_cells block_reg_reg_12__1_] [get_cells              \
block_reg_reg_12__2_] [get_cells block_reg_reg_12__3_] [get_cells              \
block_reg_reg_12__4_] [get_cells block_reg_reg_12__5_] [get_cells              \
block_reg_reg_12__6_] [get_cells block_reg_reg_12__7_] [get_cells              \
block_reg_reg_12__8_] [get_cells block_reg_reg_12__9_] [get_cells              \
block_reg_reg_12__10_] [get_cells block_reg_reg_12__11_] [get_cells            \
block_reg_reg_12__12_] [get_cells block_reg_reg_12__13_] [get_cells            \
block_reg_reg_12__14_] [get_cells block_reg_reg_12__15_] [get_cells            \
block_reg_reg_12__16_] [get_cells block_reg_reg_12__17_] [get_cells            \
block_reg_reg_12__18_] [get_cells block_reg_reg_12__19_] [get_cells            \
block_reg_reg_12__20_] [get_cells block_reg_reg_12__21_] [get_cells            \
block_reg_reg_12__22_] [get_cells block_reg_reg_12__23_] [get_cells            \
block_reg_reg_12__24_] [get_cells block_reg_reg_12__25_] [get_cells            \
block_reg_reg_12__26_] [get_cells block_reg_reg_12__27_] [get_cells            \
block_reg_reg_12__28_] [get_cells block_reg_reg_12__29_] [get_cells            \
block_reg_reg_12__30_] [get_cells block_reg_reg_12__31_] [get_cells            \
block_reg_reg_11__0_] [get_cells block_reg_reg_11__1_] [get_cells              \
block_reg_reg_11__2_] [get_cells block_reg_reg_11__3_] [get_cells              \
block_reg_reg_11__4_] [get_cells block_reg_reg_11__5_] [get_cells              \
block_reg_reg_11__6_] [get_cells block_reg_reg_11__7_] [get_cells              \
block_reg_reg_11__8_] [get_cells block_reg_reg_11__9_] [get_cells              \
block_reg_reg_11__10_] [get_cells block_reg_reg_11__11_] [get_cells            \
block_reg_reg_11__12_] [get_cells block_reg_reg_11__13_] [get_cells            \
block_reg_reg_11__14_] [get_cells block_reg_reg_11__15_] [get_cells            \
block_reg_reg_11__16_] [get_cells block_reg_reg_11__17_] [get_cells            \
block_reg_reg_11__18_] [get_cells block_reg_reg_11__19_] [get_cells            \
block_reg_reg_11__20_] [get_cells block_reg_reg_11__21_] [get_cells            \
block_reg_reg_11__22_] [get_cells block_reg_reg_11__23_] [get_cells            \
block_reg_reg_11__24_] [get_cells block_reg_reg_11__25_] [get_cells            \
block_reg_reg_11__26_] [get_cells block_reg_reg_11__27_] [get_cells            \
block_reg_reg_11__28_] [get_cells block_reg_reg_11__29_] [get_cells            \
block_reg_reg_11__30_] [get_cells block_reg_reg_11__31_] [get_cells            \
block_reg_reg_10__0_] [get_cells block_reg_reg_10__1_] [get_cells              \
block_reg_reg_10__2_] [get_cells block_reg_reg_10__3_] [get_cells              \
block_reg_reg_10__4_] [get_cells block_reg_reg_10__5_] [get_cells              \
block_reg_reg_10__6_] [get_cells block_reg_reg_10__7_] [get_cells              \
block_reg_reg_10__8_] [get_cells block_reg_reg_10__9_] [get_cells              \
block_reg_reg_10__10_] [get_cells block_reg_reg_10__11_] [get_cells            \
block_reg_reg_10__12_] [get_cells block_reg_reg_10__13_] [get_cells            \
block_reg_reg_10__14_] [get_cells block_reg_reg_10__15_] [get_cells            \
block_reg_reg_10__16_] [get_cells block_reg_reg_10__17_] [get_cells            \
block_reg_reg_10__18_] [get_cells block_reg_reg_10__19_] [get_cells            \
block_reg_reg_10__20_] [get_cells block_reg_reg_10__21_] [get_cells            \
block_reg_reg_10__22_] [get_cells block_reg_reg_10__23_] [get_cells            \
block_reg_reg_10__24_] [get_cells block_reg_reg_10__25_] [get_cells            \
block_reg_reg_10__26_] [get_cells block_reg_reg_10__27_] [get_cells            \
block_reg_reg_10__28_] [get_cells block_reg_reg_10__29_] [get_cells            \
block_reg_reg_10__30_] [get_cells block_reg_reg_10__31_] [get_cells            \
block_reg_reg_9__0_] [get_cells block_reg_reg_9__1_] [get_cells                \
block_reg_reg_9__2_] [get_cells block_reg_reg_9__3_] [get_cells                \
block_reg_reg_9__4_] [get_cells block_reg_reg_9__5_] [get_cells                \
block_reg_reg_9__6_] [get_cells block_reg_reg_9__7_] [get_cells                \
block_reg_reg_9__8_] [get_cells block_reg_reg_9__9_] [get_cells                \
block_reg_reg_9__10_] [get_cells block_reg_reg_9__11_] [get_cells              \
block_reg_reg_9__12_] [get_cells block_reg_reg_9__13_] [get_cells              \
block_reg_reg_9__14_] [get_cells block_reg_reg_9__15_] [get_cells              \
block_reg_reg_9__16_] [get_cells block_reg_reg_9__17_] [get_cells              \
block_reg_reg_9__18_] [get_cells block_reg_reg_9__19_] [get_cells              \
block_reg_reg_9__20_] [get_cells block_reg_reg_9__21_] [get_cells              \
block_reg_reg_9__22_] [get_cells block_reg_reg_9__23_] [get_cells              \
block_reg_reg_9__24_] [get_cells block_reg_reg_9__25_] [get_cells              \
block_reg_reg_9__26_] [get_cells block_reg_reg_9__27_] [get_cells              \
block_reg_reg_9__28_] [get_cells block_reg_reg_9__29_] [get_cells              \
block_reg_reg_9__30_] [get_cells block_reg_reg_9__31_] [get_cells              \
block_reg_reg_8__0_] [get_cells block_reg_reg_8__1_] [get_cells                \
block_reg_reg_8__2_] [get_cells block_reg_reg_8__3_] [get_cells                \
block_reg_reg_8__4_] [get_cells block_reg_reg_8__5_] [get_cells                \
block_reg_reg_8__6_] [get_cells block_reg_reg_8__7_] [get_cells                \
block_reg_reg_8__8_] [get_cells block_reg_reg_8__9_] [get_cells                \
block_reg_reg_8__10_] [get_cells block_reg_reg_8__11_] [get_cells              \
block_reg_reg_8__12_] [get_cells block_reg_reg_8__13_] [get_cells              \
block_reg_reg_8__14_] [get_cells block_reg_reg_8__15_] [get_cells              \
block_reg_reg_8__16_] [get_cells block_reg_reg_8__17_] [get_cells              \
block_reg_reg_8__18_] [get_cells block_reg_reg_8__19_] [get_cells              \
block_reg_reg_8__20_] [get_cells block_reg_reg_8__21_] [get_cells              \
block_reg_reg_8__22_] [get_cells block_reg_reg_8__23_] [get_cells              \
block_reg_reg_8__24_] [get_cells block_reg_reg_8__25_] [get_cells              \
block_reg_reg_8__26_] [get_cells block_reg_reg_8__27_] [get_cells              \
block_reg_reg_8__28_] [get_cells block_reg_reg_8__29_] [get_cells              \
block_reg_reg_8__30_] [get_cells block_reg_reg_8__31_] [get_cells              \
block_reg_reg_7__0_] [get_cells block_reg_reg_7__1_] [get_cells                \
block_reg_reg_7__2_] [get_cells block_reg_reg_7__3_] [get_cells                \
block_reg_reg_7__4_] [get_cells block_reg_reg_7__5_] [get_cells                \
block_reg_reg_7__6_] [get_cells block_reg_reg_7__7_] [get_cells                \
block_reg_reg_7__8_] [get_cells block_reg_reg_7__9_] [get_cells                \
block_reg_reg_7__10_] [get_cells block_reg_reg_7__11_] [get_cells              \
block_reg_reg_7__12_] [get_cells block_reg_reg_7__13_] [get_cells              \
block_reg_reg_7__14_] [get_cells block_reg_reg_7__15_] [get_cells              \
block_reg_reg_7__16_] [get_cells block_reg_reg_7__17_] [get_cells              \
block_reg_reg_7__18_] [get_cells block_reg_reg_7__19_] [get_cells              \
block_reg_reg_7__20_] [get_cells block_reg_reg_7__21_] [get_cells              \
block_reg_reg_7__22_] [get_cells block_reg_reg_7__23_] [get_cells              \
block_reg_reg_7__24_] [get_cells block_reg_reg_7__25_] [get_cells              \
block_reg_reg_7__26_] [get_cells block_reg_reg_7__27_] [get_cells              \
block_reg_reg_7__28_] [get_cells block_reg_reg_7__29_] [get_cells              \
block_reg_reg_7__30_] [get_cells block_reg_reg_7__31_] [get_cells              \
block_reg_reg_6__0_] [get_cells block_reg_reg_6__1_] [get_cells                \
block_reg_reg_6__2_] [get_cells block_reg_reg_6__3_] [get_cells                \
block_reg_reg_6__4_] [get_cells block_reg_reg_6__5_] [get_cells                \
block_reg_reg_6__6_] [get_cells block_reg_reg_6__7_] [get_cells                \
block_reg_reg_6__8_] [get_cells block_reg_reg_6__9_] [get_cells                \
block_reg_reg_6__10_] [get_cells block_reg_reg_6__11_] [get_cells              \
block_reg_reg_6__12_] [get_cells block_reg_reg_6__13_] [get_cells              \
block_reg_reg_6__14_] [get_cells block_reg_reg_6__15_] [get_cells              \
block_reg_reg_6__16_] [get_cells block_reg_reg_6__17_] [get_cells              \
block_reg_reg_6__18_] [get_cells block_reg_reg_6__19_] [get_cells              \
block_reg_reg_6__20_] [get_cells block_reg_reg_6__21_] [get_cells              \
block_reg_reg_6__22_] [get_cells block_reg_reg_6__23_] [get_cells              \
block_reg_reg_6__24_] [get_cells block_reg_reg_6__25_] [get_cells              \
block_reg_reg_6__26_] [get_cells block_reg_reg_6__27_] [get_cells              \
block_reg_reg_6__28_] [get_cells block_reg_reg_6__29_] [get_cells              \
block_reg_reg_6__30_] [get_cells block_reg_reg_6__31_] [get_cells              \
block_reg_reg_5__0_] [get_cells block_reg_reg_5__1_] [get_cells                \
block_reg_reg_5__2_] [get_cells block_reg_reg_5__3_] [get_cells                \
block_reg_reg_5__4_] [get_cells block_reg_reg_5__5_] [get_cells                \
block_reg_reg_5__6_] [get_cells block_reg_reg_5__7_] [get_cells                \
block_reg_reg_5__8_] [get_cells block_reg_reg_5__9_] [get_cells                \
block_reg_reg_5__10_] [get_cells block_reg_reg_5__11_] [get_cells              \
block_reg_reg_5__12_] [get_cells block_reg_reg_5__13_] [get_cells              \
block_reg_reg_5__14_] [get_cells block_reg_reg_5__15_] [get_cells              \
block_reg_reg_5__16_] [get_cells block_reg_reg_5__17_] [get_cells              \
block_reg_reg_5__18_] [get_cells block_reg_reg_5__19_] [get_cells              \
block_reg_reg_5__20_] [get_cells block_reg_reg_5__21_] [get_cells              \
block_reg_reg_5__22_] [get_cells block_reg_reg_5__23_] [get_cells              \
block_reg_reg_5__24_] [get_cells block_reg_reg_5__25_] [get_cells              \
block_reg_reg_5__26_] [get_cells block_reg_reg_5__27_] [get_cells              \
block_reg_reg_5__28_] [get_cells block_reg_reg_5__29_] [get_cells              \
block_reg_reg_5__30_] [get_cells block_reg_reg_5__31_] [get_cells              \
block_reg_reg_4__0_] [get_cells block_reg_reg_4__1_] [get_cells                \
block_reg_reg_4__2_] [get_cells block_reg_reg_4__3_] [get_cells                \
block_reg_reg_4__4_] [get_cells block_reg_reg_4__5_] [get_cells                \
block_reg_reg_4__6_] [get_cells block_reg_reg_4__7_] [get_cells                \
block_reg_reg_4__8_] [get_cells block_reg_reg_4__9_] [get_cells                \
block_reg_reg_4__10_] [get_cells block_reg_reg_4__11_] [get_cells              \
block_reg_reg_4__12_] [get_cells block_reg_reg_4__13_] [get_cells              \
block_reg_reg_4__14_] [get_cells block_reg_reg_4__15_] [get_cells              \
block_reg_reg_4__16_] [get_cells block_reg_reg_4__17_] [get_cells              \
block_reg_reg_4__18_] [get_cells block_reg_reg_4__19_] [get_cells              \
block_reg_reg_4__20_] [get_cells block_reg_reg_4__21_] [get_cells              \
block_reg_reg_4__22_] [get_cells block_reg_reg_4__23_] [get_cells              \
block_reg_reg_4__24_] [get_cells block_reg_reg_4__25_] [get_cells              \
block_reg_reg_4__26_] [get_cells block_reg_reg_4__27_] [get_cells              \
block_reg_reg_4__28_] [get_cells block_reg_reg_4__29_] [get_cells              \
block_reg_reg_4__30_] [get_cells block_reg_reg_4__31_] [get_cells              \
block_reg_reg_3__0_] [get_cells block_reg_reg_3__1_] [get_cells                \
block_reg_reg_3__2_] [get_cells block_reg_reg_3__3_] [get_cells                \
block_reg_reg_3__4_] [get_cells block_reg_reg_3__5_] [get_cells                \
block_reg_reg_3__6_] [get_cells block_reg_reg_3__7_] [get_cells                \
block_reg_reg_3__8_] [get_cells block_reg_reg_3__9_] [get_cells                \
block_reg_reg_3__10_] [get_cells block_reg_reg_3__11_] [get_cells              \
block_reg_reg_3__12_] [get_cells block_reg_reg_3__13_] [get_cells              \
block_reg_reg_3__14_] [get_cells block_reg_reg_3__15_] [get_cells              \
block_reg_reg_3__16_] [get_cells block_reg_reg_3__17_] [get_cells              \
block_reg_reg_3__18_] [get_cells block_reg_reg_3__19_] [get_cells              \
block_reg_reg_3__20_] [get_cells block_reg_reg_3__21_] [get_cells              \
block_reg_reg_3__22_] [get_cells block_reg_reg_3__23_] [get_cells              \
block_reg_reg_3__24_] [get_cells block_reg_reg_3__25_] [get_cells              \
block_reg_reg_3__26_] [get_cells block_reg_reg_3__27_] [get_cells              \
block_reg_reg_3__28_] [get_cells block_reg_reg_3__29_] [get_cells              \
block_reg_reg_3__30_] [get_cells block_reg_reg_3__31_] [get_cells              \
block_reg_reg_2__0_] [get_cells block_reg_reg_2__1_] [get_cells                \
block_reg_reg_2__2_] [get_cells block_reg_reg_2__3_] [get_cells                \
block_reg_reg_2__4_] [get_cells block_reg_reg_2__5_] [get_cells                \
block_reg_reg_2__6_] [get_cells block_reg_reg_2__7_] [get_cells                \
block_reg_reg_2__8_] [get_cells block_reg_reg_2__9_] [get_cells                \
block_reg_reg_2__10_] [get_cells block_reg_reg_2__11_] [get_cells              \
block_reg_reg_2__12_] [get_cells block_reg_reg_2__13_] [get_cells              \
block_reg_reg_2__14_] [get_cells block_reg_reg_2__15_] [get_cells              \
block_reg_reg_2__16_] [get_cells block_reg_reg_2__17_] [get_cells              \
block_reg_reg_2__18_] [get_cells block_reg_reg_2__19_] [get_cells              \
block_reg_reg_2__20_] [get_cells block_reg_reg_2__21_] [get_cells              \
block_reg_reg_2__22_] [get_cells block_reg_reg_2__23_] [get_cells              \
block_reg_reg_2__24_] [get_cells block_reg_reg_2__25_] [get_cells              \
block_reg_reg_2__26_] [get_cells block_reg_reg_2__27_] [get_cells              \
block_reg_reg_2__28_] [get_cells block_reg_reg_2__29_] [get_cells              \
block_reg_reg_2__30_] [get_cells block_reg_reg_2__31_] [get_cells              \
block_reg_reg_1__0_] [get_cells block_reg_reg_1__1_] [get_cells                \
block_reg_reg_1__2_] [get_cells block_reg_reg_1__3_] [get_cells                \
block_reg_reg_1__4_] [get_cells block_reg_reg_1__5_] [get_cells                \
block_reg_reg_1__6_] [get_cells block_reg_reg_1__7_] [get_cells                \
block_reg_reg_1__8_] [get_cells block_reg_reg_1__9_] [get_cells                \
block_reg_reg_1__10_] [get_cells block_reg_reg_1__11_] [get_cells              \
block_reg_reg_1__12_] [get_cells block_reg_reg_1__13_] [get_cells              \
block_reg_reg_1__14_] [get_cells block_reg_reg_1__15_] [get_cells              \
block_reg_reg_1__16_] [get_cells block_reg_reg_1__17_] [get_cells              \
block_reg_reg_1__18_] [get_cells block_reg_reg_1__19_] [get_cells              \
block_reg_reg_1__20_] [get_cells block_reg_reg_1__21_] [get_cells              \
block_reg_reg_1__22_] [get_cells block_reg_reg_1__23_] [get_cells              \
block_reg_reg_1__24_] [get_cells block_reg_reg_1__25_] [get_cells              \
block_reg_reg_1__26_] [get_cells block_reg_reg_1__27_] [get_cells              \
block_reg_reg_1__28_] [get_cells block_reg_reg_1__29_] [get_cells              \
block_reg_reg_1__30_] [get_cells block_reg_reg_1__31_] [get_cells              \
block_reg_reg_0__0_] [get_cells block_reg_reg_0__1_] [get_cells                \
block_reg_reg_0__2_] [get_cells block_reg_reg_0__3_] [get_cells                \
block_reg_reg_0__4_] [get_cells block_reg_reg_0__5_] [get_cells                \
block_reg_reg_0__6_] [get_cells block_reg_reg_0__7_] [get_cells                \
block_reg_reg_0__8_] [get_cells block_reg_reg_0__9_] [get_cells                \
block_reg_reg_0__10_] [get_cells block_reg_reg_0__11_] [get_cells              \
block_reg_reg_0__12_] [get_cells block_reg_reg_0__13_] [get_cells              \
block_reg_reg_0__14_] [get_cells block_reg_reg_0__15_] [get_cells              \
block_reg_reg_0__16_] [get_cells block_reg_reg_0__17_] [get_cells              \
block_reg_reg_0__18_] [get_cells block_reg_reg_0__19_] [get_cells              \
block_reg_reg_0__20_] [get_cells block_reg_reg_0__21_] [get_cells              \
block_reg_reg_0__22_] [get_cells block_reg_reg_0__23_] [get_cells              \
block_reg_reg_0__24_] [get_cells block_reg_reg_0__25_] [get_cells              \
block_reg_reg_0__26_] [get_cells block_reg_reg_0__27_] [get_cells              \
block_reg_reg_0__28_] [get_cells block_reg_reg_0__29_] [get_cells              \
block_reg_reg_0__30_] [get_cells block_reg_reg_0__31_] [get_cells              \
core_H3_reg_reg_0_] [get_cells core_H3_reg_reg_1_] [get_cells                  \
core_H3_reg_reg_2_] [get_cells core_H3_reg_reg_3_] [get_cells                  \
core_H3_reg_reg_4_] [get_cells core_H3_reg_reg_5_] [get_cells                  \
core_H3_reg_reg_6_] [get_cells core_H3_reg_reg_7_] [get_cells                  \
core_H3_reg_reg_8_] [get_cells core_H3_reg_reg_9_] [get_cells                  \
core_H3_reg_reg_10_] [get_cells core_H3_reg_reg_11_] [get_cells                \
core_H3_reg_reg_12_] [get_cells core_H3_reg_reg_13_] [get_cells                \
core_H3_reg_reg_14_] [get_cells core_H3_reg_reg_15_] [get_cells                \
core_H3_reg_reg_16_] [get_cells core_H3_reg_reg_17_] [get_cells                \
core_H3_reg_reg_18_] [get_cells core_H3_reg_reg_19_] [get_cells                \
core_H3_reg_reg_20_] [get_cells core_H3_reg_reg_21_] [get_cells                \
core_H3_reg_reg_22_] [get_cells core_H3_reg_reg_23_] [get_cells                \
core_H3_reg_reg_24_] [get_cells core_H3_reg_reg_25_] [get_cells                \
core_H3_reg_reg_26_] [get_cells core_H3_reg_reg_27_] [get_cells                \
core_H3_reg_reg_28_] [get_cells core_H3_reg_reg_29_] [get_cells                \
core_H3_reg_reg_30_] [get_cells core_H3_reg_reg_31_] [get_cells                \
core_H2_reg_reg_0_] [get_cells core_H2_reg_reg_1_] [get_cells                  \
core_H2_reg_reg_2_] [get_cells core_H2_reg_reg_3_] [get_cells                  \
core_H2_reg_reg_4_] [get_cells core_H2_reg_reg_5_] [get_cells                  \
core_H2_reg_reg_6_] [get_cells core_H2_reg_reg_7_] [get_cells                  \
core_H2_reg_reg_8_] [get_cells core_H2_reg_reg_9_] [get_cells                  \
core_H2_reg_reg_10_] [get_cells core_H2_reg_reg_11_] [get_cells                \
core_H2_reg_reg_12_] [get_cells core_H2_reg_reg_13_] [get_cells                \
core_H2_reg_reg_14_] [get_cells core_H2_reg_reg_15_] [get_cells                \
core_H2_reg_reg_16_] [get_cells core_H2_reg_reg_17_] [get_cells                \
core_H2_reg_reg_18_] [get_cells core_H2_reg_reg_19_] [get_cells                \
core_H2_reg_reg_20_] [get_cells core_H2_reg_reg_21_] [get_cells                \
core_H2_reg_reg_22_] [get_cells core_H2_reg_reg_23_] [get_cells                \
core_H2_reg_reg_24_] [get_cells core_H2_reg_reg_25_] [get_cells                \
core_H2_reg_reg_26_] [get_cells core_H2_reg_reg_27_] [get_cells                \
core_H2_reg_reg_28_] [get_cells core_H2_reg_reg_29_] [get_cells                \
core_H2_reg_reg_30_] [get_cells core_H2_reg_reg_31_] [get_cells                \
core_H1_reg_reg_0_] [get_cells core_H1_reg_reg_1_] [get_cells                  \
core_H1_reg_reg_2_] [get_cells core_H1_reg_reg_3_] [get_cells                  \
core_H1_reg_reg_4_] [get_cells core_H1_reg_reg_5_] [get_cells                  \
core_H1_reg_reg_6_] [get_cells core_H1_reg_reg_7_] [get_cells                  \
core_H1_reg_reg_8_] [get_cells core_H1_reg_reg_9_] [get_cells                  \
core_H1_reg_reg_10_] [get_cells core_H1_reg_reg_11_] [get_cells                \
core_H1_reg_reg_12_] [get_cells core_H1_reg_reg_13_] [get_cells                \
core_H1_reg_reg_14_] [get_cells core_H1_reg_reg_15_] [get_cells                \
core_H1_reg_reg_16_] [get_cells core_H1_reg_reg_17_] [get_cells                \
core_H1_reg_reg_18_] [get_cells core_H1_reg_reg_19_] [get_cells                \
core_H1_reg_reg_20_] [get_cells core_H1_reg_reg_21_] [get_cells                \
core_H1_reg_reg_22_] [get_cells core_H1_reg_reg_23_] [get_cells                \
core_H1_reg_reg_24_] [get_cells core_H1_reg_reg_25_] [get_cells                \
core_H1_reg_reg_26_] [get_cells core_H1_reg_reg_27_] [get_cells                \
core_H1_reg_reg_28_] [get_cells core_H1_reg_reg_29_] [get_cells                \
core_H1_reg_reg_30_] [get_cells core_H1_reg_reg_31_] [get_cells                \
core_H0_reg_reg_0_] [get_cells core_H0_reg_reg_1_] [get_cells                  \
core_H0_reg_reg_2_] [get_cells core_H0_reg_reg_3_] [get_cells                  \
core_H0_reg_reg_4_] [get_cells core_H0_reg_reg_5_] [get_cells                  \
core_H0_reg_reg_6_] [get_cells core_H0_reg_reg_7_] [get_cells                  \
core_H0_reg_reg_8_] [get_cells core_H0_reg_reg_9_] [get_cells                  \
core_H0_reg_reg_10_] [get_cells core_H0_reg_reg_11_] [get_cells                \
core_H0_reg_reg_12_] [get_cells core_H0_reg_reg_13_] [get_cells                \
core_H0_reg_reg_14_] [get_cells core_H0_reg_reg_15_] [get_cells                \
core_H0_reg_reg_16_] [get_cells core_H0_reg_reg_17_] [get_cells                \
core_H0_reg_reg_18_] [get_cells core_H0_reg_reg_19_] [get_cells                \
core_H0_reg_reg_20_] [get_cells core_H0_reg_reg_21_] [get_cells                \
core_H0_reg_reg_22_] [get_cells core_H0_reg_reg_23_] [get_cells                \
core_H0_reg_reg_24_] [get_cells core_H0_reg_reg_25_] [get_cells                \
core_H0_reg_reg_26_] [get_cells core_H0_reg_reg_27_] [get_cells                \
core_H0_reg_reg_28_] [get_cells core_H0_reg_reg_29_] [get_cells                \
core_H0_reg_reg_30_] [get_cells core_H0_reg_reg_31_] [get_cells                \
core_h_reg_reg_0_] [get_cells core_h_reg_reg_1_] [get_cells core_h_reg_reg_2_] \
[get_cells core_h_reg_reg_3_] [get_cells core_h_reg_reg_4_] [get_cells         \
core_h_reg_reg_5_] [get_cells core_h_reg_reg_6_] [get_cells core_h_reg_reg_7_] \
[get_cells core_h_reg_reg_8_] [get_cells core_h_reg_reg_9_] [get_cells         \
core_h_reg_reg_10_] [get_cells core_h_reg_reg_11_] [get_cells                  \
core_h_reg_reg_12_] [get_cells core_h_reg_reg_13_] [get_cells                  \
core_h_reg_reg_14_] [get_cells core_h_reg_reg_15_] [get_cells                  \
core_h_reg_reg_16_] [get_cells core_h_reg_reg_17_] [get_cells                  \
core_h_reg_reg_18_] [get_cells core_h_reg_reg_19_] [get_cells                  \
core_h_reg_reg_20_] [get_cells core_h_reg_reg_21_] [get_cells                  \
core_h_reg_reg_22_] [get_cells core_h_reg_reg_23_] [get_cells                  \
core_h_reg_reg_24_] [get_cells core_h_reg_reg_25_] [get_cells                  \
core_h_reg_reg_26_] [get_cells core_h_reg_reg_27_] [get_cells                  \
core_h_reg_reg_28_] [get_cells core_h_reg_reg_29_] [get_cells                  \
core_h_reg_reg_30_] [get_cells core_h_reg_reg_31_] [get_cells                  \
core_g_reg_reg_0_] [get_cells core_g_reg_reg_1_] [get_cells core_g_reg_reg_2_] \
[get_cells core_g_reg_reg_3_] [get_cells core_g_reg_reg_4_] [get_cells         \
core_g_reg_reg_5_] [get_cells core_g_reg_reg_6_] [get_cells core_g_reg_reg_7_] \
[get_cells core_g_reg_reg_8_] [get_cells core_g_reg_reg_9_] [get_cells         \
core_g_reg_reg_10_] [get_cells core_g_reg_reg_11_] [get_cells                  \
core_g_reg_reg_12_] [get_cells core_g_reg_reg_13_] [get_cells                  \
core_g_reg_reg_14_] [get_cells core_g_reg_reg_15_] [get_cells                  \
core_g_reg_reg_16_] [get_cells core_g_reg_reg_17_] [get_cells                  \
core_g_reg_reg_18_] [get_cells core_g_reg_reg_19_] [get_cells                  \
core_g_reg_reg_20_] [get_cells core_g_reg_reg_21_] [get_cells                  \
core_g_reg_reg_22_] [get_cells core_g_reg_reg_23_] [get_cells                  \
core_g_reg_reg_24_] [get_cells core_g_reg_reg_25_] [get_cells                  \
core_g_reg_reg_26_] [get_cells core_g_reg_reg_27_] [get_cells                  \
core_g_reg_reg_28_] [get_cells core_g_reg_reg_29_] [get_cells                  \
core_g_reg_reg_30_] [get_cells core_g_reg_reg_31_] [get_cells                  \
core_f_reg_reg_0_] [get_cells core_f_reg_reg_1_] [get_cells core_f_reg_reg_2_] \
[get_cells core_f_reg_reg_3_] [get_cells core_f_reg_reg_4_] [get_cells         \
core_f_reg_reg_5_] [get_cells core_f_reg_reg_6_] [get_cells core_f_reg_reg_7_] \
[get_cells core_f_reg_reg_8_] [get_cells core_f_reg_reg_9_] [get_cells         \
core_f_reg_reg_10_] [get_cells core_f_reg_reg_11_] [get_cells                  \
core_f_reg_reg_12_] [get_cells core_f_reg_reg_13_] [get_cells                  \
core_f_reg_reg_14_] [get_cells core_f_reg_reg_15_] [get_cells                  \
core_f_reg_reg_16_] [get_cells core_f_reg_reg_17_] [get_cells                  \
core_f_reg_reg_18_] [get_cells core_f_reg_reg_19_] [get_cells                  \
core_f_reg_reg_20_] [get_cells core_f_reg_reg_21_] [get_cells                  \
core_f_reg_reg_22_] [get_cells core_f_reg_reg_23_] [get_cells                  \
core_f_reg_reg_24_] [get_cells core_f_reg_reg_25_] [get_cells                  \
core_f_reg_reg_26_] [get_cells core_f_reg_reg_27_] [get_cells                  \
core_f_reg_reg_28_] [get_cells core_f_reg_reg_29_] [get_cells                  \
core_f_reg_reg_30_] [get_cells core_f_reg_reg_31_] [get_cells                  \
core_e_reg_reg_0_] [get_cells core_e_reg_reg_1_] [get_cells core_e_reg_reg_2_] \
[get_cells core_e_reg_reg_3_] [get_cells core_e_reg_reg_4_] [get_cells         \
core_e_reg_reg_5_] [get_cells core_e_reg_reg_6_] [get_cells core_e_reg_reg_7_] \
[get_cells core_e_reg_reg_8_] [get_cells core_e_reg_reg_9_] [get_cells         \
core_e_reg_reg_10_] [get_cells core_e_reg_reg_11_] [get_cells                  \
core_e_reg_reg_12_] [get_cells core_e_reg_reg_13_] [get_cells                  \
core_e_reg_reg_14_] [get_cells core_e_reg_reg_15_] [get_cells                  \
core_e_reg_reg_16_] [get_cells core_e_reg_reg_17_] [get_cells                  \
core_e_reg_reg_18_] [get_cells core_e_reg_reg_19_] [get_cells                  \
core_e_reg_reg_20_] [get_cells core_e_reg_reg_21_] [get_cells                  \
core_e_reg_reg_22_] [get_cells core_e_reg_reg_23_] [get_cells                  \
core_e_reg_reg_24_] [get_cells core_e_reg_reg_25_] [get_cells                  \
core_e_reg_reg_26_] [get_cells core_e_reg_reg_27_] [get_cells                  \
core_e_reg_reg_28_] [get_cells core_e_reg_reg_29_] [get_cells                  \
core_e_reg_reg_30_] [get_cells core_e_reg_reg_31_] [get_cells                  \
core_d_reg_reg_0_] [get_cells core_d_reg_reg_1_] [get_cells core_d_reg_reg_2_] \
[get_cells core_d_reg_reg_3_] [get_cells core_d_reg_reg_4_] [get_cells         \
core_d_reg_reg_5_] [get_cells core_d_reg_reg_6_] [get_cells core_d_reg_reg_7_] \
[get_cells core_d_reg_reg_8_] [get_cells core_d_reg_reg_9_] [get_cells         \
core_d_reg_reg_10_] [get_cells core_d_reg_reg_11_] [get_cells                  \
core_d_reg_reg_12_] [get_cells core_d_reg_reg_13_] [get_cells                  \
core_d_reg_reg_14_] [get_cells core_d_reg_reg_15_] [get_cells                  \
core_d_reg_reg_16_] [get_cells core_d_reg_reg_17_] [get_cells                  \
core_d_reg_reg_18_] [get_cells core_d_reg_reg_19_] [get_cells                  \
core_d_reg_reg_20_] [get_cells core_d_reg_reg_21_] [get_cells                  \
core_d_reg_reg_22_] [get_cells core_d_reg_reg_23_] [get_cells                  \
core_d_reg_reg_24_] [get_cells core_d_reg_reg_25_] [get_cells                  \
core_d_reg_reg_26_] [get_cells core_d_reg_reg_27_] [get_cells                  \
core_d_reg_reg_28_] [get_cells core_d_reg_reg_29_] [get_cells                  \
core_d_reg_reg_30_] [get_cells core_d_reg_reg_31_] [get_cells                  \
core_c_reg_reg_0_] [get_cells core_c_reg_reg_1_] [get_cells core_c_reg_reg_2_] \
[get_cells core_c_reg_reg_3_] [get_cells core_c_reg_reg_4_] [get_cells         \
core_c_reg_reg_5_] [get_cells core_c_reg_reg_6_] [get_cells core_c_reg_reg_7_] \
[get_cells core_c_reg_reg_8_] [get_cells core_c_reg_reg_9_] [get_cells         \
core_c_reg_reg_10_] [get_cells core_c_reg_reg_11_] [get_cells                  \
core_c_reg_reg_12_] [get_cells core_c_reg_reg_13_] [get_cells                  \
core_c_reg_reg_14_] [get_cells core_c_reg_reg_15_] [get_cells                  \
core_c_reg_reg_16_] [get_cells core_c_reg_reg_17_] [get_cells                  \
core_c_reg_reg_18_] [get_cells core_c_reg_reg_19_] [get_cells                  \
core_c_reg_reg_20_] [get_cells core_c_reg_reg_21_] [get_cells                  \
core_c_reg_reg_22_] [get_cells core_c_reg_reg_23_] [get_cells                  \
core_c_reg_reg_24_] [get_cells core_c_reg_reg_25_] [get_cells                  \
core_c_reg_reg_26_] [get_cells core_c_reg_reg_27_] [get_cells                  \
core_c_reg_reg_28_] [get_cells core_c_reg_reg_29_] [get_cells                  \
core_c_reg_reg_30_] [get_cells core_c_reg_reg_31_] [get_cells                  \
core_b_reg_reg_0_] [get_cells core_b_reg_reg_1_] [get_cells core_b_reg_reg_2_] \
[get_cells core_b_reg_reg_3_] [get_cells core_b_reg_reg_4_] [get_cells         \
core_b_reg_reg_5_] [get_cells core_b_reg_reg_6_] [get_cells core_b_reg_reg_7_] \
[get_cells core_b_reg_reg_8_] [get_cells core_b_reg_reg_9_] [get_cells         \
core_b_reg_reg_10_] [get_cells core_b_reg_reg_11_] [get_cells                  \
core_b_reg_reg_12_] [get_cells core_b_reg_reg_13_] [get_cells                  \
core_b_reg_reg_14_] [get_cells core_b_reg_reg_15_] [get_cells                  \
core_b_reg_reg_16_] [get_cells core_b_reg_reg_17_] [get_cells                  \
core_b_reg_reg_18_] [get_cells core_b_reg_reg_19_] [get_cells                  \
core_b_reg_reg_20_] [get_cells core_b_reg_reg_21_] [get_cells                  \
core_b_reg_reg_22_] [get_cells core_b_reg_reg_23_] [get_cells                  \
core_b_reg_reg_24_] [get_cells core_b_reg_reg_25_] [get_cells                  \
core_b_reg_reg_26_] [get_cells core_b_reg_reg_27_] [get_cells                  \
core_b_reg_reg_28_] [get_cells core_b_reg_reg_29_] [get_cells                  \
core_b_reg_reg_30_] [get_cells core_b_reg_reg_31_] [get_cells                  \
core_a_reg_reg_0_] [get_cells core_a_reg_reg_1_] [get_cells core_a_reg_reg_2_] \
[get_cells core_a_reg_reg_3_] [get_cells core_a_reg_reg_4_] [get_cells         \
core_a_reg_reg_5_] [get_cells core_a_reg_reg_6_] [get_cells core_a_reg_reg_7_] \
[get_cells core_a_reg_reg_8_] [get_cells core_a_reg_reg_9_] [get_cells         \
core_a_reg_reg_10_] [get_cells core_a_reg_reg_11_] [get_cells                  \
core_a_reg_reg_12_] [get_cells core_a_reg_reg_13_] [get_cells                  \
core_a_reg_reg_14_] [get_cells core_a_reg_reg_15_] [get_cells                  \
core_a_reg_reg_16_] [get_cells core_a_reg_reg_17_] [get_cells                  \
core_a_reg_reg_18_] [get_cells core_a_reg_reg_19_] [get_cells                  \
core_a_reg_reg_20_] [get_cells core_a_reg_reg_21_] [get_cells                  \
core_a_reg_reg_22_] [get_cells core_a_reg_reg_23_] [get_cells                  \
core_a_reg_reg_24_] [get_cells core_a_reg_reg_25_] [get_cells                  \
core_a_reg_reg_26_] [get_cells core_a_reg_reg_27_] [get_cells                  \
core_a_reg_reg_28_] [get_cells core_a_reg_reg_29_] [get_cells                  \
core_a_reg_reg_30_] [get_cells core_a_reg_reg_31_] [get_cells                  \
core_sha256_ctrl_reg_reg_0_] [get_cells core_sha256_ctrl_reg_reg_1_]           \
[get_cells core_H5_reg_reg_0_] [get_cells core_H5_reg_reg_1_] [get_cells       \
core_H5_reg_reg_2_] [get_cells core_H5_reg_reg_3_] [get_cells                  \
core_H5_reg_reg_4_] [get_cells core_H5_reg_reg_5_] [get_cells                  \
core_H5_reg_reg_6_] [get_cells core_H5_reg_reg_7_] [get_cells                  \
core_H5_reg_reg_8_] [get_cells core_H5_reg_reg_9_] [get_cells                  \
core_H5_reg_reg_10_] [get_cells core_H5_reg_reg_11_] [get_cells                \
core_H5_reg_reg_12_] [get_cells core_H5_reg_reg_13_] [get_cells                \
core_H5_reg_reg_14_] [get_cells core_H5_reg_reg_15_] [get_cells                \
core_H5_reg_reg_16_] [get_cells core_H5_reg_reg_17_] [get_cells                \
core_H5_reg_reg_18_] [get_cells core_H5_reg_reg_19_] [get_cells                \
core_H5_reg_reg_20_] [get_cells core_H5_reg_reg_21_] [get_cells                \
core_H5_reg_reg_22_] [get_cells core_H5_reg_reg_23_] [get_cells                \
core_H5_reg_reg_24_] [get_cells core_H5_reg_reg_25_] [get_cells                \
core_H5_reg_reg_26_] [get_cells core_H5_reg_reg_27_] [get_cells                \
core_H5_reg_reg_28_] [get_cells core_H5_reg_reg_29_] [get_cells                \
core_H5_reg_reg_30_] [get_cells core_H5_reg_reg_31_] [get_cells                \
core_H6_reg_reg_0_] [get_cells core_H6_reg_reg_1_] [get_cells                  \
core_H6_reg_reg_2_] [get_cells core_H6_reg_reg_3_] [get_cells                  \
core_H6_reg_reg_4_] [get_cells core_H6_reg_reg_5_] [get_cells                  \
core_H6_reg_reg_6_] [get_cells core_H6_reg_reg_7_] [get_cells                  \
core_H6_reg_reg_8_] [get_cells core_H6_reg_reg_9_] [get_cells                  \
core_H6_reg_reg_10_] [get_cells core_H6_reg_reg_11_] [get_cells                \
core_H6_reg_reg_12_] [get_cells core_H6_reg_reg_13_] [get_cells                \
core_H6_reg_reg_14_] [get_cells core_H6_reg_reg_15_] [get_cells                \
core_H6_reg_reg_16_] [get_cells core_H6_reg_reg_17_] [get_cells                \
core_H6_reg_reg_18_] [get_cells core_H6_reg_reg_19_] [get_cells                \
core_H6_reg_reg_20_] [get_cells core_H6_reg_reg_21_] [get_cells                \
core_H6_reg_reg_22_] [get_cells core_H6_reg_reg_23_] [get_cells                \
core_H6_reg_reg_24_] [get_cells core_H6_reg_reg_25_] [get_cells                \
core_H6_reg_reg_26_] [get_cells core_H6_reg_reg_27_] [get_cells                \
core_H6_reg_reg_28_] [get_cells core_H6_reg_reg_29_] [get_cells                \
core_H6_reg_reg_30_] [get_cells core_H6_reg_reg_31_] [get_cells                \
core_H7_reg_reg_0_] [get_cells core_H7_reg_reg_1_] [get_cells                  \
core_H7_reg_reg_2_] [get_cells core_H7_reg_reg_3_] [get_cells                  \
core_H7_reg_reg_4_] [get_cells core_H7_reg_reg_5_] [get_cells                  \
core_H7_reg_reg_6_] [get_cells core_H7_reg_reg_7_] [get_cells                  \
core_H7_reg_reg_8_] [get_cells core_H7_reg_reg_9_] [get_cells                  \
core_H7_reg_reg_10_] [get_cells core_H7_reg_reg_11_] [get_cells                \
core_H7_reg_reg_12_] [get_cells core_H7_reg_reg_13_] [get_cells                \
core_H7_reg_reg_14_] [get_cells core_H7_reg_reg_15_] [get_cells                \
core_H7_reg_reg_16_] [get_cells core_H7_reg_reg_17_] [get_cells                \
core_H7_reg_reg_18_] [get_cells core_H7_reg_reg_19_] [get_cells                \
core_H7_reg_reg_20_] [get_cells core_H7_reg_reg_21_] [get_cells                \
core_H7_reg_reg_22_] [get_cells core_H7_reg_reg_23_] [get_cells                \
core_H7_reg_reg_24_] [get_cells core_H7_reg_reg_25_] [get_cells                \
core_H7_reg_reg_26_] [get_cells core_H7_reg_reg_27_] [get_cells                \
core_H7_reg_reg_28_] [get_cells core_H7_reg_reg_29_] [get_cells                \
core_H7_reg_reg_30_] [get_cells core_H7_reg_reg_31_] [get_cells                \
core_digest_valid_reg_reg] [get_cells core_t_ctr_reg_reg_0_] [get_cells        \
core_t_ctr_reg_reg_1_] [get_cells core_t_ctr_reg_reg_2_] [get_cells            \
core_t_ctr_reg_reg_3_] [get_cells core_t_ctr_reg_reg_4_] [get_cells            \
core_t_ctr_reg_reg_5_] [get_cells core_H4_reg_reg_0_] [get_cells               \
core_H4_reg_reg_1_] [get_cells core_H4_reg_reg_2_] [get_cells                  \
core_H4_reg_reg_3_] [get_cells core_H4_reg_reg_4_] [get_cells                  \
core_H4_reg_reg_5_] [get_cells core_H4_reg_reg_6_] [get_cells                  \
core_H4_reg_reg_7_] [get_cells core_H4_reg_reg_8_] [get_cells                  \
core_H4_reg_reg_9_] [get_cells core_H4_reg_reg_10_] [get_cells                 \
core_H4_reg_reg_11_] [get_cells core_H4_reg_reg_12_] [get_cells                \
core_H4_reg_reg_13_] [get_cells core_H4_reg_reg_14_] [get_cells                \
core_H4_reg_reg_15_] [get_cells core_H4_reg_reg_16_] [get_cells                \
core_H4_reg_reg_17_] [get_cells core_H4_reg_reg_18_] [get_cells                \
core_H4_reg_reg_19_] [get_cells core_H4_reg_reg_20_] [get_cells                \
core_H4_reg_reg_21_] [get_cells core_H4_reg_reg_22_] [get_cells                \
core_H4_reg_reg_23_] [get_cells core_H4_reg_reg_24_] [get_cells                \
core_H4_reg_reg_25_] [get_cells core_H4_reg_reg_26_] [get_cells                \
core_H4_reg_reg_27_] [get_cells core_H4_reg_reg_28_] [get_cells                \
core_H4_reg_reg_29_] [get_cells core_H4_reg_reg_30_] [get_cells                \
core_H4_reg_reg_31_] [get_cells core_w_mem_inst_w_mem_reg_15__0_] [get_cells   \
core_w_mem_inst_w_mem_reg_15__1_] [get_cells core_w_mem_inst_w_mem_reg_15__2_] \
[get_cells core_w_mem_inst_w_mem_reg_15__3_] [get_cells                        \
core_w_mem_inst_w_mem_reg_15__4_] [get_cells core_w_mem_inst_w_mem_reg_15__5_] \
[get_cells core_w_mem_inst_w_mem_reg_15__6_] [get_cells                        \
core_w_mem_inst_w_mem_reg_15__7_] [get_cells core_w_mem_inst_w_mem_reg_15__8_] \
[get_cells core_w_mem_inst_w_mem_reg_15__9_] [get_cells                        \
core_w_mem_inst_w_mem_reg_15__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__0_] [get_cells core_w_mem_inst_w_mem_reg_14__1_] \
[get_cells core_w_mem_inst_w_mem_reg_14__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_14__3_] [get_cells core_w_mem_inst_w_mem_reg_14__4_] \
[get_cells core_w_mem_inst_w_mem_reg_14__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_14__6_] [get_cells core_w_mem_inst_w_mem_reg_14__7_] \
[get_cells core_w_mem_inst_w_mem_reg_14__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_14__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_14__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__0_] [get_cells core_w_mem_inst_w_mem_reg_13__1_] \
[get_cells core_w_mem_inst_w_mem_reg_13__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_13__3_] [get_cells core_w_mem_inst_w_mem_reg_13__4_] \
[get_cells core_w_mem_inst_w_mem_reg_13__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_13__6_] [get_cells core_w_mem_inst_w_mem_reg_13__7_] \
[get_cells core_w_mem_inst_w_mem_reg_13__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_13__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_13__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__0_] [get_cells core_w_mem_inst_w_mem_reg_12__1_] \
[get_cells core_w_mem_inst_w_mem_reg_12__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_12__3_] [get_cells core_w_mem_inst_w_mem_reg_12__4_] \
[get_cells core_w_mem_inst_w_mem_reg_12__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_12__6_] [get_cells core_w_mem_inst_w_mem_reg_12__7_] \
[get_cells core_w_mem_inst_w_mem_reg_12__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_12__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_12__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__0_] [get_cells core_w_mem_inst_w_mem_reg_11__1_] \
[get_cells core_w_mem_inst_w_mem_reg_11__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_11__3_] [get_cells core_w_mem_inst_w_mem_reg_11__4_] \
[get_cells core_w_mem_inst_w_mem_reg_11__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_11__6_] [get_cells core_w_mem_inst_w_mem_reg_11__7_] \
[get_cells core_w_mem_inst_w_mem_reg_11__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_11__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_11__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__0_] [get_cells core_w_mem_inst_w_mem_reg_10__1_] \
[get_cells core_w_mem_inst_w_mem_reg_10__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_10__3_] [get_cells core_w_mem_inst_w_mem_reg_10__4_] \
[get_cells core_w_mem_inst_w_mem_reg_10__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_10__6_] [get_cells core_w_mem_inst_w_mem_reg_10__7_] \
[get_cells core_w_mem_inst_w_mem_reg_10__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_10__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_10__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__31_] [get_cells core_w_mem_inst_w_mem_reg_9__0_] \
[get_cells core_w_mem_inst_w_mem_reg_9__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_9__2_] [get_cells core_w_mem_inst_w_mem_reg_9__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_9__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_9__5_] [get_cells core_w_mem_inst_w_mem_reg_9__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_9__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_9__8_] [get_cells core_w_mem_inst_w_mem_reg_9__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_9__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__11_] [get_cells core_w_mem_inst_w_mem_reg_9__12_] \
[get_cells core_w_mem_inst_w_mem_reg_9__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__14_] [get_cells core_w_mem_inst_w_mem_reg_9__15_] \
[get_cells core_w_mem_inst_w_mem_reg_9__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__17_] [get_cells core_w_mem_inst_w_mem_reg_9__18_] \
[get_cells core_w_mem_inst_w_mem_reg_9__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__20_] [get_cells core_w_mem_inst_w_mem_reg_9__21_] \
[get_cells core_w_mem_inst_w_mem_reg_9__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__23_] [get_cells core_w_mem_inst_w_mem_reg_9__24_] \
[get_cells core_w_mem_inst_w_mem_reg_9__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__26_] [get_cells core_w_mem_inst_w_mem_reg_9__27_] \
[get_cells core_w_mem_inst_w_mem_reg_9__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__29_] [get_cells core_w_mem_inst_w_mem_reg_9__30_] \
[get_cells core_w_mem_inst_w_mem_reg_9__31_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__0_] [get_cells core_w_mem_inst_w_mem_reg_8__1_]   \
[get_cells core_w_mem_inst_w_mem_reg_8__2_] [get_cells                         \
core_w_mem_inst_w_mem_reg_8__3_] [get_cells core_w_mem_inst_w_mem_reg_8__4_]   \
[get_cells core_w_mem_inst_w_mem_reg_8__5_] [get_cells                         \
core_w_mem_inst_w_mem_reg_8__6_] [get_cells core_w_mem_inst_w_mem_reg_8__7_]   \
[get_cells core_w_mem_inst_w_mem_reg_8__8_] [get_cells                         \
core_w_mem_inst_w_mem_reg_8__9_] [get_cells core_w_mem_inst_w_mem_reg_8__10_]  \
[get_cells core_w_mem_inst_w_mem_reg_8__11_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__12_] [get_cells core_w_mem_inst_w_mem_reg_8__13_] \
[get_cells core_w_mem_inst_w_mem_reg_8__14_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__15_] [get_cells core_w_mem_inst_w_mem_reg_8__16_] \
[get_cells core_w_mem_inst_w_mem_reg_8__17_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__18_] [get_cells core_w_mem_inst_w_mem_reg_8__19_] \
[get_cells core_w_mem_inst_w_mem_reg_8__20_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__21_] [get_cells core_w_mem_inst_w_mem_reg_8__22_] \
[get_cells core_w_mem_inst_w_mem_reg_8__23_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__24_] [get_cells core_w_mem_inst_w_mem_reg_8__25_] \
[get_cells core_w_mem_inst_w_mem_reg_8__26_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__27_] [get_cells core_w_mem_inst_w_mem_reg_8__28_] \
[get_cells core_w_mem_inst_w_mem_reg_8__29_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__30_] [get_cells core_w_mem_inst_w_mem_reg_8__31_] \
[get_cells core_w_mem_inst_w_mem_reg_7__0_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__1_] [get_cells core_w_mem_inst_w_mem_reg_7__2_]   \
[get_cells core_w_mem_inst_w_mem_reg_7__3_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__4_] [get_cells core_w_mem_inst_w_mem_reg_7__5_]   \
[get_cells core_w_mem_inst_w_mem_reg_7__6_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__7_] [get_cells core_w_mem_inst_w_mem_reg_7__8_]   \
[get_cells core_w_mem_inst_w_mem_reg_7__9_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__10_] [get_cells core_w_mem_inst_w_mem_reg_7__11_] \
[get_cells core_w_mem_inst_w_mem_reg_7__12_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__13_] [get_cells core_w_mem_inst_w_mem_reg_7__14_] \
[get_cells core_w_mem_inst_w_mem_reg_7__15_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__16_] [get_cells core_w_mem_inst_w_mem_reg_7__17_] \
[get_cells core_w_mem_inst_w_mem_reg_7__18_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__19_] [get_cells core_w_mem_inst_w_mem_reg_7__20_] \
[get_cells core_w_mem_inst_w_mem_reg_7__21_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__22_] [get_cells core_w_mem_inst_w_mem_reg_7__23_] \
[get_cells core_w_mem_inst_w_mem_reg_7__24_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__25_] [get_cells core_w_mem_inst_w_mem_reg_7__26_] \
[get_cells core_w_mem_inst_w_mem_reg_7__27_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__28_] [get_cells core_w_mem_inst_w_mem_reg_7__29_] \
[get_cells core_w_mem_inst_w_mem_reg_7__30_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__31_] [get_cells core_w_mem_inst_w_mem_reg_6__0_]  \
[get_cells core_w_mem_inst_w_mem_reg_6__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_6__2_] [get_cells core_w_mem_inst_w_mem_reg_6__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_6__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_6__5_] [get_cells core_w_mem_inst_w_mem_reg_6__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_6__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_6__8_] [get_cells core_w_mem_inst_w_mem_reg_6__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_6__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__11_] [get_cells core_w_mem_inst_w_mem_reg_6__12_] \
[get_cells core_w_mem_inst_w_mem_reg_6__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__14_] [get_cells core_w_mem_inst_w_mem_reg_6__15_] \
[get_cells core_w_mem_inst_w_mem_reg_6__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__17_] [get_cells core_w_mem_inst_w_mem_reg_6__18_] \
[get_cells core_w_mem_inst_w_mem_reg_6__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__20_] [get_cells core_w_mem_inst_w_mem_reg_6__21_] \
[get_cells core_w_mem_inst_w_mem_reg_6__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__23_] [get_cells core_w_mem_inst_w_mem_reg_6__24_] \
[get_cells core_w_mem_inst_w_mem_reg_6__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__26_] [get_cells core_w_mem_inst_w_mem_reg_6__27_] \
[get_cells core_w_mem_inst_w_mem_reg_6__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__29_] [get_cells core_w_mem_inst_w_mem_reg_6__30_] \
[get_cells core_w_mem_inst_w_mem_reg_6__31_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__0_] [get_cells core_w_mem_inst_w_mem_reg_5__1_]   \
[get_cells core_w_mem_inst_w_mem_reg_5__2_] [get_cells                         \
core_w_mem_inst_w_mem_reg_5__3_] [get_cells core_w_mem_inst_w_mem_reg_5__4_]   \
[get_cells core_w_mem_inst_w_mem_reg_5__5_] [get_cells                         \
core_w_mem_inst_w_mem_reg_5__6_] [get_cells core_w_mem_inst_w_mem_reg_5__7_]   \
[get_cells core_w_mem_inst_w_mem_reg_5__8_] [get_cells                         \
core_w_mem_inst_w_mem_reg_5__9_] [get_cells core_w_mem_inst_w_mem_reg_5__10_]  \
[get_cells core_w_mem_inst_w_mem_reg_5__11_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__12_] [get_cells core_w_mem_inst_w_mem_reg_5__13_] \
[get_cells core_w_mem_inst_w_mem_reg_5__14_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__15_] [get_cells core_w_mem_inst_w_mem_reg_5__16_] \
[get_cells core_w_mem_inst_w_mem_reg_5__17_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__18_] [get_cells core_w_mem_inst_w_mem_reg_5__19_] \
[get_cells core_w_mem_inst_w_mem_reg_5__20_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__21_] [get_cells core_w_mem_inst_w_mem_reg_5__22_] \
[get_cells core_w_mem_inst_w_mem_reg_5__23_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__24_] [get_cells core_w_mem_inst_w_mem_reg_5__25_] \
[get_cells core_w_mem_inst_w_mem_reg_5__26_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__27_] [get_cells core_w_mem_inst_w_mem_reg_5__28_] \
[get_cells core_w_mem_inst_w_mem_reg_5__29_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__30_] [get_cells core_w_mem_inst_w_mem_reg_5__31_] \
[get_cells core_w_mem_inst_w_mem_reg_4__0_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__1_] [get_cells core_w_mem_inst_w_mem_reg_4__2_]   \
[get_cells core_w_mem_inst_w_mem_reg_4__3_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__4_] [get_cells core_w_mem_inst_w_mem_reg_4__5_]   \
[get_cells core_w_mem_inst_w_mem_reg_4__6_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__7_] [get_cells core_w_mem_inst_w_mem_reg_4__8_]   \
[get_cells core_w_mem_inst_w_mem_reg_4__9_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__10_] [get_cells core_w_mem_inst_w_mem_reg_4__11_] \
[get_cells core_w_mem_inst_w_mem_reg_4__12_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__13_] [get_cells core_w_mem_inst_w_mem_reg_4__14_] \
[get_cells core_w_mem_inst_w_mem_reg_4__15_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__16_] [get_cells core_w_mem_inst_w_mem_reg_4__17_] \
[get_cells core_w_mem_inst_w_mem_reg_4__18_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__19_] [get_cells core_w_mem_inst_w_mem_reg_4__20_] \
[get_cells core_w_mem_inst_w_mem_reg_4__21_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__22_] [get_cells core_w_mem_inst_w_mem_reg_4__23_] \
[get_cells core_w_mem_inst_w_mem_reg_4__24_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__25_] [get_cells core_w_mem_inst_w_mem_reg_4__26_] \
[get_cells core_w_mem_inst_w_mem_reg_4__27_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__28_] [get_cells core_w_mem_inst_w_mem_reg_4__29_] \
[get_cells core_w_mem_inst_w_mem_reg_4__30_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__31_] [get_cells core_w_mem_inst_w_mem_reg_3__0_]  \
[get_cells core_w_mem_inst_w_mem_reg_3__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_3__2_] [get_cells core_w_mem_inst_w_mem_reg_3__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_3__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_3__5_] [get_cells core_w_mem_inst_w_mem_reg_3__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_3__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_3__8_] [get_cells core_w_mem_inst_w_mem_reg_3__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_3__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__11_] [get_cells core_w_mem_inst_w_mem_reg_3__12_] \
[get_cells core_w_mem_inst_w_mem_reg_3__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__14_] [get_cells core_w_mem_inst_w_mem_reg_3__15_] \
[get_cells core_w_mem_inst_w_mem_reg_3__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__17_] [get_cells core_w_mem_inst_w_mem_reg_3__18_] \
[get_cells core_w_mem_inst_w_mem_reg_3__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__20_] [get_cells core_w_mem_inst_w_mem_reg_3__21_] \
[get_cells core_w_mem_inst_w_mem_reg_3__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__23_] [get_cells core_w_mem_inst_w_mem_reg_3__24_] \
[get_cells core_w_mem_inst_w_mem_reg_3__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__26_] [get_cells core_w_mem_inst_w_mem_reg_3__27_] \
[get_cells core_w_mem_inst_w_mem_reg_3__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__29_] [get_cells core_w_mem_inst_w_mem_reg_3__30_] \
[get_cells core_w_mem_inst_w_mem_reg_3__31_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__0_] [get_cells core_w_mem_inst_w_mem_reg_2__1_]   \
[get_cells core_w_mem_inst_w_mem_reg_2__2_] [get_cells                         \
core_w_mem_inst_w_mem_reg_2__3_] [get_cells core_w_mem_inst_w_mem_reg_2__4_]   \
[get_cells core_w_mem_inst_w_mem_reg_2__5_] [get_cells                         \
core_w_mem_inst_w_mem_reg_2__6_] [get_cells core_w_mem_inst_w_mem_reg_2__7_]   \
[get_cells core_w_mem_inst_w_mem_reg_2__8_] [get_cells                         \
core_w_mem_inst_w_mem_reg_2__9_] [get_cells core_w_mem_inst_w_mem_reg_2__10_]  \
[get_cells core_w_mem_inst_w_mem_reg_2__11_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__12_] [get_cells core_w_mem_inst_w_mem_reg_2__13_] \
[get_cells core_w_mem_inst_w_mem_reg_2__14_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__15_] [get_cells core_w_mem_inst_w_mem_reg_2__16_] \
[get_cells core_w_mem_inst_w_mem_reg_2__17_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__18_] [get_cells core_w_mem_inst_w_mem_reg_2__19_] \
[get_cells core_w_mem_inst_w_mem_reg_2__20_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__21_] [get_cells core_w_mem_inst_w_mem_reg_2__22_] \
[get_cells core_w_mem_inst_w_mem_reg_2__23_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__24_] [get_cells core_w_mem_inst_w_mem_reg_2__25_] \
[get_cells core_w_mem_inst_w_mem_reg_2__26_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__27_] [get_cells core_w_mem_inst_w_mem_reg_2__28_] \
[get_cells core_w_mem_inst_w_mem_reg_2__29_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__30_] [get_cells core_w_mem_inst_w_mem_reg_2__31_] \
[get_cells core_w_mem_inst_w_mem_reg_1__0_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__1_] [get_cells core_w_mem_inst_w_mem_reg_1__2_]   \
[get_cells core_w_mem_inst_w_mem_reg_1__3_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__4_] [get_cells core_w_mem_inst_w_mem_reg_1__5_]   \
[get_cells core_w_mem_inst_w_mem_reg_1__6_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__7_] [get_cells core_w_mem_inst_w_mem_reg_1__8_]   \
[get_cells core_w_mem_inst_w_mem_reg_1__9_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__10_] [get_cells core_w_mem_inst_w_mem_reg_1__11_] \
[get_cells core_w_mem_inst_w_mem_reg_1__12_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__13_] [get_cells core_w_mem_inst_w_mem_reg_1__14_] \
[get_cells core_w_mem_inst_w_mem_reg_1__15_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__16_] [get_cells core_w_mem_inst_w_mem_reg_1__17_] \
[get_cells core_w_mem_inst_w_mem_reg_1__18_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__19_] [get_cells core_w_mem_inst_w_mem_reg_1__20_] \
[get_cells core_w_mem_inst_w_mem_reg_1__21_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__22_] [get_cells core_w_mem_inst_w_mem_reg_1__23_] \
[get_cells core_w_mem_inst_w_mem_reg_1__24_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__25_] [get_cells core_w_mem_inst_w_mem_reg_1__26_] \
[get_cells core_w_mem_inst_w_mem_reg_1__27_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__28_] [get_cells core_w_mem_inst_w_mem_reg_1__29_] \
[get_cells core_w_mem_inst_w_mem_reg_1__30_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__31_] [get_cells core_w_mem_inst_w_mem_reg_0__0_]  \
[get_cells core_w_mem_inst_w_mem_reg_0__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_0__2_] [get_cells core_w_mem_inst_w_mem_reg_0__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_0__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_0__5_] [get_cells core_w_mem_inst_w_mem_reg_0__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_0__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_0__8_] [get_cells core_w_mem_inst_w_mem_reg_0__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_0__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__11_] [get_cells core_w_mem_inst_w_mem_reg_0__12_] \
[get_cells core_w_mem_inst_w_mem_reg_0__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__14_] [get_cells core_w_mem_inst_w_mem_reg_0__15_] \
[get_cells core_w_mem_inst_w_mem_reg_0__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__17_] [get_cells core_w_mem_inst_w_mem_reg_0__18_] \
[get_cells core_w_mem_inst_w_mem_reg_0__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__20_] [get_cells core_w_mem_inst_w_mem_reg_0__21_] \
[get_cells core_w_mem_inst_w_mem_reg_0__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__23_] [get_cells core_w_mem_inst_w_mem_reg_0__24_] \
[get_cells core_w_mem_inst_w_mem_reg_0__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__26_] [get_cells core_w_mem_inst_w_mem_reg_0__27_] \
[get_cells core_w_mem_inst_w_mem_reg_0__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__29_] [get_cells core_w_mem_inst_w_mem_reg_0__30_] \
[get_cells core_w_mem_inst_w_mem_reg_0__31_] [get_cells                        \
core_w_mem_inst_w_ctr_reg_reg_0_] [get_cells core_w_mem_inst_w_ctr_reg_reg_1_] \
[get_cells core_w_mem_inst_w_ctr_reg_reg_2_] [get_cells                        \
core_w_mem_inst_w_ctr_reg_reg_3_] [get_cells core_w_mem_inst_w_ctr_reg_reg_4_] \
[get_cells core_w_mem_inst_w_ctr_reg_reg_5_]]  -to [list [get_cells digest_valid_reg_reg] [get_cells digest_reg_reg_0_]      \
[get_cells digest_reg_reg_1_] [get_cells digest_reg_reg_2_] [get_cells         \
digest_reg_reg_3_] [get_cells digest_reg_reg_4_] [get_cells digest_reg_reg_5_] \
[get_cells digest_reg_reg_6_] [get_cells digest_reg_reg_7_] [get_cells         \
digest_reg_reg_8_] [get_cells digest_reg_reg_9_] [get_cells                    \
digest_reg_reg_10_] [get_cells digest_reg_reg_11_] [get_cells                  \
digest_reg_reg_12_] [get_cells digest_reg_reg_13_] [get_cells                  \
digest_reg_reg_14_] [get_cells digest_reg_reg_15_] [get_cells                  \
digest_reg_reg_16_] [get_cells digest_reg_reg_17_] [get_cells                  \
digest_reg_reg_18_] [get_cells digest_reg_reg_19_] [get_cells                  \
digest_reg_reg_20_] [get_cells digest_reg_reg_21_] [get_cells                  \
digest_reg_reg_22_] [get_cells digest_reg_reg_23_] [get_cells                  \
digest_reg_reg_24_] [get_cells digest_reg_reg_25_] [get_cells                  \
digest_reg_reg_26_] [get_cells digest_reg_reg_27_] [get_cells                  \
digest_reg_reg_28_] [get_cells digest_reg_reg_29_] [get_cells                  \
digest_reg_reg_30_] [get_cells digest_reg_reg_31_] [get_cells                  \
digest_reg_reg_32_] [get_cells digest_reg_reg_33_] [get_cells                  \
digest_reg_reg_34_] [get_cells digest_reg_reg_35_] [get_cells                  \
digest_reg_reg_36_] [get_cells digest_reg_reg_37_] [get_cells                  \
digest_reg_reg_38_] [get_cells digest_reg_reg_39_] [get_cells                  \
digest_reg_reg_40_] [get_cells digest_reg_reg_41_] [get_cells                  \
digest_reg_reg_42_] [get_cells digest_reg_reg_43_] [get_cells                  \
digest_reg_reg_44_] [get_cells digest_reg_reg_45_] [get_cells                  \
digest_reg_reg_46_] [get_cells digest_reg_reg_47_] [get_cells                  \
digest_reg_reg_48_] [get_cells digest_reg_reg_49_] [get_cells                  \
digest_reg_reg_50_] [get_cells digest_reg_reg_51_] [get_cells                  \
digest_reg_reg_52_] [get_cells digest_reg_reg_53_] [get_cells                  \
digest_reg_reg_54_] [get_cells digest_reg_reg_55_] [get_cells                  \
digest_reg_reg_56_] [get_cells digest_reg_reg_57_] [get_cells                  \
digest_reg_reg_58_] [get_cells digest_reg_reg_59_] [get_cells                  \
digest_reg_reg_60_] [get_cells digest_reg_reg_61_] [get_cells                  \
digest_reg_reg_62_] [get_cells digest_reg_reg_63_] [get_cells                  \
digest_reg_reg_64_] [get_cells digest_reg_reg_65_] [get_cells                  \
digest_reg_reg_66_] [get_cells digest_reg_reg_67_] [get_cells                  \
digest_reg_reg_68_] [get_cells digest_reg_reg_69_] [get_cells                  \
digest_reg_reg_70_] [get_cells digest_reg_reg_71_] [get_cells                  \
digest_reg_reg_72_] [get_cells digest_reg_reg_73_] [get_cells                  \
digest_reg_reg_74_] [get_cells digest_reg_reg_75_] [get_cells                  \
digest_reg_reg_76_] [get_cells digest_reg_reg_77_] [get_cells                  \
digest_reg_reg_78_] [get_cells digest_reg_reg_79_] [get_cells                  \
digest_reg_reg_80_] [get_cells digest_reg_reg_81_] [get_cells                  \
digest_reg_reg_82_] [get_cells digest_reg_reg_83_] [get_cells                  \
digest_reg_reg_84_] [get_cells digest_reg_reg_85_] [get_cells                  \
digest_reg_reg_86_] [get_cells digest_reg_reg_87_] [get_cells                  \
digest_reg_reg_88_] [get_cells digest_reg_reg_89_] [get_cells                  \
digest_reg_reg_90_] [get_cells digest_reg_reg_91_] [get_cells                  \
digest_reg_reg_92_] [get_cells digest_reg_reg_93_] [get_cells                  \
digest_reg_reg_94_] [get_cells digest_reg_reg_95_] [get_cells                  \
digest_reg_reg_96_] [get_cells digest_reg_reg_97_] [get_cells                  \
digest_reg_reg_98_] [get_cells digest_reg_reg_99_] [get_cells                  \
digest_reg_reg_100_] [get_cells digest_reg_reg_101_] [get_cells                \
digest_reg_reg_102_] [get_cells digest_reg_reg_103_] [get_cells                \
digest_reg_reg_104_] [get_cells digest_reg_reg_105_] [get_cells                \
digest_reg_reg_106_] [get_cells digest_reg_reg_107_] [get_cells                \
digest_reg_reg_108_] [get_cells digest_reg_reg_109_] [get_cells                \
digest_reg_reg_110_] [get_cells digest_reg_reg_111_] [get_cells                \
digest_reg_reg_112_] [get_cells digest_reg_reg_113_] [get_cells                \
digest_reg_reg_114_] [get_cells digest_reg_reg_115_] [get_cells                \
digest_reg_reg_116_] [get_cells digest_reg_reg_117_] [get_cells                \
digest_reg_reg_118_] [get_cells digest_reg_reg_119_] [get_cells                \
digest_reg_reg_120_] [get_cells digest_reg_reg_121_] [get_cells                \
digest_reg_reg_122_] [get_cells digest_reg_reg_123_] [get_cells                \
digest_reg_reg_124_] [get_cells digest_reg_reg_125_] [get_cells                \
digest_reg_reg_126_] [get_cells digest_reg_reg_127_] [get_cells                \
digest_reg_reg_128_] [get_cells digest_reg_reg_129_] [get_cells                \
digest_reg_reg_130_] [get_cells digest_reg_reg_131_] [get_cells                \
digest_reg_reg_132_] [get_cells digest_reg_reg_133_] [get_cells                \
digest_reg_reg_134_] [get_cells digest_reg_reg_135_] [get_cells                \
digest_reg_reg_136_] [get_cells digest_reg_reg_137_] [get_cells                \
digest_reg_reg_138_] [get_cells digest_reg_reg_139_] [get_cells                \
digest_reg_reg_140_] [get_cells digest_reg_reg_141_] [get_cells                \
digest_reg_reg_142_] [get_cells digest_reg_reg_143_] [get_cells                \
digest_reg_reg_144_] [get_cells digest_reg_reg_145_] [get_cells                \
digest_reg_reg_146_] [get_cells digest_reg_reg_147_] [get_cells                \
digest_reg_reg_148_] [get_cells digest_reg_reg_149_] [get_cells                \
digest_reg_reg_150_] [get_cells digest_reg_reg_151_] [get_cells                \
digest_reg_reg_152_] [get_cells digest_reg_reg_153_] [get_cells                \
digest_reg_reg_154_] [get_cells digest_reg_reg_155_] [get_cells                \
digest_reg_reg_156_] [get_cells digest_reg_reg_157_] [get_cells                \
digest_reg_reg_158_] [get_cells digest_reg_reg_159_] [get_cells                \
digest_reg_reg_160_] [get_cells digest_reg_reg_161_] [get_cells                \
digest_reg_reg_162_] [get_cells digest_reg_reg_163_] [get_cells                \
digest_reg_reg_164_] [get_cells digest_reg_reg_165_] [get_cells                \
digest_reg_reg_166_] [get_cells digest_reg_reg_167_] [get_cells                \
digest_reg_reg_168_] [get_cells digest_reg_reg_169_] [get_cells                \
digest_reg_reg_170_] [get_cells digest_reg_reg_171_] [get_cells                \
digest_reg_reg_172_] [get_cells digest_reg_reg_173_] [get_cells                \
digest_reg_reg_174_] [get_cells digest_reg_reg_175_] [get_cells                \
digest_reg_reg_176_] [get_cells digest_reg_reg_177_] [get_cells                \
digest_reg_reg_178_] [get_cells digest_reg_reg_179_] [get_cells                \
digest_reg_reg_180_] [get_cells digest_reg_reg_181_] [get_cells                \
digest_reg_reg_182_] [get_cells digest_reg_reg_183_] [get_cells                \
digest_reg_reg_184_] [get_cells digest_reg_reg_185_] [get_cells                \
digest_reg_reg_186_] [get_cells digest_reg_reg_187_] [get_cells                \
digest_reg_reg_188_] [get_cells digest_reg_reg_189_] [get_cells                \
digest_reg_reg_190_] [get_cells digest_reg_reg_191_] [get_cells                \
digest_reg_reg_192_] [get_cells digest_reg_reg_193_] [get_cells                \
digest_reg_reg_194_] [get_cells digest_reg_reg_195_] [get_cells                \
digest_reg_reg_196_] [get_cells digest_reg_reg_197_] [get_cells                \
digest_reg_reg_198_] [get_cells digest_reg_reg_199_] [get_cells                \
digest_reg_reg_200_] [get_cells digest_reg_reg_201_] [get_cells                \
digest_reg_reg_202_] [get_cells digest_reg_reg_203_] [get_cells                \
digest_reg_reg_204_] [get_cells digest_reg_reg_205_] [get_cells                \
digest_reg_reg_206_] [get_cells digest_reg_reg_207_] [get_cells                \
digest_reg_reg_208_] [get_cells digest_reg_reg_209_] [get_cells                \
digest_reg_reg_210_] [get_cells digest_reg_reg_211_] [get_cells                \
digest_reg_reg_212_] [get_cells digest_reg_reg_213_] [get_cells                \
digest_reg_reg_214_] [get_cells digest_reg_reg_215_] [get_cells                \
digest_reg_reg_216_] [get_cells digest_reg_reg_217_] [get_cells                \
digest_reg_reg_218_] [get_cells digest_reg_reg_219_] [get_cells                \
digest_reg_reg_220_] [get_cells digest_reg_reg_221_] [get_cells                \
digest_reg_reg_222_] [get_cells digest_reg_reg_223_] [get_cells                \
digest_reg_reg_224_] [get_cells digest_reg_reg_225_] [get_cells                \
digest_reg_reg_226_] [get_cells digest_reg_reg_227_] [get_cells                \
digest_reg_reg_228_] [get_cells digest_reg_reg_229_] [get_cells                \
digest_reg_reg_230_] [get_cells digest_reg_reg_231_] [get_cells                \
digest_reg_reg_232_] [get_cells digest_reg_reg_233_] [get_cells                \
digest_reg_reg_234_] [get_cells digest_reg_reg_235_] [get_cells                \
digest_reg_reg_236_] [get_cells digest_reg_reg_237_] [get_cells                \
digest_reg_reg_238_] [get_cells digest_reg_reg_239_] [get_cells                \
digest_reg_reg_240_] [get_cells digest_reg_reg_241_] [get_cells                \
digest_reg_reg_242_] [get_cells digest_reg_reg_243_] [get_cells                \
digest_reg_reg_244_] [get_cells digest_reg_reg_245_] [get_cells                \
digest_reg_reg_246_] [get_cells digest_reg_reg_247_] [get_cells                \
digest_reg_reg_248_] [get_cells digest_reg_reg_249_] [get_cells                \
digest_reg_reg_250_] [get_cells digest_reg_reg_251_] [get_cells                \
digest_reg_reg_252_] [get_cells digest_reg_reg_253_] [get_cells                \
digest_reg_reg_254_] [get_cells digest_reg_reg_255_] [get_cells init_reg_reg]  \
[get_cells next_reg_reg] [get_cells mode_reg_reg] [get_cells ready_reg_reg]    \
[get_cells block_reg_reg_15__0_] [get_cells block_reg_reg_15__1_] [get_cells   \
block_reg_reg_15__2_] [get_cells block_reg_reg_15__3_] [get_cells              \
block_reg_reg_15__4_] [get_cells block_reg_reg_15__5_] [get_cells              \
block_reg_reg_15__6_] [get_cells block_reg_reg_15__7_] [get_cells              \
block_reg_reg_15__8_] [get_cells block_reg_reg_15__9_] [get_cells              \
block_reg_reg_15__10_] [get_cells block_reg_reg_15__11_] [get_cells            \
block_reg_reg_15__12_] [get_cells block_reg_reg_15__13_] [get_cells            \
block_reg_reg_15__14_] [get_cells block_reg_reg_15__15_] [get_cells            \
block_reg_reg_15__16_] [get_cells block_reg_reg_15__17_] [get_cells            \
block_reg_reg_15__18_] [get_cells block_reg_reg_15__19_] [get_cells            \
block_reg_reg_15__20_] [get_cells block_reg_reg_15__21_] [get_cells            \
block_reg_reg_15__22_] [get_cells block_reg_reg_15__23_] [get_cells            \
block_reg_reg_15__24_] [get_cells block_reg_reg_15__25_] [get_cells            \
block_reg_reg_15__26_] [get_cells block_reg_reg_15__27_] [get_cells            \
block_reg_reg_15__28_] [get_cells block_reg_reg_15__29_] [get_cells            \
block_reg_reg_15__30_] [get_cells block_reg_reg_15__31_] [get_cells            \
block_reg_reg_14__0_] [get_cells block_reg_reg_14__1_] [get_cells              \
block_reg_reg_14__2_] [get_cells block_reg_reg_14__3_] [get_cells              \
block_reg_reg_14__4_] [get_cells block_reg_reg_14__5_] [get_cells              \
block_reg_reg_14__6_] [get_cells block_reg_reg_14__7_] [get_cells              \
block_reg_reg_14__8_] [get_cells block_reg_reg_14__9_] [get_cells              \
block_reg_reg_14__10_] [get_cells block_reg_reg_14__11_] [get_cells            \
block_reg_reg_14__12_] [get_cells block_reg_reg_14__13_] [get_cells            \
block_reg_reg_14__14_] [get_cells block_reg_reg_14__15_] [get_cells            \
block_reg_reg_14__16_] [get_cells block_reg_reg_14__17_] [get_cells            \
block_reg_reg_14__18_] [get_cells block_reg_reg_14__19_] [get_cells            \
block_reg_reg_14__20_] [get_cells block_reg_reg_14__21_] [get_cells            \
block_reg_reg_14__22_] [get_cells block_reg_reg_14__23_] [get_cells            \
block_reg_reg_14__24_] [get_cells block_reg_reg_14__25_] [get_cells            \
block_reg_reg_14__26_] [get_cells block_reg_reg_14__27_] [get_cells            \
block_reg_reg_14__28_] [get_cells block_reg_reg_14__29_] [get_cells            \
block_reg_reg_14__30_] [get_cells block_reg_reg_14__31_] [get_cells            \
block_reg_reg_13__0_] [get_cells block_reg_reg_13__1_] [get_cells              \
block_reg_reg_13__2_] [get_cells block_reg_reg_13__3_] [get_cells              \
block_reg_reg_13__4_] [get_cells block_reg_reg_13__5_] [get_cells              \
block_reg_reg_13__6_] [get_cells block_reg_reg_13__7_] [get_cells              \
block_reg_reg_13__8_] [get_cells block_reg_reg_13__9_] [get_cells              \
block_reg_reg_13__10_] [get_cells block_reg_reg_13__11_] [get_cells            \
block_reg_reg_13__12_] [get_cells block_reg_reg_13__13_] [get_cells            \
block_reg_reg_13__14_] [get_cells block_reg_reg_13__15_] [get_cells            \
block_reg_reg_13__16_] [get_cells block_reg_reg_13__17_] [get_cells            \
block_reg_reg_13__18_] [get_cells block_reg_reg_13__19_] [get_cells            \
block_reg_reg_13__20_] [get_cells block_reg_reg_13__21_] [get_cells            \
block_reg_reg_13__22_] [get_cells block_reg_reg_13__23_] [get_cells            \
block_reg_reg_13__24_] [get_cells block_reg_reg_13__25_] [get_cells            \
block_reg_reg_13__26_] [get_cells block_reg_reg_13__27_] [get_cells            \
block_reg_reg_13__28_] [get_cells block_reg_reg_13__29_] [get_cells            \
block_reg_reg_13__30_] [get_cells block_reg_reg_13__31_] [get_cells            \
block_reg_reg_12__0_] [get_cells block_reg_reg_12__1_] [get_cells              \
block_reg_reg_12__2_] [get_cells block_reg_reg_12__3_] [get_cells              \
block_reg_reg_12__4_] [get_cells block_reg_reg_12__5_] [get_cells              \
block_reg_reg_12__6_] [get_cells block_reg_reg_12__7_] [get_cells              \
block_reg_reg_12__8_] [get_cells block_reg_reg_12__9_] [get_cells              \
block_reg_reg_12__10_] [get_cells block_reg_reg_12__11_] [get_cells            \
block_reg_reg_12__12_] [get_cells block_reg_reg_12__13_] [get_cells            \
block_reg_reg_12__14_] [get_cells block_reg_reg_12__15_] [get_cells            \
block_reg_reg_12__16_] [get_cells block_reg_reg_12__17_] [get_cells            \
block_reg_reg_12__18_] [get_cells block_reg_reg_12__19_] [get_cells            \
block_reg_reg_12__20_] [get_cells block_reg_reg_12__21_] [get_cells            \
block_reg_reg_12__22_] [get_cells block_reg_reg_12__23_] [get_cells            \
block_reg_reg_12__24_] [get_cells block_reg_reg_12__25_] [get_cells            \
block_reg_reg_12__26_] [get_cells block_reg_reg_12__27_] [get_cells            \
block_reg_reg_12__28_] [get_cells block_reg_reg_12__29_] [get_cells            \
block_reg_reg_12__30_] [get_cells block_reg_reg_12__31_] [get_cells            \
block_reg_reg_11__0_] [get_cells block_reg_reg_11__1_] [get_cells              \
block_reg_reg_11__2_] [get_cells block_reg_reg_11__3_] [get_cells              \
block_reg_reg_11__4_] [get_cells block_reg_reg_11__5_] [get_cells              \
block_reg_reg_11__6_] [get_cells block_reg_reg_11__7_] [get_cells              \
block_reg_reg_11__8_] [get_cells block_reg_reg_11__9_] [get_cells              \
block_reg_reg_11__10_] [get_cells block_reg_reg_11__11_] [get_cells            \
block_reg_reg_11__12_] [get_cells block_reg_reg_11__13_] [get_cells            \
block_reg_reg_11__14_] [get_cells block_reg_reg_11__15_] [get_cells            \
block_reg_reg_11__16_] [get_cells block_reg_reg_11__17_] [get_cells            \
block_reg_reg_11__18_] [get_cells block_reg_reg_11__19_] [get_cells            \
block_reg_reg_11__20_] [get_cells block_reg_reg_11__21_] [get_cells            \
block_reg_reg_11__22_] [get_cells block_reg_reg_11__23_] [get_cells            \
block_reg_reg_11__24_] [get_cells block_reg_reg_11__25_] [get_cells            \
block_reg_reg_11__26_] [get_cells block_reg_reg_11__27_] [get_cells            \
block_reg_reg_11__28_] [get_cells block_reg_reg_11__29_] [get_cells            \
block_reg_reg_11__30_] [get_cells block_reg_reg_11__31_] [get_cells            \
block_reg_reg_10__0_] [get_cells block_reg_reg_10__1_] [get_cells              \
block_reg_reg_10__2_] [get_cells block_reg_reg_10__3_] [get_cells              \
block_reg_reg_10__4_] [get_cells block_reg_reg_10__5_] [get_cells              \
block_reg_reg_10__6_] [get_cells block_reg_reg_10__7_] [get_cells              \
block_reg_reg_10__8_] [get_cells block_reg_reg_10__9_] [get_cells              \
block_reg_reg_10__10_] [get_cells block_reg_reg_10__11_] [get_cells            \
block_reg_reg_10__12_] [get_cells block_reg_reg_10__13_] [get_cells            \
block_reg_reg_10__14_] [get_cells block_reg_reg_10__15_] [get_cells            \
block_reg_reg_10__16_] [get_cells block_reg_reg_10__17_] [get_cells            \
block_reg_reg_10__18_] [get_cells block_reg_reg_10__19_] [get_cells            \
block_reg_reg_10__20_] [get_cells block_reg_reg_10__21_] [get_cells            \
block_reg_reg_10__22_] [get_cells block_reg_reg_10__23_] [get_cells            \
block_reg_reg_10__24_] [get_cells block_reg_reg_10__25_] [get_cells            \
block_reg_reg_10__26_] [get_cells block_reg_reg_10__27_] [get_cells            \
block_reg_reg_10__28_] [get_cells block_reg_reg_10__29_] [get_cells            \
block_reg_reg_10__30_] [get_cells block_reg_reg_10__31_] [get_cells            \
block_reg_reg_9__0_] [get_cells block_reg_reg_9__1_] [get_cells                \
block_reg_reg_9__2_] [get_cells block_reg_reg_9__3_] [get_cells                \
block_reg_reg_9__4_] [get_cells block_reg_reg_9__5_] [get_cells                \
block_reg_reg_9__6_] [get_cells block_reg_reg_9__7_] [get_cells                \
block_reg_reg_9__8_] [get_cells block_reg_reg_9__9_] [get_cells                \
block_reg_reg_9__10_] [get_cells block_reg_reg_9__11_] [get_cells              \
block_reg_reg_9__12_] [get_cells block_reg_reg_9__13_] [get_cells              \
block_reg_reg_9__14_] [get_cells block_reg_reg_9__15_] [get_cells              \
block_reg_reg_9__16_] [get_cells block_reg_reg_9__17_] [get_cells              \
block_reg_reg_9__18_] [get_cells block_reg_reg_9__19_] [get_cells              \
block_reg_reg_9__20_] [get_cells block_reg_reg_9__21_] [get_cells              \
block_reg_reg_9__22_] [get_cells block_reg_reg_9__23_] [get_cells              \
block_reg_reg_9__24_] [get_cells block_reg_reg_9__25_] [get_cells              \
block_reg_reg_9__26_] [get_cells block_reg_reg_9__27_] [get_cells              \
block_reg_reg_9__28_] [get_cells block_reg_reg_9__29_] [get_cells              \
block_reg_reg_9__30_] [get_cells block_reg_reg_9__31_] [get_cells              \
block_reg_reg_8__0_] [get_cells block_reg_reg_8__1_] [get_cells                \
block_reg_reg_8__2_] [get_cells block_reg_reg_8__3_] [get_cells                \
block_reg_reg_8__4_] [get_cells block_reg_reg_8__5_] [get_cells                \
block_reg_reg_8__6_] [get_cells block_reg_reg_8__7_] [get_cells                \
block_reg_reg_8__8_] [get_cells block_reg_reg_8__9_] [get_cells                \
block_reg_reg_8__10_] [get_cells block_reg_reg_8__11_] [get_cells              \
block_reg_reg_8__12_] [get_cells block_reg_reg_8__13_] [get_cells              \
block_reg_reg_8__14_] [get_cells block_reg_reg_8__15_] [get_cells              \
block_reg_reg_8__16_] [get_cells block_reg_reg_8__17_] [get_cells              \
block_reg_reg_8__18_] [get_cells block_reg_reg_8__19_] [get_cells              \
block_reg_reg_8__20_] [get_cells block_reg_reg_8__21_] [get_cells              \
block_reg_reg_8__22_] [get_cells block_reg_reg_8__23_] [get_cells              \
block_reg_reg_8__24_] [get_cells block_reg_reg_8__25_] [get_cells              \
block_reg_reg_8__26_] [get_cells block_reg_reg_8__27_] [get_cells              \
block_reg_reg_8__28_] [get_cells block_reg_reg_8__29_] [get_cells              \
block_reg_reg_8__30_] [get_cells block_reg_reg_8__31_] [get_cells              \
block_reg_reg_7__0_] [get_cells block_reg_reg_7__1_] [get_cells                \
block_reg_reg_7__2_] [get_cells block_reg_reg_7__3_] [get_cells                \
block_reg_reg_7__4_] [get_cells block_reg_reg_7__5_] [get_cells                \
block_reg_reg_7__6_] [get_cells block_reg_reg_7__7_] [get_cells                \
block_reg_reg_7__8_] [get_cells block_reg_reg_7__9_] [get_cells                \
block_reg_reg_7__10_] [get_cells block_reg_reg_7__11_] [get_cells              \
block_reg_reg_7__12_] [get_cells block_reg_reg_7__13_] [get_cells              \
block_reg_reg_7__14_] [get_cells block_reg_reg_7__15_] [get_cells              \
block_reg_reg_7__16_] [get_cells block_reg_reg_7__17_] [get_cells              \
block_reg_reg_7__18_] [get_cells block_reg_reg_7__19_] [get_cells              \
block_reg_reg_7__20_] [get_cells block_reg_reg_7__21_] [get_cells              \
block_reg_reg_7__22_] [get_cells block_reg_reg_7__23_] [get_cells              \
block_reg_reg_7__24_] [get_cells block_reg_reg_7__25_] [get_cells              \
block_reg_reg_7__26_] [get_cells block_reg_reg_7__27_] [get_cells              \
block_reg_reg_7__28_] [get_cells block_reg_reg_7__29_] [get_cells              \
block_reg_reg_7__30_] [get_cells block_reg_reg_7__31_] [get_cells              \
block_reg_reg_6__0_] [get_cells block_reg_reg_6__1_] [get_cells                \
block_reg_reg_6__2_] [get_cells block_reg_reg_6__3_] [get_cells                \
block_reg_reg_6__4_] [get_cells block_reg_reg_6__5_] [get_cells                \
block_reg_reg_6__6_] [get_cells block_reg_reg_6__7_] [get_cells                \
block_reg_reg_6__8_] [get_cells block_reg_reg_6__9_] [get_cells                \
block_reg_reg_6__10_] [get_cells block_reg_reg_6__11_] [get_cells              \
block_reg_reg_6__12_] [get_cells block_reg_reg_6__13_] [get_cells              \
block_reg_reg_6__14_] [get_cells block_reg_reg_6__15_] [get_cells              \
block_reg_reg_6__16_] [get_cells block_reg_reg_6__17_] [get_cells              \
block_reg_reg_6__18_] [get_cells block_reg_reg_6__19_] [get_cells              \
block_reg_reg_6__20_] [get_cells block_reg_reg_6__21_] [get_cells              \
block_reg_reg_6__22_] [get_cells block_reg_reg_6__23_] [get_cells              \
block_reg_reg_6__24_] [get_cells block_reg_reg_6__25_] [get_cells              \
block_reg_reg_6__26_] [get_cells block_reg_reg_6__27_] [get_cells              \
block_reg_reg_6__28_] [get_cells block_reg_reg_6__29_] [get_cells              \
block_reg_reg_6__30_] [get_cells block_reg_reg_6__31_] [get_cells              \
block_reg_reg_5__0_] [get_cells block_reg_reg_5__1_] [get_cells                \
block_reg_reg_5__2_] [get_cells block_reg_reg_5__3_] [get_cells                \
block_reg_reg_5__4_] [get_cells block_reg_reg_5__5_] [get_cells                \
block_reg_reg_5__6_] [get_cells block_reg_reg_5__7_] [get_cells                \
block_reg_reg_5__8_] [get_cells block_reg_reg_5__9_] [get_cells                \
block_reg_reg_5__10_] [get_cells block_reg_reg_5__11_] [get_cells              \
block_reg_reg_5__12_] [get_cells block_reg_reg_5__13_] [get_cells              \
block_reg_reg_5__14_] [get_cells block_reg_reg_5__15_] [get_cells              \
block_reg_reg_5__16_] [get_cells block_reg_reg_5__17_] [get_cells              \
block_reg_reg_5__18_] [get_cells block_reg_reg_5__19_] [get_cells              \
block_reg_reg_5__20_] [get_cells block_reg_reg_5__21_] [get_cells              \
block_reg_reg_5__22_] [get_cells block_reg_reg_5__23_] [get_cells              \
block_reg_reg_5__24_] [get_cells block_reg_reg_5__25_] [get_cells              \
block_reg_reg_5__26_] [get_cells block_reg_reg_5__27_] [get_cells              \
block_reg_reg_5__28_] [get_cells block_reg_reg_5__29_] [get_cells              \
block_reg_reg_5__30_] [get_cells block_reg_reg_5__31_] [get_cells              \
block_reg_reg_4__0_] [get_cells block_reg_reg_4__1_] [get_cells                \
block_reg_reg_4__2_] [get_cells block_reg_reg_4__3_] [get_cells                \
block_reg_reg_4__4_] [get_cells block_reg_reg_4__5_] [get_cells                \
block_reg_reg_4__6_] [get_cells block_reg_reg_4__7_] [get_cells                \
block_reg_reg_4__8_] [get_cells block_reg_reg_4__9_] [get_cells                \
block_reg_reg_4__10_] [get_cells block_reg_reg_4__11_] [get_cells              \
block_reg_reg_4__12_] [get_cells block_reg_reg_4__13_] [get_cells              \
block_reg_reg_4__14_] [get_cells block_reg_reg_4__15_] [get_cells              \
block_reg_reg_4__16_] [get_cells block_reg_reg_4__17_] [get_cells              \
block_reg_reg_4__18_] [get_cells block_reg_reg_4__19_] [get_cells              \
block_reg_reg_4__20_] [get_cells block_reg_reg_4__21_] [get_cells              \
block_reg_reg_4__22_] [get_cells block_reg_reg_4__23_] [get_cells              \
block_reg_reg_4__24_] [get_cells block_reg_reg_4__25_] [get_cells              \
block_reg_reg_4__26_] [get_cells block_reg_reg_4__27_] [get_cells              \
block_reg_reg_4__28_] [get_cells block_reg_reg_4__29_] [get_cells              \
block_reg_reg_4__30_] [get_cells block_reg_reg_4__31_] [get_cells              \
block_reg_reg_3__0_] [get_cells block_reg_reg_3__1_] [get_cells                \
block_reg_reg_3__2_] [get_cells block_reg_reg_3__3_] [get_cells                \
block_reg_reg_3__4_] [get_cells block_reg_reg_3__5_] [get_cells                \
block_reg_reg_3__6_] [get_cells block_reg_reg_3__7_] [get_cells                \
block_reg_reg_3__8_] [get_cells block_reg_reg_3__9_] [get_cells                \
block_reg_reg_3__10_] [get_cells block_reg_reg_3__11_] [get_cells              \
block_reg_reg_3__12_] [get_cells block_reg_reg_3__13_] [get_cells              \
block_reg_reg_3__14_] [get_cells block_reg_reg_3__15_] [get_cells              \
block_reg_reg_3__16_] [get_cells block_reg_reg_3__17_] [get_cells              \
block_reg_reg_3__18_] [get_cells block_reg_reg_3__19_] [get_cells              \
block_reg_reg_3__20_] [get_cells block_reg_reg_3__21_] [get_cells              \
block_reg_reg_3__22_] [get_cells block_reg_reg_3__23_] [get_cells              \
block_reg_reg_3__24_] [get_cells block_reg_reg_3__25_] [get_cells              \
block_reg_reg_3__26_] [get_cells block_reg_reg_3__27_] [get_cells              \
block_reg_reg_3__28_] [get_cells block_reg_reg_3__29_] [get_cells              \
block_reg_reg_3__30_] [get_cells block_reg_reg_3__31_] [get_cells              \
block_reg_reg_2__0_] [get_cells block_reg_reg_2__1_] [get_cells                \
block_reg_reg_2__2_] [get_cells block_reg_reg_2__3_] [get_cells                \
block_reg_reg_2__4_] [get_cells block_reg_reg_2__5_] [get_cells                \
block_reg_reg_2__6_] [get_cells block_reg_reg_2__7_] [get_cells                \
block_reg_reg_2__8_] [get_cells block_reg_reg_2__9_] [get_cells                \
block_reg_reg_2__10_] [get_cells block_reg_reg_2__11_] [get_cells              \
block_reg_reg_2__12_] [get_cells block_reg_reg_2__13_] [get_cells              \
block_reg_reg_2__14_] [get_cells block_reg_reg_2__15_] [get_cells              \
block_reg_reg_2__16_] [get_cells block_reg_reg_2__17_] [get_cells              \
block_reg_reg_2__18_] [get_cells block_reg_reg_2__19_] [get_cells              \
block_reg_reg_2__20_] [get_cells block_reg_reg_2__21_] [get_cells              \
block_reg_reg_2__22_] [get_cells block_reg_reg_2__23_] [get_cells              \
block_reg_reg_2__24_] [get_cells block_reg_reg_2__25_] [get_cells              \
block_reg_reg_2__26_] [get_cells block_reg_reg_2__27_] [get_cells              \
block_reg_reg_2__28_] [get_cells block_reg_reg_2__29_] [get_cells              \
block_reg_reg_2__30_] [get_cells block_reg_reg_2__31_] [get_cells              \
block_reg_reg_1__0_] [get_cells block_reg_reg_1__1_] [get_cells                \
block_reg_reg_1__2_] [get_cells block_reg_reg_1__3_] [get_cells                \
block_reg_reg_1__4_] [get_cells block_reg_reg_1__5_] [get_cells                \
block_reg_reg_1__6_] [get_cells block_reg_reg_1__7_] [get_cells                \
block_reg_reg_1__8_] [get_cells block_reg_reg_1__9_] [get_cells                \
block_reg_reg_1__10_] [get_cells block_reg_reg_1__11_] [get_cells              \
block_reg_reg_1__12_] [get_cells block_reg_reg_1__13_] [get_cells              \
block_reg_reg_1__14_] [get_cells block_reg_reg_1__15_] [get_cells              \
block_reg_reg_1__16_] [get_cells block_reg_reg_1__17_] [get_cells              \
block_reg_reg_1__18_] [get_cells block_reg_reg_1__19_] [get_cells              \
block_reg_reg_1__20_] [get_cells block_reg_reg_1__21_] [get_cells              \
block_reg_reg_1__22_] [get_cells block_reg_reg_1__23_] [get_cells              \
block_reg_reg_1__24_] [get_cells block_reg_reg_1__25_] [get_cells              \
block_reg_reg_1__26_] [get_cells block_reg_reg_1__27_] [get_cells              \
block_reg_reg_1__28_] [get_cells block_reg_reg_1__29_] [get_cells              \
block_reg_reg_1__30_] [get_cells block_reg_reg_1__31_] [get_cells              \
block_reg_reg_0__0_] [get_cells block_reg_reg_0__1_] [get_cells                \
block_reg_reg_0__2_] [get_cells block_reg_reg_0__3_] [get_cells                \
block_reg_reg_0__4_] [get_cells block_reg_reg_0__5_] [get_cells                \
block_reg_reg_0__6_] [get_cells block_reg_reg_0__7_] [get_cells                \
block_reg_reg_0__8_] [get_cells block_reg_reg_0__9_] [get_cells                \
block_reg_reg_0__10_] [get_cells block_reg_reg_0__11_] [get_cells              \
block_reg_reg_0__12_] [get_cells block_reg_reg_0__13_] [get_cells              \
block_reg_reg_0__14_] [get_cells block_reg_reg_0__15_] [get_cells              \
block_reg_reg_0__16_] [get_cells block_reg_reg_0__17_] [get_cells              \
block_reg_reg_0__18_] [get_cells block_reg_reg_0__19_] [get_cells              \
block_reg_reg_0__20_] [get_cells block_reg_reg_0__21_] [get_cells              \
block_reg_reg_0__22_] [get_cells block_reg_reg_0__23_] [get_cells              \
block_reg_reg_0__24_] [get_cells block_reg_reg_0__25_] [get_cells              \
block_reg_reg_0__26_] [get_cells block_reg_reg_0__27_] [get_cells              \
block_reg_reg_0__28_] [get_cells block_reg_reg_0__29_] [get_cells              \
block_reg_reg_0__30_] [get_cells block_reg_reg_0__31_] [get_cells              \
core_H3_reg_reg_0_] [get_cells core_H3_reg_reg_1_] [get_cells                  \
core_H3_reg_reg_2_] [get_cells core_H3_reg_reg_3_] [get_cells                  \
core_H3_reg_reg_4_] [get_cells core_H3_reg_reg_5_] [get_cells                  \
core_H3_reg_reg_6_] [get_cells core_H3_reg_reg_7_] [get_cells                  \
core_H3_reg_reg_8_] [get_cells core_H3_reg_reg_9_] [get_cells                  \
core_H3_reg_reg_10_] [get_cells core_H3_reg_reg_11_] [get_cells                \
core_H3_reg_reg_12_] [get_cells core_H3_reg_reg_13_] [get_cells                \
core_H3_reg_reg_14_] [get_cells core_H3_reg_reg_15_] [get_cells                \
core_H3_reg_reg_16_] [get_cells core_H3_reg_reg_17_] [get_cells                \
core_H3_reg_reg_18_] [get_cells core_H3_reg_reg_19_] [get_cells                \
core_H3_reg_reg_20_] [get_cells core_H3_reg_reg_21_] [get_cells                \
core_H3_reg_reg_22_] [get_cells core_H3_reg_reg_23_] [get_cells                \
core_H3_reg_reg_24_] [get_cells core_H3_reg_reg_25_] [get_cells                \
core_H3_reg_reg_26_] [get_cells core_H3_reg_reg_27_] [get_cells                \
core_H3_reg_reg_28_] [get_cells core_H3_reg_reg_29_] [get_cells                \
core_H3_reg_reg_30_] [get_cells core_H3_reg_reg_31_] [get_cells                \
core_H2_reg_reg_0_] [get_cells core_H2_reg_reg_1_] [get_cells                  \
core_H2_reg_reg_2_] [get_cells core_H2_reg_reg_3_] [get_cells                  \
core_H2_reg_reg_4_] [get_cells core_H2_reg_reg_5_] [get_cells                  \
core_H2_reg_reg_6_] [get_cells core_H2_reg_reg_7_] [get_cells                  \
core_H2_reg_reg_8_] [get_cells core_H2_reg_reg_9_] [get_cells                  \
core_H2_reg_reg_10_] [get_cells core_H2_reg_reg_11_] [get_cells                \
core_H2_reg_reg_12_] [get_cells core_H2_reg_reg_13_] [get_cells                \
core_H2_reg_reg_14_] [get_cells core_H2_reg_reg_15_] [get_cells                \
core_H2_reg_reg_16_] [get_cells core_H2_reg_reg_17_] [get_cells                \
core_H2_reg_reg_18_] [get_cells core_H2_reg_reg_19_] [get_cells                \
core_H2_reg_reg_20_] [get_cells core_H2_reg_reg_21_] [get_cells                \
core_H2_reg_reg_22_] [get_cells core_H2_reg_reg_23_] [get_cells                \
core_H2_reg_reg_24_] [get_cells core_H2_reg_reg_25_] [get_cells                \
core_H2_reg_reg_26_] [get_cells core_H2_reg_reg_27_] [get_cells                \
core_H2_reg_reg_28_] [get_cells core_H2_reg_reg_29_] [get_cells                \
core_H2_reg_reg_30_] [get_cells core_H2_reg_reg_31_] [get_cells                \
core_H1_reg_reg_0_] [get_cells core_H1_reg_reg_1_] [get_cells                  \
core_H1_reg_reg_2_] [get_cells core_H1_reg_reg_3_] [get_cells                  \
core_H1_reg_reg_4_] [get_cells core_H1_reg_reg_5_] [get_cells                  \
core_H1_reg_reg_6_] [get_cells core_H1_reg_reg_7_] [get_cells                  \
core_H1_reg_reg_8_] [get_cells core_H1_reg_reg_9_] [get_cells                  \
core_H1_reg_reg_10_] [get_cells core_H1_reg_reg_11_] [get_cells                \
core_H1_reg_reg_12_] [get_cells core_H1_reg_reg_13_] [get_cells                \
core_H1_reg_reg_14_] [get_cells core_H1_reg_reg_15_] [get_cells                \
core_H1_reg_reg_16_] [get_cells core_H1_reg_reg_17_] [get_cells                \
core_H1_reg_reg_18_] [get_cells core_H1_reg_reg_19_] [get_cells                \
core_H1_reg_reg_20_] [get_cells core_H1_reg_reg_21_] [get_cells                \
core_H1_reg_reg_22_] [get_cells core_H1_reg_reg_23_] [get_cells                \
core_H1_reg_reg_24_] [get_cells core_H1_reg_reg_25_] [get_cells                \
core_H1_reg_reg_26_] [get_cells core_H1_reg_reg_27_] [get_cells                \
core_H1_reg_reg_28_] [get_cells core_H1_reg_reg_29_] [get_cells                \
core_H1_reg_reg_30_] [get_cells core_H1_reg_reg_31_] [get_cells                \
core_H0_reg_reg_0_] [get_cells core_H0_reg_reg_1_] [get_cells                  \
core_H0_reg_reg_2_] [get_cells core_H0_reg_reg_3_] [get_cells                  \
core_H0_reg_reg_4_] [get_cells core_H0_reg_reg_5_] [get_cells                  \
core_H0_reg_reg_6_] [get_cells core_H0_reg_reg_7_] [get_cells                  \
core_H0_reg_reg_8_] [get_cells core_H0_reg_reg_9_] [get_cells                  \
core_H0_reg_reg_10_] [get_cells core_H0_reg_reg_11_] [get_cells                \
core_H0_reg_reg_12_] [get_cells core_H0_reg_reg_13_] [get_cells                \
core_H0_reg_reg_14_] [get_cells core_H0_reg_reg_15_] [get_cells                \
core_H0_reg_reg_16_] [get_cells core_H0_reg_reg_17_] [get_cells                \
core_H0_reg_reg_18_] [get_cells core_H0_reg_reg_19_] [get_cells                \
core_H0_reg_reg_20_] [get_cells core_H0_reg_reg_21_] [get_cells                \
core_H0_reg_reg_22_] [get_cells core_H0_reg_reg_23_] [get_cells                \
core_H0_reg_reg_24_] [get_cells core_H0_reg_reg_25_] [get_cells                \
core_H0_reg_reg_26_] [get_cells core_H0_reg_reg_27_] [get_cells                \
core_H0_reg_reg_28_] [get_cells core_H0_reg_reg_29_] [get_cells                \
core_H0_reg_reg_30_] [get_cells core_H0_reg_reg_31_] [get_cells                \
core_h_reg_reg_0_] [get_cells core_h_reg_reg_1_] [get_cells core_h_reg_reg_2_] \
[get_cells core_h_reg_reg_3_] [get_cells core_h_reg_reg_4_] [get_cells         \
core_h_reg_reg_5_] [get_cells core_h_reg_reg_6_] [get_cells core_h_reg_reg_7_] \
[get_cells core_h_reg_reg_8_] [get_cells core_h_reg_reg_9_] [get_cells         \
core_h_reg_reg_10_] [get_cells core_h_reg_reg_11_] [get_cells                  \
core_h_reg_reg_12_] [get_cells core_h_reg_reg_13_] [get_cells                  \
core_h_reg_reg_14_] [get_cells core_h_reg_reg_15_] [get_cells                  \
core_h_reg_reg_16_] [get_cells core_h_reg_reg_17_] [get_cells                  \
core_h_reg_reg_18_] [get_cells core_h_reg_reg_19_] [get_cells                  \
core_h_reg_reg_20_] [get_cells core_h_reg_reg_21_] [get_cells                  \
core_h_reg_reg_22_] [get_cells core_h_reg_reg_23_] [get_cells                  \
core_h_reg_reg_24_] [get_cells core_h_reg_reg_25_] [get_cells                  \
core_h_reg_reg_26_] [get_cells core_h_reg_reg_27_] [get_cells                  \
core_h_reg_reg_28_] [get_cells core_h_reg_reg_29_] [get_cells                  \
core_h_reg_reg_30_] [get_cells core_h_reg_reg_31_] [get_cells                  \
core_g_reg_reg_0_] [get_cells core_g_reg_reg_1_] [get_cells core_g_reg_reg_2_] \
[get_cells core_g_reg_reg_3_] [get_cells core_g_reg_reg_4_] [get_cells         \
core_g_reg_reg_5_] [get_cells core_g_reg_reg_6_] [get_cells core_g_reg_reg_7_] \
[get_cells core_g_reg_reg_8_] [get_cells core_g_reg_reg_9_] [get_cells         \
core_g_reg_reg_10_] [get_cells core_g_reg_reg_11_] [get_cells                  \
core_g_reg_reg_12_] [get_cells core_g_reg_reg_13_] [get_cells                  \
core_g_reg_reg_14_] [get_cells core_g_reg_reg_15_] [get_cells                  \
core_g_reg_reg_16_] [get_cells core_g_reg_reg_17_] [get_cells                  \
core_g_reg_reg_18_] [get_cells core_g_reg_reg_19_] [get_cells                  \
core_g_reg_reg_20_] [get_cells core_g_reg_reg_21_] [get_cells                  \
core_g_reg_reg_22_] [get_cells core_g_reg_reg_23_] [get_cells                  \
core_g_reg_reg_24_] [get_cells core_g_reg_reg_25_] [get_cells                  \
core_g_reg_reg_26_] [get_cells core_g_reg_reg_27_] [get_cells                  \
core_g_reg_reg_28_] [get_cells core_g_reg_reg_29_] [get_cells                  \
core_g_reg_reg_30_] [get_cells core_g_reg_reg_31_] [get_cells                  \
core_f_reg_reg_0_] [get_cells core_f_reg_reg_1_] [get_cells core_f_reg_reg_2_] \
[get_cells core_f_reg_reg_3_] [get_cells core_f_reg_reg_4_] [get_cells         \
core_f_reg_reg_5_] [get_cells core_f_reg_reg_6_] [get_cells core_f_reg_reg_7_] \
[get_cells core_f_reg_reg_8_] [get_cells core_f_reg_reg_9_] [get_cells         \
core_f_reg_reg_10_] [get_cells core_f_reg_reg_11_] [get_cells                  \
core_f_reg_reg_12_] [get_cells core_f_reg_reg_13_] [get_cells                  \
core_f_reg_reg_14_] [get_cells core_f_reg_reg_15_] [get_cells                  \
core_f_reg_reg_16_] [get_cells core_f_reg_reg_17_] [get_cells                  \
core_f_reg_reg_18_] [get_cells core_f_reg_reg_19_] [get_cells                  \
core_f_reg_reg_20_] [get_cells core_f_reg_reg_21_] [get_cells                  \
core_f_reg_reg_22_] [get_cells core_f_reg_reg_23_] [get_cells                  \
core_f_reg_reg_24_] [get_cells core_f_reg_reg_25_] [get_cells                  \
core_f_reg_reg_26_] [get_cells core_f_reg_reg_27_] [get_cells                  \
core_f_reg_reg_28_] [get_cells core_f_reg_reg_29_] [get_cells                  \
core_f_reg_reg_30_] [get_cells core_f_reg_reg_31_] [get_cells                  \
core_e_reg_reg_0_] [get_cells core_e_reg_reg_1_] [get_cells core_e_reg_reg_2_] \
[get_cells core_e_reg_reg_3_] [get_cells core_e_reg_reg_4_] [get_cells         \
core_e_reg_reg_5_] [get_cells core_e_reg_reg_6_] [get_cells core_e_reg_reg_7_] \
[get_cells core_e_reg_reg_8_] [get_cells core_e_reg_reg_9_] [get_cells         \
core_e_reg_reg_10_] [get_cells core_e_reg_reg_11_] [get_cells                  \
core_e_reg_reg_12_] [get_cells core_e_reg_reg_13_] [get_cells                  \
core_e_reg_reg_14_] [get_cells core_e_reg_reg_15_] [get_cells                  \
core_e_reg_reg_16_] [get_cells core_e_reg_reg_17_] [get_cells                  \
core_e_reg_reg_18_] [get_cells core_e_reg_reg_19_] [get_cells                  \
core_e_reg_reg_20_] [get_cells core_e_reg_reg_21_] [get_cells                  \
core_e_reg_reg_22_] [get_cells core_e_reg_reg_23_] [get_cells                  \
core_e_reg_reg_24_] [get_cells core_e_reg_reg_25_] [get_cells                  \
core_e_reg_reg_26_] [get_cells core_e_reg_reg_27_] [get_cells                  \
core_e_reg_reg_28_] [get_cells core_e_reg_reg_29_] [get_cells                  \
core_e_reg_reg_30_] [get_cells core_e_reg_reg_31_] [get_cells                  \
core_d_reg_reg_0_] [get_cells core_d_reg_reg_1_] [get_cells core_d_reg_reg_2_] \
[get_cells core_d_reg_reg_3_] [get_cells core_d_reg_reg_4_] [get_cells         \
core_d_reg_reg_5_] [get_cells core_d_reg_reg_6_] [get_cells core_d_reg_reg_7_] \
[get_cells core_d_reg_reg_8_] [get_cells core_d_reg_reg_9_] [get_cells         \
core_d_reg_reg_10_] [get_cells core_d_reg_reg_11_] [get_cells                  \
core_d_reg_reg_12_] [get_cells core_d_reg_reg_13_] [get_cells                  \
core_d_reg_reg_14_] [get_cells core_d_reg_reg_15_] [get_cells                  \
core_d_reg_reg_16_] [get_cells core_d_reg_reg_17_] [get_cells                  \
core_d_reg_reg_18_] [get_cells core_d_reg_reg_19_] [get_cells                  \
core_d_reg_reg_20_] [get_cells core_d_reg_reg_21_] [get_cells                  \
core_d_reg_reg_22_] [get_cells core_d_reg_reg_23_] [get_cells                  \
core_d_reg_reg_24_] [get_cells core_d_reg_reg_25_] [get_cells                  \
core_d_reg_reg_26_] [get_cells core_d_reg_reg_27_] [get_cells                  \
core_d_reg_reg_28_] [get_cells core_d_reg_reg_29_] [get_cells                  \
core_d_reg_reg_30_] [get_cells core_d_reg_reg_31_] [get_cells                  \
core_c_reg_reg_0_] [get_cells core_c_reg_reg_1_] [get_cells core_c_reg_reg_2_] \
[get_cells core_c_reg_reg_3_] [get_cells core_c_reg_reg_4_] [get_cells         \
core_c_reg_reg_5_] [get_cells core_c_reg_reg_6_] [get_cells core_c_reg_reg_7_] \
[get_cells core_c_reg_reg_8_] [get_cells core_c_reg_reg_9_] [get_cells         \
core_c_reg_reg_10_] [get_cells core_c_reg_reg_11_] [get_cells                  \
core_c_reg_reg_12_] [get_cells core_c_reg_reg_13_] [get_cells                  \
core_c_reg_reg_14_] [get_cells core_c_reg_reg_15_] [get_cells                  \
core_c_reg_reg_16_] [get_cells core_c_reg_reg_17_] [get_cells                  \
core_c_reg_reg_18_] [get_cells core_c_reg_reg_19_] [get_cells                  \
core_c_reg_reg_20_] [get_cells core_c_reg_reg_21_] [get_cells                  \
core_c_reg_reg_22_] [get_cells core_c_reg_reg_23_] [get_cells                  \
core_c_reg_reg_24_] [get_cells core_c_reg_reg_25_] [get_cells                  \
core_c_reg_reg_26_] [get_cells core_c_reg_reg_27_] [get_cells                  \
core_c_reg_reg_28_] [get_cells core_c_reg_reg_29_] [get_cells                  \
core_c_reg_reg_30_] [get_cells core_c_reg_reg_31_] [get_cells                  \
core_b_reg_reg_0_] [get_cells core_b_reg_reg_1_] [get_cells core_b_reg_reg_2_] \
[get_cells core_b_reg_reg_3_] [get_cells core_b_reg_reg_4_] [get_cells         \
core_b_reg_reg_5_] [get_cells core_b_reg_reg_6_] [get_cells core_b_reg_reg_7_] \
[get_cells core_b_reg_reg_8_] [get_cells core_b_reg_reg_9_] [get_cells         \
core_b_reg_reg_10_] [get_cells core_b_reg_reg_11_] [get_cells                  \
core_b_reg_reg_12_] [get_cells core_b_reg_reg_13_] [get_cells                  \
core_b_reg_reg_14_] [get_cells core_b_reg_reg_15_] [get_cells                  \
core_b_reg_reg_16_] [get_cells core_b_reg_reg_17_] [get_cells                  \
core_b_reg_reg_18_] [get_cells core_b_reg_reg_19_] [get_cells                  \
core_b_reg_reg_20_] [get_cells core_b_reg_reg_21_] [get_cells                  \
core_b_reg_reg_22_] [get_cells core_b_reg_reg_23_] [get_cells                  \
core_b_reg_reg_24_] [get_cells core_b_reg_reg_25_] [get_cells                  \
core_b_reg_reg_26_] [get_cells core_b_reg_reg_27_] [get_cells                  \
core_b_reg_reg_28_] [get_cells core_b_reg_reg_29_] [get_cells                  \
core_b_reg_reg_30_] [get_cells core_b_reg_reg_31_] [get_cells                  \
core_a_reg_reg_0_] [get_cells core_a_reg_reg_1_] [get_cells core_a_reg_reg_2_] \
[get_cells core_a_reg_reg_3_] [get_cells core_a_reg_reg_4_] [get_cells         \
core_a_reg_reg_5_] [get_cells core_a_reg_reg_6_] [get_cells core_a_reg_reg_7_] \
[get_cells core_a_reg_reg_8_] [get_cells core_a_reg_reg_9_] [get_cells         \
core_a_reg_reg_10_] [get_cells core_a_reg_reg_11_] [get_cells                  \
core_a_reg_reg_12_] [get_cells core_a_reg_reg_13_] [get_cells                  \
core_a_reg_reg_14_] [get_cells core_a_reg_reg_15_] [get_cells                  \
core_a_reg_reg_16_] [get_cells core_a_reg_reg_17_] [get_cells                  \
core_a_reg_reg_18_] [get_cells core_a_reg_reg_19_] [get_cells                  \
core_a_reg_reg_20_] [get_cells core_a_reg_reg_21_] [get_cells                  \
core_a_reg_reg_22_] [get_cells core_a_reg_reg_23_] [get_cells                  \
core_a_reg_reg_24_] [get_cells core_a_reg_reg_25_] [get_cells                  \
core_a_reg_reg_26_] [get_cells core_a_reg_reg_27_] [get_cells                  \
core_a_reg_reg_28_] [get_cells core_a_reg_reg_29_] [get_cells                  \
core_a_reg_reg_30_] [get_cells core_a_reg_reg_31_] [get_cells                  \
core_sha256_ctrl_reg_reg_0_] [get_cells core_sha256_ctrl_reg_reg_1_]           \
[get_cells core_H5_reg_reg_0_] [get_cells core_H5_reg_reg_1_] [get_cells       \
core_H5_reg_reg_2_] [get_cells core_H5_reg_reg_3_] [get_cells                  \
core_H5_reg_reg_4_] [get_cells core_H5_reg_reg_5_] [get_cells                  \
core_H5_reg_reg_6_] [get_cells core_H5_reg_reg_7_] [get_cells                  \
core_H5_reg_reg_8_] [get_cells core_H5_reg_reg_9_] [get_cells                  \
core_H5_reg_reg_10_] [get_cells core_H5_reg_reg_11_] [get_cells                \
core_H5_reg_reg_12_] [get_cells core_H5_reg_reg_13_] [get_cells                \
core_H5_reg_reg_14_] [get_cells core_H5_reg_reg_15_] [get_cells                \
core_H5_reg_reg_16_] [get_cells core_H5_reg_reg_17_] [get_cells                \
core_H5_reg_reg_18_] [get_cells core_H5_reg_reg_19_] [get_cells                \
core_H5_reg_reg_20_] [get_cells core_H5_reg_reg_21_] [get_cells                \
core_H5_reg_reg_22_] [get_cells core_H5_reg_reg_23_] [get_cells                \
core_H5_reg_reg_24_] [get_cells core_H5_reg_reg_25_] [get_cells                \
core_H5_reg_reg_26_] [get_cells core_H5_reg_reg_27_] [get_cells                \
core_H5_reg_reg_28_] [get_cells core_H5_reg_reg_29_] [get_cells                \
core_H5_reg_reg_30_] [get_cells core_H5_reg_reg_31_] [get_cells                \
core_H6_reg_reg_0_] [get_cells core_H6_reg_reg_1_] [get_cells                  \
core_H6_reg_reg_2_] [get_cells core_H6_reg_reg_3_] [get_cells                  \
core_H6_reg_reg_4_] [get_cells core_H6_reg_reg_5_] [get_cells                  \
core_H6_reg_reg_6_] [get_cells core_H6_reg_reg_7_] [get_cells                  \
core_H6_reg_reg_8_] [get_cells core_H6_reg_reg_9_] [get_cells                  \
core_H6_reg_reg_10_] [get_cells core_H6_reg_reg_11_] [get_cells                \
core_H6_reg_reg_12_] [get_cells core_H6_reg_reg_13_] [get_cells                \
core_H6_reg_reg_14_] [get_cells core_H6_reg_reg_15_] [get_cells                \
core_H6_reg_reg_16_] [get_cells core_H6_reg_reg_17_] [get_cells                \
core_H6_reg_reg_18_] [get_cells core_H6_reg_reg_19_] [get_cells                \
core_H6_reg_reg_20_] [get_cells core_H6_reg_reg_21_] [get_cells                \
core_H6_reg_reg_22_] [get_cells core_H6_reg_reg_23_] [get_cells                \
core_H6_reg_reg_24_] [get_cells core_H6_reg_reg_25_] [get_cells                \
core_H6_reg_reg_26_] [get_cells core_H6_reg_reg_27_] [get_cells                \
core_H6_reg_reg_28_] [get_cells core_H6_reg_reg_29_] [get_cells                \
core_H6_reg_reg_30_] [get_cells core_H6_reg_reg_31_] [get_cells                \
core_H7_reg_reg_0_] [get_cells core_H7_reg_reg_1_] [get_cells                  \
core_H7_reg_reg_2_] [get_cells core_H7_reg_reg_3_] [get_cells                  \
core_H7_reg_reg_4_] [get_cells core_H7_reg_reg_5_] [get_cells                  \
core_H7_reg_reg_6_] [get_cells core_H7_reg_reg_7_] [get_cells                  \
core_H7_reg_reg_8_] [get_cells core_H7_reg_reg_9_] [get_cells                  \
core_H7_reg_reg_10_] [get_cells core_H7_reg_reg_11_] [get_cells                \
core_H7_reg_reg_12_] [get_cells core_H7_reg_reg_13_] [get_cells                \
core_H7_reg_reg_14_] [get_cells core_H7_reg_reg_15_] [get_cells                \
core_H7_reg_reg_16_] [get_cells core_H7_reg_reg_17_] [get_cells                \
core_H7_reg_reg_18_] [get_cells core_H7_reg_reg_19_] [get_cells                \
core_H7_reg_reg_20_] [get_cells core_H7_reg_reg_21_] [get_cells                \
core_H7_reg_reg_22_] [get_cells core_H7_reg_reg_23_] [get_cells                \
core_H7_reg_reg_24_] [get_cells core_H7_reg_reg_25_] [get_cells                \
core_H7_reg_reg_26_] [get_cells core_H7_reg_reg_27_] [get_cells                \
core_H7_reg_reg_28_] [get_cells core_H7_reg_reg_29_] [get_cells                \
core_H7_reg_reg_30_] [get_cells core_H7_reg_reg_31_] [get_cells                \
core_digest_valid_reg_reg] [get_cells core_t_ctr_reg_reg_0_] [get_cells        \
core_t_ctr_reg_reg_1_] [get_cells core_t_ctr_reg_reg_2_] [get_cells            \
core_t_ctr_reg_reg_3_] [get_cells core_t_ctr_reg_reg_4_] [get_cells            \
core_t_ctr_reg_reg_5_] [get_cells core_H4_reg_reg_0_] [get_cells               \
core_H4_reg_reg_1_] [get_cells core_H4_reg_reg_2_] [get_cells                  \
core_H4_reg_reg_3_] [get_cells core_H4_reg_reg_4_] [get_cells                  \
core_H4_reg_reg_5_] [get_cells core_H4_reg_reg_6_] [get_cells                  \
core_H4_reg_reg_7_] [get_cells core_H4_reg_reg_8_] [get_cells                  \
core_H4_reg_reg_9_] [get_cells core_H4_reg_reg_10_] [get_cells                 \
core_H4_reg_reg_11_] [get_cells core_H4_reg_reg_12_] [get_cells                \
core_H4_reg_reg_13_] [get_cells core_H4_reg_reg_14_] [get_cells                \
core_H4_reg_reg_15_] [get_cells core_H4_reg_reg_16_] [get_cells                \
core_H4_reg_reg_17_] [get_cells core_H4_reg_reg_18_] [get_cells                \
core_H4_reg_reg_19_] [get_cells core_H4_reg_reg_20_] [get_cells                \
core_H4_reg_reg_21_] [get_cells core_H4_reg_reg_22_] [get_cells                \
core_H4_reg_reg_23_] [get_cells core_H4_reg_reg_24_] [get_cells                \
core_H4_reg_reg_25_] [get_cells core_H4_reg_reg_26_] [get_cells                \
core_H4_reg_reg_27_] [get_cells core_H4_reg_reg_28_] [get_cells                \
core_H4_reg_reg_29_] [get_cells core_H4_reg_reg_30_] [get_cells                \
core_H4_reg_reg_31_] [get_cells core_w_mem_inst_w_mem_reg_15__0_] [get_cells   \
core_w_mem_inst_w_mem_reg_15__1_] [get_cells core_w_mem_inst_w_mem_reg_15__2_] \
[get_cells core_w_mem_inst_w_mem_reg_15__3_] [get_cells                        \
core_w_mem_inst_w_mem_reg_15__4_] [get_cells core_w_mem_inst_w_mem_reg_15__5_] \
[get_cells core_w_mem_inst_w_mem_reg_15__6_] [get_cells                        \
core_w_mem_inst_w_mem_reg_15__7_] [get_cells core_w_mem_inst_w_mem_reg_15__8_] \
[get_cells core_w_mem_inst_w_mem_reg_15__9_] [get_cells                        \
core_w_mem_inst_w_mem_reg_15__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_15__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__0_] [get_cells core_w_mem_inst_w_mem_reg_14__1_] \
[get_cells core_w_mem_inst_w_mem_reg_14__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_14__3_] [get_cells core_w_mem_inst_w_mem_reg_14__4_] \
[get_cells core_w_mem_inst_w_mem_reg_14__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_14__6_] [get_cells core_w_mem_inst_w_mem_reg_14__7_] \
[get_cells core_w_mem_inst_w_mem_reg_14__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_14__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_14__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_14__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__0_] [get_cells core_w_mem_inst_w_mem_reg_13__1_] \
[get_cells core_w_mem_inst_w_mem_reg_13__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_13__3_] [get_cells core_w_mem_inst_w_mem_reg_13__4_] \
[get_cells core_w_mem_inst_w_mem_reg_13__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_13__6_] [get_cells core_w_mem_inst_w_mem_reg_13__7_] \
[get_cells core_w_mem_inst_w_mem_reg_13__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_13__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_13__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_13__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__0_] [get_cells core_w_mem_inst_w_mem_reg_12__1_] \
[get_cells core_w_mem_inst_w_mem_reg_12__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_12__3_] [get_cells core_w_mem_inst_w_mem_reg_12__4_] \
[get_cells core_w_mem_inst_w_mem_reg_12__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_12__6_] [get_cells core_w_mem_inst_w_mem_reg_12__7_] \
[get_cells core_w_mem_inst_w_mem_reg_12__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_12__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_12__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_12__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__0_] [get_cells core_w_mem_inst_w_mem_reg_11__1_] \
[get_cells core_w_mem_inst_w_mem_reg_11__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_11__3_] [get_cells core_w_mem_inst_w_mem_reg_11__4_] \
[get_cells core_w_mem_inst_w_mem_reg_11__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_11__6_] [get_cells core_w_mem_inst_w_mem_reg_11__7_] \
[get_cells core_w_mem_inst_w_mem_reg_11__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_11__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_11__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_11__31_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__0_] [get_cells core_w_mem_inst_w_mem_reg_10__1_] \
[get_cells core_w_mem_inst_w_mem_reg_10__2_] [get_cells                        \
core_w_mem_inst_w_mem_reg_10__3_] [get_cells core_w_mem_inst_w_mem_reg_10__4_] \
[get_cells core_w_mem_inst_w_mem_reg_10__5_] [get_cells                        \
core_w_mem_inst_w_mem_reg_10__6_] [get_cells core_w_mem_inst_w_mem_reg_10__7_] \
[get_cells core_w_mem_inst_w_mem_reg_10__8_] [get_cells                        \
core_w_mem_inst_w_mem_reg_10__9_] [get_cells                                   \
core_w_mem_inst_w_mem_reg_10__10_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__11_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__12_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__13_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__14_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__15_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__16_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__17_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__18_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__19_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__20_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__21_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__22_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__23_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__24_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__25_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__26_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__27_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__28_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__29_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__30_] [get_cells                                  \
core_w_mem_inst_w_mem_reg_10__31_] [get_cells core_w_mem_inst_w_mem_reg_9__0_] \
[get_cells core_w_mem_inst_w_mem_reg_9__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_9__2_] [get_cells core_w_mem_inst_w_mem_reg_9__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_9__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_9__5_] [get_cells core_w_mem_inst_w_mem_reg_9__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_9__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_9__8_] [get_cells core_w_mem_inst_w_mem_reg_9__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_9__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__11_] [get_cells core_w_mem_inst_w_mem_reg_9__12_] \
[get_cells core_w_mem_inst_w_mem_reg_9__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__14_] [get_cells core_w_mem_inst_w_mem_reg_9__15_] \
[get_cells core_w_mem_inst_w_mem_reg_9__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__17_] [get_cells core_w_mem_inst_w_mem_reg_9__18_] \
[get_cells core_w_mem_inst_w_mem_reg_9__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__20_] [get_cells core_w_mem_inst_w_mem_reg_9__21_] \
[get_cells core_w_mem_inst_w_mem_reg_9__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__23_] [get_cells core_w_mem_inst_w_mem_reg_9__24_] \
[get_cells core_w_mem_inst_w_mem_reg_9__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__26_] [get_cells core_w_mem_inst_w_mem_reg_9__27_] \
[get_cells core_w_mem_inst_w_mem_reg_9__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_9__29_] [get_cells core_w_mem_inst_w_mem_reg_9__30_] \
[get_cells core_w_mem_inst_w_mem_reg_9__31_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__0_] [get_cells core_w_mem_inst_w_mem_reg_8__1_]   \
[get_cells core_w_mem_inst_w_mem_reg_8__2_] [get_cells                         \
core_w_mem_inst_w_mem_reg_8__3_] [get_cells core_w_mem_inst_w_mem_reg_8__4_]   \
[get_cells core_w_mem_inst_w_mem_reg_8__5_] [get_cells                         \
core_w_mem_inst_w_mem_reg_8__6_] [get_cells core_w_mem_inst_w_mem_reg_8__7_]   \
[get_cells core_w_mem_inst_w_mem_reg_8__8_] [get_cells                         \
core_w_mem_inst_w_mem_reg_8__9_] [get_cells core_w_mem_inst_w_mem_reg_8__10_]  \
[get_cells core_w_mem_inst_w_mem_reg_8__11_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__12_] [get_cells core_w_mem_inst_w_mem_reg_8__13_] \
[get_cells core_w_mem_inst_w_mem_reg_8__14_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__15_] [get_cells core_w_mem_inst_w_mem_reg_8__16_] \
[get_cells core_w_mem_inst_w_mem_reg_8__17_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__18_] [get_cells core_w_mem_inst_w_mem_reg_8__19_] \
[get_cells core_w_mem_inst_w_mem_reg_8__20_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__21_] [get_cells core_w_mem_inst_w_mem_reg_8__22_] \
[get_cells core_w_mem_inst_w_mem_reg_8__23_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__24_] [get_cells core_w_mem_inst_w_mem_reg_8__25_] \
[get_cells core_w_mem_inst_w_mem_reg_8__26_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__27_] [get_cells core_w_mem_inst_w_mem_reg_8__28_] \
[get_cells core_w_mem_inst_w_mem_reg_8__29_] [get_cells                        \
core_w_mem_inst_w_mem_reg_8__30_] [get_cells core_w_mem_inst_w_mem_reg_8__31_] \
[get_cells core_w_mem_inst_w_mem_reg_7__0_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__1_] [get_cells core_w_mem_inst_w_mem_reg_7__2_]   \
[get_cells core_w_mem_inst_w_mem_reg_7__3_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__4_] [get_cells core_w_mem_inst_w_mem_reg_7__5_]   \
[get_cells core_w_mem_inst_w_mem_reg_7__6_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__7_] [get_cells core_w_mem_inst_w_mem_reg_7__8_]   \
[get_cells core_w_mem_inst_w_mem_reg_7__9_] [get_cells                         \
core_w_mem_inst_w_mem_reg_7__10_] [get_cells core_w_mem_inst_w_mem_reg_7__11_] \
[get_cells core_w_mem_inst_w_mem_reg_7__12_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__13_] [get_cells core_w_mem_inst_w_mem_reg_7__14_] \
[get_cells core_w_mem_inst_w_mem_reg_7__15_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__16_] [get_cells core_w_mem_inst_w_mem_reg_7__17_] \
[get_cells core_w_mem_inst_w_mem_reg_7__18_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__19_] [get_cells core_w_mem_inst_w_mem_reg_7__20_] \
[get_cells core_w_mem_inst_w_mem_reg_7__21_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__22_] [get_cells core_w_mem_inst_w_mem_reg_7__23_] \
[get_cells core_w_mem_inst_w_mem_reg_7__24_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__25_] [get_cells core_w_mem_inst_w_mem_reg_7__26_] \
[get_cells core_w_mem_inst_w_mem_reg_7__27_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__28_] [get_cells core_w_mem_inst_w_mem_reg_7__29_] \
[get_cells core_w_mem_inst_w_mem_reg_7__30_] [get_cells                        \
core_w_mem_inst_w_mem_reg_7__31_] [get_cells core_w_mem_inst_w_mem_reg_6__0_]  \
[get_cells core_w_mem_inst_w_mem_reg_6__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_6__2_] [get_cells core_w_mem_inst_w_mem_reg_6__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_6__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_6__5_] [get_cells core_w_mem_inst_w_mem_reg_6__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_6__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_6__8_] [get_cells core_w_mem_inst_w_mem_reg_6__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_6__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__11_] [get_cells core_w_mem_inst_w_mem_reg_6__12_] \
[get_cells core_w_mem_inst_w_mem_reg_6__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__14_] [get_cells core_w_mem_inst_w_mem_reg_6__15_] \
[get_cells core_w_mem_inst_w_mem_reg_6__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__17_] [get_cells core_w_mem_inst_w_mem_reg_6__18_] \
[get_cells core_w_mem_inst_w_mem_reg_6__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__20_] [get_cells core_w_mem_inst_w_mem_reg_6__21_] \
[get_cells core_w_mem_inst_w_mem_reg_6__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__23_] [get_cells core_w_mem_inst_w_mem_reg_6__24_] \
[get_cells core_w_mem_inst_w_mem_reg_6__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__26_] [get_cells core_w_mem_inst_w_mem_reg_6__27_] \
[get_cells core_w_mem_inst_w_mem_reg_6__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_6__29_] [get_cells core_w_mem_inst_w_mem_reg_6__30_] \
[get_cells core_w_mem_inst_w_mem_reg_6__31_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__0_] [get_cells core_w_mem_inst_w_mem_reg_5__1_]   \
[get_cells core_w_mem_inst_w_mem_reg_5__2_] [get_cells                         \
core_w_mem_inst_w_mem_reg_5__3_] [get_cells core_w_mem_inst_w_mem_reg_5__4_]   \
[get_cells core_w_mem_inst_w_mem_reg_5__5_] [get_cells                         \
core_w_mem_inst_w_mem_reg_5__6_] [get_cells core_w_mem_inst_w_mem_reg_5__7_]   \
[get_cells core_w_mem_inst_w_mem_reg_5__8_] [get_cells                         \
core_w_mem_inst_w_mem_reg_5__9_] [get_cells core_w_mem_inst_w_mem_reg_5__10_]  \
[get_cells core_w_mem_inst_w_mem_reg_5__11_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__12_] [get_cells core_w_mem_inst_w_mem_reg_5__13_] \
[get_cells core_w_mem_inst_w_mem_reg_5__14_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__15_] [get_cells core_w_mem_inst_w_mem_reg_5__16_] \
[get_cells core_w_mem_inst_w_mem_reg_5__17_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__18_] [get_cells core_w_mem_inst_w_mem_reg_5__19_] \
[get_cells core_w_mem_inst_w_mem_reg_5__20_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__21_] [get_cells core_w_mem_inst_w_mem_reg_5__22_] \
[get_cells core_w_mem_inst_w_mem_reg_5__23_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__24_] [get_cells core_w_mem_inst_w_mem_reg_5__25_] \
[get_cells core_w_mem_inst_w_mem_reg_5__26_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__27_] [get_cells core_w_mem_inst_w_mem_reg_5__28_] \
[get_cells core_w_mem_inst_w_mem_reg_5__29_] [get_cells                        \
core_w_mem_inst_w_mem_reg_5__30_] [get_cells core_w_mem_inst_w_mem_reg_5__31_] \
[get_cells core_w_mem_inst_w_mem_reg_4__0_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__1_] [get_cells core_w_mem_inst_w_mem_reg_4__2_]   \
[get_cells core_w_mem_inst_w_mem_reg_4__3_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__4_] [get_cells core_w_mem_inst_w_mem_reg_4__5_]   \
[get_cells core_w_mem_inst_w_mem_reg_4__6_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__7_] [get_cells core_w_mem_inst_w_mem_reg_4__8_]   \
[get_cells core_w_mem_inst_w_mem_reg_4__9_] [get_cells                         \
core_w_mem_inst_w_mem_reg_4__10_] [get_cells core_w_mem_inst_w_mem_reg_4__11_] \
[get_cells core_w_mem_inst_w_mem_reg_4__12_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__13_] [get_cells core_w_mem_inst_w_mem_reg_4__14_] \
[get_cells core_w_mem_inst_w_mem_reg_4__15_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__16_] [get_cells core_w_mem_inst_w_mem_reg_4__17_] \
[get_cells core_w_mem_inst_w_mem_reg_4__18_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__19_] [get_cells core_w_mem_inst_w_mem_reg_4__20_] \
[get_cells core_w_mem_inst_w_mem_reg_4__21_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__22_] [get_cells core_w_mem_inst_w_mem_reg_4__23_] \
[get_cells core_w_mem_inst_w_mem_reg_4__24_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__25_] [get_cells core_w_mem_inst_w_mem_reg_4__26_] \
[get_cells core_w_mem_inst_w_mem_reg_4__27_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__28_] [get_cells core_w_mem_inst_w_mem_reg_4__29_] \
[get_cells core_w_mem_inst_w_mem_reg_4__30_] [get_cells                        \
core_w_mem_inst_w_mem_reg_4__31_] [get_cells core_w_mem_inst_w_mem_reg_3__0_]  \
[get_cells core_w_mem_inst_w_mem_reg_3__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_3__2_] [get_cells core_w_mem_inst_w_mem_reg_3__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_3__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_3__5_] [get_cells core_w_mem_inst_w_mem_reg_3__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_3__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_3__8_] [get_cells core_w_mem_inst_w_mem_reg_3__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_3__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__11_] [get_cells core_w_mem_inst_w_mem_reg_3__12_] \
[get_cells core_w_mem_inst_w_mem_reg_3__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__14_] [get_cells core_w_mem_inst_w_mem_reg_3__15_] \
[get_cells core_w_mem_inst_w_mem_reg_3__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__17_] [get_cells core_w_mem_inst_w_mem_reg_3__18_] \
[get_cells core_w_mem_inst_w_mem_reg_3__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__20_] [get_cells core_w_mem_inst_w_mem_reg_3__21_] \
[get_cells core_w_mem_inst_w_mem_reg_3__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__23_] [get_cells core_w_mem_inst_w_mem_reg_3__24_] \
[get_cells core_w_mem_inst_w_mem_reg_3__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__26_] [get_cells core_w_mem_inst_w_mem_reg_3__27_] \
[get_cells core_w_mem_inst_w_mem_reg_3__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_3__29_] [get_cells core_w_mem_inst_w_mem_reg_3__30_] \
[get_cells core_w_mem_inst_w_mem_reg_3__31_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__0_] [get_cells core_w_mem_inst_w_mem_reg_2__1_]   \
[get_cells core_w_mem_inst_w_mem_reg_2__2_] [get_cells                         \
core_w_mem_inst_w_mem_reg_2__3_] [get_cells core_w_mem_inst_w_mem_reg_2__4_]   \
[get_cells core_w_mem_inst_w_mem_reg_2__5_] [get_cells                         \
core_w_mem_inst_w_mem_reg_2__6_] [get_cells core_w_mem_inst_w_mem_reg_2__7_]   \
[get_cells core_w_mem_inst_w_mem_reg_2__8_] [get_cells                         \
core_w_mem_inst_w_mem_reg_2__9_] [get_cells core_w_mem_inst_w_mem_reg_2__10_]  \
[get_cells core_w_mem_inst_w_mem_reg_2__11_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__12_] [get_cells core_w_mem_inst_w_mem_reg_2__13_] \
[get_cells core_w_mem_inst_w_mem_reg_2__14_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__15_] [get_cells core_w_mem_inst_w_mem_reg_2__16_] \
[get_cells core_w_mem_inst_w_mem_reg_2__17_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__18_] [get_cells core_w_mem_inst_w_mem_reg_2__19_] \
[get_cells core_w_mem_inst_w_mem_reg_2__20_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__21_] [get_cells core_w_mem_inst_w_mem_reg_2__22_] \
[get_cells core_w_mem_inst_w_mem_reg_2__23_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__24_] [get_cells core_w_mem_inst_w_mem_reg_2__25_] \
[get_cells core_w_mem_inst_w_mem_reg_2__26_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__27_] [get_cells core_w_mem_inst_w_mem_reg_2__28_] \
[get_cells core_w_mem_inst_w_mem_reg_2__29_] [get_cells                        \
core_w_mem_inst_w_mem_reg_2__30_] [get_cells core_w_mem_inst_w_mem_reg_2__31_] \
[get_cells core_w_mem_inst_w_mem_reg_1__0_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__1_] [get_cells core_w_mem_inst_w_mem_reg_1__2_]   \
[get_cells core_w_mem_inst_w_mem_reg_1__3_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__4_] [get_cells core_w_mem_inst_w_mem_reg_1__5_]   \
[get_cells core_w_mem_inst_w_mem_reg_1__6_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__7_] [get_cells core_w_mem_inst_w_mem_reg_1__8_]   \
[get_cells core_w_mem_inst_w_mem_reg_1__9_] [get_cells                         \
core_w_mem_inst_w_mem_reg_1__10_] [get_cells core_w_mem_inst_w_mem_reg_1__11_] \
[get_cells core_w_mem_inst_w_mem_reg_1__12_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__13_] [get_cells core_w_mem_inst_w_mem_reg_1__14_] \
[get_cells core_w_mem_inst_w_mem_reg_1__15_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__16_] [get_cells core_w_mem_inst_w_mem_reg_1__17_] \
[get_cells core_w_mem_inst_w_mem_reg_1__18_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__19_] [get_cells core_w_mem_inst_w_mem_reg_1__20_] \
[get_cells core_w_mem_inst_w_mem_reg_1__21_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__22_] [get_cells core_w_mem_inst_w_mem_reg_1__23_] \
[get_cells core_w_mem_inst_w_mem_reg_1__24_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__25_] [get_cells core_w_mem_inst_w_mem_reg_1__26_] \
[get_cells core_w_mem_inst_w_mem_reg_1__27_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__28_] [get_cells core_w_mem_inst_w_mem_reg_1__29_] \
[get_cells core_w_mem_inst_w_mem_reg_1__30_] [get_cells                        \
core_w_mem_inst_w_mem_reg_1__31_] [get_cells core_w_mem_inst_w_mem_reg_0__0_]  \
[get_cells core_w_mem_inst_w_mem_reg_0__1_] [get_cells                         \
core_w_mem_inst_w_mem_reg_0__2_] [get_cells core_w_mem_inst_w_mem_reg_0__3_]   \
[get_cells core_w_mem_inst_w_mem_reg_0__4_] [get_cells                         \
core_w_mem_inst_w_mem_reg_0__5_] [get_cells core_w_mem_inst_w_mem_reg_0__6_]   \
[get_cells core_w_mem_inst_w_mem_reg_0__7_] [get_cells                         \
core_w_mem_inst_w_mem_reg_0__8_] [get_cells core_w_mem_inst_w_mem_reg_0__9_]   \
[get_cells core_w_mem_inst_w_mem_reg_0__10_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__11_] [get_cells core_w_mem_inst_w_mem_reg_0__12_] \
[get_cells core_w_mem_inst_w_mem_reg_0__13_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__14_] [get_cells core_w_mem_inst_w_mem_reg_0__15_] \
[get_cells core_w_mem_inst_w_mem_reg_0__16_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__17_] [get_cells core_w_mem_inst_w_mem_reg_0__18_] \
[get_cells core_w_mem_inst_w_mem_reg_0__19_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__20_] [get_cells core_w_mem_inst_w_mem_reg_0__21_] \
[get_cells core_w_mem_inst_w_mem_reg_0__22_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__23_] [get_cells core_w_mem_inst_w_mem_reg_0__24_] \
[get_cells core_w_mem_inst_w_mem_reg_0__25_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__26_] [get_cells core_w_mem_inst_w_mem_reg_0__27_] \
[get_cells core_w_mem_inst_w_mem_reg_0__28_] [get_cells                        \
core_w_mem_inst_w_mem_reg_0__29_] [get_cells core_w_mem_inst_w_mem_reg_0__30_] \
[get_cells core_w_mem_inst_w_mem_reg_0__31_] [get_cells                        \
core_w_mem_inst_w_ctr_reg_reg_0_] [get_cells core_w_mem_inst_w_ctr_reg_reg_1_] \
[get_cells core_w_mem_inst_w_ctr_reg_reg_2_] [get_cells                        \
core_w_mem_inst_w_ctr_reg_reg_3_] [get_cells core_w_mem_inst_w_ctr_reg_reg_4_] \
[get_cells core_w_mem_inst_w_ctr_reg_reg_5_]]
group_path -name INPUT_GROUP  -from [list [get_ports clk] [get_ports reset_n] [get_ports cs] [get_ports we] \
[get_ports {address[7]}] [get_ports {address[6]}] [get_ports {address[5]}]     \
[get_ports {address[4]}] [get_ports {address[3]}] [get_ports {address[2]}]     \
[get_ports {address[1]}] [get_ports {address[0]}] [get_ports {write_data[31]}] \
[get_ports {write_data[30]}] [get_ports {write_data[29]}] [get_ports           \
{write_data[28]}] [get_ports {write_data[27]}] [get_ports {write_data[26]}]    \
[get_ports {write_data[25]}] [get_ports {write_data[24]}] [get_ports           \
{write_data[23]}] [get_ports {write_data[22]}] [get_ports {write_data[21]}]    \
[get_ports {write_data[20]}] [get_ports {write_data[19]}] [get_ports           \
{write_data[18]}] [get_ports {write_data[17]}] [get_ports {write_data[16]}]    \
[get_ports {write_data[15]}] [get_ports {write_data[14]}] [get_ports           \
{write_data[13]}] [get_ports {write_data[12]}] [get_ports {write_data[11]}]    \
[get_ports {write_data[10]}] [get_ports {write_data[9]}] [get_ports            \
{write_data[8]}] [get_ports {write_data[7]}] [get_ports {write_data[6]}]       \
[get_ports {write_data[5]}] [get_ports {write_data[4]}] [get_ports             \
{write_data[3]}] [get_ports {write_data[2]}] [get_ports {write_data[1]}]       \
[get_ports {write_data[0]}]]
group_path -name OUTPUT_GROUP  -to [list [get_ports {read_data[31]}] [get_ports {read_data[30]}] [get_ports  \
{read_data[29]}] [get_ports {read_data[28]}] [get_ports {read_data[27]}]       \
[get_ports {read_data[26]}] [get_ports {read_data[25]}] [get_ports             \
{read_data[24]}] [get_ports {read_data[23]}] [get_ports {read_data[22]}]       \
[get_ports {read_data[21]}] [get_ports {read_data[20]}] [get_ports             \
{read_data[19]}] [get_ports {read_data[18]}] [get_ports {read_data[17]}]       \
[get_ports {read_data[16]}] [get_ports {read_data[15]}] [get_ports             \
{read_data[14]}] [get_ports {read_data[13]}] [get_ports {read_data[12]}]       \
[get_ports {read_data[11]}] [get_ports {read_data[10]}] [get_ports             \
{read_data[9]}] [get_ports {read_data[8]}] [get_ports {read_data[7]}]          \
[get_ports {read_data[6]}] [get_ports {read_data[5]}] [get_ports               \
{read_data[4]}] [get_ports {read_data[3]}] [get_ports {read_data[2]}]          \
[get_ports {read_data[1]}] [get_ports {read_data[0]}] [get_ports error]]
set_input_delay -clock clk  0  [get_ports reset_n]
set_input_delay -clock clk  0  [get_ports cs]
set_input_delay -clock clk  0  [get_ports we]
set_input_delay -clock clk  0  [get_ports {address[7]}]
set_input_delay -clock clk  0  [get_ports {address[6]}]
set_input_delay -clock clk  0  [get_ports {address[5]}]
set_input_delay -clock clk  0  [get_ports {address[4]}]
set_input_delay -clock clk  0  [get_ports {address[3]}]
set_input_delay -clock clk  0  [get_ports {address[2]}]
set_input_delay -clock clk  0  [get_ports {address[1]}]
set_input_delay -clock clk  0  [get_ports {address[0]}]
set_input_delay -clock clk  0  [get_ports {write_data[31]}]
set_input_delay -clock clk  0  [get_ports {write_data[30]}]
set_input_delay -clock clk  0  [get_ports {write_data[29]}]
set_input_delay -clock clk  0  [get_ports {write_data[28]}]
set_input_delay -clock clk  0  [get_ports {write_data[27]}]
set_input_delay -clock clk  0  [get_ports {write_data[26]}]
set_input_delay -clock clk  0  [get_ports {write_data[25]}]
set_input_delay -clock clk  0  [get_ports {write_data[24]}]
set_input_delay -clock clk  0  [get_ports {write_data[23]}]
set_input_delay -clock clk  0  [get_ports {write_data[22]}]
set_input_delay -clock clk  0  [get_ports {write_data[21]}]
set_input_delay -clock clk  0  [get_ports {write_data[20]}]
set_input_delay -clock clk  0  [get_ports {write_data[19]}]
set_input_delay -clock clk  0  [get_ports {write_data[18]}]
set_input_delay -clock clk  0  [get_ports {write_data[17]}]
set_input_delay -clock clk  0  [get_ports {write_data[16]}]
set_input_delay -clock clk  0  [get_ports {write_data[15]}]
set_input_delay -clock clk  0  [get_ports {write_data[14]}]
set_input_delay -clock clk  0  [get_ports {write_data[13]}]
set_input_delay -clock clk  0  [get_ports {write_data[12]}]
set_input_delay -clock clk  0  [get_ports {write_data[11]}]
set_input_delay -clock clk  0  [get_ports {write_data[10]}]
set_input_delay -clock clk  0  [get_ports {write_data[9]}]
set_input_delay -clock clk  0  [get_ports {write_data[8]}]
set_input_delay -clock clk  0  [get_ports {write_data[7]}]
set_input_delay -clock clk  0  [get_ports {write_data[6]}]
set_input_delay -clock clk  0  [get_ports {write_data[5]}]
set_input_delay -clock clk  0  [get_ports {write_data[4]}]
set_input_delay -clock clk  0  [get_ports {write_data[3]}]
set_input_delay -clock clk  0  [get_ports {write_data[2]}]
set_input_delay -clock clk  0  [get_ports {write_data[1]}]
set_input_delay -clock clk  0  [get_ports {write_data[0]}]
set_output_delay -clock clk  0  [get_ports {read_data[31]}]
set_output_delay -clock clk  0  [get_ports {read_data[30]}]
set_output_delay -clock clk  0  [get_ports {read_data[29]}]
set_output_delay -clock clk  0  [get_ports {read_data[28]}]
set_output_delay -clock clk  0  [get_ports {read_data[27]}]
set_output_delay -clock clk  0  [get_ports {read_data[26]}]
set_output_delay -clock clk  0  [get_ports {read_data[25]}]
set_output_delay -clock clk  0  [get_ports {read_data[24]}]
set_output_delay -clock clk  0  [get_ports {read_data[23]}]
set_output_delay -clock clk  0  [get_ports {read_data[22]}]
set_output_delay -clock clk  0  [get_ports {read_data[21]}]
set_output_delay -clock clk  0  [get_ports {read_data[20]}]
set_output_delay -clock clk  0  [get_ports {read_data[19]}]
set_output_delay -clock clk  0  [get_ports {read_data[18]}]
set_output_delay -clock clk  0  [get_ports {read_data[17]}]
set_output_delay -clock clk  0  [get_ports {read_data[16]}]
set_output_delay -clock clk  0  [get_ports {read_data[15]}]
set_output_delay -clock clk  0  [get_ports {read_data[14]}]
set_output_delay -clock clk  0  [get_ports {read_data[13]}]
set_output_delay -clock clk  0  [get_ports {read_data[12]}]
set_output_delay -clock clk  0  [get_ports {read_data[11]}]
set_output_delay -clock clk  0  [get_ports {read_data[10]}]
set_output_delay -clock clk  0  [get_ports {read_data[9]}]
set_output_delay -clock clk  0  [get_ports {read_data[8]}]
set_output_delay -clock clk  0  [get_ports {read_data[7]}]
set_output_delay -clock clk  0  [get_ports {read_data[6]}]
set_output_delay -clock clk  0  [get_ports {read_data[5]}]
set_output_delay -clock clk  0  [get_ports {read_data[4]}]
set_output_delay -clock clk  0  [get_ports {read_data[3]}]
set_output_delay -clock clk  0  [get_ports {read_data[2]}]
set_output_delay -clock clk  0  [get_ports {read_data[1]}]
set_output_delay -clock clk  0  [get_ports {read_data[0]}]
set_output_delay -clock clk  0  [get_ports error]
