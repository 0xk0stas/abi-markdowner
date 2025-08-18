# tests/test_example.py

import pytest
import json
import os
from abi_markdowner.abi_markdowner import (
    transform_type, 
    generate_matrix, 
    generate_markdown_from_abi,
    generate_links_section
)
from abi_markdowner.file_io import read_abi_from_file, save_markdown_to_file


def test_transform_type_basic():
    """Test basic type transformation."""
    result = transform_type("u64")
    assert result == ("u64", False, False, False, "")


def test_transform_type_optional():
    """Test optional type transformation."""
    result = transform_type("optional<u64>")
    assert result == ("u64", True, False, False, "")


def test_transform_type_list():
    """Test list type transformation."""
    result = transform_type("List<u64>")
    assert result == ("u64", False, True, False, "")


def test_transform_type_multivalue():
    """Test multivalue type transformation."""
    result = transform_type("variadic<u64>")
    assert result == ("u64", False, False, True, "")


def test_transform_type_complex():
    """Test complex type transformation with multiple conditions."""
    result = transform_type("optional<List<u64>>")
    # Should return raw_type when at least 2 conditions are true
    assert result[0] == "u64"  # cleaned type
    assert result[1] == True   # is_optional
    assert result[2] == True   # is_list
    assert result[3] == False  # is_multivalue
    assert result[4] == "optional&lt;List&lt;u64&gt;&gt;"  # raw_type


def test_generate_matrix_basic():
    """Test matrix generation with basic parameters."""
    parameters = [
        {"name": "amount", "type": "BigUint"},
        {"name": "address", "type": "Address"}
    ]
    result = generate_matrix(parameters)
    assert "| Name | Type |" in result
    assert "| amount | BigUint |" in result
    assert "| address | Address |" in result


def test_generate_links_section_empty():
    """Test links section generation with empty deployments."""
    deployments = {"mainnet": [], "devnet": [], "testnet": []}
    result = generate_links_section(deployments)
    assert result == ""


def test_generate_links_section_with_data():
    """Test links section generation with deployment data."""
    deployments = {
        "mainnet": [{"address": "erd1abc123", "label": "Main Contract"}],
        "devnet": [],
        "testnet": []
    }
    result = generate_links_section(deployments)
    assert "Links" in result
    assert "Mainnet Deployments" in result
    assert "erd1abc123" in result


def test_generate_markdown_from_abi_basic():
    """Test basic markdown generation from ABI."""
    abi = {
        "name": "TestContract",
        "docs": ["A test contract"],
        "endpoints": [],
        "events": [],
        "types": {}
    }
    deployments = {"mainnet": [], "devnet": [], "testnet": []}
    
    result = generate_markdown_from_abi(abi, deployments)
    
    assert "# Smart Contract: TestContract" in result
    assert "A test contract" in result
    assert "abi-markdowner" in result


def test_file_io_operations(tmp_path):
    """Test file I/O operations."""
    # Test JSON writing and reading
    test_data = {"test": "data", "number": 42}
    json_file = tmp_path / "test.json"
    
    with open(json_file, 'w') as f:
        json.dump(test_data, f)
    
    # Test reading
    result = read_abi_from_file(str(json_file))
    assert result == test_data
    
    # Test markdown writing
    markdown_content = "# Test Markdown\n\nThis is a test."
    md_file = tmp_path / "test.md"
    
    save_markdown_to_file(markdown_content, str(md_file))
    
    with open(md_file, 'r') as f:
        saved_content = f.read()
    
    assert saved_content == markdown_content
