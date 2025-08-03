from tests.utils.timer_helper import TimerHelper


class PerformanceHelper:
    """Utility class for performance testing"""

    @staticmethod
    def measure_page_load_time(page_object, navigation_method, threshold_ms):
        """
        Measure page load time and verify it's within threshold

        Args:
            page_object: The page object instance
            navigation_method: Method to call for navigation
            threshold_ms: Maximum allowed load time in milliseconds

        Returns:
            tuple: (load_time_ms, is_within_threshold)
        """
        timer = TimerHelper()
        timer.start()

        navigation_method()
        page_object.wait_for_page_load()

        load_time_ms = timer.stop()
        is_within_threshold = load_time_ms <= threshold_ms

        return load_time_ms, is_within_threshold

    @staticmethod
    def assert_page_loads_within_threshold(
        page_object, navigation_method, threshold_ms, page_name
    ):
        """
        Assert that page loads within the specified threshold

        Args:
            page_object: The page object instance
            navigation_method: Method to call for navigation
            threshold_ms: Maximum allowed load time in milliseconds
            page_name: Name of the page for error message
        """
        load_time_ms, is_within_threshold = PerformanceHelper.measure_page_load_time(
            page_object, navigation_method, threshold_ms
        )

        assert is_within_threshold, (
            f"{page_name} took {load_time_ms:.2f}ms to load, "
            f"expected - {threshold_ms}ms"
        )
