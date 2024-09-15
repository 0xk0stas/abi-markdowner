# abi_markdowner.py

def transform_type(abi_type):
    """Transforms ABI type strings to desired format and checks for Optional, List, and MultiValue."""
    # Initialize flags and raw_type
    is_optional = 'optional' in abi_type or 'Option' in abi_type
    is_list = 'List' in abi_type
    is_multivalue = 'variadic' in abi_type
    
    # Escape angle brackets for raw_type
    raw_type = abi_type.replace("<", "&lt;").replace(">", "&gt;")

    # Clean abi_type
    abi_type = (abi_type.replace("optional<", "")
                        .replace("Option<", "")
                        .replace("List<", "")
                        .replace("variadic<", "")
                        .strip('>'))

    # Escape angle brackets for abi_type
    abi_type = abi_type.replace("<", "&lt;").replace(">", "&gt;")

    # Return raw_type if at least two conditions are true
    if sum([is_optional, is_multivalue, is_list]) >= 2:
        return abi_type, is_optional, is_list, is_multivalue, raw_type
    return abi_type, is_optional, is_list, is_multivalue, ""

def generate_matrix(parameters, include_column_names=True):
    """Generates a matrix for parameters, omitting columns with no data."""
    
    # Prepare the headers and a list to track if each column has data
    headers = ["Type", "Optional", "List", "MultiValue", "Raw Type"]
    if include_column_names:
        headers.insert(0, "Name")
    
    # Initialize a list to track if each column has data
    columns_data = [[] for _ in headers]  # Create a list of lists corresponding to the number of headers
    
    # Process each parameter and record the data for each column
    for param in parameters:
        param_type, is_optional, is_list, is_multivalue, raw_type = transform_type(param['type'])
        
        # Construct the row data for the parameter
        row_data = [
            param['name'] if include_column_names else param_type,  # Name (if included) or Type
            param_type,  # Type
            "✔" if is_optional else "",  # Optional
            "✔" if is_list else "",  # List
            "✔" if is_multivalue else "",  # MultiValue
            raw_type  # Raw Type
        ]
        
        # Ensure that if 'include_column_names' is False, we don't add the 'Name' column
        if not include_column_names:
            row_data.pop(0)
        
        # Add data to the corresponding columns
        for i, value in enumerate(row_data):
            columns_data[i].append(value)
    
    # Identify columns with data (non-empty strings or check marks)
    columns_to_include = [i for i, col in enumerate(columns_data) if any(col)]
    
    # Filter out columns without any data from headers and rows
    final_headers = [headers[i] for i in columns_to_include]
    matrix = f"| {' | '.join(final_headers)} |\n"
    matrix += f"| {' | '.join(['-'] * len(final_headers))} |\n"
    
    # Build rows using only the columns that contain data
    for row in zip(*columns_data):
        final_row = [row[i] for i in columns_to_include]
        matrix += f"| {' | '.join(final_row)} |\n"
    
    return matrix



def generate_links_section(deployments):
    """Generate the links section of the Markdown based on deployments."""
    markdown = ""

    networks = {
        "mainnet": deployments.get('mainnet', []),
        "devnet": deployments.get('devnet', []),
        "testnet": deployments.get('testnet', [])
    }

    if any(networks.values()):
        markdown += "<details>\n<summary>Links</summary>\n\n"
        for network, deployment_list in networks.items():
            if deployment_list:
                markdown += format_deployments(deployment_list, network)
        markdown += "</details>\n\n"

    return markdown

def format_deployments(deployments, network, default_label="Address"):
    """Format deployment addresses for Markdown."""
    base_urls = {
        "mainnet": "https://explorer.elrond.com/address/",
        "devnet": "https://devnet-explorer.elrond.com/address/",
        "testnet": "https://testnet-explorer.elrond.com/address/"
    }
    if network not in base_urls:
        raise ValueError("Invalid network provided. Use 'mainnet', 'devnet', or 'testnet'.")

    formatted_markdown = f"- **{network.capitalize()} Deployments**:\n"
    base_url = base_urls[network]
    
    for deployment in deployments:
        address = deployment['address']
        label = deployment.get('label', default_label)
        formatted_markdown += f"  - **[{label}]({base_url}{address})**: {address}\n"
    
    return formatted_markdown

