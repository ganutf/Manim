from manim import *
import pandas as pd
from manim_mobject_svg import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = WHITE

# Ensure you have the datasets in the same directory as the script or provide the correct path
plot_data1 = pd.read_csv('../v2content/book6/chart/plot-data1.csv')
plot_data2 = pd.read_csv('../v2content/book6/chart/plot-data2.csv')
plot_data3 = pd.read_csv('../v2content/book6/chart/plot-data3.csv')
plot_data4 = pd.read_csv('../v2content/book6/chart/plot-data4.csv')

class AdvertisingRevenueGraph(Scene):
    def construct(self):


        plane = NumberPlane(x_range=(-4, 4), y_range=(-7, 7), background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.1
            })

        t = Triangle(color=PURPLE, fill_opacity=0.01)
        #self.add(plane)

        
        textfont = "Suisse Works Book"

        # Create the axes
        axes = Axes(
            x_range=[1950, 2020, 10],
            y_range=[0, 80, 10],
            axis_config={
                "include_numbers": True,
                "color": DARK_GRAY,
                'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'color' : DARK_GRAY,
                },
                "font_size": 28,
            },
            x_length=7,
            y_length=12,
            tips=False,
        )

        # Add the axis labels
        axes_labels = axes.get_axis_labels(
            x_label=Text("Year", font=textfont, font_size=12, weight=BOLD).set_color(BLACK),
            y_label=Text("Revenue in Billions", font=textfont, font_size=12).set_color(BLACK)
        )

        # Extract data for plotting
        def get_plot_data(df):
            df['x'] = pd.to_datetime(df['x'])
            df['year'] = df['x'].dt.year + (df['x'].dt.dayofyear / 365.25)
            return df['year'], df[' y']

        x_values1, y_values1 = get_plot_data(plot_data1)
        x_values2, y_values2 = get_plot_data(plot_data2)
        x_values3, y_values3 = get_plot_data(plot_data3)
        x_values4, y_values4 = get_plot_data(plot_data4)

        blue_color = rgb_to_color(hex_to_rgb("#0D4382"))
        red_color = rgb_to_color(hex_to_rgb("#dd1c1a"))
        yellow_color = rgb_to_color(hex_to_rgb("#fcba04"))
        green_color = rgb_to_color(hex_to_rgb("#61B22E"))

        # Create the graph lines
        line_color = [blue_color, red_color, green_color, PINK]
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
            Text("Newspaper Print Only", font=textfont, font_size=320).scale(0.07).set_color(blue_color),
            Text("Including Digital", font=textfont, font_size=320).scale(0.07).set_color(red_color),
            Text("Facebook Revenue", font=textfont, font_size=320).scale(0.07).set_color(green_color),
            Text("Google Revenue", font=textfont, font_size=320).scale(0.07).set_color(PINK),
        )

        # Arrange labels vertically with a smaller buffer
        labels.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # Position the group of labels to the top left corner of the screen
        labels.to_edge(UP * 6 + LEFT * 3, buff=0.5)

        # Create the scene group
        scene_group = VGroup(axes, axes_labels, graphs, labels)

        # Center the scene group
        scene_group.center()

        # Display the scene
        self.add(scene_group)
        self.wait(2)