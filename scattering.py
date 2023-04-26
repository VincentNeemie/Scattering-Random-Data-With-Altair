import altair as alt
import numpy as np
import pandas as pd

def plot_random_chart():
    # Generate random data
    np.random.seed(42)
    n_points = 100
    x = np.random.normal(0, 1, n_points)
    y = np.random.normal(0, 1, n_points)
    color = np.random.choice(['red', 'blue'], size=n_points)

    # Create Altair chart
    source = pd.DataFrame({'x': x, 'y': y, 'color': color})
    chart = alt.Chart(source).mark_circle().encode(
        x='x',
        y='y',
        color='color'
    )

    # Show chart in default browser
    chart.show()

# Call the function to generate and display the random chart
plot_random_chart()