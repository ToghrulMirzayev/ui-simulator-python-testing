from pytest import mark

validation_scenarios = (
    [50, "Valid"],
    [10, "Valid"],
    [10.5, "Not an integer"],
    ["text", "Not a number"],
    [51, "Not in range"],
    [9, "Not in range"],
    [-1, "Negative integer"],
    [-1.5, "Negative number"]
)


@mark.parametrize("value_param, text_param", validation_scenarios,
                  ids=["in range integer higher boundary", "in range integer lower boundary", "not integer",
                       "not number", "out of range higher boundary", "out of range lower boundary", "negative integer",
                       "negative number"])
def test_validate_value(check_and_validate_page, value_param, text_param):
    check_and_validate_page.perform_validation(
        value=value_param,
        expected_text=text_param
    )
