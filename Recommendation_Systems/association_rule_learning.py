############################################
# ASSOCIATION RULE LEARNING (BİRLİKTELİK KURALI ÖĞRENİMİ)
############################################

# 1. Veri Ön İşleme
# 2. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
# 3. Birliktelik Kurallarının Çıkarılması
# 4. Çalışmanın Scriptini Hazırlama
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak

############################################
# 1. Veri Ön İşleme
############################################

# !pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
# çıktının tek bir satırda olmasını sağlar.
pd.set_option('display.expand_frame_repr', False)

# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

df_ = pd.read_excel("CRMAnalysis/datasets/online_retail_II.xlsx",
                    sheet_name="Year 2010-2011")
df = df_.copy()
df.head()
# Veri okuma işlemi hata alırsak bu tür okuma gerçekleştirebiliriz.
# pip install openpyxl
# df_ = pd.read_excel("datasets/online_retail_II.xlsx",
#                     sheet_name="Year 2010-2011", engine="openpyxl")


df.describe().T
df.isnull().sum()
df.shape

def retail_data_prep(dataframe):
    # ver isetindeki eksik değerleri kalıcı olarak uçur.
    dataframe.dropna(inplace=True)
    # Verisetindeki Invoce değişkeninde c harfi olanlar dışındakileri seç(~)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    return dataframe

df = retail_data_prep(df)

# Aykırı değerleri silme işlemi
# Aykırı değer bir değişkenin dağılımının dışında yer alan değerlerdir.
# Aykırı değerleri tespit etme
def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

# Aykırı değerleri eşik değerleri(low_limit, up_limit) ile değiştir.
def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

# Veri seti hazırlama ve aykırı değerleri birlikte hesaplama işlemi
def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    return dataframe

df = retail_data_prep(df)
df.info()
df.isnull().sum()
df.describe().T


############################################
# 2. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
############################################

df.head()

# Description   NINE DRAWER OFFICE TIDY   SET 2 TEA TOWELS I LOVE LONDON    SPACEBOY BABY GIFT SET
# Invoice
# 536370                              0                                 1                       0
# 536852                              1                                 0                       1
# 536974                              0                                 0                       0
# 537065                              1                                 0                       0
# 537463                              0                                 0                       1


df_fr = df[df['Country'] == "France"]

df_fr.groupby(['Invoice', 'Description']).agg({"Quantity": "sum"}).head(20)

# Description sutun(değişken) olarak ayarladık.5 satır 5 sütun getirdik.
df_fr.groupby(['Invoice', 'Description']).agg({"Quantity": "sum"}).unstack().iloc[0:5, 0:5]

# Boş olan ürünleri yani eksik değerleri 0 ile dolduralım.
df_fr.groupby(['Invoice', 'Description']).agg({"Quantity": "sum"}).unstack().fillna(0).iloc[0:5, 0:5]

# boş olanları 0 ile doldurduktan sonra dolu olan değerleri 1 ile dolduralım.
df_fr.groupby(['Invoice', 'StockCode']). \
          agg({"Quantity": "sum"}). \
          unstack(). \
          fillna(0). \
          apply(lambda x: x.apply(lambda y: 1 if y > 0 else 0)).iloc[0:5, 0:5]
          # applymap(lambda x: 1 if x > 0 else 0).iloc[0:5, 0:5]


# Yukardaki işlemleri fonksiyonlaştıralım. Eğer True girilirse StockCode göre işlem yap. değilse Descriptiona göre
def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', "StockCode"])['Quantity'].sum().unstack().fillna(0). \
            apply(lambda x: x.apply(lambda y: 1 if y > 0 else 0))
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0). \
            apply(lambda x: x.apply(lambda y: 1 if y > 0 else 0))

fr_inv_pro_df = create_invoice_product_df(df_fr)

fr_inv_pro_df = create_invoice_product_df(df_fr, id=True)

# Stock code verilen ürünün adına ulaşmak.
def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code][["Description"]].values[0].tolist()
    print(product_name)


check_id(df_fr, 10120)

############################################
# 3. Birliktelik Kurallarının Çıkarılması
############################################
# min_support : eşik değeri , df kolon isimleri kullanılacaksa true
fr_inv_pro_df = fr_inv_pro_df.astype(bool)  # veri setimiz apriori de daha iyi performans göstermesi iiçn bool tipine çevirdik.
frequent_itemsets = apriori(fr_inv_pro_df,
                            min_support=0.01,
                            use_colnames=True)

frequent_itemsets.sort_values("support", ascending=False)

rules = association_rules(frequent_itemsets,
                          metric="support",
                          min_threshold=0.01)

rules[(rules["support"]>0.05) & (rules["confidence"]>0.1) & (rules["lift"]>5)]

check_id(df_fr, 21086)

rules[(rules["support"] > 0.05) & (rules["confidence"] > 0.1) & (rules["lift"] > 5)]. \
sort_values("confidence", ascending=False)

############################################
# 4. Çalışmanın Scriptini Hazırlama
############################################

def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    return dataframe


def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', "StockCode"])['Quantity'].sum().unstack().fillna(0). \
            apply(lambda x: x.apply(lambda y: 1 if y > 0 else 0))
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0). \
            apply(lambda x: x.apply(lambda y: 1 if y > 0 else 0))


def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code][["Description"]].values[0].tolist()
    print(product_name)


def create_rules(dataframe, id=True, country="France"):
    dataframe = dataframe[dataframe['Country'] == country]
    dataframe = create_invoice_product_df(dataframe, id)
    dataframe = dataframe.astype(bool)  # veri setimiz apriori de daha iyi performans göstermesi iiçn bool tipine çevirdik.
    frequent_itemsets = apriori(dataframe, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)
    return rules

df = df_.copy()

df = retail_data_prep(df)
rules = create_rules(df)

rules[(rules["support"]>0.05) & (rules["confidence"]>0.1) & (rules["lift"]>5)]. \
sort_values("confidence", ascending=False)

############################################
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak
############################################

# Örnek:
# Kullanıcı örnek ürün id: 22492

product_id = 22492
check_id(df, product_id)

#  Kuralları lift değerine göre sıralıyoruz
sorted_rules = rules.sort_values("lift", ascending=False)

# öneri litesi
recommendation_list = []

for i, product in enumerate(sorted_rules["antecedents"]):
    for j in list(product):
        if j == product_id:
            recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])

# İlk 3 öneri
recommendation_list[0:3]

check_id(df, 22326)

# İşlemleri fonksiyonlaştıralım
def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])

    return recommendation_list[0:rec_count]

# II. YOL
def arl_recommender1(rules_df, product_id, rec_count=1):
    sorted_rules1 = rules_df.sort_values("lift", ascending=False)
    recommendation_list1 = (
        sorted_rules.loc[
            sorted_rules["antecedents"]
            .apply(lambda antecedents_list: product_id in antecedents_list)
            , "consequents"
        ].apply(list).tolist()
    )

    return recommendation_list1[0:rec_count]


# III. YOL
def arl_recommender2(rules_df, product_id, rec_count=1):
    sorted_rules2 = rules_df.sort_values("lift", ascending=False)
    recommendation_list2 = [list(rule.consequents)[0]
                            for rule in sorted_rules.itertuples()
                            if product_id in rule.antecedents]

    return recommendation_list2[0:rec_count]


arl_recommender(rules, 22492, 1)
arl_recommender1(rules, 22492, 3)
arl_recommender2(rules, 22492, 3)
arl_recommender(rules, 22492, 2)
arl_recommender(rules, 22492, 3)





