def calculate_total_hours(hours_per_day, days):
    """
    說明caculate_total_hours如何使用
    """
    total_hours = hours_per_day * days
    return total_hours
    print()#寫在return後的描述不會被執行 



hours_per_day = float(input("每天學習幾小時："))
days = int(input("學習幾天："))

total_hours = calculate_total_hours(hours_per_day, days)

print("--- 執行結果 ---")
print(f"總學習時數：{total_hours:.1f} 小時")