# 导入所需库
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ========== utils、读取数据 + 数据清洗 ==========
df = pd.read_csv("movie_box.csv")  # 天池影视数据集文件名

# 填充成本缺失值
genre_mean_cost = df.groupby("genre")["cost"].transform("mean")
df["cost"] = df["cost"].fillna(genre_mean_cost)

# 剔除异常数据
df = df[(df["total_box"] >= 10) & (df["runtime"] >= 60)]
# 去重
df = df.drop_duplicates(subset="movie_name")

# 拆分上映日期，新增档期列
df["release_date"] = pd.to_datetime(df["release_date"])
df["month"] = df["release_date"].dt.month
def get_season(month):
    if month in [1,2]:
        return "春节档"
    elif month in [7,8]:
        return "暑期档"
    elif month == 10:
        return "国庆档"
    else:
        return "普通档期"
df["season"] = df["month"].apply(get_season)

# ========== 分析1：各题材票房箱线图 ==========
plt.figure(figsize=(10,6))
main_genre = ["喜剧","动作","科幻","动画","爱情","悬疑"]
genre_data = [df[df["genre"]==g]["total_box"] for g in main_genre]
plt.boxplot(genre_data,labels=main_genre)
plt.title("各题材电影票房分布箱线图")
plt.ylabel("总票房（万元）")
plt.savefig("1_题材票房箱线图.png")
plt.show()

# ========== 分析2：各档期平均票房柱状图 ==========
season_box = df.groupby("season")["total_box"].mean()
plt.figure(figsize=(8,5))
plt.bar(season_box.index, season_box.values, color=["red","orange","gold","gray"])
plt.title("四大档期平均票房对比")
plt.ylabel("平均票房（万元）")
plt.savefig("2_档期票房柱状图.png")
plt.show()

# ========== 分析3：成本与票房相关性散点图 ==========
corr, p_value = pearsonr(df["cost"], df["total_box"])
plt.figure(figsize=(9,6))
plt.scatter(df["cost"], df["total_box"], alpha=0.4)
# 拟合趋势线
z = np.polyfit(df["cost"], df["total_box"], 1)
p = np.poly1d(z)
plt.plot(df["cost"],p(df["cost"]),"r--")
plt.title(f"制作成本-票房散点图 相关系数r={corr:.2f}")
plt.xlabel("制作成本（万元）")
plt.ylabel("总票房（万元）")
plt.savefig("3_成本票房散点图.png")
plt.show()

# ========== 分析4：年度备案数量折线图 ==========
year_count = df.groupby("file_year").size()
plt.figure(figsize=(8,5))
plt.plot(year_count.index, year_count.values, marker="o", linewidth=2)
plt.title("2018-2024年电影备案数量变化")
plt.xlabel("年份")
plt.ylabel("备案影片总数")
plt.grid(alpha=0.3)
plt.savefig("4_年度备案折线图.png")
plt.show()

# 输出核心统计结果
print("======= 数据分析汇总结果 =======")
print("utils.各题材平均票房：")
print(df.groupby("genre")["total_box"].mean().sort_values(ascending=False))
print("\n2.各档期平均票房：")
print(df.groupby("season")["total_box"].mean())
print(f"\n3.成本与票房皮尔逊相关系数：{corr:.2f}")
print("\n4.各年度备案影片数量：")
print(year_count)