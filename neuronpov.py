from manim import *

class NeuronPOV(Scene):
    def construct(self):
        # Create a neuron
        neuron = Circle(radius=0.5, color=BLUE, fill_opacity=1)
        self.play(Create(neuron))
        self.wait()

        # Incoming connections
        num_incoming = 10
        incoming_lines = VGroup(*[Line(start=np.random.uniform(-5, 5, size=3), end=neuron.get_center(), stroke_width=0.5, color=YELLOW) for _ in range(num_incoming)])
        self.play(Create(incoming_lines), run_time=2)
        self.wait()

        # Incoming signals
        def activate_line(line):
            return Succession(
                line.animate.set_color(RED),
                line.animate.set_color(YELLOW)
            )

        self.play(LaggedStart(*[activate_line(line) for line in incoming_lines], lag_ratio=0.5), run_time=4)
        self.wait()

        # Neuron activation
        neuron_activation = Succession(
            neuron.animate.scale(1.2).set_color(RED),
            neuron.animate.scale(1/1.2).set_color(BLUE)
        )
        self.play(neuron_activation, run_time=1)
        self.wait()

        # Outgoing connections
        num_outgoing = 5
        outgoing_lines = VGroup(*[Line(start=neuron.get_center(), end=np.random.uniform(-5, 5, size=3), stroke_width=0.5, color=GREEN) for _ in range(num_outgoing)])
        self.play(Create(outgoing_lines), run_time=2)
        self.wait()

        # Outgoing signals
        def send_signal(line):
            signal = Dot(color=GREEN).scale(0.5).move_to(neuron.get_center())
            return Succession(
                Create(signal),
                signal.animate.move_to(line.end),
                FadeOut(signal)
            )

        self.play(LaggedStart(*[send_signal(line) for line in outgoing_lines], lag_ratio=0.5), run_time=3)
        self.wait()

        # Surrounding activity
        surrounding_neurons = VGroup(*[Dot(np.random.uniform(-7, 7, size=3), color=BLUE) for _ in range(50)])
        self.play(Create(surrounding_neurons), run_time=2)
        self.wait()

        def random_blink(neuron):
            return Succession(
                neuron.animate.set_color(RED),
                neuron.animate.set_color(BLUE)
            )

        self.play(LaggedStart(*[random_blink(neuron) for neuron in surrounding_neurons], lag_ratio=0.1), run_time=5)
        self.wait()