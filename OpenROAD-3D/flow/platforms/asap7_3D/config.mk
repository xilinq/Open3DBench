export PROCESS                 = 7
export ASAP7_USE_VT           ?= LVT

#-----------------------------------------------------
# Tech/Libs
# ----------------------------------------------------
export TECH_LEF = $(PLATFORM_DIR)/lef/asap7_tech_f2f_3d.lef
# export SC_LEF = $(PLATFORM_DIR)/lef_upper/asap7sc7p5t_28_L_upper.lef \
#                         $(PLATFORM_DIR)/lef_bottom/asap7sc7p5t_28_L_bottom.lef
export SC_LEF = $(PLATFORM_DIR)/lef_upper/asap7_upper.lef \
                        $(PLATFORM_DIR)/lef_bottom/asap7_bottom.lef                        

# export LIB_FILES = $(PLATFORM_DIR)/lib/NangateOpenCellLibrary_typical.lib \
#                      $(ADDITIONAL_LIBS)
export LIB_FILES = $(ADDITIONAL_LIBS)

export GDS_FILES = $(sort $(wildcard $(PLATFORM_DIR)/gds/*.gds)) \
                     $(ADDITIONAL_GDS)
# Dont use cells to ease congestion
# Specify at least one filler cell if none
export DONT_USE_CELLS = TAPCELL_upper FILLER_upper

# Fill cells used in fill cell insertion
export FILL_CELLS ?= TAPCELL_bottom

# -----------------------------------------------------
#  Yosys
#  ----------------------------------------------------
# Ungroup size for hierarchical synthesis
export MAX_UNGROUP_SIZE ?= 10000
# Set the TIEHI/TIELO cells
# These are used in yosys synthesis to avoid logical 1/0's in the netlist
export TIEHI_CELL_AND_PORT = TIEHIx1_bottom Z
export TIELO_CELL_AND_PORT = TIELOx1_bottom Z

# Used in synthesis
export MIN_BUF_CELL_AND_PORTS = BUFx2_bottom A Z


# Yosys mapping files
export LATCH_MAP_FILE = $(PLATFORM_DIR)/cells_latch.v
export CLKGATE_MAP_FILE = $(PLATFORM_DIR)/cells_clkgate.v
export ADDER_MAP_FILE ?= $(PLATFORM_DIR)/cells_adders.v
#
export ABC_DRIVER_CELL = BUFx2_bottom
# BUF_X1, pin (A) = 0.974659. Arbitrarily multiply by 4
export ABC_LOAD_IN_FF = 3.898

#--------------------------------------------------------
# Floorplan
# -------------------------------------------------------

# Placement site for core cells
# This can be found in the technology lef
export PLACE_SITE = asap7sc7p5t

# IO Placer pin layers
export IO_PLACER_H = M4
export IO_PLACER_V = M4

# Define default PDN config
export PDN_TCL ?= $(PLATFORM_DIR)/grid_strategy-M1-M2-M5-M6.tcl

# Endcap and Welltie cells
export TAPCELL_TCL ?= $(PLATFORM_DIR)/tapcell.tcl
# export TAP_CELL_NAME = TAPCELL_ASAP7_75t_L_bottom TAPCELL_ASAP7_75t_L_upper
export TAP_CELL_NAME = TAPCELL_bottom TAPCELL_upper

export MACRO_PLACE_HALO ?= 10 10
export MACRO_ROWS_HALO_X            ?= 2
export MACRO_ROWS_HALO_Y            ?= 2

#---------------------------------------------------------
# Place
# --------------------------------------------------------
# Cell padding in SITE widths to ease rout-ability.  Applied to both sides
export CELL_PAD_IN_SITES_GLOBAL_PLACEMENT ?= 0
export CELL_PAD_IN_SITES_DETAIL_PLACEMENT ?= 0
#

export PLACE_DENSITY ?= 0.60

# --------------------------------------------------------
#  CTS
#  -------------------------------------------------------
# TritonCTS options
export CTS_BUF_CELL   ?= BUFx2_bottom

# ---------------------------------------------------------
#  Route
# ---------------------------------------------------------
# FastRoute options
export MIN_ROUTING_LAYER = M2
export MIN_CLK_ROUTING_LAYER   ?= M4
export MAX_ROUTING_LAYER = M14

# Define fastRoute tcl
export FASTROUTE_TCL ?= $(PLATFORM_DIR)/fastroute.tcl

# KLayout technology file
export KLAYOUT_TECH_FILE = $(PLATFORM_DIR)/asap7.lyt

# KLayout DRC ruledeck
# export KLAYOUT_DRC_FILE = $(PLATFORM_DIR)/drc/FreePDK45.lydrc

# KLayout LVS ruledeck
# export KLAYOUT_LVS_FILE = $(PLATFORM_DIR)/lvs/FreePDK45.lylvs

# Allow empty GDS cell
# export GDS_ALLOW_EMPTY ?= fakeram.*

# export CDL_FILE = $(PLATFORM_DIR)/cdl/NangateOpenCellLibrary.cdl

# Template definition for power grid analysis
# export TEMPLATE_PGA_CFG ?= $(PLATFORM_DIR)/template_pga.cfg

# OpenRCX extRules
export RCX_RULES               = $(PLATFORM_DIR)/asap7_3D.rules
# ---------------------------------------------------------
#  IR Drop
# ---------------------------------------------------------

# IR drop estimation supply net name to be analyzed and supply voltage variable
# For multiple nets: PWR_NETS_VOLTAGES  = "VDD1 1.8 VDD2 1.2"
export PWR_NETS_VOLTAGES  ?= "VDD 0.7"
export GND_NETS_VOLTAGES  ?= "VSS 0.0"
export IR_DROP_LAYER ?= M1
