utl::set_metrics_stage "finish__{}"
source $::env(SCRIPTS_DIR)/load.tcl
load_design 6_1_fill.odb 6_1_fill.sdc "Starting final report"

set_propagated_clock [all_clocks]

# Ensure all OR created (rsz/cts) instances are connected
global_connect

# Delete routing obstructions for final DEF
source $::env(SCRIPTS_DIR)/deleteRoutingObstructions.tcl
deleteRoutingObstructions

write_db $::env(RESULTS_DIR)/6_final.odb
write_def $::env(RESULTS_DIR)/6_final.def
write_verilog $::env(RESULTS_DIR)/6_final.v

#debug:
# report_checks -unconstrained -path_delay max

#new:
puts [clock format [clock seconds]]

check_setup -verbose -unconstrained_endpoints

estimate_parasitics -placement
puts "-----------post placement phase----------------"
report_wns
report_tns
report_worst_slack
# report_power
set setup_violations [find_timing_paths -path_delay max -slack_max 0 -group_count 50000]
set num_setup_violations [llength $setup_violations]
puts "Total Setup Violations: $num_setup_violations"
# estimate_parasitics -global_routing
# puts "global routing phase"
# report_wns
# report_tns
# report_worst_slack
# report_power
source $::env(SCRIPTS_DIR)/count_cross_die_nets.tcl

# 提取单元级时序信息（2D时打开）
# source $::env(SCRIPTS_DIR)/my_report_metric.tcl

# Run extraction and STA
if {[info exist ::env(RCX_RULES)]} {

  # Set RC corner for RCX
  # Set in config.mk
  if {[info exist ::env(RCX_RC_CORNER)]} {
    set rc_corner $::env(RCX_RC_CORNER)
  }

  # RCX section
  define_process_corner -ext_model_index 0 tt0p7v25c
  extract_parasitics -ext_model_file $::env(RCX_RULES)

  # Write Spef
  write_spef $::env(RESULTS_DIR)/6_final.spef
  file delete $::env(DESIGN_NAME).totCap

  # report_checks -path_group DFF -fields nets

  # puts "---------------------------."

  # Read Spef for OpenSTA
  read_spef $::env(RESULTS_DIR)/6_final.spef
  # report_parasitic_annotation -report_unannotated

  # report_checks -path_group DFF -fields nets

  # Static IR drop analysis
  # if {[info exist ::env(PWR_NETS_VOLTAGES)]} {
  #   dict for {pwrNetName pwrNetVoltage}  {*}$::env(PWR_NETS_VOLTAGES) {
  #       set_pdnsim_net_voltage -net ${pwrNetName} -voltage ${pwrNetVoltage}
  #       analyze_power_grid -net ${pwrNetName} \
  #           -error_file $::env(REPORTS_DIR)/${pwrNetName}.rpt
  #   }
  # } else {
  #   puts "IR drop analysis for power nets is skipped because PWR_NETS_VOLTAGES is undefined"
  # }
  # if {[info exist ::env(GND_NETS_VOLTAGES)]} {
  #   dict for {gndNetName gndNetVoltage}  {*}$::env(GND_NETS_VOLTAGES) {
  #       set_pdnsim_net_voltage -net ${gndNetName} -voltage ${gndNetVoltage}
  #       analyze_power_grid -net ${gndNetName} \
  #           -error_file $::env(REPORTS_DIR)/${gndNetName}.rpt
  #   }
  # } else {
  #   puts "IR drop analysis for ground nets is skipped because GND_NETS_VOLTAGES is undefined"
  # }

} else {
  puts "OpenRCX is not enabled for this platform."
}

puts [clock format [clock seconds]]

puts "------------post routing phase----------------"
report_wns
report_tns
report_worst_slack
report_power
set setup_violations [find_timing_paths -path_delay max -slack_max 0 -group_count 50000]
set num_setup_violations [llength $setup_violations]
puts "Total Setup Violations: $num_setup_violations"

# source $::env(SCRIPTS_DIR)/report_metrics.tcl
# report_metrics "finish"

# Save a final image if openroad is compiled with the gui
if {[expr [llength [info procs save_image]] > 0]} {
    gui::show "source $::env(SCRIPTS_DIR)/save_images.tcl" false
}
