import plotly.express as px
import pandas as pd
# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Scatter Plot")
# fig.show()

df = px.data.election()
fig = px.scatter_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner", title="3D Scatter Plot")
fig.show()