from sklearn import datasets
import pandas as pd
import numpy as np
iris = datasets.load_iris()
x = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print("target_names: "+str(iris['target_names']))
y = pd.DataFrame(iris['target'], columns=['target'])
iris_data = pd.concat([x,y], axis=1)
iris_data.head(3)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('y label')
plt.xlabel('x label')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
print("t: " + str(t))
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
x = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25]
y = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]
plt.bar(x, y)
x = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25]
y = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]

plt.scatter(x, y)

#Pandas plot
iris_data.plot.scatter(x='sepal length (cm)', y='sepal width (cm)', c='target')
color = {
    0:'r',
    1:'g',
    2:'b'
}
iris_data['color'] = iris_data['target'].map(color)
iris_data.head(5)
iris_data.plot.scatter(x='sepal length (cm)', y='sepal width (cm)', c=iris_data['color'])
#Add label
iris_data[iris_data['target']==0].plot.scatter(x='sepal length (cm)', y='petal width (cm)',color='r', label='setosa')
iris_data[iris_data['target']==1].plot.scatter(x='sepal length (cm)', y='petal width (cm)',color='g', label='versicolor')
iris_data[iris_data['target']==2].plot.scatter(x='sepal length (cm)', y='petal width (cm)',color='b', label='virginica')
ax = iris_data[iris_data['target']==0].plot.scatter(x='sepal length (cm)', y='petal width (cm)',color='r', label='setosa')
ax = iris_data[iris_data['target']==1].plot.scatter(x='sepal length (cm)', y='petal width (cm)',color='g', label='versicolor', ax=ax)
iris_data[iris_data['target']==2].plot.scatter(x='sepal length (cm)', y='petal width (cm)',color='b', label='virginica', ax=ax)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.style.available
plt.style.use('ggplot')
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.style.use('classic')

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
#Seaborn
import seaborn as sns
sns.lmplot('sepal length (cm)','petal width (cm)',data=iris_data, fit_reg=False, hue='target')
target_name = {
    0:'setosa',
    1:'versicolor',
    2:'virginica'
}
iris_data['target_name'] = iris_data['target'].map(target_name)
sns.lmplot('sepal length (cm)','petal width (cm)', data=iris_data, fit_reg=False, hue='target_name')
#Plotly
import plotly
from plotly.graph_objs import Scatter, Layout
plotly.offline.init_notebook_mode(connected=True)
plotly.offline.iplot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
plotly.offline.iplot(data, filename='basic-scatter')
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

# Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)
trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)

data = [trace0, trace1, trace2]
plotly.offline.iplot(data, filename='scatter-mode')
trace0 = go.Scatter(
    x = iris_data[iris_data['target']==0]['sepal length (cm)'],
    y = iris_data[iris_data['target']==0]['petal width (cm)'],
    mode = 'markers',
    name = 'setosa'
)
trace1 = go.Scatter(
    x = iris_data[iris_data['target']==1]['sepal length (cm)'],
    y = iris_data[iris_data['target']==1]['petal width (cm)'],
    mode = 'markers',
    name = 'versicolor'
)
trace2 = go.Scatter(
    x = iris_data[iris_data['target']==2]['sepal length (cm)'],
    y = iris_data[iris_data['target']==2]['petal width (cm)'],
    mode = 'markers',
    name = 'virginica'
)

data = [trace0, trace1, trace2]
plotly.offline.iplot(data, filename='basic-scatter')

plt.show()