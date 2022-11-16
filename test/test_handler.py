from src.point_entree import upper_message


class TestHandler:
    def test_when_call_upper_function_should_return_message_with_capital_letters(self):
        # Given
        message_to_capitalize = "some_message"

        # When
        result_message = upper_message(message_to_capitalize)

        # Then
        assert result_message == "SOME_MESSAGE"
