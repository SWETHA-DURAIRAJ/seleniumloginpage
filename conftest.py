import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from pathlib import Path

BaseUrl="https://practicetestautomation.com/practice-test-login/"
email="student1"
password="Password123"
@pytest.fixture(scope="class",autouse=True)
def launch_browser(request):
    #chrome_option=Options()
    #chrome_option.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today=datetime.now()
    report_dr=Path("hrmreport",today.strftime("%Y%m%d"))
    report_dr.mkdir(parents=True, exist_ok=True) # to create folder
    pytest_html=report_dr/ f"Report-{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained=True
'''| Line                                             | What it does                                    |
| ------------------------------------------------ | ----------------------------------------------- |
| `today = datetime.now()`                         | Gets current date and time                      |
| `Path("hrmreport", today.strftime("%Y%m%d"))`    | Creates a subfolder like `hrmreport/20251026`   |
| `mkdir(parents=True, exist_ok=True)`             | Ensures the folder exists                       |
| `f"Report-{today.strftime('%Y%m%d-%H%M')}.html"` | Names file based on date and time               |
| `config.option.htmlpath = str(report_file)`      | Sets pytest-html output path                    |
| `config.option.self_contained_html = True`       | Embeds all CSS/JS in one file (no dependencies) |

hrmreport/
└── 20251026/
    └── Report-20251026-1930.html
'''


def pytest_html_report_title(report):
    report.title = "HRM Report"

