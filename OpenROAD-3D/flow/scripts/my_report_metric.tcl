################################################################################
# OpenSTA Cell Reporting Script
# 功能：报出每个 Instance 的名称、类型、扇出、以及输出引脚的 Slack
################################################################################

# 1. 设置输出文件
set output_file $::env(RESULTS_DIR)/cell_timing_report.csv
set out_fh [open $output_file "w"]

# 写入表头 (CSV 格式)
puts $out_fh "Instance,Cell_Type,Output_Pin,Fanout,Worst_Slack,Path_Count"

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
# 得到时钟周期
set clk_period [get_property [get_clocks *] period]

# 3. 遍历每个实例
foreach inst $all_instances {
    
    # 过滤掉包含 clk 或 CLK 的实例名
    set inst_name_check [get_property $inst full_name]
    if {[string match "*clk*" $inst_name_check] || [string match "*CLK*" $inst_name_check]} {
        continue
    }
    
    set inst_name [get_property $inst full_name]
    set cell_type [get_property $inst ref_name]

    # 4. 获取该实例的所有输出引脚
    set out_pins [get_pins -of_objects $inst -filter "direction==output"]

    foreach pin $out_pins {
        # 确保该引脚不是时钟引脚（排除 clock gating cells 等的时钟输出）
        set clocks [get_property $pin clocks]
        
        if {[llength $clocks] == 0} {
            set pin_name [get_property $pin full_name]
            
            # --- 获取扇出数量 ---
            set net [get_nets -of_objects $pin]
            if {$net != ""} {
                set net_pins [get_pins -of_objects $net]
                # 减去驱动引脚本身
                set fanout [expr {[llength $net_pins] - 1}]
            } else {
                set fanout 0
            }
            if {$fanout < 1} { set fanout 1 }

            # --- 获取 Slack ---
            set slack [get_property $pin slack_max]
            
            # 处理 slack 为无穷大的情况（无约束路径）
            if {$slack > $clk_period} { set slack $clk_period }
            
            # --- 获取路径数量 ---
            # find_timing_paths 返回的是 collection，需要用 llength 计算
            set paths [find_timing_paths -through $pin -group_count 100 -path_delay max]
            set path_count [llength $paths]
            if {$path_count == 0} { set path_count 1 }

            # 5. 写入文件
            puts $out_fh "$inst_name,$cell_type,$pin_name,$fanout,$slack,$path_count"
        }
    }
}

# 6. 关闭文件并清理
close $out_fh
puts "Report generation complete: $output_file"