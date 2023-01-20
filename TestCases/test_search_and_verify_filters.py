import time

import pytest
from Pages.pracujpl_launch_page import LaunchPage
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    def test_search_job(self):
        search_job_results = self.lp.search_for_job(locations=["Katowice"], positions=["Tester Oprogramowania"])
        search_job_results.check_if_title_contains("tester", "oprogramowania", "tester oprogramowania")

        search_job_results.prnt()
