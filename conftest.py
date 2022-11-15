import os.path
from datetime import datetime
import pytest


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            name = datetime.strftime(datetime.now(), '%m-%d_%H-%M-%S')
            file_name = f'screenshot{name}.png'
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="/var/lib/jenkins/workspace/Quicklly/screenshots/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    path = os.path.join('screenshots', name)
    print(path)