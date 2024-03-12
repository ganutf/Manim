from manim import *
import random

class Network(VGroup):
    def __init__(self, N, base_size, min_connections, max_connections, color, background_color):
        super().__init__()
        self.N = N
        self.base_size = base_size
        self.min_distance = 2
        self.min_connections = min_connections
        self.max_connections = max_connections
        self.color = color
        self.background_color = background_color
        self.stroke_width = 2.5

        self.positions = self.generate_positions()
        self.nodes, self.white_nodes = self.create_nodes()
        self.edges = self.create_edges()

        self.node_group = VGroup(*self.nodes, *self.white_nodes)
        self.edge_group = VGroup(*self.edges)

        self.add(self.node_group, self.edge_group)
    
    def generate_positions(self):
        positions = []
        for i in range(self.N):
            while True:
                x = random.uniform(-5, 5)
                y = random.uniform(-3, 3)
                position = np.array([x, y, 0])
                if all(np.linalg.norm(position - p) >= self.min_distance for p in positions):
                    positions.append(position)
                    break
        return positions
    
    def create_nodes(self):
        nodes = []
        white_nodes = []
        for i in range(self.N):
            if i in [3, 4]:
                size = self.base_size * 1.3
            elif i == 5:
                size = self.base_size * 1.5
            else:
                size = self.base_size
            
            node = Dot(self.positions[i], radius=size, color=self.background_color, z_index=2)
            nodes.append(node)
            
            white_size = size * 0.6
            white_node = Dot(self.positions[i], radius=white_size, color=self.color, z_index=3)
            white_nodes.append(white_node)
        
        return nodes, white_nodes
    
    def create_edges(self):
        edges = []
        connection_counts = [0] * self.N
        
        for i in range(self.N):
            while connection_counts[i] < self.min_connections:
                j = random.randint(0, self.N - 1)
                if i != j and connection_counts[j] < self.max_connections:
                    edge = Line(self.positions[i], self.positions[j], z_index=1, stroke_width = self.stroke_width)
                    edge.color = self.color
                    edges.append(edge)
                    connection_counts[i] += 1
                    connection_counts[j] += 1
        
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if connection_counts[i] < self.max_connections and connection_counts[j] < self.max_connections and \
                   random.random() < 0.3:
                    edge = Line(self.positions[i], self.positions[j], z_index=1, stroke_width = self.stroke_width)
                    edge.color = self.color
                    
                    edges.append(edge)
                    connection_counts[i] += 1
                    connection_counts[j] += 1
        
        return edges

class MainScene(Scene):
    def construct(self):
        self.camera.background_color = color.WHITE
        red_color = rgb_to_color(hex_to_rgb("#dd1c1a"))
        blue_color = rgb_to_color(hex_to_rgb("#0a3363"))
        yellow_color = rgb_to_color(hex_to_rgb("#fcba04"))
        black_color = rgb_to_color(hex_to_rgb("#000000"))


        yellowNetwork = Network(8, 0.4, 4, 5, yellow_color, self.camera.background_color)
        yellowNetwork.scale(0.35)  # Set the size of the network
        # Position the network in the desired location
        yellowNetwork.move_to([-1.5, 2.6,1])  # Position the network in the upper right quadrant
        yellowText = Text("Decentralized Media", font_size=16, color=yellow_color).next_to(yellowNetwork, DOWN)
        self.play(Create(yellowNetwork), Write(yellowText))
        self.wait(1)



        redNetwork = Network(8, 0.4, 3, 6, red_color, self.camera.background_color)
        redNetwork.scale(0.35)  # Set the size of the network
        # Position the network in the desired location
        redNetwork.move_to([-1.5, -2.6,1])  # Position the network in the lower left quadrant
        redText = Text("Red Media", font_size=16, color=red_color).next_to(redNetwork, RIGHT)
        self.play(Create(redNetwork), Write(redText))
        self.wait(1)


        blueNetwork = Network(9, 0.4, 4, 7, blue_color, self.camera.background_color)
        blueNetwork.scale(0.35)  # Set the size of the network
        # Position the network in the desired location
        blueNetwork.move_to([-4.5, 0, 1])  # Position the network in the upper left quadrant
        blueText = Text("Establishment Storytellers", font_size=16, color=blue_color).next_to(blueNetwork, DOWN)
        self.play(Create(blueNetwork), Write(blueText))
        self.wait(1)

        ccpNetwork = Network(10, 0.4, 4, 6, black_color, self.camera.background_color)
        ccpNetwork.scale(0.35)  # Set the size of the network
        # Position the network in the desired location
        ccpNetwork.move_to([4.5, 0, 1])  # Position the network in the lower right quadrant
        ccpText = Text("CCP Media", font_size=16, color=black_color).next_to(ccpNetwork, DOWN)
        self.play(Create(ccpNetwork), Write(ccpText))
        self.wait(1)

