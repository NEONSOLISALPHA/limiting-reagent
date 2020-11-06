from manim import *  # noqa: F403


class Intro(Scene):
    def construct(self):
        q = MathTex("What is a ", "Limiting Reagent?")
        q[1].set_color(ORANGE)
        q.scale(1.4)

        q_answer = Tex("Answer: ", "The ", "Limiting reagent "
                       "in a chemical reaction is\n\t"
                       "the substance that is totally consumed when the "  # noqa: E501
                       "chemical reaction is completed and\n\t"
                       "stops the reaction from continuing any further")  # noqa: E501
        q_answer[0].set_color(RED)
        q_answer[2].set_color(GREEN)
        q_answer.scale(0.8)

        q.generate_target()
        q.target.shift(UP * 0.4)

        q_answer.next_to(q, DOWN)

        self.play(Write(q), runtime=2)
        self.wait(2)  # gap b/w Write and text apppearing

        self.play(MoveToTarget(q), FadeInFrom(q_answer, direction=DOWN))
        self.wait(3)

        v = VGroup(q, q_answer)
        v.generate_target()
        v.target.shift(UP * 1.1)

        q2_answer = Tex(
            "The ", "Excess reagent ",
            "is the reactant in a chemical reaction which is present "
            "\n\tin a greater amount than necessary to react completely"
            "with the limiting reactant")
        q2_answer[1].set_color(YELLOW)
        q2_answer.scale(0.8)
        q2_answer.next_to(q_answer, DOWN)
        q2_answer.shift(UP * 0.8)

        self.play(MoveToTarget(v), FadeInFrom(q2_answer, direction=DOWN))
        self.wait(4)

        self.play(Uncreate(q), Uncreate(q_answer, run_time=1),
                  Uncreate(q2_answer, run_time=1))
        self.wait(2)


class Bread(Scene):
    def construct(self):
        eg = MathTex("\\rm Eg..")
        eg.scale(3)

        self.play(Write(eg))

        eg.generate_target()
        eg.target.to_corner(UL, buff=SMALL_BUFF)
        eg.target.shift(LEFT * 0.2)
        eg.target.scale(0.3)

        self.play(MoveToTarget(eg))               # moving to location
        self.wait()

        equa = Tex(
            "\\emph{if} ", "1 ", "Cheese ",
            "+ ", "2 ", "Bread ", "$\\ce{->}$ ",
            "1 ", "Cheese ", " Sandwich"
        )
        equa[2].set_color(YELLOW)
        equa[5].set_color(color="#b0781e")
        equa.scale(1.1)

        self.play(FadeInFrom(equadirection=DOWN))
        self.wait()

        equa.generate_target()
        equa.target.next_to(eg, RIGHT)
        # equa.target.shift(LEFT*0.2)
        equa.target.scale(1.1 * (1 / 1.3))

        self.play(MoveToTarget(equa))  # moving to location
        self.wait()  # dec fade in delay

        val = ValueTracker(3)

        dec = DecimalNumber(0, num_decimal_places=0)
        dec.set_value(val.get_value())

        ce = Tex("Cheese ", "+ ", "6 ", "Bread ",
                 "$\\ce{->}$ ", "3 ", "Cheese ", " Sandwiches")

        ced = Tex("Cheese ", "+ ", "6 ", "Bread ",
                  "$\\ce{->}$ ", "more ", "Cheese ", " Sandwiches")
        ced.shift(RIGHT * 0.7)

        lim = Tex("Limiting\n\tReagent")
        exc = Tex("Excess\n\tReagent")

        ce[0].set_color(YELLOW)  # Yellow
        ce[3].set_color(color="#b0781e")

        ced[0].set_color(YELLOW)  # Yellow
        ced[3].set_color(color="#b0781e")

        ce.shift(RIGHT * 0.5)

        cross = Cross(ced[4])
        cross.set_stroke(RED, 6)

        dec.next_to(ce, LEFT)

        self.play(FadeInFrom(ce,direction=DOWN), FadeInFrom(dec, direction=DOWN))

        dec.add_updater(lambda d: d.set_value(val.get_value()))
        dec.add_updater(lambda d: d.next_to(ce, LEFT))

        self.add(dec)
        self.wait()  # increment Start Point

        self.play(val.increment_value, 7)
        self.wait()

        self.play(val.increment_value, 90)
        self.wait()

        # there is a bug where the increment is over or under executed so this value accounts for that  # noqa: E501
        self.play(val.increment_value, 900, runtime=2)
        self.wait()

        changes_1 = [
            (0, 1, 2, 3, 4, 5, 6, 7),
            (0, 1, 2, 3, 4, 5, 6, 7)
        ]

        self.play(
            *[
                ReplacementTransform(ce[i], ced[j])
                for i, j in zip(changes_1[0], changes_1[1])
            ],
            ShowCreation(cross)
        )
        self.wait()

        br1 = Brace(ced[0], DOWN)

        exc.next_to(br1, DOWN)

        br2 = Brace(ced[3], DOWN)

        lim.next_to(br2, DOWN)

        self.play(ShowCreation(br2), ShowCreation(lim))
        self.wait()

        self.play(ReplacementTransform(br2, br1),
                  ReplacementTransform(lim, exc))
        self.wait()

        self.play(*[Uncreate(i)
                    for i in [eg, br1, br2, lim, exc, ced, dec, cross, equa]])
        self.wait()

        bye = MathTex("Thanks for Watching!").scale(2.5)

        self.play(Write(bye))
        self.wait()

        self.play(Uncreate(bye))

        name = MathTex("Adithyadev R")
        Class = MathTex("Class \\rm X\\rm I \\rm A")
        name_class = VGroup(name, Class).arrange(DOWN).scale(2)

        self.play(Write(name_class))
        self.wait()

        self.play(Uncreate(name_class))
        self.wait()


class H2O(Scene):
    def construct(self):
        h2o = MathTex("2", "{H}_{2}", "+", "1",
                      "{O}_{2}", "\\ce{->}", "2", "{H}_{2}{O}")
        h2ox = MathTex("6", "{H}_{2}", "+", "2", "{O}_{2}", "\\ce{->}", "?")
        h2oy = MathTex("6", "{H}_{2}", "+", "2",
                       "{O}_{2}", "\\ce{->}", "4", "{H}_{2}{O}")

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
