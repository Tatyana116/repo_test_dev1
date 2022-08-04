class ValiueError:
    pass


class Figure():
  name = None

  @property
  def area(self) -> float:
      return True

  @property
  def perimetr(self) -> float:
      return True

  def add_area(self, figure):
      if not isinstance(figure, Figure):
          raise ValueError("Not instance of figure!")
      return self.area + figure.area
