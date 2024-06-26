# -*- coding: utf-8 -*-
"""LVADSUSR183_SajjaTarunTeja_FLab3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HD9gZTfAsc1ciKXgSZFiEcyA_iF-mSO4
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns
import pandas as pd

df = pd.read_csv("/content/customer_segmentation.csv")

df.head()

df.info()

df.isna().sum()
# 24 Null values in Income

df = df.dropna()
# Dropping Null Values

ndf = df.drop(["Education","Marital_Status","Dt_Customer"],axis=1)
# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(ndf.corr(), annot=True, cmap='summer', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

inertia_values = []
silhouette_scores = []
k_values = range(2, 10)

df = ndf
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df)
    inertia_values.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(df, kmeans.labels_))

plt.plot(k_values, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores for Optimal k value')
plt.xticks(k_values)
plt.show()

plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve for Optimal k value')
plt.xticks(k_values)
plt.show()

# 3 is the best value for K
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(df)

cluster_labels = kmeans.predict(df)
silhouette_avg = silhouette_score(df, cluster_labels)
print("Average silhouette score: ",silhouette_avg)

df['Cluster'] = kmeans.labels_
cluster_profiles = df.groupby('Cluster').mean()
print(cluster_profiles)

