from manim import *  # noqa: F403


class H2O(Scene):
    def construct(self):
        h2o = MathTex("2", "{H}_{2}", "+", "1", "{O}_{2}",
                      "\\ce{->}", "2", "{H}_{2}{O}")
        h2ox = MathTex("6", "{H}_{2}", "+", "2", "{O}_{2}", "\\ce{->}", "?")
        h2oy = MathTex("6", "{H}_{2}", "+", "2", "{O}_{2}",
                       "\\ce{->}", "4", "{H}_{2}{O}")

        h2o[0].set_color(color="#34c9eb")
        h2o[3].set_color(color="#34c9eb")
        h2o[6].set_color(color="#34c9eb")

        h2ox[0].set_color(color="#34c9eb")
        h2ox[3].set_color(color="#34c9eb")
        h2ox[6].set_color(WHITE)

        h2oy[0].set_color(color="#34c9eb")
        h2oy[3].set_color(color="#34c9eb")
        h2oy[6].set_color(color="#34c9eb")

        changes_ = [
            (0, 1, 2, 3, 4, 5, 6, 7),
            (0, 1, 2, 3, 4, 5, 6, 6)
        ]

        self.play(
            *[
                Transform(h2o[i], h2ox[j])
                # change zip(changes[0],changes[1]) to zip(uno,dos) if using multiple stages  # noqa: E501
                for i, j in zip(changes_[0], changes_[1])
            ]
        )
        self.wait(5)

        changes = [
            # this is to avoid rendering issueshile transforming
            (0, 1, 2, 3, 4, 5, 6, 7),
            (0, 1, 2, 3, 4, 5, 6, 7)
        ]

        self.play(
            *[
                Transform(h2o[i], h2oy[j])
                for i, j in zip(changes[0], changes[1])
            ]
        )
        self.wait()
