import os

def generate_flyer(topic, description, date, time, location, bg = None):
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join("assets", "template.svg")
    with open(template_path, "r", encoding="utf-8") as file:
        svg_data = file.read()

    # Replaces data in the template
    svg_data = svg_data.replace("TOPIC", topic)
    svg_data = svg_data.replace("DESCRIPTION", description)
    svg_data = svg_data.replace("DATE", date)
    svg_data = svg_data.replace("TIME", time)
    svg_data = svg_data.replace("LOCATION", location)

    if bg is None:
        bg = os.path.join(script_dir, "assets", "default.png")

    image_tag = f'<image x="0" y="0" width="612" height="792" href="{bg}" />\n'
    svg_data = svg_data.replace("</defs>", f"</defs>\n{image_tag}")
    
    # Creates an output folder
    output_dir = os.path.join(script_dir, "output")
    os.makedirs(output_dir, exist_ok=True)


    # Places creation in the output folder
    output_path = os.path.join(output_dir, "flyer_output.svg")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(svg_data)

    return output_path
    