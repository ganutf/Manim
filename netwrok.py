from manim import *

class NetworkDiagram(Scene):
    def construct(self):
        # Create blue nodes with specified positions and sizes
        blue_nodes = [
            Dot(point=np.array([-4.23, 0, 0]), radius=0.15, color=BLUE, z_index=3),
            Dot(point=np.array([-2.82, 1.41, 0]), radius=0.15, color=BLUE, z_index=3),
            Dot(point=np.array([-1.41, 0, 0]), radius=0.15, color=BLUE, z_index=3),
            Dot(point=np.array([0, 1.41, 0]), radius=0.165, color=BLUE, z_index=3),
            Dot(point=np.array([0, -1.41, 0]), radius=0.165, color=BLUE, z_index=3),
            Dot(point=np.array([1.41, 0, 0]), radius=0.18, color=BLUE, z_index=3),
            Dot(point=np.array([2.82, -1.41, 0]), radius=0.15, color=BLUE, z_index=3),
            Dot(point=np.array([2.82, 1.41, 0]), radius=0.15, color=BLUE, z_index=3),
            Dot(point=np.array([4.23, 0, 0]), radius=0.15, color=BLUE, z_index=3)
        ]

        # Create black nodes at the same positions as blue nodes but with 150% size
        black_nodes = [
            Dot(point=node.get_center(), radius=node.radius * 1.5, color=BLACK, z_index=2)
            for node in blue_nodes
        ]

        # Create edges based on the specified connections
        edges = [
            Line(black_nodes[0].get_center(), black_nodes[1].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[0].get_center(), black_nodes[3].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[0].get_center(), black_nodes[4].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[1].get_center(), black_nodes[2].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[1].get_center(), black_nodes[5].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[2].get_center(), black_nodes[3].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[2].get_center(), black_nodes[4].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[3].get_center(), black_nodes[5].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[3].get_center(), black_nodes[7].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[4].get_center(), black_nodes[5].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[4].get_center(), black_nodes[6].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[5].get_center(), black_nodes[6].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[5].get_center(), black_nodes[7].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[6].get_center(), black_nodes[8].get_center(), color=BLUE, stroke_width=2.1, z_index=1),
            Line(black_nodes[7].get_center(), black_nodes[8].get_center(), color=BLUE, stroke_width=2.1, z_index=1)
        ]

        # Animate the creation of nodes and edges
        self.play(*[Create(edge) for edge in edges], *[Create(node) for node in black_nodes], *[Create(node) for node in blue_nodes])

        self.wait()