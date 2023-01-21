import pytest
import softest
from ddt import ddt, data, unpack, file_data
from Pages.pracujpl_launch_page import LaunchPage
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @file_data("../TestData/data.json")
    def test_search_job(self, locations, positions, strings):
        search_job_results = self.lp.search_for_job(positions, locations)
        search_job_results.check_if_page_title_contains(strings)
