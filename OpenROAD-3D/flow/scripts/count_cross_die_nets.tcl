puts "Starting cross-die net analysis..."

# 1. 初始化计数器
set cross_die_count 0
set processed_nets 0

# 获取所有 Net (如果你只想看特定模块，可以修改 get_nets 的参数)
set all_nets [get_nets *]
set total_nets [llength $all_nets]

puts "Total nets to analyze: $total_nets"

# 2. 遍历每个 Net
foreach net $all_nets {
    incr processed_nets
    
    # 简单的进度打印 (每处理 10000 个 net 打印一次)
    if { [expr $processed_nets % 10000] == 0 } {
        puts "Processed $processed_nets / $total_nets nets..."
    }

    # 获取该 Net 连接的所有 Pin (注意：排除顶层 Port，因为 Port 没有 ref_name)
    # leaf_pins 指的是标准单元上的 pin
    set pins [get_pins -of_objects $net]
    
    # 标志位初始化
    set has_bottom 0
    set has_upper 0
    
    # 3. 遍历该 Net 上的所有 Pin
    foreach pin $pins {
        # 获取 Pin 所属的 Cell 对象
        set cell [get_cells -of_objects $pin]
        
        # 获取 Cell 的参考库名字 (Reference Name)
        # 例如: NAND2_bottom, BUF_upper
        set ref_name [get_property $cell ref_name]
        
        # 4. 判断类型
        if { [string match "*_bottom*" $ref_name] } {
            set has_bottom 1
        } elseif { [string match "*_upper*" $ref_name] } {
            set has_upper 1
        }
        
        # 5. 快速退出机制：如果两个标志都为 1，说明已经是跨 Die 了，不需要再看这个 Net 的其他 Pin
        if { $has_bottom && $has_upper } {
            incr cross_die_count
            break 
        }
    }
}

puts "------------------------------------------------"
puts "Analysis Complete."
puts "Total Cross-Die Nets Found: $cross_die_count"
puts "------------------------------------------------"