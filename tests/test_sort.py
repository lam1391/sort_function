import pytest
from app.sort import sort

# --- Happy path & edge cases ---

@pytest.mark.parametrize(
    "w,h,l,m,expected",
    [
        (10, 10, 10, 0, "STANDARD"),             # tiny, mass 0
        (99, 101, 99, 19, "STANDARD"),           # just below all thresholds
        (100, 100, 100, 10, "SPECIAL"),          # bulky by volume (exact edge)
        (150, 10, 10, 0, "SPECIAL"),             # bulky by dimension (exact edge)
        (10, 10, 10, 20, "SPECIAL"),             # heavy (exact edge)
        (150, 100, 100, 20, "REJECTED"),         # both bulky and heavy
        (200, 1, 1, 50, "REJECTED"),             # both via dimension and mass
    ],
)
def test_sort_classification(w,h,l,m,expected):
    assert sort(w,h,l,m) == expected


def test_standard_just_below_thresholds():
    # 149 x 149 x 45 = 999,045 (< 1_000_000), mass 19 -> STANDARD
    assert sort(149, 149, 45, 19) == "STANDARD"


# --- Validation ---

@pytest.mark.parametrize("value", [0, -1, -100])
def test_invalid_dimensions(value):
    with pytest.raises(ValueError):
        sort(value, 10, 10, 0)  # width invalid
    with pytest.raises(ValueError):
        sort(10, value, 10, 0)  # height invalid
    with pytest.raises(ValueError):
        sort(10, 10, value, 0)  # length invalid


@pytest.mark.parametrize("mass", [-1, -10])
def test_invalid_mass(mass):
    with pytest.raises(ValueError):
        sort(10, 10, 10, mass)

