from random_poems.poems import declaim, get_random_poem


class TestDeclaim:
    def test_declaim(self, capsys):
        title = "Super Cool"
        poem = (
            "Roses are red\n"
            "Violets are blue\n"
            "I think the Global South\n"
            "is super cool"
        )
        author = "Tonino"
        expected_output = (
            "---------------------------------------------------\n"
            "Super Cool\n"
            "\n"
            "Roses are red\n"
            "Violets are blue\n"
            "I think the Global South\n"
            "is super cool\n"
            "\n"
            "By Tonino\n"
            "---------------------------------------------------\n"
        )

        declaim(title, poem, author)

        captured = capsys.readouterr()

        assert captured.out == expected_output


class TestGetRandomPoem:
    def test_get_random_poem(self, mocker):
        request_mock = mocker.patch("random_poems.poems.requests.get")
        request_mock.return_value.status_code = 200
        request_mock.return_value.json.return_value = [{
            "title": "Super Cool",
            "lines": [
                "Roses are red",
                "Violets are blue",
                "I think the Global South",
                "is super cool"
            ],
            "author": "Tonino"
        }]
        expected_poem = {
            "title": "Super Cool",
            "poem": (
                "Roses are red\n"
                "Violets are blue\n"
                "I think the Global South\n"
                "is super cool"
            ),
            "author": "Tonino"
        }
        poem = get_random_poem()

        assert poem == expected_poem
