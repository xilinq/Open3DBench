################################################################################
# OpenSTA Cell Reporting Script
# 功能：报出每个 Instance 的名称、类型、扇出、以及输出引脚的 Slack
################################################################################

# 1. 设置输出文件
set output_file $::env(RESULTS_DIR)/cell_timing_report.csv
set out_fh [open $output_file "w"]

# 写入表头 (CSV 格式)
puts $out_fh "Instance,Cell_Type,Output_Pin,Fanout,Worst_Slack"

# 报告slack
# 检查snake_loss_report.txt是否存在，如果存在则删除，否则执行report_checks
set snake_loss_file "$::env(RESULTS_DIR)/snake_loss_report.txt"
if {[file exists $snake_loss_file]} {
    file delete $snake_loss_file
} else {
    report_checks -path_delay max -slack_max 0 -group_count 20 -path_group DFF >> $snake_loss_file
}
report_checks -path_delay max -slack_max 0 -group_count 20 -path_group DFF >> $snake_loss_file
# 处理snake loss报告
source $::env(SCRIPTS_DIR)/extract_snake_loss.tcl

# 2. 获取所有实例的集合
# 根据需要可以增加 filter，例如: get_cells * -filter "is_hierarchical == false"
set all_instances [get_cells *]

# 3. 遍历每个实例
foreach inst $all_instances {
    # 如果 ref_name 含有 DFF，则跳过
    # set ref_name [get_property $inst ref_name]
    # if {[string match "*DFF*" $ref_name]} {
    #     continue
    # }

    # 如果实例名中带有clk，则跳过
    set inst_name_check [get_property $inst full_name]
    if {[string match "*clk*" $inst_name_check] || [string match "*CLK*" $inst_name_check]} {
        continue
    }
    set inst_name [get_property $inst full_name]
    
    # 获取单元类型 (Ref Name)
    set cell_type [get_property $inst ref_name]

    # 4. 获取该实例的所有输出引脚
    set out_pins [get_pins -of_objects $inst -filter "direction==output"]

    foreach pin $out_pins {
        set clocks [get_property $pin clocks]
        if {[llength $clocks] == 0} {

            set pin_name [get_property $pin full_name]
            
            # --- 获取扇出数量 ---
            # 提示：OpenSTA 中通常可以使用 get_property 获取 fanout
            set net [get_nets -of_objects $pin]
            set net_pins [get_pins -of_objects $net]
            set fanout [expr {[llength $net_pins] - 1}]  ;# 减去驱动引脚本身

            # --- 获取 Slack ---
            # 提示：需要考虑 Setup (max) 或 Hold (min)，通常默认报 Setup
            # 如果引脚上没有约束，slack 可能返回无穷大
            set slack [get_property $pin slack_max]
            
            # 格式化输出 (如果 slack 为空或数值极大，进行处理)
            if {$slack > 1e20} { set slack "N/A" }

            # 5. 写入文件
            puts $out_fh "$inst_name,$cell_type,$pin_name,$fanout,$slack"
        }
    }
}

# 6. 关闭文件并清理
close $out_fh
puts "Report generation complete: $output_file"