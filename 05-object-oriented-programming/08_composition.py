"""
Composition vs Inheritance

Two ways to reuse behavior between classes — choose based on the relationship.

Inheritance ("is-a"):
  Car IS A Vehicle — subclass extends parent behavior.
  Good when the subtype truly is a specialized version of the parent.

Composition ("has-a"):
  Car HAS AN Engine — class owns parts and delegates to them.
  Good when behavior comes from swappable, independent components.

Prefer composition when:
  You want flexible parts without deep inheritance hierarchies
  Behavior might change at runtime (swap Engine implementation)
  Multiple unrelated capabilities would force awkward multiple inheritance

"Favor composition over inheritance" — not a ban on inheritance, but a
default when the relationship is ownership rather than specialization.

Gotcha: deep inheritance trees become fragile — a change in a base class
can break distant subclasses. Composition keeps boundaries explicit.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Inheritance example — "is-a"
# ------------------------------------------------------------
class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def start(self) -> None:
        print(f"{self.brand} vehicle started")


class Car(Vehicle):
    def honk(self) -> None:
        print(f"{self.brand} honks")


car = Car("Toyota")
car.start()
car.honk()
print()


# ------------------------------------------------------------
# Composition example — "has-a"
# ------------------------------------------------------------
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> None:
        print(f"Engine ({self.horsepower} hp) rumbling...")


class ComposedCar:
    def __init__(self, brand: str, engine: Engine) -> None:
        self.brand = brand
        self.engine = engine  # Car HAS an Engine

    def start(self) -> None:
        print(f"{self.brand} turning key...")
        self.engine.start()

    def swap_engine(self, new_engine: Engine) -> None:
        self.engine = new_engine
        print(f"{self.brand} got a new engine ({new_engine.horsepower} hp)")


small_engine = Engine(90)
big_engine = Engine(300)

my_car = ComposedCar("Honda", small_engine)
my_car.start()
my_car.swap_engine(big_engine)
my_car.start()
print()


# ------------------------------------------------------------
# Why composition?
# ------------------------------------------------------------
# - Swap parts at runtime (swap_engine above)
# - Avoid fragile base-class changes rippling through subclasses
# - Mix and match capabilities without multiple inheritance


# ------------------------------------------------------------
# Challenge — Playlist has Songs
# ------------------------------------------------------------
# playlist = Playlist("Road Trip")
# playlist.add(Song("Bohemian Rhapsody", 355))
# playlist.add(Song("Hotel California", 391))
# playlist.play_all()
#
# Road Trip playlist (2 songs):
#   Now playing: Bohemian Rhapsody (355s)
#   Now playing: Hotel California (391s)
# Total duration: 746s


class Song:
    def __init__(self, title: str, duration_seconds: int) -> None:
        self.title = title
        self.duration_seconds = duration_seconds

    def play(self) -> None:
        print(f"  Now playing: {self.title} ({self.duration_seconds}s)")


class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self._songs: list[Song] = []

    def add(self, song: Song) -> None:
        self._songs.append(song)

    def play_all(self) -> None:
        print(f"{self.name} playlist ({len(self._songs)} songs):")
        total = 0
        for song in self._songs:
            song.play()
            total += song.duration_seconds
        print(f"Total duration: {total}s")


playlist = Playlist("Road Trip")
playlist.add(Song("Bohemian Rhapsody", 355))
playlist.add(Song("Hotel California", 391))
playlist.play_all()
