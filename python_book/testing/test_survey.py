from survey import AnonymousSurvey
import pytest

# def test_store_single_response():
#     """Test that a single response is store correctly."""
#     question = "What language did you learn fist?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response("Python")
#     assert "Python" in language_survey.responses
#
#
# def test_store_all_responses():
#     """Test that all response are stored correctly"""
#     question = "What language did you learn fist?"
#     language_survey = AnonymousSurvey(question)
#     responses = ["Python", "English", "Toddlerish", "Vegamamian"]
#     for response in responses:
#         language_survey.store_response(response)
#     for response in responses:
#         assert response in language_survey.responses


"""Using fixture as a decorator"""
@pytest.fixture
def language_survey():
    """A survey that will be available to all tests."""
    question = "What language did you learn first?"
    languavge_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """Test that a single response is stored correctly."""
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_all_responses(language_survey):
    """Test that all the responses are stored correctly."""
    responses = ["Python", "ABC", "Dadaya"]
    for response in responses:
        language_survey.stroe_response(response)
    for response in responses:
        assert response in language_survey.responses