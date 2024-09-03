# abi_markdowner.py

def transform_type(abi_type):
    """Transforms ABI type strings to desired format."""
    if abi_type.startswith("variadic<"):
        abi_type = abi_type.replace("variadic", "MultiValue")
    if abi_type.startswith("optional<"):
        abi_type = abi_type.replace("optional", "OptionalValue")
    # Escape angle brackets for Markdown
    return abi_type.replace("<", "&lt;").replace(">", "&gt;")

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
    markdown += "## Table of Contents\n\n"
    markdown += "- [Types](#types)\n"
    markdown += "- [Endpoints](#endpoints)\n"
    markdown += "  - [Deployment - Upgrade](#deployment---upgrade)\n"
    markdown += "  - [Owner Only](#owner-only)\n"
    markdown += "  - [Other](#other)\n"
    markdown += "- [Views](#views)\n"
    markdown += "- [Events](#events)\n\n"

    # Types Section
    if 'types' in abi:
        markdown += "## Types\n\n"
        for type_name, type_info in abi['types'].items():
            markdown += f"<details>\n<summary>{type_name}</summary>\n\n"
            markdown += add_docs(type_info.get('docs'))

            if type_info['type'] == 'enum':
                markdown += "#### Enum Variants:\n"
                for variant in type_info['variants']:
                    markdown += f"- **{variant['name']}** (Discriminant: {variant['discriminant']})\n"
            elif type_info['type'] == 'struct':
                markdown += "#### Struct Fields:\n"
                for field in type_info['fields']:
                    markdown += f"- **{field['name']}**: {transform_type(field['type'])}\n"
            markdown += "\n</details>\n\n"

    # Endpoints Section
    markdown += "## Endpoints\n\n"

    def add_endpoint_section(title, endpoints):
        """Add a section for endpoints."""
        if endpoints:
            markdown = f"### {title}\n\n"
            for endpoint in endpoints:
                markdown += f"<details>\n<summary>{endpoint['name']}</summary>\n\n"
                if 'payableInTokens' in endpoint:
                    payable_by = 'EGLD only' if endpoint['payableInTokens'][0] == 'EGLD' else 'any token'
                    markdown += f"#### This endpoint is payable by {payable_by}.\n\n"
                markdown += add_docs(endpoint.get('docs'))
                if 'inputs' in endpoint and endpoint['inputs']:
                    markdown += "#### Inputs:\n"
                    for inp in endpoint['inputs']:
                        markdown += f"- **{inp['name']}**: {transform_type(inp['type'])}\n"
                if 'outputs' in endpoint and endpoint['outputs']:
                    markdown += "#### Outputs:\n"
                    for out in endpoint['outputs']:
                        markdown += f"- **Type**: {transform_type(out['type'])}\n"
                markdown += "\n</details>\n\n"
            return markdown
        return ""

    # Categorizing Endpoints
    owner_only_endpoints = []
    other_endpoints = []
    readonly_endpoints = []

    if 'endpoints' in abi:
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
        markdown += add_endpoint_section("Views", readonly_endpoints)

    # Events Section
    if 'events' in abi:
        markdown += "## Events\n\n"
        for event in abi['events']:
            markdown += f"<details>\n<summary>{event['identifier']}</summary>\n\n"
            markdown += add_docs(event.get('docs'))
            if 'inputs' in event and event['inputs']:
                markdown += "#### Inputs:\n"
                for inp in event['inputs']:
                    markdown += f"- **{inp['name']}**: {transform_type(inp['type'])}"
                    if inp.get('indexed', False):
                        markdown += " (indexed)"
                    markdown += "\n"
            markdown += "</details>\n\n"

    return markdown
