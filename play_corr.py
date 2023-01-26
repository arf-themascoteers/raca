from sklearn.metrics import r2_score
from scipy.stats import pearsonr
a = [1,2,3]
b = [1,2,3]
c = [10,20,30]
print(r2_score(a,c))
print(pearsonr(a,c).statistic)

pear = pearsonr(a,c)
print(pear.pvalue)