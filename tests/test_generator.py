import os
import random

import pytest

from lib.generator import Generator, utils
from lib.utils import get_path

KEYS = ['shapes', 'physical nature', 'distinguishing characteristic', 'items', 'season', 'time', 'inside', 'outside']


@pytest.fixture
def gen():
    yield Generator(idea_path=f"{get_path(8)}//test_ideas.txt")


def test_init_default_context(gen):
    assert gen.context == 'general'


def test_init_rand_items(gen):
    assert len(gen.rand_items) == 0


def test_lst_matches_keys(gen):
    assert gen.get_keys() == KEYS


def test_lst_keys_are_found(gen):
    for key in KEYS:
        assert key in gen.lst


def test_lst_keys_return_arrays(gen):
    for key in KEYS:
        assert len(gen.lst[key]) > 0


def test_generate(gen):
    expected = ['Oval', 'Bird', 'Kung Fu Master', 'Clouds', 'Winter', 'Night', 'Space Shuttle', 'Wetland']
    random.seed(1)
    gen.generate()
    assert gen.rand_items == expected


def test_export_unique_path():
    export_file_path = f'{get_path(8)}//exported.txt'
    assert not os.path.exists(export_file_path)

    gen = Generator(idea_path=f'{get_path(8)}//tst_export.txt')
    gen.export_lst(export_file_path)
    assert os.path.exists(export_file_path)

    os.remove(export_file_path)


def test_export_default_path():
    original_path = f'{get_path(8)}//original.txt'
    assert os.path.exists(original_path)

    gen = Generator(idea_path=original_path)
    os.remove(original_path)

    assert not os.path.exists(original_path)
    gen.export_lst()

    assert os.path.exists(original_path)


def test_convert_file_to_array():
    expected = ['Hello', 'Please', 'Convert', 'Me', 'To', 'Array']
    converted_file = Generator.convert_file_to_array(f'{get_path(8)}//file_to_convert_to_array.txt')
    assert expected == converted_file