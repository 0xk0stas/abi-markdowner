# abi_markdowner.py

def transform_type(abi_type):
    """Transforms ABI type strings to desired format and checks for Optional, List, and MultiValue."""
    is_optional = False
    is_multivalue = False
    is_list = False
    
    raw_type = abi_type.replace("<", "&lt;").replace(">", "&gt;")

    if "optional" in abi_type or "Option" in abi_type:
        abi_type = abi_type.replace("optional<", "").replace("Option<", "")
        # abi_type = abi_type[1:-1]
        is_optional = True

    if "List" in abi_type:
        abi_type = abi_type.replace("List<", "")
        # abi_type = abi_type[1:-1]
        is_list = True

    if "variadic" in abi_type:
        abi_type = abi_type.replace("variadic<", "")
        # abi_type = abi_type[1:-1]
        is_multivalue = True

    abi_type = abi_type.strip('>')
    
    # Escape angle brackets for Markdown
    abi_type = abi_type.replace("<", "&lt;").replace(">", "&gt;")

    if sum([is_optional, is_multivalue, is_list]) >= 2:
        return abi_type, is_optional, is_list, is_multivalue, raw_type
    else:
        return abi_type, is_optional, is_list, is_multivalue, ""

def generate_matrix(parameters, include_column_names=True):
    """Generates a matrix for parameters."""
    matrix = ""
    if include_column_names:
        matrix += "| Name | Type | Optional | List | MultiValue | Raw Type |\n"
        matrix += "| - | - | - | - | - | - |\n"
    else:
        matrix += "| Type | Optional | List | MultiValue | Raw Type |\n"
        matrix += "| - | - | - | - | - |\n"
        
    for param in parameters:
        param_type, is_optional, is_list, is_multivalue, raw_type = transform_type(param['type'])
        optional = "✔" if is_optional else ""
        list = "✔" if is_list else ""
        multivalue = "✔" if is_multivalue else ""
        
        if include_column_names:
            param_name = param['name']
            matrix += f"| {param_name} | {param_type} | {optional} | {list} | {multivalue} | {raw_type} |\n"
        else:
            matrix += f"| {param_type} | {optional} | {list} | {multivalue} | {raw_type} |\n"

    return matrix

def generate_links_section(deployments):
    """Generate the links section of the Markdown based on deployments."""
    markdown = ""
    
    mainnet_deployments = deployments.get('mainnet', [])
    devnet_deployments = deployments.get('devnet', [])
    testnet_deployments = deployments.get('testnet', [])
    
    # Links Section
    if mainnet_deployments or devnet_deployments:
        markdown += "<details>\n<summary>Links</summary>\n\n"

        # Process mainnet deployments
        if mainnet_deployments:
            markdown += format_deployments(mainnet_deployments, "mainnet")

        # Process devnet deployments
        if devnet_deployments:
            markdown += format_deployments(devnet_deployments, "devnet")

        # Process testnet deployments
        if testnet_deployments:
            markdown += format_deployments(testnet_deployments, "testnet")

        markdown += "</details>\n\n"
    
    return markdown

def format_deployments(deployments, network, default_label="Address"):
    """Format deployment addresses for Markdown."""
    
    if network == "mainnet":
        base_url = "https://explorer.elrond.com/address/"
    elif network == "devnet":
        base_url = "https://devnet-explorer.elrond.com/address/"
    elif network == "testnet":
        base_url = "https://testnet-explorer.elrond.com/address/"
    else:
        raise ValueError("Invalid network provided. Use 'mainnet' or 'devnet'.")

    formatted_markdown = "- **" + network.capitalize() + " Deployments**:\n"
    for deployment in deployments:
        address = deployment['address']
        label = deployment.get('label', default_label)  # Use the provided label or default
        formatted_markdown += f"  - **[{label}]({base_url}{address})**: {address}\n"
    return formatted_markdown


