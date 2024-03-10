from manim import *

class Network(VGroup):
    def __init__(self, node_positions, node_colors, node_sizes, edge_connections, **kwargs):
        super().__init__(**kwargs)
        self.nodes = []
        self.edges = []

        for pos, color, size in zip(node_positions, node_colors, node_sizes):
            node = Dot(point=pos, radius=size, color=color, z_index=3)
            self.nodes.append(node)
            self.add(node)

        for start, end in edge_connections:
            edge = Line(self.nodes[start].get_center(), self.nodes[end].get_center(), color=BLUE, stroke_width=2.1, z_index=1)
            self.edges.append(edge)
            self.add(edge)

class NetworkDiagram(Scene):
    def construct(self):
        # Create Glenn Greenwald node
        glenn = Network(
            node_positions=[ORIGIN],
            node_colors=[BLUE],
            node_sizes=[0.4],
            edge_connections=[]
        )
        glenn_label = Text("Glenn Greenwald", font_size=20).next_to(glenn, UP)

        # Create Decentralized Media network
        decentralized = Network(
            node_positions=[UP*0.5+LEFT*1.5, UP*0.5+LEFT*0.5, UP*0.5+RIGHT*0.5, UP*0.5+RIGHT*1.5,
                            DOWN*0.5+LEFT*1.5, DOWN*0.5+LEFT*0.5, DOWN*0.5+RIGHT*0.5, DOWN*0.5+RIGHT*1.5],
            node_colors=[RED]*8,
            node_sizes=[0.2]*8,
            edge_connections=[(0,1), (0,4), (1,2), (1,5), (2,3), (2,6), (3,7), (4,5), (4,6), (5,6), (5,7), (6,7)]
        )

        # Create Oliver Darcy node
        oliver = Network(
            node_positions=[ORIGIN],
            node_colors=[GREEN],
            node_sizes=[0.4],
            edge_connections=[]
        )
        oliver_label = Text("Oliver Darcy", font_size=20).next_to(oliver, DOWN)

        # Create Establishment Storytellers network
        storytellers = Network(
            node_positions=[UP*0.5+LEFT, UP*0.5, UP*0.5+RIGHT, DOWN*0.5+LEFT, DOWN*0.5, DOWN*0.5+RIGHT],
            node_colors=[YELLOW]*6,
            node_sizes=[0.2]*6,
            edge_connections=[(0,1), (0,3), (1,2), (1,4), (2,5), (3,4), (4,5)]
        )

        # Create Red Media network
        red_media = Network(
            node_positions=[UP*0.5+LEFT, UP*0.5, UP*0.5+RIGHT, DOWN*0.5+LEFT, DOWN*0.5, DOWN*0.5+RIGHT],
            node_colors=[MAROON]*6,
            node_sizes=[0.2]*6,
            edge_connections=[(0,1), (0,3), (1,2), (1,4), (2,5), (3,4), (4,5)]
        )

        # Create CCP Media node
        ccp_media = Network(
            node_positions=[ORIGIN],
            node_colors=[PURPLE],
            node_sizes=[0.4],
            edge_connections=[]
        )
        ccp_media_label = Text("CCP Media", font_size=20).next_to(ccp_media, DOWN)

        # Position networks
        glenn.move_to(UP * 2 + LEFT * 4)
        decentralized.move_to(UP * 1)
        oliver.move_to(DOWN * 1 + RIGHT * 4)
        storytellers.move_to(DOWN * 2 + LEFT * 4)
        red_media.move_to(DOWN * 3)
        ccp_media.move_to(RIGHT * 4)

        # Draw edges between networks
        de_gl = Arrow(decentralized.get_right(), glenn.get_left(), buff=0.2, color=WHITE)
        de_ol = Arrow(decentralized.get_corner(DOWN + RIGHT), oliver.get_corner(UP + LEFT), buff=0.2, color=WHITE)
        st_re = Arrow(storytellers.get_top(), red_media.get_bottom(), buff=0.2, color=WHITE)
        re_de = Arrow(red_media.get_top(), decentralized.get_bottom(), buff=0.2, color=WHITE)

        # Create Prestige arrow
        prestige_arrow = Arrow(LEFT, RIGHT, color=WHITE).scale(2)
        prestige_label = Text("Prestige", font_size=24).next_to(prestige_arrow, UP)
        prestige_group = Group(prestige_arrow, prestige_label).move_to(RIGHT * 2 + UP * 0.5)

        # Animate the creation of the diagram
        self.play(
            Create(glenn), Write(glenn_label),
            Create(oliver), Write(oliver_label),
            Create(ccp_media), Write(ccp_media_label)
        )
        self.play(
            Create(decentralized),
            GrowArrow(de_gl), GrowArrow(de_ol)
        )
        self.play(
            Create(storytellers), Create(red_media),
            GrowArrow(st_re), GrowArrow(re_de)
        )
        self.play(
            GrowArrow(prestige_arrow), Write(prestige_label)
        )

        self.wait()

if __name__ == "__main__":
    scene = NetworkDiagram()
    scene.render()