import pytest
from lib.functions import is_component

@pytest.mark.parametrize('input', 
["src/components/test.component.html",
"src/components/test.component.css",
"src/app/test.component.css"])
def test_is_component_recognizes_components(input):
    assert is_component(input)

@pytest.mark.parametrize('input', 
["src/styles/_buttons.scss",
"src/app/index.css",
"src/app/components/module.scss"])
def test_is_component_recognizes_not_components(input):
    assert not is_component(input)