def generate_markdown_from_abi(abi, deployments):
    """Generate Markdown content from ABI."""

    def add_docs(docs):
        """Add documentation if available."""
        if docs:
            return "\n".join([f"{doc}\n" for doc in docs])
        return ""
    
    markdown = "<sub>*This file has been auto-generated using the [AbiMarkdowner](https://github.com/0xk0stas/AbiMarkdowner).*</sub>\n\n"
    markdown += f"# Smart Contract: {abi['name']}\n\n"

    # General Documentation
    if 'docs' in abi:
        markdown += add_docs(abi['docs'])

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
    has_types = 'types' in abi and abi['types']
    has_endpoints = 'endpoints' in abi and abi['endpoints']
    has_views = 'endpoints' in abi and any(endpoint.get('mutability') == 'readonly' for endpoint in abi['endpoints'])
    has_events = 'events' in abi and abi['events']
    if has_types or has_endpoints or has_events:
        markdown += "## Table of Contents\n\n"
        if has_types:
            markdown += "- [Types](#types)\n"
        if has_endpoints:
            markdown += "- [Endpoints](#endpoints)\n"
            # markdown += "  - [Deployment - Upgrade](#deployment---upgrade)\n"
            # markdown += "  - [Owner Only](#owner-only)\n"
            # markdown += "  - [Other](#other)\n"
        if has_views:
            markdown += "- [Views](#views)\n"
        if has_events:
            markdown += "- [Events](#events)\n\n"

    # Types Section
    if 'types' in abi and abi['types']:
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
        if endpoints:
            markdown = f"### {title}\n\n" if title else ""
            for endpoint in endpoints:
                markdown += f"<details>\n<summary>{endpoint['name']}</summary>\n\n"
                markdown += add_docs(endpoint.get('docs'))
                if 'payableInTokens' in endpoint:
                    payable_by = 'EGLD only' if endpoint['payableInTokens'][0] == 'EGLD' else 'any token'
                    markdown += f"#### Note: This endpoint is payable by {payable_by}.\n\n"
                if 'inputs' in endpoint and endpoint['inputs']:
                    markdown += "#### Inputs:\n"
                    markdown += generate_matrix(endpoint['inputs']) + "\n"
                if 'outputs' in endpoint and endpoint['outputs']:
                    markdown += "#### Outputs:\n"
                    markdown += generate_matrix(endpoint['outputs'], False) + "\n"
                markdown += "\n</details>\n\n"
            return markdown
        return ""

    markdown += "## Endpoints\n\n"
    
    # Deployment (Constructor)
    if 'constructor' in abi:
        markdown += "### Deployment - Upgrade\n\n"
        markdown += "<details>\n<summary>init</summary>\n\n"
        
        markdown += add_docs(abi['constructor']['docs'])

        markdown += "#### Inputs:\n"
        markdown += generate_matrix(abi['constructor']['inputs'], False) + "\n"
        markdown += "</details>\n\n"

    # Upgrade Constructor
    if 'upgradeConstructor' in abi:
        markdown += "<details>\n<summary>upgrade</summary>\n\n"

        markdown += add_docs(abi['upgradeConstructor']['docs'])

        markdown += "#### Inputs:\n"
        markdown += generate_matrix(abi['upgradeConstructor']['inputs'], False) + "\n"
        markdown += "</details>\n\n"

    # Categorizing Endpoints
    owner_only_endpoints = []
    other_endpoints = []
    readonly_endpoints = []

    if 'endpoints' in abi and abi['endpoints']:
        for endpoint in abi['endpoints']:
            if endpoint.get('mutability') == 'readonly':
                readonly_endpoints.append(endpoint)
            elif endpoint.get('onlyOwner', False):
                owner_only_endpoints.append(endpoint)
            else:
                other_endpoints.append(endpoint)

    markdown += add_endpoint_section("Owner Only", owner_only_endpoints)
    markdown += add_endpoint_section("Other", other_endpoints)

    # Views (Readonly Endpoints)
    if readonly_endpoints:
        markdown += "## Views\n\n"
        markdown += add_endpoint_section("", readonly_endpoints)

    # Events Section
    if 'events' in abi:
        markdown += "## Events\n\n"
        for event in abi['events']:
            markdown += f"<details>\n<summary>{event['identifier']}</summary>\n\n"
            markdown += add_docs(event.get('docs'))
            if 'inputs' in event and event['inputs']:
                markdown += "#### Inputs:\n"
                markdown += generate_matrix(event['inputs']) + "\n"
            markdown += "</details>\n\n"

    return markdown
