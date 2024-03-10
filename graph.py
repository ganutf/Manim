from manim import *
import pandas as pd

# Ensure you have the datasets in the same directory as the script or provide the correct path
plot_data1 = pd.read_csv('../v2content/book6/chart/plot-data1.csv')
plot_data2 = pd.read_csv('../v2content/book6/chart/plot-data2.csv')
plot_data3 = pd.read_csv('../v2content/book6/chart/plot-data3.csv')
plot_data4 = pd.read_csv('../v2content/book6/chart/plot-data4.csv')

print("Dataset 1 head:", plot_data1.head())
print("Dataset 2 head:", plot_data2.head())
print("Dataset 3 head:", plot_data3.head())
print("Dataset 4 head:", plot_data4.head())

class AdvertisingRevenueGraph(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[1950, 2020, 10],
            y_range=[0, 80, 10],
            axis_config={"color": BLUE},
            x_length=10,
            y_length=6,
            tips=False,
        )

        # Add the axis labels
        x_labels = axes.get_axis_labels(x_label=Text("Year", font_size=12).set_color(WHITE), y_label= Text("Revenue in Billions", font_size=12).set_color(WHITE))

        # Extract data for plotting
        def get_plot_data(df):
            df['x'] = pd.to_datetime(df['x'])
            df['year'] = df['x'].dt.year + (df['x'].dt.dayofyear / 365.25)
    
            # Notice the space in ' y'
            return df['year'], df[' y']

        x_values1, y_values1 = get_plot_data(plot_data1)
        x_values2, y_values2 = get_plot_data(plot_data2)
        x_values3, y_values3 = get_plot_data(plot_data3)
        x_values4, y_values4 = get_plot_data(plot_data4)

        # Create the graph lines
        line_color = [BLUE, RED, GREEN, PINK]
        graphs = VGroup()
        for i, (x_values, y_values) in enumerate(zip([x_values1, x_values2, x_values3, x_values4], 
                                                      [y_values1, y_values2, y_values3, y_values4])):
            graph = axes.plot_line_graph(
                x_values=x_values.tolist(),
                y_values=y_values.tolist(),
                line_color=line_color[i],
                add_vertex_dots=False,
            )
            graphs.add(graph)
            
        # Create and add labels for the graph lines
        labels = VGroup(
            Text("Newspaper Print Only", font_size=12).set_color(BLUE),
            Text("Including Digital", font_size=12).set_color(RED),
            Text("Facebook Revenue", font_size=12).set_color(GREEN),
            Text("Google Revenue", font_size=12).set_color(PINK),
        )
        # Arrange labels vertically with a smaller buffer
        labels.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        # Position the group of labels to the top left corner of the screen
        labels.to_edge(UP, buff=1)

        # Display the axes, labels, and the graph lines
        self.play(Create(axes), Write(x_labels))
        self.play(*[Create(graph) for graph in graphs])
        self.play(*[Write(label) for label in labels])

        # Keep the scene displayed
        self.wait(2)
