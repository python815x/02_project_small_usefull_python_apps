# import plotly.express as px
# import pandas as pd
#
# # Define the cigar characteristics and their corresponding ratings
# characteristics = [
#     'Strength (1 = Mild, 2 = Medium, 3 = Full-bodied)',
#     'Flavor (1 = Earthy, 2 = Spicy, 3 = Nutty, etc.)',
#     'Aroma (1 = Weak/unappealing, 2 = Pleasant, etc.)',
#     'Age (1 = Young, 2 = Moderately aged, 3 = Well-aged)',
#     'Price (1 = Affordable, 2 = Mid-range, 3 = Expensive)',
# ]
#
# ratings = [1, 5, 2, 2, 3]
#
# # Create a DataFrame with characteristics and ratings
# df = pd.DataFrame({'r': ratings, 'theta': characteristics})
#
# # Create the polar chart with style modifications
# fig = px.line_polar(df, r='r', theta='theta', line_close=True)
#
# # Style modifications
# fig.update_polars(
#     radialaxis=dict(
#         visible=True,
#         range=[0, 5],  # Adjust the range as needed
#         showticklabels=False  # Hide tick labels
#     ),
#     angularaxis=dict(
#         direction='counterclockwise',  # Counterclockwise direction
#         rotation=90,  # Rotate the radial axis
#         showline=True,
#         linecolor='black'  # Color of the radial lines
#     ),
#     showline=True,
#     linecolor='black'  # Color of the outer boundary line
# )
#
# fig.update_layout(
#     polar=dict(
#         bgcolor='antiquewhite'  # Background color
#     ),
#     title='Cigar Journal Ratings',  # Title of the chart
#     showlegend=False  # Hide the legend
# )
#
# # Show the chart
# fig.show()
pass
# import plotly.express as px
# import pandas as pd
#
# # Define the cigar characteristics and their corresponding ratings
# characteristics = [
#     'Strength (1 = Mild, 2 = Medium, 3 = Full-bodied)',
#     'Flavor (1 = Earthy, 2 = Spicy, 3 = Nutty, etc.)',
#     'Aroma (1 = Weak/unappealing, 2 = Pleasant, etc.)',
#     'Age (1 = Young, 2 = Moderately aged, 3 = Well-aged)',
#     'Price (1 = Affordable, 2 = Mid-range, 3 = Expensive)',
# ]
#
# ratings = [1, 5, 2, 2, 3]
#
# # Create a DataFrame with characteristics and ratings
# df = pd.DataFrame({'r': ratings, 'theta': characteristics})
#
# # Create the polar chart with style modifications
# fig = px.line_polar(df, r='r', theta='theta', line_close=True)
#
# # Style modifications
# fig.update_traces(fill='toself')  # Fill the area inside the lines
# fig.update_layout(
#     polar=dict(
#         radialaxis=dict(
#             showticklabels=False,
#             ticks='',
#         ),
#         angularaxis=dict(
#             rotation=90,
#             direction='clockwise',  # Clockwise direction
#         ),
#         bgcolor='antiquewhite',
#     ),
#     title='Cigar Journal Ratings',
#     showlegend=False,
# )
#
# # Show the chart
# fig.show()

import plotly.express as px
import pandas as pd

# Define the cigar characteristics and their corresponding ratings
characteristics = [
    'Strength (1 = Mild, 2 = Medium, 3 = Full-bodied)',
    'Flavor (1 = Earthy, 2 = Spicy, 3 = Nutty, etc.)',
    'Aroma (1 = Weak/unappealing, 2 = Pleasant, etc.)',
    'Age (1 = Young, 2 = Moderately aged, 3 = Well-aged)',
    'Price (1 = Affordable, 2 = Mid-range, 3 = Expensive)',
]

ratings = [1, 5, 2, 2, 3]

# Create a DataFrame with characteristics and ratings
df = pd.DataFrame({'r': ratings, 'theta': characteristics})

# Create the polar chart with style modifications
fig = px.line_polar(df, r='r', theta='theta', line_close=True)

# Style modifications
fig.update_traces(fill='toself')  # Fill the area inside the lines
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            showticklabels=False,
            ticks='',
        ),
        angularaxis=dict(
            rotation=90,
            direction='clockwise',  # Clockwise direction
        ),
        bgcolor='antiquewhite',
    ),
    title='Cigar Journal Ratings',
    showlegend=False,
)

# Add a cigar image in the background
fig.add_layout_image(
    source="",  # Replace with the URL of your cigar image
    x=0.5,
    y=0.5,
    xref="paper",
    yref="paper",
    xanchor="center",
    yanchor="middle",
    sizex=1,
    sizey=1,
    opacity=0.3,
)

# Add a logo to the top right
fig.add_layout_image(
    source="",  # Replace with the URL of your logo image
    x=0.5,
    y=0.5,
    xref="paper",
    yref="paper",
    xanchor="right",
    yanchor="top",
    sizex=1,  # Adjust the size as needed
    sizey=1,
    opacity=0.5,
)

# Show the chart
fig.show()
