from src import utils


def test_sort_by_date():
    assert utils.sort_by_date([{}, {"date": "2018-01-21T01:10:28.317704"},
                               {"date": "2019-01-21T01:10:28.317704"}]) == [{"date": "2019-01-21T01:10:28.317704"},
                                                                            {"date": "2018-01-21T01:10:28.317704"}]


def test_get_executed():
    assert utils.get_executed([{"state": "CANCELED"}, {"state": "EXECUTED"}, {"state": "EXECUTED"},
                               {"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "EXECUTED"},
                               {"state": "EXECUTED"}]) == [{"state": "EXECUTED"},
                               {"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "EXECUTED"},
                               {"state": "EXECUTED"}]


def test_get_date():
    assert utils.get_date([{"date": "2019-12-08T22:46:21.935582"}]) == [{'date': '08.12.2019'}]
