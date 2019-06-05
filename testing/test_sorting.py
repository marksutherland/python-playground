import hypothesis
from hypothesis import strategies
import sorting


class TestSorting:
    @hypothesis.given(int_list=strategies.lists(strategies.integers()))
    @hypothesis.settings(verbosity=hypothesis.Verbosity.verbose)
    def test_quicksort(self, int_list):
        assert sorted(int_list) == sorting.quicksort(int_list)

    @hypothesis.given(int_list=strategies.lists(strategies.integers()))
    @hypothesis.settings(verbosity=hypothesis.Verbosity.verbose)
    def test_inplace_quicksort(self, int_list):
        sorting.inplace_quicksort(int_list)
        assert sorted(int_list) == int_list
