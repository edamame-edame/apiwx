from __init__ import (
    WrappedApp,
    WrappedWindow,
    WrappedPanel,
    WrappedButton,
    WrappedImage,
    DetectWindow,
    DetectPanel,
    NotTransition,
    uilog,
    uilog_output_remaining,
)


class SilicaApp(WrappedApp[DetectWindow]):
    def __init__(self):
        super().__init__("Silica")

    class SilicaWindow(WrappedWindow[DetectPanel]):
        def __init__(self, app: "SilicaApp"):
            super().__init__(
            app,
            size=(800, 600),
            pos=(100, 100),
            title="Silica Application"
        )

            self.show()

        class TransControlPanel(WrappedPanel[NotTransition]):
            def __init__(self, window: "SilicaApp.SilicaWindow"):
                super().__init__(
                    window,
                    size=(800, 40),
                    pos=(0, 0),
                )


if __name__ == "__main__":
    app = SilicaApp()

    app.mainloop()

    uilog_output_remaining()