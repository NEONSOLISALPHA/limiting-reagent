from manim import *  # noqa: F403


class Test(Scene):
    def construct(self):
        self.play(
            ShowCreation(Circle()),
            Write(MathTex(
                "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
                "g(x)\\frac{d}{dx}f(x)"
            ))
        )
        self.wait()
