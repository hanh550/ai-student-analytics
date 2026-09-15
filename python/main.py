import mysql.connector
import pandas as pd


# Kết nối tới MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc",
    database="ai_student_analytics"
)

print("Kết nối MySQL thành công!")


# Lấy dữ liệu từ bảng student_analytics
query = """
SELECT
    student_id,
    name,
    study_group,
    gpa_hk1,
    attendance_rate,
    completion_rate
FROM student_analytics;
"""


# Đưa dữ liệu MySQL vào Pandas DataFrame
df = pd.read_sql(query, conn)


# Hiển thị dữ liệu
print("\nDữ liệu học sinh:")
print(df)
print("\n--- THÔNG TIN DỮ LIỆU ---")
print(df.info())

print("\n--- THỐNG KÊ DỮ LIỆU ---")
print(df.describe())

print("\n--- KIỂM TRA DỮ LIỆU TRỐNG ---")
print(df.isnull().sum())
print("\n--- PHÂN TÍCH NGUY CƠ ---")

df["risk_level"] = "On dinh"

df.loc[
    (df["gpa_hk1"] < 6.5) |
    (df["attendance_rate"] < 90) |
    (df["completion_rate"] < 70),
    "risk_level"
] = "Nguy co"

df.loc[
    (
        (df["gpa_hk1"] >= 6.5) &
        (df["gpa_hk1"] < 8.0)
    ) |
    (
        (df["attendance_rate"] >= 90) &
        (df["attendance_rate"] < 95)
    ) |
    (
        (df["completion_rate"] >= 70) &
        (df["completion_rate"] < 85)
    ),
    "risk_level"
] = "Can theo doi"

print(
    df[
        [
            "name",
            "gpa_hk1",
            "attendance_rate",
            "completion_rate",
            "risk_level"
        ]
    ]
)
# Đóng kết nối
conn.close()
print("\n--- CHUẨN BỊ DỮ LIỆU MACHINE LEARNING ---")

X = df[
    [
        "gpa_hk1",
        "attendance_rate",
        "completion_rate"
    ]
]

y = df["risk_level"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)