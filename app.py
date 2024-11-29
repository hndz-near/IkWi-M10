# Import the necessary libraries
import dash
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Add the title to the dashboard (Task 2.1)
    html.H1(
        "Automobile Sales Statistics Dashboard",  # Title text
        style={
            'textAlign': 'center',  # Center the title
            'color': '#503D36',     # Title color
            'font-size': '24px'     # Title font size
        }
    ),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
