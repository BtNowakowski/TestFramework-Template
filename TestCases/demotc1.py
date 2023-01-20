import time
import pytest
from Pages.pracujpl_launch_page import LaunchPage
from Pages.results_page import ResultPage
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_job(self):
        lp = LaunchPage(self.driver)
        lp.select_location("Zabrze", "Bytom", "Katowice")
        lp.select_position("Tester Oprogramowania", "QA")
        lp.click_submit()
        rp = ResultPage(self.driver)
        rp.check_title("tester oprogramowania", "Zabrze")
