from gmlib import *


class UIButton:
    def __init__(self, rectangle: Rectangle):
        self._rectangle = rectangle

        self._hovered = False
        self._pressed = False
        self._previous_tick_clicked = False
        self._on_clicked = False

    def update(self, mouse_position: Point, mouse_clicked: bool):
        self._hovered = self._rectangle.pointOnRectangle(mouse_position)
        if self._hovered:
            if mouse_clicked:
                self._pressed = True
                if self._previous_tick_clicked:
                    self._on_clicked = False
                else:
                    self._on_clicked = True
                self._previous_tick_clicked = True
            else:
                self._pressed = False
                self._previous_tick_clicked = False
                self._on_clicked = False
        else:
            self._pressed = False
            self._previous_tick_clicked = False
            self._on_clicked = False

    def onHovered(self):
        return self._hovered

    def onPressed(self):
        return self._pressed

    def onClicked(self):
        return self._on_clicked