def generate_markdown_from_abi(abi, deployments):
    """Generate Markdown content from ABI."""

    def add_docs(docs):
        """Add documentation if available."""
        return "\n".join([f"{doc}\n" for doc in docs]) if docs else ""

    markdown = "<sub>*This file has been auto-generated using the [abi-markdowner](https://github.com/0xk0stas/abi-markdowner).*</sub>\n\n"
    markdown += f"# Smart Contract: {abi['name']}\n\n"

    # General Documentation
    if 'docs' in abi:
        markdown += "<details>\n<summary>Documentation</summary>\n\n"
        markdown += add_docs(abi['docs'])
        markdown += "</details>\n\n"

    # Build Information Section
    if 'buildInfo' in abi:
        rustc_info = abi['buildInfo']['rustc']
        framework_info = abi['buildInfo']['framework']
        markdown += "<details>\n<summary>Build info</summary>\n\n"
        markdown += f"- **Rustc Version**: {rustc_info['version']}\n"
        markdown += f"- **Commit Hash**: {rustc_info['commitHash']}\n"
        markdown += f"- **Commit Date**: {rustc_info['commitDate']}\n"
        markdown += f"- **Channel**: {rustc_info['channel']}\n\n"
        markdown += f"- **Framework**: {framework_info['name']}\n"
        markdown += f"- **Version**: {framework_info['version']}\n"
        markdown += "</details>\n\n"

    # Links Section
    markdown += generate_links_section(deployments)

    # Table of Contents
    sections = {
        "Types": 'types' in abi and abi['types'],
        "Endpoints": 'endpoints' in abi and abi['endpoints'],
        "Views": 'endpoints' in abi and any(endpoint.get('mutability') == 'readonly' for endpoint in abi['endpoints']),
        "Events": 'events' in abi and abi['events']
    }
    if any(sections.values()):
        markdown += "## Table of Contents\n\n"
        for section, exists in sections.items():
            if exists:
                markdown += f"- [{section}](#{section.lower()})\n"
        markdown += "\n"

    # Types Section
    if sections["Types"]:
        markdown += "## Types\n\n"
        for type_name, type_info in abi['types'].items():
            markdown += f"<details>\n<summary>{type_name}</summary>\n\n"
            markdown += add_docs(type_info.get('docs'))
            if type_info['type'] == 'enum':
                markdown += "#### Enum Variants:\n"
                for variant in type_info['variants']:
                    markdown += f"- **{variant['name']}** (Discriminant: {variant['discriminant']})\n"
                markdown += "\n"
            elif type_info['type'] == 'struct':
                markdown += "#### Struct Fields:\n"
                markdown += generate_matrix(type_info['fields']) + "\n"
            markdown += "</details>\n\n"

    # Endpoints Section
    def add_endpoint_section(title, endpoints):
        """Add a section for endpoints."""
        if endpoints and endpoints[0] != {}:
            section_markdown = f"### {title}\n\n" if title else ""
            for endpoint in endpoints:
                if title == "Deploy":
                    endpoint_name = "init"
                elif title == "Upgrade":
                    endpoint_name = "upgrade"
                else:
                    endpoint_name = endpoint.get('name')
                section_markdown += f"<details>\n<summary>{endpoint_name}</summary>\n\n"
                section_markdown += add_docs(endpoint.get('docs'))
                if 'payableInTokens' in endpoint:
                    payable_by = 'EGLD only' if endpoint['payableInTokens'][0] == 'EGLD' else 'any token'
                    section_markdown += f"#### Note: This endpoint is payable by {payable_by}.\n\n"
                if 'inputs' in endpoint and endpoint['inputs']:
                    section_markdown += "#### Inputs:\n"
                    section_markdown += generate_matrix(endpoint['inputs']) + "\n"
                if 'outputs' in endpoint and endpoint['outputs']:
                    section_markdown += "#### Outputs:\n"
                    section_markdown += generate_matrix(endpoint['outputs'], False) + "\n"
                section_markdown += "\n</details>\n\n"
            return section_markdown
        return ""

    # Generate sections for endpoints
    markdown += "## Endpoints\n\n"
    markdown += add_endpoint_section("Deploy", [abi.get('constructor', {})])
    markdown += add_endpoint_section("Upgrade", [abi.get('upgradeConstructor', {})])

    # Categorizing Endpoints
    owner_only_endpoints = [ep for ep in abi.get('endpoints', []) if ep.get('onlyOwner', False)]
    readonly_endpoints = [ep for ep in abi.get('endpoints', []) if ep.get('mutability') == 'readonly']
    other_endpoints = [ep for ep in abi.get('endpoints', []) if ep not in owner_only_endpoints and ep not in readonly_endpoints]

    markdown += add_endpoint_section("Owner Only", owner_only_endpoints)
    markdown += add_endpoint_section("Other", other_endpoints)

    # Views (Readonly Endpoints)
    if readonly_endpoints:
        markdown += "## Views\n\n"
        markdown += add_endpoint_section("", readonly_endpoints)

    # Events Section
    if sections["Events"]:
        markdown += "## Events\n\n"
        for event in abi['events']:
            markdown += f"<details>\n<summary>{event['identifier']}</summary>\n\n"
            markdown += add_docs(event.get('docs'))
            if 'inputs' in event and event['inputs']:
                markdown += "#### Inputs:\n"
                markdown += generate_matrix(event['inputs']) + "\n"
            markdown += "</details>\n\n"

    return markdown
