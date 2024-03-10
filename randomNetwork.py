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

        redNetwork = Network(9, 0.4, 3, 7, red_color, self.camera.background_color)
        redNetwork.scale(0.35)  # Set the size of the network
        # Position the network in the desired location
        redNetwork.move_to(RIGHT * 5, DOWN * 5)  # Position the network to the left of the scene

        blueNetwork = Network(7, 0.4, 3, 7, blue_color, self.camera.background_color)
        blueNetwork.scale(0.35)  # Set the size of the network
        # Position the network in the desired location
        blueNetwork.move_to(LEFT * 5, DOWN * 5)  # Position the network to the left of the scene

        blueNetwork = Network(7, 0.4, 3, 7, blue_color, self.camera.background_color)
        blueNetwork.scale(0.35)  # Set the size of the network
        # Position the network in the desired location
        blueNetwork.move_to(LEFT * 5, DOWN * 5)  # Position the network to the left of the scene

        self.play(Create(redNetwork))
        self.wait(2)

        self.play(Create(blueNetwork))
        self.wait(2)
