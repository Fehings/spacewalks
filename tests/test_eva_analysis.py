from eva_data_analysis import text_to_duration, calculate_crew_size
import pytest


def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected integer value when minutes are zero
    """
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected float value for typical durations
    with non-zero minute components
    """
    assert text_to_duration("10:20") == pytest.approx(10.3333333)

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

