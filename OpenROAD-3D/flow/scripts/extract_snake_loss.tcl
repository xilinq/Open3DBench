# 打开输入文件
set input_file $::env(RESULTS_DIR)/snake_loss_report.txt
set output_file $::env(RESULTS_DIR)/snake_loss_weight.csv
set sdc_file $::env(RESULTS_DIR)/6_final.sdc

# 读取SDC文件，提取period值
set period 0
set sdc_fin [open $sdc_file r]
while {[gets $sdc_fin sdc_line] >= 0} {
    if {[regexp {\-period\s+([\d.]+)} $sdc_line match period_value]} {
        set period $period_value
        break
    }
}
close $sdc_fin

# 打印period值
puts "Found clock period: $period"

# 检查period是否有效
if {$period == 0} {
    puts "Error: Could not find -period in SDC file"
    exit 1
}

set fin [open $input_file r]

# 使用数组存储数据，key为"instance_a,instance_b"，value为累加的weight
array set weight_map {}

set in_path 0
set cells [list]
set slack_value ""

while {[gets $fin line] >= 0} {
    # 检测新路径开始
    if {[regexp {^Startpoint:} $line]} {
        set in_path 1
        set cells [list]
        continue
    }
    
    # 在路径中，检测以 _bottom) 结尾的行
    if {$in_path == 1} {
        # 检查是否到达 data arrival time
        if {[regexp {data arrival time} $line]} {
            set in_path 2
            continue
        }
        
        # 检查行是否以 _bottom) 结尾，提取实例名
        # 格式: 数字 数字 [v^] 实例名/引脚名 (单元类型_bottom)
        if {[regexp {_bottom\)$} $line]} {
            # 提取实例名/引脚名部分，然后去掉最后的引脚名
            # 匹配格式: 时间 时间 方向 实例路径/引脚 (类型)
            if {[regexp {^\s*[\d.]+\s+[\d.]+\s+[v\^]\s+(\S+)/\S+\s+\(\S+_bottom\)$} $line match instance_path]} {
                lappend cells $instance_path
            }
        }
    }
    
    # 在 data arrival time 之后，检测 slack (VIOLATED)
    if {$in_path == 2} {
        if {[regexp {^\s*(-?[\d.]+)\s+slack \(VIOLATED\)} $line match slack]} {
            set slack_value $slack
            
            # 计算weight = (period - slack) / period
            set weight [expr {($period - $slack_value) / $period}]
            
            # 处理相邻单元对
            set num_cells [llength $cells]
            for {set i 0} {$i < [expr {$num_cells - 1}]} {incr i} {
                set cell_a [lindex $cells $i]
                set cell_b [lindex $cells [expr {$i + 1}]]
                
                # 跳过 instance_a == instance_b 的情况
                if {$cell_a eq $cell_b} {
                    continue
                }
                
                # 构建key
                set key "${cell_a},${cell_b}"
                
                # 累加weight
                if {[info exists weight_map($key)]} {
                    set weight_map($key) [expr {$weight_map($key) + $weight}]
                } else {
                    set weight_map($key) $weight
                }
            }
            
            # 重置状态，准备下一个路径
            set in_path 0
            set cells [list]
            set slack_value ""
        }
    }
}

close $fin

# 写入CSV文件
set fout [open $output_file w]
puts $fout "instance_a,instance_b,weight"

foreach key [array names weight_map] {
    puts $fout "$key,$weight_map($key)"
}

close $fout

puts "Done! Output written to $output_file"
puts "Total unique cell pairs: [array size weight_map]"