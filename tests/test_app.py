import pytest
from dash import html, dcc
from app import app  # make sure app.py is importable

# This tells pytest-dash to use your Dash app instance
@pytest.fixture
def dash_app():
    return app

def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Dashboard" in header.text

def test_graph_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("div.js-plotly-plot")
    assert graph is not None

def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio = dash_duo.find_element("div[class*='dash-radioitems']")
    assert radio is not None
    options = dash_duo.find_elements("input[type='radio']")
    assert len(options) == 5  # north, east, south, west, all
