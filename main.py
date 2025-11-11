def analyze_text(s):  # 修正函数名为analyze_text
    """分析字符串中字符出现频率，并按降序打印"""
    # 创建字符计数字典
    char_count = {}
    
    # 遍历字符串，统计每个字符的出现次数
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 按出现频率降序排序（频率相同则按字符升序排列）
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # 打印结果
    for char, count in sorted_chars:
        print(f"'{char}': {count}次")


# 主程序
if __name__ == "__main__":
    # 获取用户输入的字符串
    user_input = input("请输入一个字符串：")
    
    # 处理空字符串情况
    if not user_input:
        print("输入的字符串为空！")
    else:
        print("字符出现频率（按降序排列）：")
        analyze_text(user_input)  # 调用修正后的函数名
